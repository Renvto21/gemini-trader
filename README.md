# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 22:20:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$34.36 USD** | **$38.36 USD** | 🔴 **-4.11%** ($-1.64) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $709.80 | $9.87 | 📉 -1.27% | 11h 39m |
| `ETH-USD` | 0.004178 | $2393.62 | $2383.68 | $9.96 | 📉 -0.42% | 9h 29m |
| `SOL-USD` | 0.096034 | $104.13 | $104.05 | $9.99 | 📉 -0.08% | 5h 39m |
| `BTC-USD` | 0.000056 | $81874.05 | $81302.19 | $4.54 | 📉 -0.70% | 5h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto 24/7 con un sesgo ligeramente bajista y consolidación en la mayoría de los activos, mientras que los mercados tradicionales permanecen cerrados. Las posiciones en cripto muestran pérdidas moderadas dentro de los rangos tolerados antes del stop-loss estricto (-2.0%), y QQQ se encuentra temporalmente congelado por el cierre de sesión de Wall Street. Mantendremos la paciencia táctica esperando el catalizador de volumen en cripto."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD se mantiene cerca de la zona de entrada con una pérdida menor del -0.42%. El RSI diario en 23.6 sugiere una sobreventa profunda, por lo que esperamos que se produzca el rebote técnico esperado sin violar el stop-loss.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD presenta un RSI diario extremo de 19.4 y una pérdida nominal del -0.08%. Mantenemos la posición para capturar el esperado rebote de reversión a la media.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca ETH-USD, SOL-USD y BTC-USD en busca de un repunte en el RSI de 1 hora por encima de 40 para confirmar el rebote técnico. Mantener stop-loss estricto a -2.0% y take-profit entre +2.0% y +3.5%. Si las criptomonedas continúan estancadas y se rompen soportes, rotaremos el capital hacia oportunidades con mayor momentum."
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
