# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 13:40:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$36.14 USD** | **$40.14 USD** | 🟢 **+0.36%** ($+0.14) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001175 | $2553.82 | $2529.56 | $2.97 | 📉 -0.95% |
| `SOL-USD` | 0.305055 | $109.55 | $108.73 | $33.17 | 📉 -0.75% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones claras de sobreventa extrema, liderado por SOL-USD con un RSI de 26.9 y ETH-USD con RSI de 32.7, ofreciendo una oportunidad táctica de rebote técnico (Mean Reversion). Dado que nuestras posiciones actuales en ETH y SOL están ligeramente en rojo pero el efectivo disponible es de apenas $4.00, mantendremos la disciplina operativa sin forzar ventas anticipadas con pérdidas menores, permitiendo que el rebote técnico actúe a nuestro favor."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 82%): SOL se encuentra en una clara zona de sobreventa con un RSI de 26.9 y una caída acumulada semanal del -9.98%. Mantenemos la posición para capturar el rebote inminente hacia la media, respetando nuestro estricto stop-loss pero aprovechando la alta volatilidad actual.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 12:20` | 🟢 BUY | `SOL-USD` | $3.42 | $108.91 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 27.1 y una caída acumulada ... |
| `2026-10-12 12:10` | 🟢 BUY | `SOL-USD` | $10.00 | $108.93 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 27.2 y una... |
| `2026-10-12 12:01` | 🟢 BUY | `SOL-USD` | $10.00 | $109.96 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 28.5 y una caída semanal de... |
| `2026-10-12 11:50` | 🟢 BUY | `SOL-USD` | $10.00 | $110.00 | SOL-USD presenta un RSI de 28.6 indicando sobreventa extrema y una caída acumulada semanal... |
| `2026-10-12 11:40` | 🔴 SELL | `SOL-USD` | $37.42 | $108.72 | Activación del stop-loss estricto debido a que la posición ha caído un -2.58%, rompiendo e... |

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
