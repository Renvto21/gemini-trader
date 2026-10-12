# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 17:20:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.01 USD** | **$40.11 USD** | **$40.12 USD** | 🟢 **+0.30%** ($+0.12) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.369549 | $109.24 | $108.55 | $40.11 | 📉 -0.63% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un tono de cautela con descensos moderados en criptomonedas y tecnología, destacando una clara sobreventa en SOL-USD con un RSI de 26.7. Mantenemos nuestra posición en SOL-USD ya que se encuentra cerca del soporte y cumpliendo con nuestra tesis de rebote técnico, sin tocar aún el stop-loss estricto del -2.5% al -3.0%. Al tener todo el capital invertido y efectivo casi en cero, la decisión actual es mantener para permitir que el rebote esperado tome fuerza."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición actual en SOL-USD registra una ligera pérdida del -0.63%, muy lejos del stop-loss estricto. Su RSI en 26.7 indica una fuerte sobreventa y un excelente candidato para un rebote técnico inminente, por lo que decidimos mantener la posición y no realizar ventas prematuras.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 16:40` | 🟢 BUY | `SOL-USD` | $2.95 | $108.01 | Aprovechamos el capital liberado de Ethereum para incrementar la exposición en SOL-USD. Su... |
| `2026-10-12 16:40` | 🔴 SELL | `ETH-USD` | $2.95 | $2515.02 | Vendemos la posición completa en ETH-USD para liberar liquidez y concentrar el capital dis... |
| `2026-10-12 15:40` | 🟢 BUY | `SOL-USD` | $4.00 | $107.58 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 25.6 y una caída acumulada ... |
| `2026-10-12 12:20` | 🟢 BUY | `SOL-USD` | $3.42 | $108.91 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 27.1 y una caída acumulada ... |
| `2026-10-12 12:10` | 🟢 BUY | `SOL-USD` | $10.00 | $108.93 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 27.2 y una... |

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
