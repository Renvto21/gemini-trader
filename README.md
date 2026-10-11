# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 15:30:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$37.17 USD** | **$41.17 USD** | 🟢 **+2.92%** ($+1.17) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.004740 | $2531.44 | $2538.00 | $12.03 | 📈 +0.26% |
| `SOL-USD` | 0.224836 | $111.90 | $111.81 | $25.14 | 📉 -0.08% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra oportunidades claras de rebote técnico por sobreventa en criptomonedas, especialmente en SOL-USD que presenta un RSI de 27.9 y caídas recientes acumuladas. ETH-USD se mantiene estable con un RSI de 33.8 buscando piso. Mantendremos las posiciones actuales para capturar el rebote alcista ya que cumplen perfectamente con nuestra estrategia de Mean Reversion y alta volatilidad, respetando la reserva mínima de efectivo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD se encuentra en zona de profunda sobreventa técnica con un RSI de 27.9, lo que activa nuestra regla de cazar rebotes. Mantenemos la posición para capturar el movimiento alcista esperado del 2% al 6%.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD muestra un RSI de 33.8 cerca de la zona de sobreventa, manteniendo un comportamiento lateral estable con ganancias marginales. Mantenemos la posición a la espera de confirmación de momentum alcista.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 14:10` | 🟢 BUY | `SOL-USD` | $5.16 | $111.90 | SOL-USD presenta un RSI de 28.2 indicando sobreventa clara tras una caída semanal del 7.33... |
| `2026-10-11 14:00` | 🟢 BUY | `SOL-USD` | $10.00 | $112.02 | SOL-USD se encuentra en clara sobreventa tecnica con un RSI de 28.5 tras una caida semanal... |
| `2026-10-11 13:40` | 🟢 BUY | `SOL-USD` | $10.00 | $111.79 | SOL-USD presenta una excelente oportunidad de rebote técnico de alta convicción al encontr... |
| `2026-10-11 13:30` | 🔴 SELL | `SOL-USD` | $19.04 | $111.95 | SOL-USD ha alcanzado un rendimiento cercano a nuestra meta de take-profit del 2.5% (+2.43%... |
| `2026-10-11 13:20` | 🟢 BUY | `ETH-USD` | $12.00 | $2531.44 | ETH-USD se encuentra en zona de profunda sobreventa técnica con un RSI de 32.8 y una caída... |

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
