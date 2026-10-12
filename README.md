# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 20:30:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$35.29 USD** | **$39.28 USD** | 🔴 **-1.79%** ($-0.72) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.220744 | $106.59 | $105.99 | $23.40 | 📉 -0.57% |
| `ETH-USD` | 0.004838 | $2480.41 | $2457.72 | $11.89 | 📉 -0.91% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto presenta una fuerte corrección a corto plazo, llevando a activos como SOL-USD y ETH-USD a niveles extremos de sobreventa con RSI de 23.9 y 28.2 respectivamente. Aunque la tendencia inmediata es bajista, esto activa nuestra estrategia de Mean Reversion para buscar rebotes técnicos agresivos. Mantenemos las posiciones actuales ya que están cerca de tocar piso y no han alcanzado el stop-loss estricto del 3%, operando con la liquidez disponible al mínimo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 82%): SOL-USD se encuentra en un RSI de 23.9, profundamente sobrevendido tras una caída semanal del 12.25%. A pesar de estar bajo la SMA20, esperamos un rebote técnico inminente de corto plazo por lo que mantenemos la posición para capturar la recuperación sin vender con pérdida.

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
