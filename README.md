# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 23:40:51`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.06 USD** | **$38.35 USD** | 🔴 **-4.13%** ($-1.65) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.16 | $10.04 | 📈 +0.43% | 8h 39m |
| `ETH-USD` | 0.004144 | $2412.98 | $2416.74 | $10.02 | 📈 +0.16% | 7h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional se encuentra cerrado, por lo que toda la actividad se concentra exclusivamente en el mercado de criptomonedas (24/7). Las criptomonedas principales como SOL-USD y ETH-USD muestran consolidación tras caídas recientes, con indicadores técnicos en zonas de sobreventa diaria y un impulso de 1 hora estancado pero estable. Mantenemos la disciplina táctica sin realizar cierres prematuros ya que las posiciones no han alcanzado el take-profit óptimo ni han roto el stop-loss."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición acumula una ganancia moderada del +0.43% tras 8 horas de holding. El RSI de 1 hora se mantiene estable en 35.7 y el precio respeta los niveles de soporte, por lo que se mantiene en cartera a la espera de alcanzar el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): La posición presenta un rendimiento positivo del +0.16% tras 7 horas de holding. A pesar de un RSI de 1 hora bajo (24.3), el soporte diario se mantiene intacto y no hay señales de ruptura del stop-loss, por lo que se prioriza dejar correr la ganancia hacia el objetivo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en SOL-USD y ETH-USD vigilando de cerca su evolución en busca del objetivo de take-profit entre +2.0% y +3.5%. El stop-loss estricto permanece en -2.0% para proteger el capital. La liquidez de 18.29 USD se conserva a la espera de un claro rompimiento al alza en el volumen de cripto antes de incrementar la exposición, respetando la reserva mínima."
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
