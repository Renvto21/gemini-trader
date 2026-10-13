# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 07:40:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.38 USD** | **$39.38 USD** | 🔴 **-1.55%** ($-0.62) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $106.42 | $31.41 | 📉 -0.70% |
| `ETH-USD` | 0.003192 | $2506.03 | $2495.66 | $7.97 | 📉 -0.41% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa en SOL-USD (RSI de 25.4) y debilidad persistente en ETH-USD, aunque ambas se encuentran en nuestra cartera con pérdidas moderadas. Mantenemos una postura agresiva y de rotación táctica: SOL-USD sigue siendo una apuesta clara de rebote por su extrema sobreventa, mientras que ETH-USD muestra un RSI de 34.5 que nos permite mantener o evaluar la rotación. No realizaremos ventas forzosas ya que las posiciones actuales no han alcanzado el stop-loss estricto ni presentan sobrecompra, y dado que nuestro efectivo disponible es 0, priorizamos mantener las posiciones actuales a la espera de un rebote técnico inminente."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en una situación de sobreventa técnica extrema con un RSI de 25.4, lo que aumenta drásticamente la probabilidad de un rebote fuerte (mean reversion). Mantenemos la posición para capturar el movimiento alcista esperado sin vender en el suelo.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un RSI de 34.5 aproximándose a la zona de sobreventa y registrando un incremento del 2.4h del 2.1%. No se activa el stop-loss de -2.5% y el activo muestra indicios de recuperación, por lo que decidimos retener para permitir que alcance objetivos de ganancia.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 02:30` | 🟢 BUY | `SOL-USD` | $4.00 | $108.19 | SOL-USD presenta un RSI extremadamente bajo de 26.3, lo que indica sobreventa técnica seve... |
| `2026-10-13 01:30` | 🟢 BUY | `SOL-USD` | $6.23 | $107.75 | SOL-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.8 tras una caída s... |
| `2026-10-13 01:10` | 🟢 BUY | `ETH-USD` | $8.00 | $2506.03 | ETH-USD se encuentra en clara sobreventa técnica con un RSI de 31.1 tras una caída semanal... |
| `2026-10-13 01:10` | 🔴 SELL | `SOL-USD` | $16.14 | $107.57 | Vendemos parcialmente SOL-USD para liberar liquidez y poder financiar la entrada en ETH-US... |
| `2026-10-13 01:00` | 🟢 BUY | `SOL-USD` | $12.00 | $107.31 | Aprovechamos la sobreventa extrema de SOL-USD (RSI 25.3 y caída semanal de -11.16%) para i... |

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
