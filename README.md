# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 15:10:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.31 USD** | **$19.84 USD** | **$39.15 USD** | 🔴 **-2.12%** ($-0.85) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.34 | $9.89 | 📉 -1.10% | 4h 19m |
| `SOL-USD` | 0.095511 | $104.70 | $104.21 | $9.95 | 📉 -0.47% | 2h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general muestra un tono bajista con la mayoría de los activos principales por debajo de sus medias móviles de 20 períodos, reflejando presión a la baja en el corto plazo. AAPL se mantiene relativamente resiliente sobre su tendencia alcista con un RSI de 1h en 56.8, mientras que SOL-USD muestra debilidad temporal con un RSI de 1h en 26.2, manteniéndose cerca de nuestra zona de control sin romper el stop-loss estricto del -2.0%."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 75%): AAPL se encuentra operando de forma estable sobre su soporte macro con un RSI de 1h en 56.8, manteniendo una pérdida contenida del -1.1%. Esperaremos a que se acerque a la zona de take-profit (+2% a +3.5%) para realizar ganancias.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD registra una pequeña pérdida del -0.47% con un RSI de 1h en 26.2. Dado que el mercado cripto opera 24/7 y la pérdida está muy por debajo del límite de stop-loss del -2.0%, mantendremos la posición a la espera de un rebote por reversión a la media.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré las posiciones de AAPL y SOL-USD vigilando de cerca el stop-loss estricto del -2.0%. Para AAPL, esperaré una aproximación a la zona de sobrecompra en RSI de 1h (>70) o el objetivo de take-profit entre +2.0% y +3.5% para asegurar beneficios. En cuanto a SOL-USD, el RSI de 1h se mantiene deprimido; mantendré la posición actual monitoreando un giro inminente en el momentum intradiario. Si persiste el estancamiento o la pérdida supera el -2.0%, procederé a recortar pérdidas inmediatamente para liberar liquidez y buscar oportunidades en criptomonedas o tecnología."
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
