# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 00:20:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.66 USD** | **$38.66 USD** | 🔴 **-3.35%** ($-1.34) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 13h 39m |
| `ETH-USD` | 0.004178 | $2393.62 | $2402.23 | $10.04 | 📈 +0.36% | 11h 29m |
| `SOL-USD` | 0.096034 | $104.13 | $104.82 | $10.07 | 📈 +0.66% | 7h 39m |
| `BTC-USD` | 0.000105 | $81767.70 | $81779.07 | $8.57 | 📈 +0.01% | 7h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene operando 24/7 con un comportamiento lateral a ligeramente alcista en busca de consolidación tras las recientes caídas, destacando SOL-USD y ETH-USD con rendimientos positivos marginales en las posiciones actuales. Los activos tradicionales como QQQ y SPY se encuentran cerrados, por lo que la liquidez está plenamente concentrada en mantener y gestionar los rebotes técnicos de las criptomonedas abiertas."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD muestra un rendimiento positivo del 0.66% y un RSI de 1 hora en 58.7, manteniendo un comportamiento constructivo hacia el rebote técnico desde niveles de sobreventa diaria. Continuamos esperando el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD se mantiene estable con un PnL positivo de 0.36% y un RSI diario en niveles de sobreventa profunda (24.3), lo que justifica conservar la posición para capturar el rebote esperado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en criptomonedas (SOL-USD, ETH-USD, BTC-USD) y QQQ a la espera de la apertura de Wall Street. El objetivo es monitorear el take-profit parcial si SOL-USD o ETH-USD extienden sus ganancias hacia el rango de +2% a +3.5%, o si su RSI de 1 hora supera consistentemente los 70 puntos. Si no hay suficiente impulso en BTC-USD, consideraremos rotar capital hacia activos con mayor dinamismo en la apertura del mercado bursátil."
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
