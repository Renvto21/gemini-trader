# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 06:20:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.47 USD** | **$38.47 USD** | 🔴 **-3.82%** ($-1.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 19h 39m |
| `ETH-USD` | 0.004178 | $2393.62 | $2382.24 | $9.95 | 📉 -0.48% | 17h 29m |
| `SOL-USD` | 0.096034 | $104.13 | $104.10 | $10.00 | 📉 -0.03% | 13h 39m |
| `BTC-USD` | 0.000105 | $81767.70 | $81426.78 | $8.53 | 📉 -0.42% | 13h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con una tendencia general bajista pero mostrando señales incipientes de estabilización y acumulación en marcos temporales cortos. Los activos tradicionales como QQQ están cerrados, por lo que la liquidez activa se concentra en mantener y evaluar el comportamiento de las posiciones abiertas en criptomonedas (ETH-USD, SOL-USD, BTC-USD). El RSI de 1 hora se mantiene en niveles neutrales sin alcanzar todavía la zona de sobrecompra (>70) que active la toma de beneficios inmediata, y las pérdidas actuales se mantienen contenidas por debajo de nuestro límite de stop-loss de -2.0%."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD muestra un RSI diario muy deprimido (21.2) y un RSI de 1h en recuperación (53.2) con un cambio horario levemente positivo. Se mantiene la posición a la espera de que el rebote técnico alcance el objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (QQQ, ETH-USD, SOL-USD y BTC-USD) dado que ninguna ha alcanzado el stop-loss estricto de -2.0% ni el objetivo de take-profit de +2.5% a +3.5%. Vigilar de cerca el comportamiento de SOL-USD y BTC-USD en busca de un impulso alcista que eleve el RSI de 1 hora por encima de 70 para asegurar ganancias parciales o totales. En el siguiente ciclo, si alguna posición se estanca o rompe soportes a la baja, procederé a vender inmediatamente para rotar el capital hacia oportunidades de mayor momentum."
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
