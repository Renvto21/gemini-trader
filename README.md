# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 07:30:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.86 USD** | **$38.47 USD** | 🔴 **-3.83%** ($-1.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 20h 39m |
| `BTC-USD` | 0.000061 | $81640.68 | $80931.98 | $4.96 | 📉 -0.87% | 10h 20m |
| `ETH-USD` | 0.002539 | $2362.71 | $2361.78 | $6.00 | 📉 -0.04% | 6h 19m |
| `SOL-USD` | 0.058789 | $102.06 | $101.96 | $5.99 | 📉 -0.10% | 4h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando en un entorno bajista de corto plazo pero con compresión de precios en gráficos horarios, lo que sugiere posibles intentos de rebote técnico (Mean Reversion). Los mercados tradicionales (AAPL, QQQ, SPY) permanecen cerrados, por lo que toda la atención táctica se concentra en la gestión de las criptomonedas abiertas (ETH-USD, SOL-USD, BTC-USD). Las posiciones muestran pérdidas mínimas estables y se observa una ligera consolidación a la espera de un catalizador de volumen para activar ganancias o cortar pérdidas rigurosamente."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD se mantiene estable con una pérdida marginal del -0.04% tras su reciente apertura. Su RSI de 1h en 35 muestra que aún conserva potencial de rebote técnico sin haber activado las condiciones de stop-loss ni take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en criptomonedas (BTC-USD, ETH-USD, SOL-USD) y la posición tecnológica (AAPL) que continúa cerrada. Monitorear de cerca los indicadores de 1h y el comportamiento de las criptomonedas para asegurar beneficios si ETH-USD o SOL-USD reactivan su impulso hacia el rango de +2% a +3.5%. Proteger rigurosamente el capital respetando el stop-loss de -2.0% ante cualquier quiebre bajista imprevisto. Si alguna posición estancada pierde tracción o supera el límite de tiempo sin momentum, procederé a rotar el capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **54** | 🎯 **40.7%** (22W / 18L / 14BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 03:20` | 🟢 BUY | `SOL-USD` | $6.00 | $102.06 | SOL-USD muestra un RSI de 1h en 33.3 saliendo de zonas de compresión bajista, acompañado d... |
| `2026-10-15 01:10` | 🟢 BUY | `ETH-USD` | $6.00 | $2362.71 | ETH-USD presenta un RSI de 1h extremadamente bajo en 23.5 saliendo de sobreventa y un camb... |
| `2026-10-14 23:30` | 🔴 SELL (-0.30$) | `SOL-USD` | $9.70 | $101.32 | La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin ... |
| `2026-10-14 23:30` | 🔴 SELL (-0.32$) | `ETH-USD` | $9.68 | $2340.86 | 🚨 STOP-LOSS AUTOMÁTICO (CIRCUIT BREAKER): Pérdida de -3.20% superó el límite de seguridad ... |
| `2026-10-14 21:10` | 🟢 BUY | `BTC-USD` | $5.00 | $81640.68 | BTC-USD presenta un RSI de 1h en 24.9 (sobreventa extrema) y liquidez disponible suficient... |

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
