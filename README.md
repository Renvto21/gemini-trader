# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 17:40:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.00 USD** | **$38.29 USD** | 🔴 **-4.29%** ($-1.71) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $103.73 | $10.00 | 📈 +0.02% | 2h 39m |
| `ETH-USD` | 0.004144 | $2412.98 | $2411.88 | $10.00 | 📉 -0.05% | 1h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario tradicional (Wall Street) se encuentra CERRADO, por lo que toda la actividad se concentra en el mercado de criptomonedas (ABIERTO 24/7). Las criptomonedas principales (SOL-USD y ETH-USD) se mantienen estables con ligeros cambios positivos en la última hora, manteniendo nuestros niveles de entrada bajo supervisión cercana sin alcanzar todavía el objetivo de take-profit (+2.0% a +3.5%) ni activar los stop-loss (-2.0%)."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición se mantiene estable con una pequeña ganancia del 0.02% tras 2 horas y 39 minutos. Mantiene un RSI de 1 hora en 31.3 buscando consolidar el rebote. Esperaremos a alcanzar el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 70%): La posición muestra un rendimiento neutral (-0.05%) tras 1 hora y 9 minutos de haber sido abierta. El RSI diario se encuentra en niveles de sobreventa extrema (30.2), por lo que mantenemos la posición esperando el impulso alcista.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en SOL-USD y ETH-USD. Monitorear de cerca el RSI de 1 hora y el cambio porcentual para asegurar ganancias si se alcanza el rango de +2.0% a +3.5%, o recortar si el precio rompe el soporte del stop-loss en -2.0%. Mantener la reserva de efectivo mínima de $4.00 y evaluar nuevas entradas solo si se presenta una oportunidad de alta convicción en cripto."
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
