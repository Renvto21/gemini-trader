# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 03:40:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.62 USD** | **$38.62 USD** | 🔴 **-3.44%** ($-1.38) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 16h 59m |
| `ETH-USD` | 0.004178 | $2393.62 | $2396.54 | $10.01 | 📈 +0.12% | 14h 49m |
| `SOL-USD` | 0.096034 | $104.13 | $104.70 | $10.05 | 📈 +0.55% | 10h 59m |
| `BTC-USD` | 0.000105 | $81767.70 | $81749.99 | $8.56 | 📉 -0.02% | 10h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que la liquidez y operativa se concentran exclusivamente en las criptomonedas (ABIERTO 24/7). Los activos en cartera (QQQ, ETH-USD, SOL-USD y BTC-USD) se mantienen relativamente estables con movimientos laterales de corto plazo, sin alcanzar todavía los objetivos de take-profit (+2% a +3.5%) ni activar los stop-loss (-2%). Mantenemos las posiciones activas a la espera de un mayor impulso alcista que permita asegurar beneficios."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición muestra un pequeño beneficio del 0.55% y un RSI de 1 hora en 55.5 con tendencia alcista leve. Mantenemos la posición a la espera de que se acerque a la zona de sobrecompra para asegurar beneficios.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Continuar monitoreando las posiciones actuales en criptomonedas (SOL-USD, ETH-USD, BTC-USD) y QQQ. Estar atento a la apertura de los mercados tradicionales para evaluar la rotación de capital si alguna posición permanece estancada. El objetivo es asegurar ganancias parciales al alcanzar un PnL de +2% o si el RSI de 1 hora supera los 70 puntos."
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
