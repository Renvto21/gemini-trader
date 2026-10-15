# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 02:20:35`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$17.61 USD** | **$20.87 USD** | **$38.49 USD** | 🔴 **-3.78%** ($-1.51) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 15h 29m |
| `BTC-USD` | 0.000061 | $81640.68 | $81116.53 | $4.97 | 📉 -0.64% | 5h 9m |
| `ETH-USD` | 0.002539 | $2362.71 | $2362.36 | $6.00 | 📉 -0.01% | 1h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra completamente cerrado, por lo que toda la atención táctica se traslada al mercado de criptomonedas (abierto 24/7). Los activos digitales como BTC-USD y ETH-USD muestran una tendencia bajista de fondo bajo la SMA20, pero ETH-USD y SOL-USD presentan niveles de RSI diario muy deprimidos (< 30), lo que abre la puerta a potenciales rebotes por sobreventa extrema (mean reversion). Mantenemos nuestras posiciones actuales esperando confirmación de impulso alcista en los marcos temporales de 1 hora."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): La posición en ETH-USD lleva poco tiempo abierta (1h 9m) y se encuentra operando prácticamente tablas (-0.01%). El RSI diario está profundamente oversold en 27.4 y el RSI de 1h se encuentra en 30.0, manteniendo el potencial intacto para un rebote técnico inminente de corto plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en AAPL, BTC-USD y ETH-USD. Monitorear de cerca ETH-USD y BTC-USD en busca de un incremento en el RSI de 1h y un cambio porcentual positivo que valide un rebote técnico para asegurar ganancias entre +2.0% y +3.5%. Ejecutar stop-loss estricto en -2.0% si alguna posición rompe soportes a la baja para proteger el capital. No sobrecargar la exposición hasta ver un cambio de tendencia más claro en el mercado cripto."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **54** | 🎯 **40.7%** (22W / 18L / 14BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 01:10` | 🟢 BUY | `ETH-USD` | $6.00 | $2362.71 | ETH-USD presenta un RSI de 1h extremadamente bajo en 23.5 saliendo de sobreventa y un camb... |
| `2026-10-14 23:30` | 🔴 SELL (-0.30$) | `SOL-USD` | $9.70 | $101.32 | La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin ... |
| `2026-10-14 23:30` | 🔴 SELL (-0.32$) | `ETH-USD` | $9.68 | $2340.86 | 🚨 STOP-LOSS AUTOMÁTICO (CIRCUIT BREAKER): Pérdida de -3.20% superó el límite de seguridad ... |
| `2026-10-14 21:10` | 🟢 BUY | `BTC-USD` | $5.00 | $81640.68 | BTC-USD presenta un RSI de 1h en 24.9 (sobreventa extrema) y liquidez disponible suficient... |
| `2026-10-14 19:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2418.34 | ETH-USD presenta un RSI de 1h en 22.0 (sobreventa extrema) y un cambio de 1h que comienza ... |

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
