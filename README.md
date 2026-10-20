# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 15:01:05`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.91 USD** | **$39.03 USD** | 🔴 **-2.42%** ($-0.97) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.89 | $9.98 | 📉 -0.22% | 2h 59m |
| `ETH-USD` | 0.004058 | $2452.17 | $2447.00 | $9.93 | 📉 -0.21% | 1h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un comportamiento mixto con un sesgo bajista general en los principales índices y activos (bajo SMA20), aunque las criptomonedas mantienen un tono relativamente estable con leves ganancias en 24 horas. Los activos en cartera (AAPL y ETH-USD) se encuentran operando con ligeras pérdidas estancadas, sin la fuerza esperada de rebote en este ciclo preciso. AAPL muestra un RSI de 1 hora moderado en 42.7 y ETH-USD se mantiene cerca de la zona de entrada con un RSI de 1 hora en 60.9, pero con un cambio de 1 hora ligeramente negativo (-0.04%). Dado que mantenemos una postura agresiva y de rotación activa, conservaremos ETH-USD a la espera de un impulso mayor hacia el objetivo de take-profit, mientras que mantendremos temporalmente a AAPL evaluando su próximo movimiento."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD se encuentra abierto 24/7 con una pérdida menor del -0.21%. Su RSI de 1 hora está en 60.9, lo que indica que aún tiene espacio para buscar la zona de sobrecompra (>70) donde ejecutaremos el take-profit según la estrategia.
- **[HOLD] AAPL** (Confianza: 60%): AAPL registra una pérdida marginal de -0.22%. Aunque el mercado está abierto, se prefiere mantener por el momento monitoreando su soporte y stop-loss antes de ejecutar una venta forzada, evaluando si recupera fuerza en el corto plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener ETH-USD y AAPL en observación cercana. Para el próximo ciclo, si ETH-USD alcanza el objetivo de take-profit entre +2.0% y +3.5% o su RSI de 1 hora supera 70, proceder a vender para asegurar ganancias. Si AAPL profundiza pérdidas acercándose al stop-loss de -2.0% o continúa estancada sin momentum, liquidaremos la posición para liberar capital y buscar nuevas oportunidades de alta convicción en criptomonedas con mayor volatilidad y volumen."
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
