# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 03:10:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$6.92 USD** | **$34.59 USD** | **$41.50 USD** | 🟢 **+3.76%** ($+1.50) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.219306 | $111.68 | $112.25 | $24.62 | 📈 +0.51% |
| `ETH-USD` | 0.003904 | $2561.78 | $2554.19 | $9.97 | 📉 -0.30% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un rebote moderado en criptomonedas y tecnología. SOL-USD y ETH-USD se encuentran en zonas de sobreventa técnica con RSI de 29.2 y 36.0 respectivamente, mostrando intentos de recuperación en las últimas 24 horas (+2%). Mantenemos nuestro capital principalmente invertido con una reserva de liquidez cercana al objetivo, permitiendo retener las posiciones actuales que comienzan a estabilizarse y buscar un rebote más fuerte."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD muestra un RSI profundamente sobrevendido (29.2) pero con un cambio positivo de 24 horas del +2.01%. El precio está intentando un rebote técnico y nos encontramos cerca de la zona de entrada óptima, por lo que decidimos mantener la posición para capturar la recuperación.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 03:01` | 🟢 BUY | `ETH-USD` | $10.00 | $2561.78 | ETH-USD se encuentra en clara sobreventa técnica (RSI de 37) y muestra un repunte del 2.31... |
| `2026-10-12 03:01` | 🔴 SELL | `SOL-USD` | $16.91 | $112.74 | Vendemos parcialmente SOL-USD para capitalizar una pequeña ganancia y liberar efectivo, pe... |
| `2026-10-12 02:30` | 🟢 BUY | `SOL-USD` | $4.95 | $112.41 | SOL-USD mantiene un RSI en zona crítica de sobreventa (29.7) y un cambio positivo de 2.16%... |
| `2026-10-12 02:30` | 🔴 SELL | `ETH-USD` | $4.95 | $2553.65 | Tomamos beneficios totales en ETH-USD ya que se encuentra mostrando un rebote positivo per... |
| `2026-10-12 00:40` | 🟢 BUY | `SOL-USD` | $4.00 | $111.56 | SOL-USD muestra un RSI de 27.1, indicando una condición de sobreventa profunda tras una ca... |

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
