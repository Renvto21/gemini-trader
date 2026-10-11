# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 03:00:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.28 USD** | **$40.28 USD** | 🟢 **+0.71%** ($+0.28) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.220969 | $109.11 | $109.28 | $24.15 | 📈 +0.16% |
| `ETH-USD` | 0.006448 | $2481.58 | $2502.51 | $16.13 | 📈 +0.84% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado general muestra un tono mixto con soporte en los índices tecnológicos y SPY, mientras que las criptomonedas experimentan una fuerte presión bajista semanal previa pero presentan condiciones extremas de sobreventa técnica (RSI inferior a 30 en SOL y ETH), lo cual activa nuestra estrategia táctica de mean reversion y captura de rebotes rápidos."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra en un estado extremo de sobreventa con un RSI de 21.5 tras una caída semanal del 10%. Aunque está bajo la SMA20, la regla de cazar rebotes en cripto nos indica mantener y esperar la consolidación del rebote alcista hacia nuestro objetivo de take-profit sin vender prematuramente.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un RSI de 27.7, también en zona de sobreventa profunda, manteniendo una leve ganancia positiva del 0.84%. Mantenemos la posición para capturar el impulso de recuperación alcista esperado en activos digitales sobrevendidos.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 02:20` | 🟢 BUY | `SOL-USD` | $4.11 | $109.54 | SOL-USD se encuentra en extrema sobreventa técnica con un RSI de 22.4 y una caída semanal ... |
| `2026-10-10 12:10` | 🔴 SELL | `MSFT` | $4.11 | $535.07 | MSFT ha alcanzado un RSI de 72.3 (sobrecompra) cumpliendo con la regla táctica de toma de ... |
| `2026-10-10 12:00` | 🟢 BUY | `MSFT` | $4.11 | $535.07 | Aprovechamos el capital liberado de GLD para entrar en MSFT, que muestra un fuerte momentu... |
| `2026-10-10 12:00` | 🔴 SELL | `GLD` | $4.11 | $384.58 | Liberamos la totalidad de la posición en GLD ya que se encuentra estancada con 0% de PnL y... |
| `2026-10-10 11:50` | 🟢 BUY | `GLD` | $4.11 | $384.58 | Aprovechamos el efectivo disponible para cazar un rebote por sobreventa en GLD, cuyo RSI s... |

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
