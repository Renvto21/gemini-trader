# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 15:50:33`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$36.98 USD** | **$40.98 USD** | 🟢 **+2.46%** ($+0.98) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.004740 | $2531.44 | $2527.25 | $11.98 | 📉 -0.17% |
| `SOL-USD` | 0.224836 | $111.90 | $111.21 | $25.00 | 📉 -0.62% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto se encuentra en una clara zona de sobreventa técnica profunda, destacando SOL-USD con un RSI de 26.0 y ETH-USD con 32.2, lo cual representa una excelente oportunidad para cazar rebotes agresivos (mean reversion). Por otro lado, los índices tecnológicos como QQQ y SPY muestran fortaleza alcista moderada, pero nuestra estrategia agresiva exige maximizar el potencial en los activos digitales más golpeados. Dado que mantenemos nuestra liquidez al límite mínimo requerido de $4.00 USD y no tenemos efectivo libre significativo para rotar sin cerrar posiciones, decidimos mantener nuestras posiciones actuales en cripto mientras aprovechan el rebote técnico inminente."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD presenta un RSI extremadamente bajo de 26.0, indicando una condición de sobreventa severa perfecta para nuestra estrategia de rebotes técnicos. Aunque muestra una tendencia bajista de corto plazo, el potencial de recuperación rápida es elevado. Mantenemos la posición para capturar el impulso alcista.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD se encuentra en zona de sobreventa con un RSI de 32.2. A pesar de una ligera pérdida no realizada (-0.17%), las condiciones técnicas sugieren un rebote inminente alineado con nuestra táctica agresiva de recuperación de precios.

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
