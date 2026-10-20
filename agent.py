import os
import sys
import json
import time
from typing import Dict, Any, List, Literal, Optional
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

class TradeAction(BaseModel):
    action: Literal["BUY", "SELL", "HOLD"]
    ticker: str
    amount_usd: Optional[float] = Field(default=0.0, description="Amount in USD if BUY")
    shares: Optional[float] = Field(default=0.0, description="Number of shares/crypto to sell if SELL")
    confidence: float = Field(description="Conviction level between 0.0 and 1.0")
    reasoning: str = Field(description="Detailed explanation of the trade decision")

class AgentDecision(BaseModel):
    market_analysis: str = Field(description="Summary of market state, macro sentiment, and technical conditions")
    memory_notes: str = Field(
        description="Tactical memory and journal for upcoming cycles: price targets, stop-loss levels, and expected catalysts."
    )
    actions: List[TradeAction] = Field(description="List of trade actions to take (maximum 1 or 2 per cycle)")

class TradingAgent:
    def __init__(self, api_key: Optional[str] = None, model_name: str = "gemini-3.5-flash-lite"):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "No se encontró GEMINI_API_KEY. Asegúrate de configurarla en tu archivo .env o variable de entorno."
            )
        self.client = genai.Client(
            api_key=self.api_key,
            http_options=types.HttpOptions(timeout=60000)
        )
        self.model_name = model_name

    def evaluate_market_and_decide(
        self,
        portfolio_summary: Dict[str, Any],
        market_snapshot: Dict[str, Any],
        memory_context: Optional[Dict[str, Any]] = None,
        lang: str = "en"
    ) -> AgentDecision:
        initial_cap = portfolio_summary.get('initial_capital', 40.0)
        is_en = (lang.lower() == "en")
        
        default_notes = "No previous notes. Initializing journal." if is_en else "Sin notas previas. Primera ejecución con bitácora."
        mem_notes = memory_context.get("previous_notes", default_notes) if memory_context else default_notes
        recent_trades = memory_context.get("recent_trades", []) if memory_context else []
        cb_events = memory_context.get("circuit_breakers", []) if memory_context else []
        
        trades_text = ""
        if recent_trades:
            trades_lines = []
            for t in recent_trades:
                ts = t.get("timestamp", "")[:16].replace("T", " ")
                reason_label = "Reason" if is_en else "Motivo"
                trades_lines.append(f"- [{ts}] {t.get('action')} {t.get('ticker')}: ${t.get('amount_usd', 0):.2f} @ ${t.get('price', 0):.2f}. {reason_label}: {t.get('reason', '')[:100]}")
            trades_text = "\n".join(trades_lines)
        else:
            trades_text = "No recent trades recorded." if is_en else "No hay operaciones recientes registradas."

        cb_text = ""
        if cb_events:
            cb_title = "\n⚠️ AUTOMATIC CIRCUIT BREAKER ALERTS TRIGGERED THIS CYCLE:\n" if is_en else "\n⚠️ ALERTAS DE SEGURIDAD EJECUTADAS EN ESTE CICLO (CIRCUIT BREAKER AUTOMÁTICO):\n"
            cb_lines = [f"- {e.get('reason')}" for e in cb_events]
            cb_text = cb_title + "\n".join(cb_lines) + "\n"

        if is_en:
            prompt = f"""
You are an institutional quantitative portfolio manager focused on disciplined Capital Preservation, Trend-Following Pullbacks, and Asymmetric Risk/Reward for an experimental ${initial_cap:.2f} USD portfolio.

CORE QUANTITATIVE RULES:
1. MARKET HOURS:
   - Check 'market_status'. If an asset is 'CERRADO' (Wall Street closed / weekends), DO NOT buy or sell it. Focus active liquidity on Cryptocurrencies ('ABIERTO (24/7)').
2. STRICT TREND FILTER (RULE OF GOLD - NEVER CATCH FALLING KNIVES):
   - Check 'is_above_sma20' and 'trend'.
   - NEVER BUY any asset that is in a DOWNTREND (below SMA20). In a bear trend, an oversold RSI is a warning of continuous collapse, NOT a buy signal.
   - ONLY BUY pullbacks in confirmed UPTREND assets (above SMA20). We only buy high-quality assets on a temporary dip, never collapsing assets.
3. REVERSAL CONFIRMATION TRIGGER:
   - Do NOT enter while the price is freefalling.
   - Only enter a pullback if 'rsi_1h' >= 32 AND 'change_1h_pct' > 0.0 (the 1-hour candle has turned green). This confirms the bounce has actually started.
4. ANTI-CORRELATION CONSTRAINT (MAX 1 CRYPTO POSITION):
   - NEVER hold more than ONE crypto position simultaneously (e.g. if SOL-USD is open, DO NOT open ETH-USD or BTC-USD). Crypto assets share ~90% downside correlation; holding multiple crypto positions creates dangerous duplicate risk.
5. ASYMMETRIC RISK/REWARD (LET WINNERS RUN, CUT LOSSES FAST):
   - Take-Profit Target: Aim for +3.0% to +5.0% gain (or if 'rsi_1h' > 72 with profit >= +2.5%). Do NOT sell prematurely for pennies (+0.5% or +0.8%).
   - Stop-Loss: Cut losses strictly if a position drops past -1.8% to -2.0%. The system code enforces a hard Circuit Breaker at -2.0%.
   - This ensures 1 winning trade (+3.5%) pays for 2 losing trades (-1.8%).
6. EQUITY HOLDING PATIENCE:
   - Stocks and ETFs (AAPL, NVDA, SPY, QQQ) move slower than crypto. Do NOT rotate or sell an equity position just because it has been flat for 24-48 hours. Give stocks time to play out unless stop-loss is hit.
7. POSITION SIZING:
   - Standard trade: $6.00 to $10.00 USD.
   - Maintain a minimum cash reserve of $4.00 USD.
8. OPERATIONAL MEMORY & JOURNAL ('memory_notes'):
   - Review your PREVIOUS JOURNAL NOTES. Evaluate if your plan materialized.
   - In 'memory_notes', write a concise tactical update for your next cycles in English: target prices, stop-loss levels, and what catalyst or confirmation you are waiting for.
9. LANGUAGE:
   - Write all your reasoning, market analysis, and memory_notes in clear, professional English.
{cb_text}
PREVIOUS OPERATIONAL MEMORY / JOURNAL:
"{mem_notes}"

RECENT TRADE HISTORY:
{trades_text}

CURRENT PORTFOLIO STATE (includes holding time):
{json.dumps(portfolio_summary, indent=2, ensure_ascii=False)}

CURRENT MARKET SNAPSHOT (with 1H RSI, Daily RSI, 1H/24H Changes, SMA20 Trend, and Market Status):
{json.dumps(market_snapshot, indent=2, ensure_ascii=False)}

Analyze the market and output your structured decision (BUY, SELL, or HOLD) along with your updated journal ('memory_notes').
"""
        else:
            prompt = f"""
Eres un gestor de inversiones cuantitativo enfocado en Preservación de Capital, Retrocesos en Tendencia Alcista y Ratio Riesgo/Beneficio Asimétrico para un portafolio experimental de ${initial_cap:.2f} USD.

REGLAS CUANTITATIVAS CLAVE:
1. OBJETIVO Y HORARIOS DE MERCADO:
   - Revisa 'market_status'. Si un activo está 'CERRADO' (Wall Street fuera de horario o fines de semana), NO lo operes. Enfoca la liquidez activa en Criptomonedas ('ABIERTO (24/7)').
2. FILTRO ESTRICTO DE TENDENCIA (REGLA DE ORO - PROHIBIDO CUCHILLOS CAYENDO):
   - Revisa 'is_above_sma20' y 'trend'.
   - PROHIBIDO COMPRAR activos en tendencia BAJISTA (bajo SMA20). En tendencia bajista, un RSI bajo es señal de desplome, NO de compra.
   - SOLO COMPRA retrocesos en activos con tendencia ALCISTA (sobre SMA20). Compramos activos fuertes con descuento temporal, nunca activos en caída libre.
3. GATILLO DE CONFIRMACIÓN DE REBOTE:
   - No compres mientras el precio siga cayendo.
   - Solo entra si 'rsi_1h' >= 32 Y 'change_1h_pct' > 0.0 (la última hora es verde). Esto confirma que el rebote ya inició.
4. REGLA ANTI-CORRELACIÓN (MÁXIMO 1 CRIPTO A LA VEZ):
   - PROHIBIDO tener más de UNA posición cripto al mismo tiempo (ej: si tienes SOL-USD, NO compres ETH-USD ni BTC-USD). Las criptos caen juntas el 90% de las veces; duplicar criptos duplica el riesgo.
5. RATIO RIESGO/BENEFICIO ASIMÉTRICO (DEJAR CORRER GANADORAS, CORTAR PÉRDIDAS RÁPIDO):
   - Take-Profit: Busca ganancias de +3.0% a +5.0% (o si 'rsi_1h' > 72 con ganancia >= +2.5%). NO vendas por centavos (+0.5% o +0.8%).
   - Stop-Loss: Corta estrictamente si una posición cae de -1.8% a -2.0%. El código tiene un Circuit Breaker a -2.0%.
   - Esto asegura que 1 ganadora (+3.5%) pague 2 perdedoras (-1.8%).
6. PACIENCIA CON ACCIONES TRADICIONALES:
   - Acciones y ETFs (AAPL, NVDA, SPY, QQQ) se mueven más lento. NO vendas una acción solo porque lleva 24-48 horas estancada. Dales tiempo a que desarrollen su movimiento.
7. TAMAÑO DE OPERACIÓN:
   - Operaciones normales: $6.00 a $10.00 USD.
   - Reserva mínima de efectivo: $4.00 USD.
8. MEMORIA Y BITÁCORA OPERATIVA ('memory_notes'):
   - Revisa tu bitácora previa y anota tus precios objetivo, stop-loss y qué confirmación esperas.
9. IDIOMA:
   - Explica tus razones, análisis y notas en español con claridad y convicción.
{cb_text}
BITÁCORA / MEMORIA DE TU CICLO ANTERIOR:
"{mem_notes}"

ÚLTIMAS OPERACIONES REGISTRADAS:
{trades_text}

ESTADO ACTUAL DE TU PORTAFOLIO:
{json.dumps(portfolio_summary, indent=2, ensure_ascii=False)}

DATOS ACTUALES DEL MERCADO:
{json.dumps(market_snapshot, indent=2, ensure_ascii=False)}

Analiza la información y genera tu decisión estructurada (BUY, SELL o HOLD) junto con tu actualización de bitácora ('memory_notes').
"""

        models_to_try = [
            self.model_name,
            "gemini-flash-latest"
        ]
        seen = set()
        models = [m for m in models_to_try if not (m in seen or seen.add(m))]

        last_error = None
        for m in models:
            for attempt in range(2):
                try:
                    print(f"   [Consulting model: {m} (attempt {attempt+1})]...", flush=True)
                    response = self.client.models.generate_content(
                        model=m,
                        contents=prompt,
                        config=types.GenerateContentConfig(
                            response_mime_type="application/json",
                            response_schema=AgentDecision,
                            temperature=0.2,
                        ),
                    )
                    data = json.loads(response.text)
                    return AgentDecision(**data)
                except Exception as e:
                    last_error = e
                    error_str = str(e).lower()
                    if any(k in error_str for k in ["503", "504", "deadline", "unavailable", "timed out", "timeout", "handshake"]):
                        print(f"   ⚠️ Congestion/Network error in {m} (attempt {attempt+1}): {e}. Waiting 3s...", flush=True)
                        time.sleep(3)
                    else:
                        print(f"   ⚠️ Model {m} incompatible ({e}), trying next...", flush=True)
                        break

        # Fallback seguro: HOLD si todos fallan
        print(f"[Error in Gemini API]: {last_error}")
        fallback_analysis = (
            f"Temporary notice from Gemini ({last_error}). Safety HOLD rule applied to protect positions."
            if is_en else
            f"Aviso temporal de Gemini ({last_error}). Se aplica regla de seguridad HOLD para proteger posiciones."
        )
        fallback_notes = (
            "Holding positions and previous plan while connection with Gemini stabilizes."
            if is_en else
            "Mantener posiciones y plan previo mientras se estabiliza la conexión con Gemini."
        )
        fallback_reason = (
            "Temporary connection issue, safely holding current positions."
            if is_en else
            "Error temporal de conexión, manteniendo posiciones de forma segura."
        )

        return AgentDecision(
            market_analysis=fallback_analysis,
            memory_notes=fallback_notes,
            actions=[TradeAction(action="HOLD", ticker="PORTFOLIO", confidence=1.0, reasoning=fallback_reason)]
        )
