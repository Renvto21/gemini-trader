# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 02:20:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$36.05 USD** | **$40.05 USD** | 🟢 **+0.12%** ($+0.05) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.258226 | $107.03 | $108.40 | $27.99 | 📈 +1.28% |
| `ETH-USD` | 0.003192 | $2506.03 | $2523.95 | $8.06 | 📈 +0.72% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra cierta presión bajista en criptomonedas y tecnológicas de alto beta, con SOL-USD registrando un RSI de 26.5 y ETH-USD un RSI de 32.3, lo que representa condiciones claras de sobreventa para cazar rebotes por mean reversion. Nuestra liquidez en efectivo es de $4.00 USD, cumpliendo el límite mínimo requerido, por lo que decidimos mantener nuestras posiciones actuales con ganancias modestas y esperar a la rotación de capital para entradas futuras más agresivas."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD está en condiciones de extrema sobreventa (RSI 26.5) y aunque muestra una baja de -2.55% en 24h, mantenemos la posición para capturar el rebote técnico inminente sin disparar ventas innecesarias antes de alcanzar nuestro objetivo de take-profit.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 01:30` | 🟢 BUY | `SOL-USD` | $6.23 | $107.75 | SOL-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.8 tras una caída s... |
| `2026-10-13 01:10` | 🟢 BUY | `ETH-USD` | $8.00 | $2506.03 | ETH-USD se encuentra en clara sobreventa técnica con un RSI de 31.1 tras una caída semanal... |
| `2026-10-13 01:10` | 🔴 SELL | `SOL-USD` | $16.14 | $107.57 | Vendemos parcialmente SOL-USD para liberar liquidez y poder financiar la entrada en ETH-US... |
| `2026-10-13 01:00` | 🟢 BUY | `SOL-USD` | $12.00 | $107.31 | Aprovechamos la sobreventa extrema de SOL-USD (RSI 25.3 y caída semanal de -11.16%) para i... |
| `2026-10-13 01:00` | 🔴 SELL | `ETH-USD` | $10.10 | $2504.55 | Vendemos la totalidad de ETH-USD para liberar capital líquido de inmediato y redirigirlo h... |

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
