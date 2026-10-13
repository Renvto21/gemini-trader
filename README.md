# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 00:50:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$35.71 USD** | **$39.70 USD** | 🔴 **-0.75%** ($-0.30) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.238581 | $106.59 | $107.36 | $25.61 | 📈 +0.72% |
| `ETH-USD` | 0.004032 | $2480.01 | $2502.90 | $10.09 | 📈 +0.92% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto presenta condiciones de sobreventa extrema con SOL-USD en un RSI de 25.3 y ETH-USD en 30.9, ofreciendo una oportunidad clásica de rebote por reversión a la media (Mean Reversion). Ambas posiciones actuales se mantienen estables con pequeñas ganancias (+0.72% y +0.92%), pero sin alcanzar aún el objetivo de toma de beneficios del +2.5%. El efectivo disponible es el mínimo requerido de $4.00 USD, por lo que no se pueden realizar nuevas compras sin antes rotar capital, y las posiciones actuales deben mantenerse mientras desarrollan su impulso alcista desde la zona de soporte."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra en clara sobreventa (RSI 25.3), lo cual activa nuestra regla de cazar rebotes en cripto. Aunque ha tenido una caída de 24 horas del -3.49%, mantiene un pequeño beneficio flotante del +0.72%. Mantendremos la posición para capturar el rebote técnico hacia el objetivo del +2.5% o superior.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un RSI de 30.9 en zona de compresión bajista y un beneficio actual de +0.92%. La estrategia agresiva nos dicta mantener la posición ante la inminencia de un rebote técnico en activos digitales de alta volatilidad, evitando vender prematuramente antes de exprimir el movimiento.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 00:40` | 🟢 BUY | `SOL-USD` | $3.43 | $107.26 | SOL-USD se encuentra en profunda sobreventa técnica con un RSI de 25.2 y una caída del 11.... |
| `2026-10-13 00:10` | 🟢 BUY | `SOL-USD` | $10.00 | $106.61 | SOL-USD se encuentra en una clara condición de sobreventa con un RSI de 24.5 y una caída d... |
| `2026-10-12 23:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2480.01 | Ethereum se encuentra en clara sobreventa con un RSI de 29.5 y una caída semanal del 8.06%... |
| `2026-10-12 23:40` | 🟢 BUY | `SOL-USD` | $12.00 | $106.38 | SOL-USD presenta una clara condición de sobreventa técnica extrema con RSI de 24.3 tras un... |
| `2026-10-12 23:40` | 🔴 SELL | `GLD` | $12.00 | $382.15 | Posición estancada con rendimiento de 0% sin momentum alcista. Vendo la totalidad para lib... |

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
