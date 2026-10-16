# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 18:50:36`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.05 USD** | **$38.34 USD** | 🔴 **-4.16%** ($-1.66) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.17 | $10.04 | 📈 +0.44% | 3h 49m |
| `ETH-USD` | 0.004144 | $2412.98 | $2414.13 | $10.00 | 📈 +0.05% | 2h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la actividad se concentra exclusivamente en las criptomonedas (ABIERTO 24/7). Los principales activos cripto (BTC-USD, ETH-USD y SOL-USD) muestran un comportamiento lateral con sesgo bajista y un impulso moderado. SOL-USD y ETH-USD se mantienen dentro de nuestras posiciones abiertas con ganancias marginales (+0.44% y +0.05% respectivamente), consolidando tras haber salido de condiciones de sobreventa. No se observan todavía los catalizadores de fuerte volumen necesarios para alcanzar la zona de take-profit objetivo entre +2.0% y +3.5%, pero tampoco han activado los niveles de stop-loss. Con $18.29 USD en efectivo, mantenemos la disciplina operativa y una reserva de liquidez adecuada."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 65%): La posición en SOL-USD se mantiene en terreno positivo (+0.44%) tras poco menos de 4 horas abierta. El precio se consolida de manera estable y no ha alcanzado ni el objetivo de take-profit ni el stop-loss, por lo que se prefiere mantener para permitir que el momentum alcista se desarrolle.
- **[HOLD] ETH-USD** (Confianza: 65%): ETH-USD muestra un comportamiento plano (+0.05%) desde su apertura reciente. El RSI diario se encuentra en niveles de sobreventa, lo que sugiere un potencial rebote técnico a mediano plazo que justifica mantener la posición abierta.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales en SOL-USD y ETH-USD a la espera de un incremento en el volumen que impulse el rebote técnico hacia el objetivo de take-profit (+2.0% a +3.5%). Monitorearemos de cerca el RSI de 1 hora y el comportamiento de BTC-USD. Si alguna posición rompe a la baja superando el -2.0% de pérdida, ejecutaremos el stop-loss de inmediato para proteger el capital. No se realizarán nuevas compras en este ciclo para conservar la liquidez y dejar trabajar a las posiciones actuales."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **63** | 🎯 **38.1%** (24W / 25L / 14BE) | 🔴 **$-1.60 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 16:30` | 🟢 BUY | `ETH-USD` | $10.00 | $2412.98 | ETH-USD muestra un RSI diario en niveles de sobreventa extrema (30.3) y un cambio positivo... |
| `2026-10-16 16:30` | 🔴 SELL (-0.11$) | `MSFT` | $6.39 | $526.18 | MSFT lleva más de 1 día y 5 horas abierto mostrando debilidad persistente y un rendimiento... |
| `2026-10-16 15:01` | 🟢 BUY | `SOL-USD` | $10.00 | $103.71 | SOL-USD presenta un RSI de 1 hora en 34.3 saliendo de la zona de sobreventa extrema, acomp... |
| `2026-10-16 14:30` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2399.90 | ETH-USD ha rebasado el umbral estricto de stop-loss (-2.12%), operando en tendencia bajist... |
| `2026-10-16 13:40` | 🔴 SELL (-0.02$) | `NVDA` | $7.98 | $216.80 | NVDA lleva más de 24 horas abierto operando bajo la SMA20 con un momentum débil, acumula u... |

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
