# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 12:01:27`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$29.31 USD** | **$9.97 USD** | **$39.27 USD** | 🔴 **-1.81%** ($-0.73) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $345.00 | $9.97 | 📉 -0.33% | 1h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de acciones y criptomonedas muestra una tendencia bajista general de corto plazo con un sesgo de contracción, aunque varios activos como GLD, ETH-USD y SOL-USD se encuentran en niveles de sobreventa extrema en el RSI de 1 hora. AAPL, nuestra posición abierta actual, se mantiene estable con un RSI de 1h en 63.1 pero mostrando un ligero retroceso de -0.29% en la última hora, aproximándose a nuestro rango objetivo de take-profit sin romper soportes clave."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 75%): La posición en AAPL lleva poco tiempo abierta (1h 10m) y presenta un PnL levemente negativo de -0.33%. El contexto técnico diario sigue siendo alcista sobre la SMA20 y el RSI de 1h se mantiene saludable en 63.1. Daremos tiempo a que evolucione hacia nuestra zona objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos la posición en AAPL activa para buscar el take-profit entre +2.0% y +3.5%, vigilando de cerca que el RSI de 1h no colapse y activando el stop-loss si el precio perfora la zona crítica. El efectivo disponible se mantiene en reserva a la espera de que activos en sobreventa extrema (como ETH-USD o SOL-USD) muestren una confirmación clara de reversión alcista con un cambio de 1h positivo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **51** | 🎯 **43.1%** (22W / 15L / 14BE) | 🔴 **$-0.59 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 11:20` | 🔴 SELL (-0.09$) | `BTC-USD` | $5.89 | $81874.95 | BTC-USD lleva más de 14 horas abierto con un PnL negativo persistente (-1.51%) y un RSI de... |
| `2026-10-14 10:50` | 🟢 BUY | `AAPL` | $10.00 | $346.15 | AAPL se encuentra con un excelente momentum alcista intradiario, un incremento de 1.4% en ... |
| `2026-10-14 10:10` | 🔴 SELL (-0.11$) | `SOL-USD` | $5.89 | $105.41 | La posición en SOL-USD acumula una pérdida cercana al -1.9%, rozando nuestro stop-loss est... |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |

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
