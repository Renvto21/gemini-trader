# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 02:00:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.73 USD** | **$38.73 USD** | 🔴 **-3.17%** ($-1.27) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 15h 20m |
| `ETH-USD` | 0.004178 | $2393.62 | $2408.43 | $10.06 | 📈 +0.62% | 13h 9m |
| `SOL-USD` | 0.096034 | $104.13 | $105.07 | $10.09 | 📈 +0.90% | 9h 20m |
| `BTC-USD` | 0.000105 | $81767.70 | $81967.24 | $8.59 | 📈 +0.24% | 8h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene operando 24/7 con un comportamiento lateral a ligeramente alcista, mientras que los mercados tradicionales se encuentran cerrados. Las posiciones en cripto (SOL, ETH, BTC) muestran rendimientos positivos cercanos al rango objetivo, acercándose a condiciones de sobrecompra en gráficos de 1 hora (RSI de SOL en 67.4 y ETH en 63.8), lo que sugiere vigilar de cerca la toma de beneficios para asegurar ganancias rápidas."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD presenta una ganancia actual de +0.9% y un RSI de 1 hora en 67.4, acercándose a la zona de sobrecompra (>70). Se mantiene la posición para buscar el objetivo de take-profit del +2%.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un beneficio del +0.62% con un RSI de 1 hora en 63.8. Se mantiene en cartera esperando la extensión del impulso alcista hacia el rango objetivo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones activas actuales en Cripto (SOL-USD, ETH-USD, BTC-USD) y la posición en QQQ a la espera de la apertura de Wall Street. Monitorear los niveles de RSI de 1 hora en SOL y ETH; si superan 70, proceder con la venta parcial o total para asegurar ganancias del +1% al +2.5%. No abrir nuevas posiciones hasta liberar efectivo con alguna toma de beneficios."
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
