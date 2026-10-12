# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 19:40:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$17.53 USD** | **$21.96 USD** | **$39.49 USD** | 🔴 **-1.28%** ($-0.51) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.093484 | $106.97 | $106.57 | $9.96 | 📉 -0.37% |
| `ETH-USD` | 0.004838 | $2480.41 | $2480.41 | $12.00 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto presenta condiciones extremas de sobreventa con ETH-USD (RSI en 29.5) y SOL-USD (RSI en 24.5) registrando fuertes caídas recientes. Mantenemos nuestra posición en SOL-USD ya que está cerca del soporte y muestra una oportunidad clásica de rebote técnico (Mean Reversion). Dado el nivel extremo de sobreventa en ETH-USD, aprovechamos nuestra liquidez para iniciar una compra agresiva buscando capturar un rebote técnico rápido del 3% al 5%."*

**Operaciones del ciclo:**
- **[BUY] ETH-USD** (Confianza: 88%): ETH-USD se encuentra en una clara condición de sobreventa con un RSI de 14 de 29.5 y una caída acumulada del 8.05% en los últimos 7 días. Aplicamos la regla de alta convicción asignando $12.00 USD para cazar el rebote técnico de corto plazo.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 19:40` | 🟢 BUY | `ETH-USD` | $12.00 | $2480.41 | ETH-USD se encuentra en una clara condición de sobreventa con un RSI de 14 de 29.5 y una c... |
| `2026-10-12 19:30` | 🟢 BUY | `SOL-USD` | $10.00 | $106.97 | SOL-USD se encuentra en clara condición de sobreventa profunda con un RSI de 24.9 y una ca... |
| `2026-10-12 19:20` | 🔴 SELL | `SOL-USD` | $39.52 | $106.94 | La posición actual en SOL-USD acumula un PnL de -2.11% acercándose peligrosamente al stop-... |
| `2026-10-12 16:40` | 🟢 BUY | `SOL-USD` | $2.95 | $108.01 | Aprovechamos el capital liberado de Ethereum para incrementar la exposición en SOL-USD. Su... |
| `2026-10-12 16:40` | 🔴 SELL | `ETH-USD` | $2.95 | $2515.02 | Vendemos la posición completa en ETH-USD para liberar liquidez y concentrar el capital dis... |

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
