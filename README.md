# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 22:30:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.08 USD** | **$38.37 USD** | 🔴 **-4.08%** ($-1.63) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.37 | $10.06 | 📈 +0.64% | 7h 29m |
| `ETH-USD` | 0.004144 | $2412.98 | $2417.13 | $10.02 | 📈 +0.17% | 5h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "Los mercados tradicionales (Wall Street) se encuentran cerrados, por lo que toda la actividad se concentra exclusivamente en las criptomonedas (ABIERTO 24/7). Las criptos principales (BTC-USD, ETH-USD, SOL-USD) muestran un comportamiento lateral a bajista con RSI de 1 hora en niveles de compresión o sobreventa leve, sin confirmar todavía el impulso alcista necesario para un rebote fuerte. Nuestras posiciones actuales en SOL-USD y ETH-USD se mantienen estables con ligeras ganancias (+0.64% y +0.17% respectivamente), operando dentro del rango de acumulación sin alcanzar aún nuestra meta de take-profit (+2.0% a +3.5%) ni activar los stop-loss. Mantenemos la cautela y la liquidez en reserva ante la ausencia de una ruptura clara con volumen."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 60%): La posición en SOL-USD lleva poco más de 7 horas abierta con un rendimiento positivo de +0.64%. El RSI de 1 hora se encuentra en 31.8 y el cambio horario es ligeramente positivo (+0.13%). Se mantiene en rango de soporte esperando el impulso necesario para alcanzar la zona de take-profit sin invalidar el stop-loss.
- **[HOLD] ETH-USD** (Confianza: 60%): ETH-USD muestra un rendimiento estable de +0.17% tras casi 6 horas de holding. Aunque el RSI de 1 hora ha bajado a 20.5, el precio se mantiene respetando la zona de compra inicial y el soporte diario. Mantenemos la posición a la espera de un rebote técnico inminente.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en SOL-USD y ETH-USD supervisando de cerca el soporte y esperando a que el RSI de 1 hora rompa claramente al alza con volumen para asegurar ganancias al llegar al objetivo de +2.0% a +3.5%. Conservar el efectivo actual como reserva táctica debido al contexto bajista general de los criptoactivos, evitando sobreexponer el capital hasta que se confirme una señal clara de momentum."
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
