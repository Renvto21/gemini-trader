# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 14:01:11`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.93 USD** | **$39.05 USD** | 🔴 **-2.36%** ($-0.95) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $340.41 | $9.99 | 📉 -0.07% | 1h 59m |
| `ETH-USD` | 0.004058 | $2452.17 | $2448.76 | $9.94 | 📉 -0.14% | 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo defensivo general con la mayoría de los activos bajo la media móvil de 20 días en el gráfico diario. Sin embargo, las criptomonedas mantienen un mejor comportamiento en el marco de 24 horas. Los mercados de acciones y materias primas registran ligeros retrocesos en el corto plazo."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 70%): La posición lleva cerca de 2 horas abierta con una pérdida mínima de -0.07%. Su tendencia diaria es alcista y el rsi_1h está en 38.4, aproximándose a la zona de rebote técnico sin romper soportes críticos.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un buen impulso de 24 horas con un +1.83% y un rsi_1h estable en 60.9. Mantenemos la posición para capturar la continuación del movimiento alcista intradiario.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos AAPL y ETH-USD por este ciclo. AAPL muestra un rsi_1h de 38.4 y mantiene una tendencia diaria alcista, por lo que le daremos margen para buscar el rebote. ETH-USD tiene un rsi_1h saludable de 60.9 y un rendimiento de 24h positivo del 1.83%. Establecemos stop-loss estricto en -2.0% para ambas posiciones y buscaremos take-profit al alcanzar +2.5% de ganancia o si el rsi_1h supera 70."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **82** | 🎯 **43.9%** (36W / 31L / 15BE) | 🔴 **$-0.79 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-20 13:51` | 🟢 BUY | `ETH-USD` | $9.95 | $2452.17 | ETH-USD muestra un excelente impulso de corto plazo con change_1h_pct positivo (+0.55%) y ... |
| `2026-10-20 13:51` | 🔴 SELL (-0.05$) | `GLD` | $9.95 | $377.90 | GLD se encuentra estancado con un rendimiento ligeramente negativo (-0.47%) y un rsi_1h de... |
| `2026-10-20 12:01` | 🟢 BUY | `GLD` | $10.00 | $379.70 | GLD presenta un RSI de 1 hora en 31.4, acercándose a la zona ideal de sobreventa para acti... |
| `2026-10-20 12:01` | 🟢 BUY | `AAPL` | $10.00 | $340.64 | AAPL se encuentra en tendencia alcista diaria con un RSI de 1 hora en 33.1 (cercano a sobr... |
| `2026-10-20 11:10` | 🔴 SELL (+0.12$) | `BTC-USD` | $8.69 | $82949.93 | BTC-USD muestra un RSI de 1 hora en 72.2 (sobrecompra) y un rendimiento positivo de +1.45%... |

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
