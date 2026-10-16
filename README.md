# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 10:20:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.17 USD** | **$34.59 USD** | **$38.75 USD** | 🔴 **-3.11%** ($-1.25) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 23h 29m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 22h 0m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 21h 30m |
| `ETH-USD` | 0.002855 | $2451.90 | $2460.60 | $7.02 | 📈 +0.35% | 5h 49m |
| `SOL-USD` | 0.028214 | $106.33 | $105.41 | $2.97 | 📉 -0.87% | 5h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario de EE. UU. se encuentra cerrado con precios congelados, manteniendo a QQQ, MSFT y NVDA en pausa técnica. Por otro lado, el mercado de criptomonedas opera 24/7 con un comportamiento lateral a ligeramente bajista; ETH-USD muestra un RSI 1H en 62.5 acercándose a la zona de sobrecompra, mientras que SOL-USD se mantiene en sobreventa diaria (RSI diario de 26.7) pero sin un momentum de corto plazo explosivo todavía. Mantenemos el enfoque táctico protegiendo la liquidez mínima y esperando que se acerquen los objetivos de take-profit o stop-loss."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un rendimiento positivo constante (+0.35%) acercándose progresivamente al objetivo de take-profit. Mantenemos la posición a la espera de que el RSI 1H supere 70 para asegurar ganancias de manera óptima.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de acciones y criptomonedas intactas este ciclo ya que ninguna ha tocado el stop-loss de -2.0% ni el take-profit del rango +2.0% a +3.5%. Vigilaré de cerca a ETH-USD por si su RSI 1H supera 70 para realizar una toma parcial de beneficios. Si el mercado cripto rompe a la baja afectando a SOL-USD por debajo de -2.0%, ejecutaremos la venta de inmediato para cortar pérdidas."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **58** | 🎯 **41.4%** (24W / 20L / 14BE) | 🔴 **$-1.22 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 05:10` | 🟢 BUY | `SOL-USD` | $3.00 | $106.33 | SOL-USD presenta un RSI diario en zona de sobreventa extrema (29.0) y un cambio positivo e... |
| `2026-10-16 04:30` | 🟢 BUY | `ETH-USD` | $7.00 | $2451.90 | Aprovechamos la liquidez disponible sobre la reserva mínima ($14.17 vs $4.00 requeridos) p... |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |

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
