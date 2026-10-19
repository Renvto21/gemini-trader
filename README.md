# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 18:50:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$34.64 USD** | **$38.63 USD** | 🔴 **-3.42%** ($-1.37) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 8h 9m |
| `ETH-USD` | 0.004178 | $2393.62 | $2399.98 | $10.03 | 📈 +0.27% | 5h 59m |
| `SOL-USD` | 0.096034 | $104.13 | $104.59 | $10.04 | 📈 +0.44% | 2h 9m |
| `BTC-USD` | 0.000056 | $81874.05 | $81925.38 | $4.57 | 📈 +0.06% | 1h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional (QQQ y acciones) se encuentra cerrado, por lo que el foco operativo se centra totalmente en el mercado cripto (24/7). Las posiciones en criptomonedas (ETH-USD, SOL-USD y BTC-USD) muestran ligeras ganancias pero con un impulso técnico aún moderado y lateralizado, con RSI de 1 hora recuperándose lentamente desde zonas de sobreventa pero sin alcanzar los niveles de sobrecompra necesarios para tomas masivas de beneficio. Mantenemos la disciplina táctica sin realizar cierres prematuros, ya que las pérdidas son nulas y esperamos una extensión alcista."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): La posición en ETH-USD registra una leve ganancia del 0.27% y un RSI de 1 hora en 37.5. El rebote técnico sigue en curso y mantenemos la posición a la espera de un objetivo de take-profit más cercano al rango de sobrecompra.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD presenta el mejor desempeño actual con un 0.44% de ganancia y un RSI diario profundamente sobrevendido (21.0), lo que valida mantener la posición para buscar una expansión alcista mayor.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en ETH-USD, SOL-USD, BTC-USD y QQQ. Monitorear de cerca el RSI de 1 hora en cripto buscando que cruce por encima de 60 para ejecutar tomas de ganancias progresivas (Take-Profit) de entre +2% y +3.5%. QQQ se mantiene inalterado hasta la apertura del mercado tradicional. No se requieren nuevas compras en este ciclo dado que la liquidez en efectivo está al límite mínimo ($4.00 USD)."
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
