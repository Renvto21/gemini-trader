# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 12:10:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$7.42 USD** | **$32.78 USD** | **$40.20 USD** | 🟢 **+0.50%** ($+0.20) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001175 | $2553.82 | $2525.66 | $2.97 | 📉 -1.10% |
| `SOL-USD` | 0.273653 | $109.63 | $108.93 | $29.81 | 📉 -0.64% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un tono mixto con presión bajista en criptomonedas y tecnológicas de alto beta, generando excelentes oportunidades de sobreventa (Mean Reversion). SOL-USD presenta un RSI muy deprimido en 27.2, lo que activa nuestra estrategia de cazar rebotes agresivos para capitalizar un fuerte movimiento alcista de recuperación, mientras mantenemos la disciplina de stop-loss estricto."*

**Operaciones del ciclo:**
- **[BUY] SOL-USD** (Confianza: 88%): SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 27.2 y una caída del -9.82% en los últimos 7 días. Aplicando nuestra estrategia agresiva de cazar rebotes y aprovechando la alta convicción, destinamos capital para promediar la posición y capturar el próximo rebote técnico hacia la media.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 12:10` | 🟢 BUY | `SOL-USD` | $10.00 | $108.93 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 27.2 y una... |
| `2026-10-12 12:01` | 🟢 BUY | `SOL-USD` | $10.00 | $109.96 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 28.5 y una caída semanal de... |
| `2026-10-12 11:50` | 🟢 BUY | `SOL-USD` | $10.00 | $110.00 | SOL-USD presenta un RSI de 28.6 indicando sobreventa extrema y una caída acumulada semanal... |
| `2026-10-12 11:40` | 🔴 SELL | `SOL-USD` | $37.42 | $108.72 | Activación del stop-loss estricto debido a que la posición ha caído un -2.58%, rompiendo e... |
| `2026-10-12 11:10` | 🟢 BUY | `SOL-USD` | $4.00 | $110.16 | SOL-USD presenta un RSI extremadamente bajo de 28.8 y una caída acumulada del 8.8% en 7 dí... |

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
