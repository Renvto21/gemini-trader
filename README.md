# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 15:10:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$21.90 USD** | **$16.40 USD** | **$38.30 USD** | 🔴 **-4.25%** ($-1.70) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $527.30 | $6.40 | 📉 -1.47% | 1d 4h |
| `SOL-USD` | 0.096423 | $103.71 | $103.67 | $10.00 | 📉 -0.04% | 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo bajista generalizado en temporalidad diaria con la mayoría de los índices y activos principales cotizando por debajo de su SMA20. Sin embargo, en el corto plazo (1H), varios activos se encuentran en zonas de sobreventa o intentando rebotar. MSFT se mantiene firme con tendencia alcista diaria sobre su SMA20, mientras que criptomonedas como BTC-USD y SOL-USD muestran condiciones técnicas de posible rebote por sobreventa, aunque con cautela por la tendencia bajista macro."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 75%): La posición en MSFT lleva más de 24 horas abierta con una pérdida moderada de -1.47%, pero se mantiene con tendencia alcista sobre la SMA20 y un RSI de 1 hora recuperándose a 36.1. Mantengo la posición esperando el objetivo de take-profit o la señal del stop-loss estricto.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD fue abierto recientemente tras mostrar un RSI de 1 hora saliendo de sobreventa. Su PnL está plano (-0.04%) y se mantiene dentro de los parámetros esperados para cazar un rebote de corto plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantengo la posición en MSFT vigilando el soporte y buscando el objetivo de take-profit en +2.0%, con un stop-loss estricto a -2.0%. En cuanto a SOL-USD, la posición recién abierta se mantiene vigilando el rebote técnico desde la sobreventa, estableciendo el mismo criterio de stop-loss estricto del -2.0% y take-profit rápido del +2.5%. Mantendré liquidez o evaluaré entradas adicionales si el momentum de BTC-USD o SOL-USD se consolida en las siguientes horas."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **62** | 🎯 **38.7%** (24W / 24L / 14BE) | 🔴 **$-1.49 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 15:01` | 🟢 BUY | `SOL-USD` | $10.00 | $103.71 | SOL-USD presenta un RSI de 1 hora en 34.3 saliendo de la zona de sobreventa extrema, acomp... |
| `2026-10-16 14:30` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2399.90 | ETH-USD ha rebasado el umbral estricto de stop-loss (-2.12%), operando en tendencia bajist... |
| `2026-10-16 13:40` | 🔴 SELL (-0.02$) | `NVDA` | $7.98 | $216.80 | NVDA lleva más de 24 horas abierto operando bajo la SMA20 con un momentum débil, acumula u... |
| `2026-10-16 12:50` | 🔴 SELL (-0.06$) | `SOL-USD` | $2.94 | $104.34 | SOL-USD lleva varias horas abierto sin generar el rebote esperado, acumulando una pérdida ... |
| `2026-10-16 10:50` | 🔴 SELL (-0.04$) | `QQQ` | $9.95 | $721.83 | QQQ lleva más de 22 horas abierto operando bajo la SMA20 con un RSI de 1 hora en 30.2 y un... |

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
