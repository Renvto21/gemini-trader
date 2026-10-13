# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 01:20:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$10.23 USD** | **$29.56 USD** | **$39.79 USD** | 🔴 **-0.53%** ($-0.21) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.200407 | $106.82 | $107.53 | $21.55 | 📈 +0.67% |
| `ETH-USD` | 0.003192 | $2506.03 | $2509.01 | $8.01 | 📈 +0.12% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa con ETH-USD (RSI 31.3) y SOL-USD (RSI 25.5) ofreciendo una clara oportunidad de rebote técnico por mean reversion. Mantenemos nuestras posiciones actuales esperando un impulso alcista que nos acerque a la toma de ganancias, mientras conservamos liquidez para la gestión de riesgos."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en clara sobreventa con un RSI de 25.5 tras una caída semanal del 10.98%. A pesar de la tendencia bajista actual, las condiciones técnicas son ideales para un rebote de corto plazo hacia nuestro objetivo de ganancia, por lo que mantenemos la posición.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 01:10` | 🟢 BUY | `ETH-USD` | $8.00 | $2506.03 | ETH-USD se encuentra en clara sobreventa técnica con un RSI de 31.1 tras una caída semanal... |
| `2026-10-13 01:10` | 🔴 SELL | `SOL-USD` | $16.14 | $107.57 | Vendemos parcialmente SOL-USD para liberar liquidez y poder financiar la entrada en ETH-US... |
| `2026-10-13 01:00` | 🟢 BUY | `SOL-USD` | $12.00 | $107.31 | Aprovechamos la sobreventa extrema de SOL-USD (RSI 25.3 y caída semanal de -11.16%) para i... |
| `2026-10-13 01:00` | 🔴 SELL | `ETH-USD` | $10.10 | $2504.55 | Vendemos la totalidad de ETH-USD para liberar capital líquido de inmediato y redirigirlo h... |
| `2026-10-13 00:40` | 🟢 BUY | `SOL-USD` | $3.43 | $107.26 | SOL-USD se encuentra en profunda sobreventa técnica con un RSI de 25.2 y una caída del 11.... |

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
