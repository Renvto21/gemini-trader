# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 00:40:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.54 USD** | **$17.09 USD** | **$39.63 USD** | 🔴 **-0.93%** ($-0.37) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2515.16 | $5.01 | 📈 +0.27% | 7h 30m |
| `BTC-USD` | 0.000072 | $83128.62 | $83760.25 | $6.05 | 📈 +0.76% | 3h 39m |
| `SOL-USD` | 0.055840 | $107.45 | $107.97 | $6.03 | 📈 +0.48% | 1h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto y operando con un sesgo positivo moderado en las últimas 24 horas (BTC +2.44%, ETH +2.90%, SOL +2.28%). Los mercados tradicionales (Wall Street) se encuentran cerrados, por lo que toda la liquidez y atención táctica se concentra exclusivamente en el sector cripto. Los activos en cartera (ETH-USD, BTC-USD y SOL-USD) muestran ganancias marginales estables pero aún no alcanzan el objetivo de take-profit de +2.0% a +3.5%, y sus indicadores de RSI de 1 hora se acercan a la zona de atención (entre 59 y 64), preparándose para un posible tramo alcista que permita asegurar beneficios próximamente."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD muestra un PnL positivo de +0.76% con un RSI de 1 hora en 62.5. Mantiene un buen impulso de corto plazo, por lo que se mantiene en cartera esperando alcanzar la zona objetivo de take-profit (+2.0% a +3.5%).
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD registra un PnL del +0.27% y un RSI de 1 hora en 59.1. La posición es estable y se encuentra dentro de los parámetros esperados de recuperación técnica.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra un PnL de +0.48% con un RSI de 1 hora en 64.6 acercándose a zona de sobrecompra. Se mantiene para buscar la toma de beneficios en el próximo ciclo si el impulso continúa.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, ETH-USD y SOL-USD mientras continúen con su estructura de rebote de corto plazo. Vigilar el RSI de 1 hora de cada activo: si superan los 70 o alcanzan un PnL de +2.0% a +3.5%, ejecutar la toma de beneficios para rotar capital. Mantener el stop-loss estricto en -2.0% y asegurar una reserva mínima de efectivo de $4.00 USD. No realizar nuevas compras en este ciclo para consolidar el portafolio actual."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **48** | 🎯 **45.8%** (22W / 12L / 14BE) | 🔴 **$-0.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |

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
