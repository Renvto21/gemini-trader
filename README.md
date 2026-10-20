# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 09:10:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.42 USD** | **$38.42 USD** | 🔴 **-3.95%** ($-1.58) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 22h 30m |
| `ETH-USD` | 0.004178 | $2393.62 | $2378.80 | $9.94 | 📉 -0.62% | 20h 19m |
| `SOL-USD` | 0.096034 | $104.13 | $103.90 | $9.98 | 📉 -0.22% | 16h 30m |
| `BTC-USD` | 0.000105 | $81767.70 | $81250.60 | $8.51 | 📉 -0.63% | 16h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general muestra una tendencia bajista de corto plazo con la mayoría de los activos tradicionales cerrados. Las criptomonedas se mantienen operando 24/7 pero sin momentum alcista claro, mostrando estancamiento en niveles de sobreventa moderada (RSI 1H alrededor de 30-31) y ligeros retrocesos en las últimas 24 horas. No hay liquidez disponible en efectivo para nuevas entradas."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 60%): El mercado de Wall Street está cerrado y la posición en QQQ se mantiene estable con una pérdida mínima del -0.08%, sin justificar una salida anticipada antes de la apertura.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Las posiciones actuales llevan más de 16-22 horas abiertas con variaciones marginalmente negativas pero lejos del stop-loss del -2.0%. Mantendremos la exposición actual en cripto y QQQ esperando un cambio de tendencia que active el take-profit entre +2.0% y +3.5%. Si el estancamiento persiste y las criptomonedas rompen los soportes actuales, procederemos a vender parcialmente para liberar efectivo y rotar hacia oportunidades más dinámicas."
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
