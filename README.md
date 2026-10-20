# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 10:00:53`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.53 USD** | **$38.53 USD** | 🔴 **-3.68%** ($-1.47) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 23h 20m |
| `ETH-USD` | 0.004178 | $2393.62 | $2391.44 | $9.99 | 📉 -0.09% | 21h 9m |
| `SOL-USD` | 0.096034 | $104.13 | $104.27 | $10.01 | 📈 +0.13% | 17h 20m |
| `BTC-USD` | 0.000105 | $81767.70 | $81447.46 | $8.53 | 📉 -0.39% | 16h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra completamente cerrado, manteniendo los precios y métricas congelados para activos como QQQ. En el sector cripto (abierto 24/7), los activos muestran un movimiento lateral a bajista de corto plazo con cambios de 1 hora cercanos a cero y valores de RSI de 1 hora estancados en la zona de 38 a 41. Las posiciones actuales muestran ligeras variaciones negativas pero se mantienen estables dentro de los límites del stop-loss."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 60%): La posición se mantiene estable con una pequeña ganancia del 0.13%. El RSI de 1 hora está en 39.6 y el mercado cripto muestra baja volatilidad horaria. Se mantiene a la espera de que supere la zona de sobrecompra para asegurar beneficios.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (QQQ, ETH-USD, SOL-USD, BTC-USD) a la espera de un catalizador que impulse el RSI de 1 hora por encima de 50 para asegurar tomas de ganancias entre +2.0% y +3.5%. Vigilar estrictamente el soporte de las criptomonedas para ejecutar stop-loss si alguna posición supera la pérdida de -2.0%. Dado que no hay efectivo disponible y las posiciones llevan más de 16 horas abiertas sin gran dinamismo, en el siguiente ciclo evaluaré rotar capital si el impulso no se materializa."
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
