# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 07:20:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.50 USD** | **$38.50 USD** | 🔴 **-3.74%** ($-1.50) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 20h 39m |
| `ETH-USD` | 0.004178 | $2393.62 | $2386.88 | $9.97 | 📉 -0.28% | 18h 29m |
| `SOL-USD` | 0.096034 | $104.13 | $104.12 | $10.00 | 📉 -0.01% | 14h 39m |
| `BTC-USD` | 0.000105 | $81767.70 | $81535.90 | $8.54 | 📉 -0.28% | 14h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario de EE.UU. se encuentra cerrado con precios congelados, por lo que la liquidez activa se concentra en las criptomonedas (24/7). Las cripto muestran ligeros intentos de recuperación a 1 hora (cambios positivos y RSI acercándose a 40), aunque la tendencia macro sigue siendo bajista bajo la SMA20. Las posiciones actuales se mantienen estables dentro de los márgenes de tolerancia de stop-loss, sin alcanzar aún los objetivos de take-profit."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 70%): La posición en BTC-USD registra una variación mínima (-0.28%) y el RSI de 1 hora se sitúa en 39.5 con un sesgo positivo reciente. Mantenemos la posición a la espera de que el RSI supere los 50 puntos para buscar un take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas actuales (QQQ, ETH-USD, SOL-USD, BTC-USD) ya que ninguna ha alcanzado el stop-loss estricto de -2.0%. Monitorear de cerca el RSI de 1 hora en las criptomonedas buscando rupturas por encima de 50 para asegurar tomas parciales de beneficios. En el próximo ciclo, si persisten los movimientos laterales sin momentum, procederé a rotar capital hacia oportunidades con mayor tracción."
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
