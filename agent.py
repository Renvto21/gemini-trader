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
    amount_usd: Optional[float] = Field(default=0.0, description="Monto en USD si la acción es BUY")
    shares: Optional[float] = Field(default=0.0, description="Cantidad de acciones o cripto a vender si es SELL")
    confidence: float = Field(description="Nivel de convicción entre 0.0 y 1.0")
    reasoning: str = Field(description="Explicación detallada del por qué de la decisión")

class AgentDecision(BaseModel):
    market_analysis: str = Field(description="Resumen del estado general del mercado y sentimiento macro")
    actions: List[TradeAction] = Field(description="Lista de acciones a tomar (máximo 1 o 2 operaciones por ciclo)")

class TradingAgent:
    def __init__(self, api_key: Optional[str] = None, model_name: str = "gemini-3.5-flash"):
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
        market_snapshot: Dict[str, Any]
    ) -> AgentDecision:
        initial_cap = portfolio_summary.get('initial_capital', 40.0)
        prompt = f"""
Eres un gestor de inversiones cuantitativo y agresivo enfocado en Crecimiento Acelerado, Momentum y Rebotes Técnicos (Mean Reversion) para un portafolio experimental de inversión de ${initial_cap:.2f} USD.

ESTRATEGIA Y REGLAS OPERATIVAS (TÁCTICA AGRESIVA):
1. OBJETIVO: Capturar movimientos rápidos del +2% al +6% en activos de alta volatilidad (Cripto como SOL-USD, ETH-USD, BTC-USD y Tech de alto beta como NVDA, QQQ) y rotar el capital con dinamismo.
2. CAZAR REBOTES EN CRIPTO Y TECH: Si criptomonedas (SOL, ETH, BTC) o acciones están en sobreventa técnica (RSI < 38) o muestran señales de reversión alcista, entra con decisión buscando el rebote. No temas a la volatilidad, úsala a tu favor.
3. TAMAÑO DINÁMICO DE OPERACIÓN:
   - Operaciones normales: $5.00 a $8.00 USD.
   - En oportunidades de ALTA CONVICCIÓN (confianza >= 85%): puedes asignar hasta $10.00 o $12.00 USD para maximizar el impacto de la jugada.
4. TOMA RÁPIDA DE GANANCIAS (TAKE-PROFIT):
   - Si una posición en cartera acumula una ganancia de +2.5% o superior, o su RSI entra en sobrecompra (> 70), VENDE (total o parcialmente) para asegurar las ganancias en efectivo y buscar la siguiente oportunidad con descuento. ¡Rota el capital!
5. STOP-LOSS ESTRICTO:
   - Si una posición cae más de -2.5% a -3.0% y rompe a la baja, VENDE de inmediato para cortar la pérdida. Es preferible asumir una pequeña pérdida de centavos que quedar atrapado en caídas profundas.
6. RESERVA DE LIQUIDEZ MÍNIMA:
   - Mantén solo una reserva mínima de efectivo de $4.00 USD. Todo el resto del efectivo debe estar trabajando activamente si detectas oportunidades atractivas en el mercado.
7. ROTACIÓN ACTIVA DE CAPITAL:
   - Si tienes posiciones estancadas (ganancia/pérdida cercana a 0% sin momentum) y surge una oportunidad con fuerte impulso en Cripto o Tech, puedes vender la posición lenta para financiar la nueva jugada de alto potencial.
8. Explica tus razones en español con claridad y convicción.

ESTADO ACTUAL DE TU PORTAFOLIO:
{json.dumps(portfolio_summary, indent=2, ensure_ascii=False)}

DATOS ACTUALES DEL MERCADO (Precios, RSI 14, Tendencia y Noticias):
{json.dumps(market_snapshot, indent=2, ensure_ascii=False)}

Analiza la información y genera tu decisión estructurada (BUY, SELL o HOLD).
"""

        models_to_try = [self.model_name, "gemini-3.5-flash", "gemini-flash-latest", "gemini-3.8-flash"]
        # Eliminar duplicados manteniendo orden
        seen = set()
        models = [m for m in models_to_try if not (m in seen or seen.add(m))]

        last_error = None
        for m in models:
            for attempt in range(2):
                try:
                    print(f"   [Consultando modelo: {m} (intento {attempt+1})]...", flush=True)
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
                        print(f"   ⚠️ Congestión/Red en {m} (intento {attempt+1}): {e}. Esperando 3s y reintentando...", flush=True)
                        time.sleep(3)
                    else:
                        print(f"   ⚠️ Modelo {m} incompatible ({e}), pasando al siguiente...", flush=True)
                        break

        # Fallback seguro: HOLD si todos fallan
        print(f"[Error en Gemini API]: {last_error}")
        return AgentDecision(
            market_analysis=f"Aviso temporal de Gemini ({last_error}). Se aplica regla de seguridad HOLD para proteger posiciones.",
            actions=[TradeAction(action="HOLD", ticker="PORTFOLIO", confidence=1.0, reasoning="Error temporal de conexión, manteniendo posiciones de forma segura.")]
        )
