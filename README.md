# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 22:10:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$34.35 USD** | **$38.34 USD** | 🔴 **-4.14%** ($-1.66) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $709.80 | $9.87 | 📉 -1.27% | 11h 29m |
| `ETH-USD` | 0.004178 | $2393.62 | $2379.80 | $9.94 | 📉 -0.58% | 9h 19m |
| `SOL-USD` | 0.096034 | $104.13 | $104.09 | $10.00 | 📉 -0.04% | 5h 29m |
| `BTC-USD` | 0.000056 | $81874.05 | $81273.13 | $4.54 | 📉 -0.73% | 4h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas permanece abierto pero muestra un tono de debilidad y baja volatilidad alcista, con los principales activos (ETH, SOL, BTC) operando por debajo de sus medias móviles y con un momentum de corto plazo neutral o ligeramente bajista. Los mercados tradicionales como QQQ y SPY se encuentran cerrados, manteniendo congeladas las posiciones actuales. No hay suficiente confirmación de rebote agresivo en este momento, por lo que la prioridad es proteger el capital y mantener liquidez."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 60%): ETH-USD se encuentra operando sin grandes cambios tras varias horas. Aunque su RSI diario es profundo (23.4), el impulso de 1 hora aún no genera una ruptura alcista clara. Mantenemos la posición a la espera de un volumen de compra.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones actuales (QQQ, ETH-USD, SOL-USD, BTC-USD) ya que ninguna ha alcanzado el take-profit (+2% a +3.5%) ni ha perforado el stop-loss estricto (-2.0%). Dado que los mercados de acciones están cerrados y las criptos muestran un momentum lateral/bajista, mantendremos las posiciones actuales esperando un catalizador de volumen en el próximo ciclo o la apertura de Wall Street para evaluar la rotación de QQQ si persisten las pérdidas."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |
| `2026-10-19 01:50` | 🔴 SELL (+0.09$) | `ETH-USD` | $8.09 | $2428.97 | ETH-USD registra una ganancia acumulada y su RSI de 1 hora ha alcanzado 68.3, acercándose ... |

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
