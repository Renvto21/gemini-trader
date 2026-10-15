# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 15:10:56`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.26 USD** | **$34.45 USD** | **$38.71 USD** | 🔴 **-3.22%** ($-1.29) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $343.05 | $9.91 | 📉 -0.90% | 1d 4h |
| `MSFT` | 0.012146 | $535.17 | $539.35 | $6.55 | 📈 +0.78% | 4h 20m |
| `QQQ` | 0.013791 | $725.09 | $724.29 | $9.99 | 📉 -0.11% | 2h 50m |
| `NVDA` | 0.036812 | $217.32 | $217.32 | $8.00 | 📈 +0.00% | 2h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo defensivo con la mayoría de los activos tecnológicos operando bajo su SMA20. Sin embargo, los niveles de RSI en 1 hora se mantienen extremadamente deprimidos en activos clave como QQQ (22.0) y NVDA (20.2), lo que indica condiciones maduras para un rebote técnico inminente. El efectivo disponible actual es de $4.26 USD, manteniéndose por debajo de la reserva mínima operativa, por lo que priorizaremos mantener las posiciones existentes mientras desarrollan su momentum alcista y vigilar posibles tomas de ganancias o recortes si perforan los soportes."

**Operaciones del ciclo:**
- *Sin cambios en este ciclo (HOLD)*

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (AAPL, MSFT, QQQ, NVDA) evaluando su evolución en las próximas horas. Vigilar el take-profit en MSFT si alcanza el rango del +2.0% al +3.5%. Monitorear de cerca los niveles de stop-loss en -2.0% para AAPL, QQQ y NVDA, y estar preparados para rotar capital hacia criptomonedas o liquidez en caso de que fallen los rebotes esperados."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **57** | 🎯 **42.1%** (24W / 19L / 14BE) | 🔴 **$-1.12 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |
| `2026-10-15 12:10` | 🔴 SELL (+0.14$) | `ETH-USD` | $6.14 | $2417.73 | ETH-USD ha alcanzado un rendimiento del +2.33%, cumpliendo con el rango establecido para l... |
| `2026-10-15 11:50` | 🔴 SELL (+0.13$) | `SOL-USD` | $6.13 | $104.21 | SOL-USD ha alcanzado un rendimiento de +2.11%, cumpliendo con la regla de toma rápida de g... |
| `2026-10-15 10:50` | 🟢 BUY | `MSFT` | $6.50 | $535.17 | MSFT presenta un RSI de 1h ultra comprimido en sobreventa extrema (14.7) con un cambio pos... |

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
