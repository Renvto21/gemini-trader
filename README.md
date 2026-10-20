# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 21:20:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$34.43 USD** | **$38.43 USD** | 🔴 **-3.93%** ($-1.57) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $709.80 | $9.87 | 📉 -1.27% | 10h 40m |
| `ETH-USD` | 0.004178 | $2393.62 | $2391.38 | $9.99 | 📉 -0.09% | 8h 29m |
| `SOL-USD` | 0.096034 | $104.13 | $104.34 | $10.02 | 📈 +0.20% | 4h 39m |
| `BTC-USD` | 0.000056 | $81874.05 | $81480.78 | $4.55 | 📉 -0.48% | 4h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas permanece abierto con un sesgo bajista y consolidación de corto plazo, mostrando un momentum débil pero sin romper soportes críticos. Los mercados tradicionales como QQQ están cerrados, por lo que la liquidez activa debe enfocarse en mantener y rotar la cartera de cripto activos según la evolución de su RSI y los umbrales de take-profit o stop-loss."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD se mantiene estable con una pequeña ganancia del 0.2% y un RSI diario profundo en 20.3. Mantenemos la posición a la espera de un impulso mayor hacia el objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en criptomonedas (SOL-USD, ETH-USD, BTC-USD) y QQQ. Monitorear de cerca los objetivos de take-profit entre +2.0% y +3.5% para asegurar ganancias rápidamente y el stop-loss estricto en -2.0%. Si SOL-USD o ETH-USD no muestran un impulso alcista claro en los siguientes ciclos, considerar la rotación del capital hacia oportunidades con mayor momentum."
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
