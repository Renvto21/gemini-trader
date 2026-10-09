# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 20:11:35`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.03 USD** | **$40.14 USD** | 🟢 **+0.36%** ($+0.14) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.07 | $20.01 | 📈 +0.04% |
| `ETH-USD` | 0.006448 | $2481.58 | $2485.34 | $16.02 | 📈 +0.15% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado de renta variable tradicional (QQQ, SPY, MSFT) mantiene sesgo alcista pero con señales de sobrecompra en megacaps, mientras que el sector cripto atraviesa una fase de capitulación técnica extrema con RSI en niveles críticos de sobreventa profunda (SOL en 20.3 y ETH en 25.5). Con BTC rebotando +1.08% en las últimas 24h, el escenario técnico favorece un inminente rebote por reversión a la media (mean reversion) en SOL y ETH, donde se concentra nuestro capital."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL se encuentra en una zona de sobreventa extrema con RSI 14 en 20.3 tras una corrección semanal de -8.84%. La posición actual está equilibrada (+0.04% PnL) y lista para capturar el rebote proyectado de +2.5% a +5.0%. No se activa take-profit ni stop-loss, y el efectivo libre disponible ($0.11 sobre el mínimo de reserva de $4.00) no permite aumentar posición sin comprometer el buffer de liquidez.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH muestra agotamiento vendedor con RSI 14 en 25.5 y leve recuperación intradiaria (+0.54%). Con el PnL actual en +0.15%, nos mantenemos firmes esperando el impulso alcista hacia el umbral de toma de beneficios (+2.5%). Mantener la posición maximiza la exposición al catalizador de rebote cripto sin vulnerar la reserva obligatoria de $4.00 USD en efectivo.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-09 19:00` | 🟢 BUY | `ETH-USD` | $5.00 | $2482.07 | ETH-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.0. Utilizando el c... |
| `2026-10-09 19:00` | 🔴 SELL | `NVDA` | $4.99 | $229.28 | Rotación activa de capital. NVDA se encuentra estancada con un rendimiento de -0.16% y un ... |
| `2026-10-09 18:50` | 🟢 BUY | `SOL-USD` | $5.00 | $108.91 | Oportunidad de alta convicción por sobreventa extrema. SOL-USD tiene un RSI de 20.2 tras u... |
| `2026-10-09 18:50` | 🔴 SELL | `QQQ` | $5.00 | $751.27 | Rotación de capital activo. QQQ se encuentra estancado con rendimiento plano (-0.06%) y si... |
| `2026-10-09 18:40` | 🟢 BUY | `SOL-USD` | $5.00 | $109.02 | SOL-USD está extremadamente sobrevendido con un RSI de 20.3. Ejecutamos una compra agresiv... |

---

<details>
<summary>⚙️ Ver configuración técnica y comandos locales</summary>

### Comandos disponibles
* **Ver estado actual:** `python main.py --status`
* **Ejecutar 1 ciclo de prueba:** `python main.py --run-once`
* **Ejecutar en bucle local:** `python main.py --loop --interval 300`

### Módulos del sistema
* `main.py`: Orquestador principal del bot.
* `dashboard.py`: Generador del panel dinámico en README.
* `agent.py`: Conexión con Gemini Flash y reglas de riesgo.
* `portfolio.py`: Registro de operaciones, cálculo de saldo y PnL.
* `market_data.py`: Descarga y cálculo técnico con yfinance.
* `portfolio.json`: Base de datos de posiciones.
</details>
