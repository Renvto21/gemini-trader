# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 19:30:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.10 USD** | **$38.38 USD** | 🔴 **-4.04%** ($-1.62) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.36 | $10.06 | 📈 +0.63% | 4h 29m |
| `ETH-USD` | 0.004144 | $2412.98 | $2420.89 | $10.03 | 📈 +0.33% | 2h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "Los mercados tradicionales (Wall Street) se encuentran cerrados, por lo que la liquidez activa se concentra en el mercado de criptomonedas, que opera 24/7. Tanto SOL-USD como ETH-USD muestran ligeras ganancias pero se mantienen en rangos estables sin alcanzar aún el objetivo de take-profit entre +2.0% y +3.5%, y sin activar ningún stop-loss. El sentimiento general sigue siendo defensivo en cripto con tendencias por debajo de la SMA20, pero manteniendo los rebotes técnicos esperados."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición en SOL-USD se mantiene en terreno positivo (+0.63%) tras pocas horas abierta. No ha alcanzado el objetivo de take-profit (+2.0% a +3.5%) ni ha roto niveles de stop-loss, por lo que se mantiene para permitir que el rebote madure.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un rendimiento positivo constante (+0.33%) desde su apertura. Se mantiene la posición activa buscando alcanzar el objetivo de take-profit en el corto plazo sin señales de fallo en el momentum.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en SOL-USD y ETH-USD durante este ciclo mientras continúan su evolución hacia el objetivo de take-profit (+2.0% a +3.5%). Monitorear de cerca el RSI de 1 hora y el comportamiento del precio para asegurar beneficios de forma temprana si se alcanza la meta o cortar pérdidas si el precio cae por debajo del stop-loss de -2.0%. Mantener la liquidez en reserva según las reglas operativas."
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
