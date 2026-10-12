# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 02:30:54`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.01 USD** | **$41.51 USD** | **$41.52 USD** | 🟢 **+3.80%** ($+1.52) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.369306 | $111.68 | $112.41 | $41.51 | 📈 +0.65% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con sesgo alcista moderado en los principales índices como SPY y QQQ, mientras que el sector cripto (SOL y ETH) intenta consolidar un rebote técnico tras caídas semanales recientes. SOL-USD presenta una clara condición de sobreventa con un RSI de 29.7, lo que activa nuestra estrategia de caza de rebotes (mean reversion). Nuestro portafolio se encuentra totalmente invertido y con ganancias generales de +3.8%, por lo que ejecutaremos una ligera toma de beneficios en ETH-USD para liberar liquidez y rotar capital hacia una mayor acumulación en SOL-USD."*

**Operaciones del ciclo:**
- **[SELL] ETH-USD** (Confianza: 85%): Tomamos beneficios totales en ETH-USD ya que se encuentra mostrando un rebote positivo pero queremos liberar efectivo para concentrar el capital en oportunidades de mayor asimetría y sobreventa.
- **[BUY] SOL-USD** (Confianza: 90%): SOL-USD mantiene un RSI en zona crítica de sobreventa (29.7) y un cambio positivo de 2.16% en las últimas 24 horas, indicando el inicio de un rebote técnico alcista ideal para capturar ganancias rápidas.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 02:30` | 🟢 BUY | `SOL-USD` | $4.95 | $112.41 | SOL-USD mantiene un RSI en zona crítica de sobreventa (29.7) y un cambio positivo de 2.16%... |
| `2026-10-12 02:30` | 🔴 SELL | `ETH-USD` | $4.95 | $2553.65 | Tomamos beneficios totales en ETH-USD ya que se encuentra mostrando un rebote positivo per... |
| `2026-10-12 00:40` | 🟢 BUY | `SOL-USD` | $4.00 | $111.56 | SOL-USD muestra un RSI de 27.1, indicando una condición de sobreventa profunda tras una ca... |
| `2026-10-12 00:30` | 🟢 BUY | `ETH-USD` | $4.93 | $2542.03 | ETH-USD se encuentra en zona de clara sobreventa técnica con un RSI de 34.4 tras una caída... |
| `2026-10-12 00:20` | 🔴 SELL | `ETH-USD` | $4.93 | $2542.39 | ETH-USD se encuentra estancado con una ganancia marginal del 0.04% y bajo momentum inmedia... |

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
