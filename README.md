# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 23:20:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.33 USD** | **$40.44 USD** | 🟢 **+1.09%** ($+0.44) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.91 | $20.16 | 📈 +0.81% |
| `ETH-USD` | 0.006448 | $2481.58 | $2506.98 | $16.16 | 📈 +1.02% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con el sector tecnológico y los índices principales (QQQ, SPY) manteniendo una tendencia alcista moderada, mientras que las criptomonedas (SOL-USD y ETH-USD) se encuentran en zonas de sobreventa técnica extrema con RSI de 23.7 y 28.4 respectivamente, tras caídas semanales significativas. El efectivo actual es bajo ($4.11 USD), cumpliendo con la regla de mantener solo la reserva mínima. Dado que nuestras posiciones actuales en SOL-USD y ETH-USD aún no han alcanzado el objetivo de toma de ganancias del +2.5% y mantienen una ligera ganancia sin romper los stop-loss, y no disponemos de capital libre significativo para nuevas rotaciones agresivas, la decisión óptima es mantener las posiciones actuales para capturar el rebote esperado por sobreventa."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra en condición de sobreventa extrema (RSI 23.7) tras una caída semanal del -9.56%. Mantenemos la posición ya que se encuentra dentro de los márgenes del stop-loss y buscamos el rebote técnico hacia el objetivo de +2.5% de ganancia.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un RSI de 28.4 en zona de sobreventa con un rendimiento positivo actual del +1.02%. Esperamos que continúe el impulso alcista a corto plazo para asegurar ganancias al llegar al umbral de take-profit.

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
