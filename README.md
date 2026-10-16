# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 01:10:54`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.17 USD** | **$24.59 USD** | **$38.76 USD** | 🔴 **-3.11%** ($-1.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 14h 20m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 12h 50m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 12h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra actualmente cerrado y con precios congelados, por lo que las acciones en cartera (MSFT, QQQ, NVDA) permanecen sin cambios en su cotización. Por otro lado, los activos cripto (BTC-USD, ETH-USD, SOL-USD) están abiertos 24/7 pero muestran un momentum moderado sin configuraciones claras de sobreventa extrema en el RSI de 1h que justifiquen una entrada inmediata. La prioridad actual es mantener la liquidez y esperar la apertura de los mercados tradicionales para buscar la toma de beneficios en las posiciones actuales si alcanzan el rango objetivo."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 80%): El mercado de acciones está cerrado y la posición muestra una ligera ganancia (0.8%). Se mantiene a la espera de la apertura para buscar el take-profit entre +2.0% y +3.5%.
- **[HOLD] QQQ** (Confianza: 80%): El activo se encuentra en mercado cerrado con una ganancia marginal del 0.4%. Mantenemos la posición para capturar el rebote técnico una vez reanude la sesión.
- **[HOLD] NVDA** (Confianza: 75%): La posición está prácticamente plana (-0.04%) en un mercado cerrado. Esperaremos la apertura bursátil para evaluar su comportamiento y decidir si se rota el capital o se mantiene buscando el rebote.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré las posiciones actuales (MSFT, QQQ, NVDA) vigilando la apertura de Wall Street para asegurar beneficios en cuanto toquen el rango de +2.0% a +3.5%. En criptomonedas, esperaré a que se produzca una corrección más pronunciada con un RSI de 1h por debajo de 35 antes de arriesgar capital en SOL-USD o ETH-USD. La reserva de efectivo está en niveles saludables y no se realizarán operaciones en este ciclo para evitar sobrecomprar en mercados cerrados."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **58** | 🎯 **41.4%** (24W / 20L / 14BE) | 🔴 **$-1.22 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |
| `2026-10-15 12:10` | 🔴 SELL (+0.14$) | `ETH-USD` | $6.14 | $2417.73 | ETH-USD ha alcanzado un rendimiento del +2.33%, cumpliendo con el rango establecido para l... |
| `2026-10-15 11:50` | 🔴 SELL (+0.13$) | `SOL-USD` | $6.13 | $104.21 | SOL-USD ha alcanzado un rendimiento de +2.11%, cumpliendo con la regla de toma rápida de g... |

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
