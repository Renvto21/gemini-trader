# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 13:40:57`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.97 USD** | **$39.09 USD** | 🔴 **-2.28%** ($-0.91) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $340.80 | $10.00 | 📈 +0.05% | 1h 39m |
| `GLD` | 0.026337 | $379.70 | $378.23 | $9.96 | 📉 -0.39% | 1h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un comportamiento mixto con un sesgo moderadamente defensivo. Los activos tradicionales como AAPL y GLD se mantienen estables pero sin el impulso alcista rápido que buscamos, operando en rangos estrechos tras casi dos horas. Las criptomonedas operan de manera lateral con ligeros sesgos positivos pero sin detonar rupturas claras de sobreventa en 1h. Mantenemos la cautela y la disciplina operativa protegiendo el capital."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 60%): La posición en AAPL se mantiene con un rendimiento casi plano (0.05%) tras 1 hora y 39 minutos. Su tendencia diaria sigue siendo alcista y el RSI de 1h se recupera lentamente hacia 39.7. No amerita venta ni compra adicional por el momento.
- **[HOLD] GLD** (Confianza: 60%): La posición en GLD registra una pérdida menor de -0.39%, manteniéndose muy por encima del stop-loss estricto de -2.0%. El RSI de 1h sigue bajo en 32.2, sugiriendo que la presión vendedora se debilita. Daremos espacio para que se materialice el rebote técnico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos nuestras posiciones abiertas actuales (AAPL y GLD) durante un ciclo más al no haber alcanzado ni el stop-loss de -2.0% ni el take-profit de +2.0%. Si en el próximo ciclo AAPL o GLD no muestran un incremento claro en su momentum (rsi_1h superior a 50) y se estancan, procederemos a la rotación de capital hacia activos de mayor volatilidad o cripto con mayor dinamismo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **81** | 🎯 **44.4%** (36W / 30L / 15BE) | 🔴 **$-0.74 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-20 12:01` | 🟢 BUY | `GLD` | $10.00 | $379.70 | GLD presenta un RSI de 1 hora en 31.4, acercándose a la zona ideal de sobreventa para acti... |
| `2026-10-20 12:01` | 🟢 BUY | `AAPL` | $10.00 | $340.64 | AAPL se encuentra en tendencia alcista diaria con un RSI de 1 hora en 33.1 (cercano a sobr... |
| `2026-10-20 11:10` | 🔴 SELL (+0.12$) | `BTC-USD` | $8.69 | $82949.93 | BTC-USD muestra un RSI de 1 hora en 72.2 (sobrecompra) y un rendimiento positivo de +1.45%... |
| `2026-10-20 11:10` | 🔴 SELL (+0.28$) | `SOL-USD` | $10.28 | $107.08 | SOL-USD registra un excelente rendimiento de +2.83% con un RSI de 1 hora en sobrecompra (7... |
| `2026-10-20 11:10` | 🔴 SELL (+0.23$) | `ETH-USD` | $10.23 | $2449.11 | ETH-USD ha alcanzado un PnL de +2.32% y su RSI de 1 hora ha tocado el nivel de sobrecompra... |

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
