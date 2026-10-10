# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 15:40:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.38 USD** | **$40.49 USD** | 🟢 **+1.23%** ($+0.49) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.14 | $20.21 | 📈 +1.03% |
| `ETH-USD` | 0.006448 | $2481.58 | $2508.93 | $16.18 | 📈 +1.10% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra divergencias interesantes. Las criptomonedas principales como SOL-USD y ETH-USD se encuentran en niveles de sobreventa técnica extrema con RSI de 24.5 y 28.7 respectivamente, lo cual activa nuestra estrategia de Mean Reversion para buscar rebotes rápidos. Por otro lado, activos tecnológicos como MSFT muestran sobrecompra (RSI 72.3) tras un fuerte impulso. Mantenemos nuestras posiciones actuales en cripto a la espera de que los rebotes alcancen nuestro objetivo de take-profit, y aprovechamos el efectivo disponible para retener liquidez según las reglas operativas."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD está en clara sobreventa con un RSI de 24.5, lo que cumple perfectamente con la estrategia de cazar rebotes. Mantenemos la posición para capturar el movimiento alcista hacia el objetivo de take-profit del +2.5%.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD presenta un RSI de 28.7 en zona de sobreventa y la pérdida actual está contenida. Esperamos el rebote técnico inminente para asegurar ganancias y rotar el capital de manera dinámica.

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
