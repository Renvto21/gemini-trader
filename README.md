# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 15:50:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$21.90 USD** | **$16.33 USD** | **$38.23 USD** | 🔴 **-4.42%** ($-1.77) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $526.29 | $6.39 | 📉 -1.66% | 1d 4h |
| `SOL-USD` | 0.096423 | $103.71 | $103.10 | $9.94 | 📉 -0.59% | 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se encuentra bajo presión bajista con la mayoría de los índices y criptoactivos cotizando por debajo de su SMA20 y experimentando correcciones en las últimas 24 horas. Los niveles de RSI en 1 hora se mantienen comprimidos en zonas cercanas o inferiores a 35, lo que refleja un sesgo bajista continuo pero con oportunidades latentes de rebote por sobreventa si se activan catalizadores de corto plazo."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 60%): MSFT mantiene una tendencia diaria alcista sobre la SMA20, aunque su PnL se sitúa en -1.66% tras más de un día de holding. Mantendré la posición evaluando si respeta el soporte antes de considerar una rotación de capital.
- **[HOLD] SOL-USD** (Confianza: 65%): SOL-USD presenta un RSI de 1 hora en 30.2, reflejando condiciones de sobreventa. Aunque ha tenido un leve retroceso en la última hora, el plan táctico busca capturar el rebote técnico hacia el objetivo de take-profit, manteniendo el stop-loss estricto en -2.0%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré bajo estricto monitoreo las posiciones actuales de MSFT y SOL-USD. En MSFT, el holding supera un día con un PnL de -1.66%; si el precio rompe a la baja el soporte actual o no muestra recuperación, procederé a vender para liberar capital. En SOL-USD, el RSI de 1 hora se mantiene bajo presión (30.2); evaluaré si logra recuperar terreno hacia el objetivo de take-profit en +2.5% o si se activa el stop-loss en -2.0% para evitar pérdidas mayores. La liquidez en efectivo se mantendrá vigilante para futuras entradas de alta convicción."
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
