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
        self.client = genai.Client(api_key=self.api_key)
        self.model_name = model_name

    def evaluate_market_and_decide(
        self,
        portfolio_summary: Dict[str, Any],
        market_snapshot: Dict[str, Any]
    ) -> AgentDecision:
        prompt = f"""
Eres un gestor de inversiones cuantitativo y prudente. Tu objetivo es hacer crecer de manera sostenible un pequeño portafolio experimental de inversión inicial de $20.00 USD.

REGLAS DE GESTIÓN DE RIESGO:
1. Capital inicial muy pequeño: $20.00 USD. Máxima prudencia.
2. NUNCA arriesgues todo el capital en un solo activo. Máximo $5.00 a $8.00 USD por compra.
3. Mantén siempre una reserva de efectivo (cash) de al menos $3.00 USD para imprevistos o caídas.
4. Si el mercado está indeciso, sobrecalentado (RSI > 70) o las noticias son negativas, la decisión más inteligente es HOLD.
5. Solo compra activos con tendencia favorable, RSI en niveles atractivos o catalizadores positivos claros.
6. Si una posición tiene ganancias considerables o el activo rompe soporte a la baja, puedes decidir SELL para tomar ganancias o cortar pérdidas.
7. Explica tus razones en español con claridad.

ESTADO ACTUAL DE TU PORTAFOLIO:
{json.dumps(portfolio_summary, indent=2, ensure_ascii=False)}

DATOS ACTUALES DEL MERCADO (Precios, RSI 14, Tendencia y Noticias):
{json.dumps(market_snapshot, indent=2, ensure_ascii=False)}

Analiza la información y genera tu decisión estructurada.
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
                    error_str = str(e)
                    if "503" in error_str or "UNAVAILABLE" in error_str:
                        print(f"   ⚠️ Pico de demanda (503) en {m}. Esperando 4 segundos...", flush=True)
                        time.sleep(4)
                    else:
                        print(f"   ⚠️ Modelo {m} no disponible ({e}), pasando al siguiente...", flush=True)
                        break

        # Fallback seguro: HOLD si todos fallan
        print(f"[Error en Gemini API]: {last_error}")
        return AgentDecision(
            market_analysis=f"Aviso temporal de Gemini ({last_error}). Se aplica regla de seguridad HOLD para proteger posiciones.",
            actions=[TradeAction(action="HOLD", ticker="PORTFOLIO", confidence=1.0, reasoning="Error temporal de conexión, manteniendo posiciones de forma segura.")]
        )
