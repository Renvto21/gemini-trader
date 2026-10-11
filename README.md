# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 13:20:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$10.12 USD** | **$30.96 USD** | **$41.08 USD** | 🟢 **+2.69%** ($+1.08) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.170099 | $109.29 | $111.47 | $18.96 | 📈 +1.99% |
| `ETH-USD` | 0.004740 | $2531.44 | $2531.44 | $12.00 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa con ETH-USD (RSI 32.8) y SOL-USD (RSI 26.8), presentando una oportunidad ideal de rebote técnico (Mean Reversion). Nuestra posición actual en SOL-USD tiene un rendimiento positivo del 1.99%, acercándose al objetivo de toma de ganancias. En paralelo, ETH-USD ofrece un punto de entrada excelente para capitalizar la fuerte caída semanal y buscar un rebote rápido. Mantendremos la liquidez al límite inferior permitido para maximizar la exposición a estos activos de alta volatilidad."*

**Operaciones del ciclo:**
- **[BUY] ETH-USD** (Confianza: 88%): ETH-USD se encuentra en zona de profunda sobreventa técnica con un RSI de 32.8 y una caída semanal del -6.62%. Esto activa nuestra regla táctica de cazar rebotes en cripto con alta convicción, destinando un monto de 12.0 USD para capturar un movimiento alcista rápido.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 13:20` | 🟢 BUY | `ETH-USD` | $12.00 | $2531.44 | ETH-USD se encuentra en zona de profunda sobreventa técnica con un RSI de 32.8 y una caída... |
| `2026-10-11 13:10` | 🔴 SELL | `ETH-USD` | $9.99 | $2530.10 | ETH-USD se encuentra estancado con un P&L cercano a 0% (-0.06%) y bajo tendencia bajista e... |
| `2026-10-11 13:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2531.65 | ETH-USD se encuentra en clara sobreventa técnica con un RSI de 32.8 y una fuerte caída sem... |
| `2026-10-11 13:00` | 🔴 SELL | `SOL-USD` | $19.02 | $111.81 | Tomamos beneficios de manera parcial en SOL-USD ya que la posición acumula una ganancia ce... |
| `2026-10-11 12:50` | 🔴 SELL | `ETH-USD` | $3.10 | $2526.95 | Vendemos la posición completa de ETH-USD para liberar capital en efectivo y aprovechar las... |

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
