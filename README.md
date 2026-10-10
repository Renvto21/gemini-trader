# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 17:00:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.43 USD** | **$40.54 USD** | 🟢 **+1.35%** ($+0.54) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.33 | $20.24 | 📈 +1.20% |
| `ETH-USD` | 0.006448 | $2481.58 | $2511.00 | $16.19 | 📈 +1.19% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra signos de sobreventa extrema con ETH-USD (RSI 29.1) y SOL-USD (RSI 25.1) operando en niveles de profundo descuento tras caídas semanales, lo que activa nuestra estrategia de captura de rebotes por reversión a la media. En el sector tecnológico tradicional, MSFT ha entrado en territorio de sobrecompra (RSI 72.3), lo que indica cautela. Nuestro portafolio se mantiene operando con un capital total de $40.54 USD y una liquidez ajustada de $4.11 USD. Dado que nuestras posiciones actuales en SOL-USD y ETH-USD aún no alcanzan la meta de take-profit del +2.5% (están en +1.2% y +1.19% respectivamente) y no han tocado ningún stop-loss, y considerando que la liquidez disponible cumple estrictamente con el mínimo requerido de $4.00 USD, decidimos mantener la estructura actual de la cartera para permitir que el momentum alcista diario termine de consolidar la ganancia objetivo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): La posición mantiene un rendimiento positivo de +1.2% tras el rebote diario, operando en una zona de sobreventa previa muy clara (RSI 25.1). Dado que el precio actual está cerca de consolidar nuestro objetivo de take-profit (+2.5%), optamos por mantener y no vender todavía para maximizar el rendimiento del rebote técnico.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH-USD se encuentra con un PnL de +1.19% y un RSI de 29.1 recuperándose desde mínimos semanales. Mantenemos la posición para capturar el movimiento alcista hacia la zona de take-profit establecida sin incurrir en costos de rotación prematuros.

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
