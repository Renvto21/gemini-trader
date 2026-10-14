# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 13:11:04`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.31 USD** | **$19.88 USD** | **$39.19 USD** | 🔴 **-2.02%** ($-0.81) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $344.31 | $9.95 | 📉 -0.53% | 2h 20m |
| `SOL-USD` | 0.095511 | $104.70 | $104.03 | $9.94 | 📉 -0.64% | 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general muestra presión bajista con la mayoría de los activos cotizando por debajo de su SMA20 y RSI de 1 hora deprimidos en varios sectores. Sin embargo, las criptomonedas y algunos activos tecnológicos específicos siguen operando 24/7 con oportunidades tácticas de rebote. AAPL mantiene una tendencia alcista a nivel diario pero muestra un ligero retroceso en la última hora, mientras que SOL-USD se mantiene en vigilancia estrecha ante posibles oscilaciones de corto plazo."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 70%): AAPL mantiene una estructura alcista diaria saludable (por encima de SMA20) a pesar del leve retroceso de 1h. El RSI diario está en 59.1 y no ha alcanzado el objetivo de take-profit, por lo que se mantiene la posición actual protegiendo el stop-loss.
- **[HOLD] SOL-USD** (Confianza: 65%): SOL-USD muestra un cambio de 1h positivo ligero (+0.27%) aunque con un RSI de 1h bajo en 21.7. Dado que el tiempo abierto es corto (40m), se le dará margen para desarrollar el rebote técnico esperado sin incurrir en pérdidas prematuras.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos AAPL y SOL-USD bajo estrecha supervisión aplicando un stop-loss estricto a -2.0% si el impulso falla o los soportes ceden. Conservaremos el efectivo disponible ($19.31) para asegurar una liquidez prudente, esperando confirmaciones adicionales de volumen y RSI antes de incrementar la exposición o abrir nuevas posiciones."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **51** | 🎯 **43.1%** (22W / 15L / 14BE) | 🔴 **$-0.59 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 12:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.70 | SOL-USD presenta un RSI de 1h en 29.2 saliendo de sobreventa extrema y un cambio de 1h pos... |
| `2026-10-14 11:20` | 🔴 SELL (-0.09$) | `BTC-USD` | $5.89 | $81874.95 | BTC-USD lleva más de 14 horas abierto con un PnL negativo persistente (-1.51%) y un RSI de... |
| `2026-10-14 10:50` | 🟢 BUY | `AAPL` | $10.00 | $346.15 | AAPL se encuentra con un excelente momentum alcista intradiario, un incremento de 1.4% en ... |
| `2026-10-14 10:10` | 🔴 SELL (-0.11$) | `SOL-USD` | $5.89 | $105.41 | La posición en SOL-USD acumula una pérdida cercana al -1.9%, rozando nuestro stop-loss est... |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |

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
