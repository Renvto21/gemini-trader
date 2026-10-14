# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 07:10:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$11.94 USD** | **$39.47 USD** | 🔴 **-1.33%** ($-0.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83166.67 | $6.00 | 📈 +0.05% | 10h 9m |
| `SOL-USD` | 0.055840 | $107.45 | $106.37 | $5.94 | 📉 -1.01% | 7h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario tradicional (SPY, QQQ, MSFT, AAPL, NVDA, GLD) se encuentra cerrado, por lo que toda la actividad se concentra en el sector cripto. BTC-USD mantiene un comportamiento lateral con un PnL cercano a cero tras más de 10 horas, mientras que SOL-USD muestra un leve retroceso (-1.01%) con un RSI diario extremadamente bajo (27.0), manteniendo el potencial de rebote pero probando la paciencia del portafolio."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 60%): BTC-USD se mantiene estable sin alcanzar el objetivo de take-profit (+2.0%) ni disparar alertas de stop-loss, con un holding time de 10 horas y un PnL plano de 0.05%.
- **[HOLD] SOL-USD** (Confianza: 55%): SOL-USD registra una pequeña pérdida de -1.01%, manteniéndose por encima de nuestro umbral estricto de stop-loss de -2.0%. Su RSI diario en 27.0 justifica retener la posición a la espera del rebote.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos nuestras posiciones actuales en BTC-USD y SOL-USD ya que ninguna ha alcanzado el stop-loss estricto del -2.0% y sus soportes macro diarios siguen vigentes a pesar del bajo momentum horario. Monitorearemos la evolución de SOL-USD para evaluar una salida si continúa perdiendo terreno o si rompe niveles críticos, manteniendo la liquidez en reserva para futuras oportunidades."
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
