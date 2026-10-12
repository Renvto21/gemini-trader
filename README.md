# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 15:40:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.77 USD** | **$39.77 USD** | 🔴 **-0.58%** ($-0.23) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001175 | $2553.82 | $2510.19 | $2.95 | 📉 -1.71% |
| `SOL-USD` | 0.342237 | $109.34 | $107.58 | $36.82 | 📉 -1.61% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto y tecnológico muestra correcciones moderadas, destacando a SOL-USD y ETH-USD en zonas de sobreventa técnica profunda con RSI de 25.6 y 31.3 respectivamente. Nuestras posiciones actuales están experimentando pérdidas menores que rondan el -1.7% y -1.8%, manteniéndose lejos del stop-loss estricto del -3%. Dada la fuerte sobreventa en Solana, el mercado ofrece un excelente escenario de rebote táctico (mean reversion) para maximizar la agresividad del portafolio."*

**Operaciones del ciclo:**
- **[BUY] SOL-USD** (Confianza: 88%): SOL-USD se encuentra en clara sobreventa técnica con un RSI de 25.6 y una caída acumulada semanal del 10.93%. Con una alta convicción (0.88), aprovechamos nuestro efectivo disponible para promediar la posición y cazar un rebote rápido del 3% al 5% en línea con nuestra estrategia agresiva de crecimiento.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 15:40` | 🟢 BUY | `SOL-USD` | $4.00 | $107.58 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 25.6 y una caída acumulada ... |
| `2026-10-12 12:20` | 🟢 BUY | `SOL-USD` | $3.42 | $108.91 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 27.1 y una caída acumulada ... |
| `2026-10-12 12:10` | 🟢 BUY | `SOL-USD` | $10.00 | $108.93 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 27.2 y una... |
| `2026-10-12 12:01` | 🟢 BUY | `SOL-USD` | $10.00 | $109.96 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 28.5 y una caída semanal de... |
| `2026-10-12 11:50` | 🟢 BUY | `SOL-USD` | $10.00 | $110.00 | SOL-USD presenta un RSI de 28.6 indicando sobreventa extrema y una caída acumulada semanal... |

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
