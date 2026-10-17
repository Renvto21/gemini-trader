# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 01:10:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.13 USD** | **$38.42 USD** | 🔴 **-3.95%** ($-1.58) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.65 | $10.09 | 📈 +0.91% | 10h 9m |
| `ETH-USD` | 0.004144 | $2412.98 | $2423.06 | $10.04 | 📈 +0.42% | 8h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional (Wall Street) se encuentra cerrado, por lo que toda la actividad se concentra exclusivamente en el mercado de criptomonedas, que opera 24/7. Las posiciones actuales en SOL-USD y ETH-USD muestran ligeras ganancias positivas (+0.91% y +0.42% respectivamente) tras más de 8-10 horas de holding, pero el momentum de corto plazo se ha enfriado ligeramente (RSI de 1 hora moderado y cambios de 1 hora negativos pequeños). Mantendremos las posiciones actuales ya que no han alcanzado el objetivo de take-profit (+2.0% a +3.5%) ni han violado el stop-loss, y el efectivo actual se preservará a la espera de una fuerte señal de volumen o sobreventa extrema en cripto para rotar o ampliar exposición."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición mantiene una ganancia moderada de +0.91% tras 10 horas abierta. Aunque el RSI de 1 hora se ha enfriado a 41.9, el precio se mantiene estable y no ha tocado niveles de stop-loss ni ha alcanzado el objetivo de take-profit (+2.0% a +3.5%). Se mantiene para dejar correr el potencial rebote técnico.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD registra una ganancia del +0.42% con un RSI diario fuertemente deprimido en 30.7. Mantenemos la posición abierta para permitir que se desarrolle el rebote de mean reversion hacia los objetivos de take-profit establecidos, vigilando estrictamente el stop-loss.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca SOL-USD y ETH-USD en busca de una aceleración del RSI de 1 hora hacia la zona de sobrecompra (>70) para ejecutar tomas de ganancias parciales o totales entre el +2.0% y +3.5%. Vigilar el soporte para evitar activar el stop-loss estricto en -2.0%. Mantener la liquidez disponible para futuras oportunidades de alta convicción en cripto mientras los activos tradicionales permanezcan cerrados."
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
