# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 09:10:53`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.84 USD** | **$38.45 USD** | 🔴 **-3.88%** ($-1.55) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 22h 20m |
| `BTC-USD` | 0.000061 | $81640.68 | $80792.63 | $4.95 | 📉 -1.04% | 12h 0m |
| `ETH-USD` | 0.002539 | $2362.71 | $2359.47 | $5.99 | 📉 -0.14% | 8h 0m |
| `SOL-USD` | 0.058789 | $102.06 | $101.87 | $5.99 | 📉 -0.19% | 5h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado y congelado, por lo que toda la actividad debe centrarse exclusivamente en las criptomonedas (abiertas 24/7). Las criptos principales (BTC-USD, ETH-USD, SOL-USD) muestran un comportamiento lateral a ligeramente bajista en el corto plazo, con RSI de 1 hora comprimidos cerca de zonas de soporte pero sin mostrar todavía la fuerza de rebote esperada. El portafolio acumula una leve pérdida general (-3.88%), manteniendo posiciones dentro de los márgenes de stop-loss estricto (-2.0%). Dado que los activos abiertos llevan horas sin romper al alza de forma contundente y no se observan catalizadores inmediatos de impulso, se opta por mantener la estructura actual y conservar la liquidez disponible a la espera de una ruptura clara de volumen."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD se mantiene estable con una pérdida marginal del -0.14% tras 8 horas de holding. El RSI de 1 hora se sitúa en 33.6, consolidando en zona de soporte. Se mantiene a la espera de un cambio de tendencia intradiario positivo que active el take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas (AAPL, BTC-USD, ETH-USD, SOL-USD) mientras respeten el stop-loss estricto del -2.0%. Monitorear de cerca los indicadores de ETH-USD y SOL-USD: si el RSI de 1 hora supera los 60 puntos y se registra un take-profit entre +2.0% y +3.5%, ejecutar ventas parciales para asegurar ganancias y liberar liquidez. No abrir nuevas posiciones hasta que se observe una confirmación clara de impulso alcista en el sector cripto o hasta que abran los mercados tradicionales."
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
