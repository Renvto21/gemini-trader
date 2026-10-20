# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 07:50:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.47 USD** | **$38.47 USD** | 🔴 **-3.83%** ($-1.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 21h 9m |
| `ETH-USD` | 0.004178 | $2393.62 | $2383.64 | $9.96 | 📉 -0.42% | 18h 59m |
| `SOL-USD` | 0.096034 | $104.13 | $103.97 | $9.98 | 📉 -0.15% | 15h 9m |
| `BTC-USD` | 0.000105 | $81767.70 | $81446.49 | $8.53 | 📉 -0.39% | 14h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 pero con un sesgo lateral a bajista de corto plazo, con un RSI de 1 hora recuperándose ligeramente pero sin mostrar la fuerza de volumen necesaria para un rebote explosivo. Los mercados tradicionales (QQQ) se encuentran cerrados. El portafolio actual registra un PnL total de -3.83%, sin embargo, ninguna posición ha tocado el stop-loss estricto de -2.0%. Dado que no disponemos de efectivo libre en este momento y que el momentum técnico actual es moderado, optamos por mantener las posiciones vigentes y monitorear de cerca la evolución del RSI en los criptoactivos."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 60%): La posición se mantiene dentro de parámetros aceptables con una pérdida menor de -0.39%. Aunque el RSI de 1 hora está en 36.3 y muestra un cambio positivo leve (+0.08%), no hay suficiente liquidez en efectivo para incrementar exposición y el movimiento aún carece de la fuerza compradora necesaria para justificar una rotación.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (QQQ, ETH-USD, SOL-USD, BTC-USD) ya que las pérdidas se mantienen acotadas por debajo del umbral de -2.0%. En el próximo ciclo, si alguna criptomoneda experimenta un impulso alcista que eleve su RSI de 1 hora por encima de 70, realizaremos una toma de beneficios parcial o total para liberar liquidez. Si alguna posición rompe a la baja el soporte crítico con una pérdida cercana al -2.0%, ejecutaremos una venta inmediata para proteger el capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 23:00` | 🟢 BUY | `BTC-USD` | $4.00 | $81646.39 | BTC-USD presenta un RSI de 1 hora en 27.7, nivel de sobreventa profunda ideal para un rebo... |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |

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
