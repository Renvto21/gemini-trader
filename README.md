# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 05:51:18`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.17 USD** | **$34.62 USD** | **$38.79 USD** | 🔴 **-3.02%** ($-1.21) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 19h 0m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 17h 30m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 17h 0m |
| `ETH-USD` | 0.002855 | $2451.90 | $2459.37 | $7.02 | 📈 +0.30% | 1h 20m |
| `SOL-USD` | 0.028214 | $106.33 | $106.85 | $3.01 | 📈 +0.49% | 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario de Wall Street se encuentra cerrado con precios congelados, por lo que toda la actividad operativa debe centrarse exclusivamente en las criptomonedas que operan 24/7. ETH-USD y SOL-USD muestran ligeros avances positivos y un comportamiento de rebote técnico favorable tras el soporte diario, mientras que el efectivo se mantiene cerca del mínimo operativo."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 80%): La posición muestra un rendimiento positivo constante y un momentum favorable en 1H, manteniendo la expectativa de alcanzar el objetivo de take-profit sin necesidad de operar todavía.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD continúa consolidando su rebote técnico desde la zona de sobreventa diaria con un cambio positivo en la última hora, por lo que se mantiene en cartera a la espera de mayores ganancias.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones de criptomonedas actuales (ETH-USD y SOL-USD) buscando alcanzar el rango de take-profit del +2.0% al +3.5% o un RSI de 1H superior a 70. Las posiciones de acciones (MSFT, QQQ, NVDA) permanecerán en HOLD hasta la apertura de Wall Street. No se ejecutan nuevas compras en este ciclo para preservar el efectivo por encima del límite mínimo de $4.00."
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
