# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 13:41:00`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.31 USD** | **$19.94 USD** | **$39.24 USD** | 🔴 **-1.89%** ($-0.76) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $344.80 | $9.96 | 📉 -0.39% | 2h 50m |
| `SOL-USD` | 0.095511 | $104.70 | $104.43 | $9.97 | 📉 -0.26% | 1h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se encuentra bajo presión con una tendencia bajista de corto plazo (por debajo de las SMA20 en la mayoría de los activos), aunque varios instrumentos muestran condiciones extremas de sobreventa intradiaria en el RSI de 1 hora. AAPL mantiene una postura relativamente sólida y se acerca a la zona de toma de ganancias (RSI 1h en 65), mientras que SOL-USD muestra un intento de rebote con un cambio de 1h positivo a pesar de un RSI bajo. La liquidez disponible se mantiene saludable para aprovechar oportunidades tácticas."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 75%): AAPL mantiene una tendencia alcista diaria sólida y un RSI de 1h en 65, cerca del umbral de sobrecompra (>70) establecido para la toma de ganancias. Mantendremos la posición activa buscando asegurar el beneficio en el corto plazo.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD muestra un cambio de 1h positivo (+0.66%) y un inicio de recuperación técnica. Aunque está bajo la SMA20, el holding time es bajo y daremos margen para que el rebote intradiario se consolide.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener AAPL vigilando de cerca si su RSI de 1h cruza 70 para asegurar beneficios rápidamente, y retener SOL-USD mientras su cambio de 1h sea positivo. Estar preparados para rotar capital hacia ETH-USD o BTC-USD si sus indicadores de 1h muestran una ruptura de volumen alcista más firme desde la sobreventa actual."
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
