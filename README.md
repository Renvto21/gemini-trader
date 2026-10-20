# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 23:50:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.68 USD** | **$38.68 USD** | 🔴 **-3.30%** ($-1.32) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 13h 9m |
| `ETH-USD` | 0.004178 | $2393.62 | $2399.52 | $10.02 | 📈 +0.25% | 10h 59m |
| `SOL-USD` | 0.096034 | $104.13 | $105.18 | $10.10 | 📈 +1.01% | 7h 9m |
| `BTC-USD` | 0.000105 | $81767.70 | $81738.69 | $8.56 | 📉 -0.04% | 6h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se encuentra abierto 24/7 mostrando ligeros signos de recuperación en el corto plazo con cambios horarios positivos, mientras que los activos tradicionales permanecen cerrados. SOL-USD muestra un avance favorable con un PnL de +1.01% acercándose a la zona objetivo, y ETH-USD se mantiene estable. BTC-USD y QQQ operan con leves variaciones negativas pero sin perforar los umbrales de stop-loss."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD muestra un comportamiento alcista sostenido con un PnL positivo del 1.01% y un cambio horario positivo. Se mantiene en cartera para buscar el take-profit en el rango de +2.0% a +3.5%.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD se mantiene estable con un pequeño PnL positivo del 0.25% y un RSI de 1 hora recuperándose. Sin motivos para vender todavía.
- **[HOLD] BTC-USD** (Confianza: 70%): BTC-USD opera ligeramente por debajo del precio de entrada pero muy lejos del stop-loss del -2.0%. Se espera consolidación del rebote técnico.
- **[HOLD] QQQ** (Confianza: 70%): El mercado de Wall Street está cerrado y QQQ se encuentra sin movimientos significativos y con un PnL casi plano (-0.08%). Se mantiene hasta la apertura del mercado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales mientras se monitorea de cerca a SOL-USD para asegurar ganancias si alcanza el rango de +2.0% a +3.5%. Estar atento al RSI de 1 hora en BTC-USD y ETH-USD para evaluar salidas tácticas o rotación de capital en caso de pérdida de momentum."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 23:00` | 🟢 BUY | `BTC-USD` | $4.00 | $81646.39 | BTC-USD presenta un RSI de 1 hora en 27.7, nivel de sobreventa profunda ideal para un rebo... |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |

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
