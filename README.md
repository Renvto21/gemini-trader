# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 19:40:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.40 USD** | **$40.52 USD** | 🟢 **+1.29%** ($+0.52) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.40 | $20.25 | 📈 +1.26% |
| `ETH-USD` | 0.006448 | $2481.58 | $2505.19 | $16.15 | 📈 +0.95% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo mixto con criptomonedas fuertemente sobrevendidas tras caídas semanales pero presentando RSI en zona de capitulación extrema (SOL-USD en 25.4 y ETH-USD en 28.1), ideales para capturar rebotes agresivos de reversión a la media. Las acciones tecnológicas y los índices principales se mantienen estables o alcistas, destacando MSFT en sobrecompra (RSI 72.3). Nuestra liquidez actual es muy ajustada y las posiciones actuales no han alcanzado el objetivo de take-profit del +2.5%, por lo que mantendremos la exposición actual para dejar madurar las ganancias."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD tiene un RSI de 25.4 indicando una sobreventa extrema. Aunque la tendencia es bajista, el potencial de rebote técnico es alto y nos encontramos dentro de una ganancia del 1.26%, manteniendo la posición para buscar el objetivo del +2.5%.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD presenta un RSI de 28.1, también en zona de sobreventa profunda. La posición muestra un ligero rendimiento positivo y preferimos retenerla para capturar el rebote técnico hacia la media sin incurrir en costos de rotación innecesarios.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-10 12:10` | 🔴 SELL | `MSFT` | $4.11 | $535.07 | MSFT ha alcanzado un RSI de 72.3 (sobrecompra) cumpliendo con la regla táctica de toma de ... |
| `2026-10-10 12:00` | 🟢 BUY | `MSFT` | $4.11 | $535.07 | Aprovechamos el capital liberado de GLD para entrar en MSFT, que muestra un fuerte momentu... |
| `2026-10-10 12:00` | 🔴 SELL | `GLD` | $4.11 | $384.58 | Liberamos la totalidad de la posición en GLD ya que se encuentra estancada con 0% de PnL y... |
| `2026-10-10 11:50` | 🟢 BUY | `GLD` | $4.11 | $384.58 | Aprovechamos el efectivo disponible para cazar un rebote por sobreventa en GLD, cuyo RSI s... |
| `2026-10-09 19:00` | 🟢 BUY | `ETH-USD` | $5.00 | $2482.07 | ETH-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.0. Utilizando el c... |

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
