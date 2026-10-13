# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 06:00:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.74 USD** | **$39.74 USD** | 🔴 **-0.65%** ($-0.26) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $107.46 | $31.72 | 📈 +0.27% |
| `ETH-USD` | 0.003192 | $2506.03 | $2511.60 | $8.02 | 📈 +0.22% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra señales claras de sobreventa en activos clave como SOL-USD (RSI de 28.3) y ETH-USD (RSI de 36.2), cumpliendo con nuestra estrategia de cazar rebotes por mean reversion. Ambas posiciones actuales están ligeramente en positivo pero estancadas en tendencia bajista a corto plazo, por lo que decidimos mantenerlas ya que están en zonas óptimas de rebote técnico. No realizamos ventas ni nuevas compras en este ciclo para preservar la estabilidad de las posiciones actuales."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL se encuentra en condiciones de sobreventa extrema con un RSI de 28.3 y mostrando un pequeño repunte de 24 horas del 1.8%. Mantenemos la posición para capturar el rebote técnico esperado.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH muestra un RSI de 36.2 y un incremento del 2.75% en las últimas 24 horas, lo que valida nuestra tesis de rebote inminente. Mantenemos la posición actual para maximizar la ganancia.

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
