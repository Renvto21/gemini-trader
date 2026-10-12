# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 10:50:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$36.89 USD** | **$40.89 USD** | 🟢 **+2.23%** ($+0.89) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.307862 | $111.77 | $110.16 | $33.91 | 📉 -1.44% |
| `ETH-USD` | 0.001175 | $2553.82 | $2531.67 | $2.97 | 📉 -0.87% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto se encuentra en una fase de corrección de corto plazo pero con activos como SOL-USD y ETH-USD en clara zona de sobreventa técnica con RSI de 28.8 y 32.8 respectivamente. Nuestra estrategia exige cazar rebotes en sobreventa. Mantenemos posiciones actuales bajo control de riesgo, y aunque SOL-USD muestra un PnL de -1.44%, aún no toca el stop-loss estricto de -2.5% a -3.0%. El efectivo disponible es de $4.00 USD (nuestra reserva mínima requerida), por lo que para realizar cualquier nueva entrada táctica agresiva requeriríamos liquidar parte de las posiciones actuales o esperar flujos. Dado que las posiciones actuales están cercanas a la zona de rebote y no han alcanzado pérdidas críticas ni take-profit, optamos por mantener y monitorear."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): El activo se encuentra en profunda sobreventa con un RSI de 28.8, alineándose perfectamente con nuestra estrategia de buscar rebotes por Mean Reversion. El PnL actual es de -1.44%, el cual está muy por encima de nuestro stop-loss estricto (-2.5% a -3.0%). Mantenemos la posición esperando el impulso alcista hacia el objetivo de ganancia.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un RSI de 32.8, acercándose a la zona ideal de sobreventa para capturar un rebote técnico rápido. Al no haber alcanzado el límite de stop-loss (-0.87% actual) y con una liquidez en efectivo al límite mínimo de $4.00, es óptimo mantener y dejar que el precio desarrolle su movimiento.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 07:40` | 🟢 BUY | `ETH-USD` | $3.00 | $2553.82 | ETH-USD presenta un RSI de 35.7 indicando condiciones cercanas a la sobreventa, lo que act... |
| `2026-10-12 07:30` | 🔴 SELL | `ETH-USD` | $7.00 | $2553.60 | ETH-USD se encuentra estancado con un PnL cercano a 0% sin momentum inmediato. Vendemos la... |
| `2026-10-12 07:00` | 🟢 BUY | `SOL-USD` | $4.00 | $111.65 | SOL-USD está en zona de sobreventa profunda con un RSI de 31.8 y una caída semanal de -7.5... |
| `2026-10-12 06:10` | 🟢 BUY | `ETH-USD` | $2.00 | $2552.03 | ETH-USD presenta un RSI de 35.5 en clara zona de sobreventa tras caídas semanales del -5.3... |
| `2026-10-12 05:50` | 🟢 BUY | `ETH-USD` | $5.00 | $2553.65 | ETH-USD presenta un RSI de 35.7 en clara zona de sobreventa técnica tras una caída semanal... |

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
