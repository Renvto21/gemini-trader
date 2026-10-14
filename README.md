# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 14:40:56`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.31 USD** | **$19.87 USD** | **$39.17 USD** | 🔴 **-2.07%** ($-0.83) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $341.78 | $9.87 | 📉 -1.26% | 3h 50m |
| `SOL-USD` | 0.095511 | $104.70 | $104.61 | $9.99 | 📉 -0.09% | 2h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento predominantemente bajista de corto plazo en la mayoría de los activos tradicionales y criptomonedas, con múltiples índices y criptos operando por debajo de sus medias móviles de 20 días y RSI de 1 hora comprimidos en zonas de sobreventa. Los activos en cartera se mantienen estables pero sin el momentum alcista esperado. AAPL muestra un RSI de 1h en 55.3 manteniéndose sobre la SMA20, mientras que SOL-USD presenta un RSI de 1h en 28.7 en una zona de posible consolidación."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 70%): AAPL se mantiene sobre su SMA20 con un RSI de 1h neutral (55.3) y una pérdida menor (-1.26%). No ha tocado el stop-loss ni el objetivo de take-profit, por lo que se mantiene la posición para permitir que el momentum se desarrolle.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD tiene un holding time corto (2h 10m) y un PnL plano (-0.09%). Aunque el RSI de 1h está en 28.7, se mantiene la posición a la espera de un volumen de compra que impulse el rebote técnico hacia la zona objetivo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (AAPL y SOL-USD) mientras no alcancen el stop-loss estricto del -2.0% o el take-profit entre +2.0% y +3.5%. Para el siguiente ciclo, estar atentos a cualquier ruptura del RSI de 1h por encima de 35 con cambio porcentual positivo en criptos como ETH-USD o BTC-USD para evaluar posibles entradas o rotación de capital."
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
