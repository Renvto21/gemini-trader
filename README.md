# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 07:50:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$11.99 USD** | **$39.52 USD** | 🔴 **-1.20%** ($-0.48) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83367.41 | $6.02 | 📈 +0.29% | 10h 49m |
| `SOL-USD` | 0.055840 | $107.45 | $107.00 | $5.97 | 📉 -0.42% | 8h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado por lo que la liquidez activa se concentra en las criptomonedas. BTC-USD y SOL-USD muestran ligeras recuperaciones con rendimientos de 1 hora positivos pero con un momentum lateralizado sin la fuerza explosiva esperada tras varias horas en cartera. Mantenemos la cautela y conservamos las posiciones vigentes mientras se espera una ruptura de volumen más clara."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 60%): La posición lleva casi 11 horas abierta con un PnL marginal de +0.29%. El RSI de 1H se encuentra neutral en 50.3 y el cambio de 1h es positivo (+0.25%). Mantenemos a la espera de que el precio alcance el objetivo de take-profit del +2.0%.
- **[HOLD] SOL-USD** (Confianza: 60%): La posición se mantiene abierta por más de 8 horas con un PnL de -0.42%, muy lejos del stop-loss estricto de -2.0%. El RSI diario en sobreventa extrema (28.2) y el ligero cambio positivo de 1H (+0.47%) respaldan mantener la operación buscando el rebote técnico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener BTC-USD y SOL-USD en este ciclo mientras no rompan el stop-loss de -2.0%. Si alcanzan la zona de +2.0% a +3.5% procedemos a asegurar beneficios de inmediato. Vigilar la liquidez en efectivo ($27.53 USD) para desplegarla en nuevas rupturas en cuanto el mercado accionario abra o si ETH-USD u otras criptos generan un setup de alta convicción con RSI saliendo de sobreventa."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **49** | 🎯 **44.9%** (22W / 13L / 14BE) | 🔴 **$-0.39 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |

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
