# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 04:40:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$12.01 USD** | **$39.53 USD** | 🔴 **-1.17%** ($-0.47) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83362.88 | $6.02 | 📈 +0.28% | 7h 39m |
| `SOL-USD` | 0.055840 | $107.45 | $107.25 | $5.99 | 📉 -0.19% | 5h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con un sesgo moderadamente positivo, mientras que los mercados tradicionales permanecen cerrados. BTC-USD y SOL-USD se mantienen estables con ligeras ganancias pero sin alcanzar aún los umbrales de take-profit (>2.0%). El RSI de 1H en ambos activos se encuentra en niveles neutrales (alrededor de 50-60), lo que sugiere consolidación tras el rebote inicial. Mantenemos el enfoque táctico en cripto debido a las restricciones de horario en Wall Street."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD mantiene un rendimiento positivo estable (+0.28%) tras casi 8 horas de holding. El RSI de 1H se encuentra en 59.3, sin llegar a sobrecompra y sin señales de reversión bajista. Se mantiene la posición a la espera del objetivo de take-profit.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD muestra un comportamiento neutral (-0.19%) con un RSI de 1H en 52.7. Aunque el movimiento ha sido lateral, el RSI diario en sobreventa sugiere potencial alcista a mediano plazo, por lo que se mantiene la posición en busca de un rebote mayor.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de BTC-USD y SOL-USD en este ciclo, vigilando de cerca si el RSI de 1H se aproxima a sobrecompra (>70) para realizar tomas de beneficios parciales o totales. Si SOL-USD o BTC-USD pierden soporte y su PnL cae por debajo de -1.5%, consideraremos recortar posiciones para preservar capital. Evaluaremos nuevas entradas en cripto solo si se presentan oportunidades de alta convicción con liquidez disponible."
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
