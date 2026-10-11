# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 12:30:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.40 USD** | **$40.40 USD** | 🟢 **+1.01%** ($+0.40) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.340197 | $109.29 | $109.72 | $37.33 | 📈 +0.39% |
| `ETH-USD` | 0.001228 | $2504.75 | $2506.38 | $3.08 | 📈 +0.07% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa con SOL-USD (RSI en 21.6) y ETH-USD (RSI en 28.9), lo cual presenta una oportunidad clásica de rebote por reversión a la media (Mean Reversion). En contraste, activos tradicionales como MSFT entran en sobrecompra (RSI 72.3). Dado que el capital está totalmente invertido en SOL y ETH y no hay efectivo libre, mantendremos las posiciones actuales para capturar el rebote técnico inminente sin realizar ventas prematuras, ya que ninguna ha alcanzado el take-profit del 2.5% ni el stop-loss."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 90%): SOL-USD se encuentra en un nivel de sobreventa extrema (RSI 14 en 21.6) tras una caída semanal del 9.14%. Mantenemos la posición para capturar el rebote técnico hacia la media, ya que la pérdida está contenida y el potencial alcista a corto plazo es alto.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 12:10` | 🟢 BUY | `ETH-USD` | $3.08 | $2504.75 | ETH-USD se encuentra en un estado de sobreventa extrema con un RSI de 28.6 y una caída sem... |
| `2026-10-11 11:00` | 🟢 BUY | `SOL-USD` | $12.00 | $109.33 | Aprovechamos la altísima sobreventa en SOL-USD (RSI de 21.2 y -9.46% en 7 días) para incre... |
| `2026-10-11 11:00` | 🔴 SELL | `ETH-USD` | $10.00 | $2499.66 | ETH-USD está estancado con un PnL cercano a 0% (-0.03%). Vendemos la posición completa par... |
| `2026-10-11 10:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2500.42 | ETH-USD presenta un RSI de 28.2 en profunda sobreventa y una caída semanal del 7.77%, cump... |
| `2026-10-11 10:50` | 🔴 SELL | `SOL-USD` | $10.93 | $109.32 | Liberamos liquidez de SOL-USD que se encuentra estancada para aprovechar la oportunidad de... |

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
