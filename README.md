# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 06:20:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.17 USD** | **$34.59 USD** | **$38.76 USD** | 🔴 **-3.11%** ($-1.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 19h 29m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 18h 0m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 17h 30m |
| `ETH-USD` | 0.002855 | $2451.90 | $2450.88 | $7.00 | 📉 -0.04% | 1h 49m |
| `SOL-USD` | 0.028214 | $106.33 | $106.52 | $3.01 | 📈 +0.18% | 1h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional (Wall Street) se encuentra cerrado, por lo que la liquidez activa debe enfocarse exclusivamente en criptomonedas (abiertas 24/7). Las posiciones en cripto (ETH-USD y SOL-USD) muestran un comportamiento lateral con ligeros cambios, mientras que las acciones en cartera (MSFT, QQQ, NVDA) están estables pero con precios congelados hasta la apertura. Mantenemos la disciplina táctica sin forzar salidas prematuras ya que ninguna posición activa ha cruzado el stop-loss de -2.0% ni alcanzado el take-profit."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): La posición lleva poco tiempo abierta (1h 49m) y se encuentra operando cerca del precio de entrada (-0.04%). El RSI diario está en zona de soporte (32.7) y esperamos el desarrollo del rebote técnico sin necesidad de intervenir prematuramente.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD mantiene un rendimiento ligeramente positivo (+0.18%) tras la reciente entrada basada en sobreventa diaria (RSI diario 29.4). Mantenemos la posición a la espera de un incremento de volumen que impulse el precio hacia el objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en criptomonedas (ETH-USD y SOL-USD) y monitorear su momentum intradiario. Vigilar la aproximación a la zona de take-profit (+2.0% a +3.5%) o un RSI de 1H superior a 70 para asegurar beneficios. El efectivo disponible ($4.17) se encuentra en el límite de la reserva mínima requerida ($4.00), por lo que no se realizarán nuevas compras hasta que se libere capital mediante la toma de ganancias en posiciones abiertas o ante una señal de alta convicción con fuerte rebote técnico en cripto."
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
