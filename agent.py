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
    memory_notes: str = Field(
        description="Bitácora mental para los siguientes ciclos: tu plan táctico, objetivos de salida o stop-loss de posiciones abiertas, y qué evento o confirmación estás esperando."
    )
    actions: List[TradeAction] = Field(description="Lista de acciones a tomar (máximo 1 o 2 operaciones por ciclo)")

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
        memory_context: Optional[Dict[str, Any]] = None
    ) -> AgentDecision:
        initial_cap = portfolio_summary.get('initial_capital', 40.0)
        
        mem_notes = memory_context.get("previous_notes", "Sin notas previas. Primera ejecución con bitácora.") if memory_context else "Sin notas previas."
        recent_trades = memory_context.get("recent_trades", []) if memory_context else []
        cb_events = memory_context.get("circuit_breakers", []) if memory_context else []
        
        trades_text = ""
        if recent_trades:
            trades_lines = []
            for t in recent_trades:
                ts = t.get("timestamp", "")[:16].replace("T", " ")
                trades_lines.append(f"- [{ts}] {t.get('action')} {t.get('ticker')}: ${t.get('amount_usd', 0):.2f} @ ${t.get('price', 0):.2f}. Motivo: {t.get('reason', '')[:100]}")
            trades_text = "\n".join(trades_lines)
        else:
            trades_text = "No hay operaciones recientes registradas."

        cb_text = ""
        if cb_events:
            cb_lines = [f"- {e.get('reason')}" for e in cb_events]
            cb_text = f"\n⚠️ ALERTAS DE SEGURIDAD EJECUTADAS EN ESTE CICLO (CIRCUIT BREAKER AUTOMÁTICO):\n" + "\n".join(cb_lines) + "\n"

        prompt = f"""
Eres un gestor de inversiones cuantitativo y agresivo enfocado en Crecimiento Acelerado, Momentum y Rebotes Técnicos (Mean Reversion) para un portafolio experimental de inversión de ${initial_cap:.2f} USD.

ESTRATEGIA Y REGLAS OPERATIVAS (TÁCTICA AGRESIVA):
1. OBJETIVO Y HORARIOS DE MERCADO:
   - Revisa el campo 'market_status'. Si un activo está 'CERRADO' (Wall Street fuera de horario o fines de semana), NO intentes comprarlo ni venderlo. Enfoca el 100% de la liquidez activa en Criptomonedas ('ABIERTO 24/7').
2. CAZAR REBOTES CON INDICADORES INTRADIARIOS Y DIARIOS:
   - 'rsi_1h' y 'change_1h_pct': Muestran el pulso de corto plazo de las últimas horas. Si 'rsi_1h' sale de sobreventa extrema (< 35) y 'change_1h_pct' se torna positivo, entra con decisión buscando el rebote.
   - 'rsi_daily' y 'trend': Muestran el contexto general (soporte macro).
3. TAMAÑO DINÁMICO DE OPERACIÓN:
   - Operaciones normales: $5.00 a $8.00 USD.
   - En oportunidades de ALTA CONVICCIÓN (confianza >= 85%): puedes asignar hasta $10.00 o $12.00 USD para maximizar el impacto de la jugada.
4. TOMA RÁPIDA DE GANANCIAS (TAKE-PROFIT):
   - Si una posición en cartera acumula una ganancia de +2.0% a +3.5%, o su 'rsi_1h' entra en sobrecompra (> 70), VENDE (total o parcialmente) para asegurar las ganancias en efectivo y buscar la siguiente oportunidad. ¡Rota el capital!
5. STOP-LOSS ESTRICTO Y CIRCUIT BREAKER:
   - El sistema cuenta con un Circuit Breaker automático en código a -3.0%. Tú debes actuar antes: si una posición pierde más de -2.0% o rompe su soporte a la baja, VENDE para cortar la pérdida y proteger la cuenta.
6. RESERVA DE LIQUIDEZ MÍNIMA:
   - Mantén solo una reserva mínima de efectivo de $4.00 USD. Todo el resto del efectivo debe estar trabajando activamente si detectas oportunidades atractivas en activos abiertos.
7. ROTACIÓN ACTIVA DE CAPITAL:
   - Si tienes posiciones estancadas (ganancia/pérdida cercana a 0% sin momentum) y surge una oportunidad con fuerte impulso en Cripto o Tech, puedes vender la posición lenta para financiar la nueva jugada de alto potencial.
8. GESTIÓN DEL TIEMPO Y CONTINUIDAD (MEMORIA Y BITÁCORA OPERATIVA):
   - Revisa tu BITÁCORA DEL CICLO ANTERIOR. Evalúa si tus expectativas se cumplieron o si debes ajustar el plan.
   - Revisa el campo 'holding_time' de las posiciones abiertas: si una posición lleva varias horas/ciclos abierta sin mostrar el rebote esperado, no repitas la misma justificación en bucle; asume que el impulso falló y rota el capital hacia activos con mayor dinamismo.
   - En 'memory_notes', redacta tu bitácora actualizada para tu próximo ciclo: anota tus precios objetivo (take-profit/stop-loss), qué catalizador esperas, o qué condición te haría salir o rotar.
9. Explica tus razones en español con claridad y convicción.
{cb_text}
BITÁCORA / MEMORIA DE TU CICLO ANTERIOR:
"{mem_notes}"

ÚLTIMAS OPERACIONES REGISTRADAS:
{trades_text}

ESTADO ACTUAL DE TU PORTAFOLIO (incluye tiempo abierto 'holding_time' por posición):
{json.dumps(portfolio_summary, indent=2, ensure_ascii=False)}

DATOS ACTUALES DEL MERCADO (Precios, RSI 1H, RSI Diario, Cambio 1H/24H/7D, Tendencia y Noticias):
{json.dumps(market_snapshot, indent=2, ensure_ascii=False)}

Analiza la información y genera tu decisión estructurada (BUY, SELL o HOLD) junto con tu actualización de bitácora ('memory_notes').
"""

        models_to_try = [
            self.model_name,
            "gemini-flash-latest"
        ]
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
            memory_notes="Mantener posiciones y plan previo mientras se estabiliza la conexión con Gemini.",
            actions=[TradeAction(action="HOLD", ticker="PORTFOLIO", confidence=1.0, reasoning="Error temporal de conexión, manteniendo posiciones de forma segura.")]
        )
