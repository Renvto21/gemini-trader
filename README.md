# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 15:00:52`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.31 USD** | **$19.82 USD** | **$39.13 USD** | 🔴 **-2.17%** ($-0.87) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $341.81 | $9.87 | 📉 -1.25% | 4h 10m |
| `SOL-USD` | 0.095511 | $104.70 | $104.18 | $9.95 | 📉 -0.50% | 2h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo bajista generalizado en la mayoría de los activos tradicionales y criptomonedas, con índices como QQQ, SPY y NVDA bajo sus medias móviles y con niveles de RSI de 1 hora extremadamente deprimidos (<20). AAPL se mantiene relativamente resiliente operando en tendencia alcista sobre su SMA20, mientras que las criptomonedas como SOL-USD y ETH-USD muestran debilidad de corto plazo pero podrían generar oportunidades de rebote por sobreventa si se activa el momentum intradiario."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 70%): AAPL mantiene una tendencia alcista estructural sobre su SMA20 y se encuentra con un RSI de 1h en 55.4, mostrando estabilidad a pesar de la presión bajista general del mercado. Mantengo la posición buscando el objetivo de take-profit.
- **[HOLD] SOL-USD** (Confianza: 60%): SOL-USD registra una pérdida leve del -0.5% y un RSI de 1h en 26.1. Aunque el impulso de corto plazo se ha ralentizado, la zona actual representa un soporte potencial para un rebote técnico de media reversión, por lo que mantendré la posición vigilando estrictamente el stop-loss.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré las posiciones de AAPL y SOL-USD vigilando de cerca el stop-loss estricto del -2.0%. Para AAPL, esperaré una aproximación a la zona de sobrecompra en RSI de 1h (>70) o el objetivo de take-profit entre +2.0% y +3.5% para asegurar beneficios. En cuanto a SOL-USD, el RSI de 1h ha vuelto a caer a 26.1; mantendré la posición actual monitoreando un giro inminente en el momentum intradiario. Si persiste el estancamiento o la pérdida supera el -2.0%, procederé a recortar pérdidas inmediatamente para liberar liquidez."
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
