# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 17:10:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$36.97 USD** | **$40.96 USD** | 🟢 **+2.41%** ($+0.96) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.004740 | $2531.44 | $2533.43 | $12.01 | 📈 +0.08% |
| `SOL-USD` | 0.224836 | $111.90 | $111.00 | $24.96 | 📉 -0.81% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo positivo general con QQQ y SPY en tendencia alcista. En cripto, SOL-USD presenta una condición de sobreventa extrema con un RSI de 25.3, ideal para una jugada de rebote táctico (mean reversion). ETH-USD también está en zona de sobreventa con un RSI de 33.1. Mantendremos la exposición a SOL-USD y ETH-USD aprovechando sus niveles actuales para buscar una recuperación rápida, operando estrictamente dentro de nuestra estrategia agresiva."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD tiene un RSI de 25.3 en clara zona de sobreventa, lo cual encaja perfectamente en nuestra estrategia de cazar rebotes técnicos de alta convicción.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 14:10` | 🟢 BUY | `SOL-USD` | $5.16 | $111.90 | SOL-USD presenta un RSI de 28.2 indicando sobreventa clara tras una caída semanal del 7.33... |
| `2026-10-11 14:00` | 🟢 BUY | `SOL-USD` | $10.00 | $112.02 | SOL-USD se encuentra en clara sobreventa tecnica con un RSI de 28.5 tras una caida semanal... |
| `2026-10-11 13:40` | 🟢 BUY | `SOL-USD` | $10.00 | $111.79 | SOL-USD presenta una excelente oportunidad de rebote técnico de alta convicción al encontr... |
| `2026-10-11 13:30` | 🔴 SELL | `SOL-USD` | $19.04 | $111.95 | SOL-USD ha alcanzado un rendimiento cercano a nuestra meta de take-profit del 2.5% (+2.43%... |
| `2026-10-11 13:20` | 🟢 BUY | `ETH-USD` | $12.00 | $2531.44 | ETH-USD se encuentra en zona de profunda sobreventa técnica con un RSI de 32.8 y una caída... |

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
