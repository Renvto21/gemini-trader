# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 11:01:01`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.12 USD** | **$24.48 USD** | **$38.60 USD** | 🔴 **-3.50%** ($-1.40) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $537.14 | $6.52 | 📈 +0.37% | 1d 0h |
| `NVDA` | 0.036812 | $217.32 | $216.27 | $7.96 | 📉 -0.48% | 22h 10m |
| `ETH-USD` | 0.002855 | $2451.90 | $2456.55 | $7.01 | 📈 +0.19% | 6h 30m |
| `SOL-USD` | 0.028214 | $106.33 | $105.63 | $2.98 | 📉 -0.66% | 5h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un tono mixto con presión bajista en tecnológicas y criptomonedas, aunque se observan oportunidades de rebote técnico en activos sobrevendidos. NVDA y QQQ continúan débiles, pero NVDA mantiene un RSI de 1 hora extremadamente bajo (22.3), lo que podría anticipar un rebote inminente. Las criptomonedas ETH-USD y SOL-USD se mantienen estables con ligeras recuperaciones, mientras que los mercados de EE.UU. están abiertos y activos para operar."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 70%): MSFT se mantiene estable sobre la SMA20 con una leve ganancia y tendencia alcista en el contexto diario, por lo que decidimos mantener la posición en busca de mayores beneficios.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos MSFT, ETH-USD y SOL-USD evaluando su momentum. NVDA se mantiene bajo vigilancia estricta debido a su debilidad prolongada; si no muestra un rebote en el próximo ciclo, procederemos a liquidar la posición para evitar mayores pérdidas y liberar capital. Mantendremos liquidez cercana al mínimo operativo de $4.00 USD."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **59** | 🎯 **40.7%** (24W / 21L / 14BE) | 🔴 **$-1.26 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 10:50` | 🔴 SELL (-0.04$) | `QQQ` | $9.95 | $721.83 | QQQ lleva más de 22 horas abierto operando bajo la SMA20 con un RSI de 1 hora en 30.2 y un... |
| `2026-10-16 05:10` | 🟢 BUY | `SOL-USD` | $3.00 | $106.33 | SOL-USD presenta un RSI diario en zona de sobreventa extrema (29.0) y un cambio positivo e... |
| `2026-10-16 04:30` | 🟢 BUY | `ETH-USD` | $7.00 | $2451.90 | Aprovechamos la liquidez disponible sobre la reserva mínima ($14.17 vs $4.00 requeridos) p... |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |

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
