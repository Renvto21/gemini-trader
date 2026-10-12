# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 20:40:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$35.08 USD** | **$39.07 USD** | 🔴 **-2.32%** ($-0.93) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.220744 | $106.59 | $105.38 | $23.26 | 📉 -1.14% |
| `ETH-USD` | 0.004838 | $2480.41 | $2441.97 | $11.81 | 📉 -1.55% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa con SOL-USD (RSI en 23.3) y ETH-USD (RSI en 27.4) experimentando caídas significativas recientes. A pesar de la tendencia bajista a corto plazo, estas lecturas abren una ventana ideal para buscar rebotes técnicos agresivos (mean reversion). Mantendremos nuestras posiciones actuales ya que están cerca de la zona de soporte y acumulación, y preservaremos la liquidez actual sin realizar nuevas compras para no sobreexponer el portafolio en este momento de alta volatilidad."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): A pesar de la caída del 5.27% en 24 horas, el RSI en 23.3 indica una condición de sobreventa extrema. Mantenemos la posición para capturar el rebote técnico inminente sin disparar ventas de pánico.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 20:10` | 🟢 BUY | `SOL-USD` | $5.53 | $106.20 | SOL-USD presenta una condición de sobreventa extrema con un RSI de 24.1 y una caída de 7 d... |
| `2026-10-12 20:00` | 🟢 BUY | `SOL-USD` | $8.00 | $106.40 | SOL-USD se encuentra en clara sobreventa con un RSI de 24.3 y una caída de -11.91% en 7 dí... |
| `2026-10-12 19:40` | 🟢 BUY | `ETH-USD` | $12.00 | $2480.41 | ETH-USD se encuentra en una clara condición de sobreventa con un RSI de 14 de 29.5 y una c... |
| `2026-10-12 19:30` | 🟢 BUY | `SOL-USD` | $10.00 | $106.97 | SOL-USD se encuentra en clara condición de sobreventa profunda con un RSI de 24.9 y una ca... |
| `2026-10-12 19:20` | 🔴 SELL | `SOL-USD` | $39.52 | $106.94 | La posición actual en SOL-USD acumula un PnL de -2.11% acercándose peligrosamente al stop-... |

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
