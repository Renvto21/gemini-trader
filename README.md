# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 19:20:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.37 USD** | **$40.48 USD** | 🟢 **+1.20%** ($+0.48) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.17 | $20.21 | 📈 +1.05% |
| `ETH-USD` | 0.006448 | $2481.58 | $2505.94 | $16.16 | 📈 +0.98% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con el sector tecnológico y los índices principales (SPY, QQQ) manteniendo una tendencia alcista estable. En el sector cripto, SOL-USD (RSI 24.6) y ETH-USD (RSI 28.3) continúan profundamente en zona de sobreventa técnica tras caídas semanales, lo que presenta una excelente oportunidad de acumulación para un rebote de reversión a la media (Mean Reversion). Dado que nuestras posiciones actuales en SOL-USD y ETH-USD se encuentran con ganancias moderadas (+1.05% y +0.98% respectivamente) y el efectivo disponible es de apenas $4.11 USD (alineado con nuestra regla de reserva mínima), mantendremos las posiciones actuales para permitirles madurar hacia el objetivo de take-profit del +2.5% o superior, maximizando la eficiencia del capital sin realizar ventas prematuras ni compras adicionales por falta de liquidez."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): La posición en SOL-USD se mantiene con un rendimiento positivo del +1.05%. El RSI de 14 días en 24.6 indica una condición de sobreventa extrema, lo que respalda nuestra tesis de rebote técnico. Mantenemos la posición para capturar el objetivo de ganancia del +2.5% o más.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD muestra un comportamiento similar con un RSI de 28.3 y una ganancia actual del +0.98%. La estructura de mercado sugiere un potencial rebote inminente hacia la media, por lo que conservamos el activo para optimizar el rendimiento del portafolio.

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
