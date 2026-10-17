# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 22:00:51`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.06 USD** | **$38.35 USD** | 🔴 **-4.12%** ($-1.65) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.17 | $10.04 | 📈 +0.44% | 6h 59m |
| `ETH-USD` | 0.004144 | $2412.98 | $2417.90 | $10.02 | 📈 +0.20% | 5h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accional de EE.UU. se encuentra cerrado con precios congelados. En el mercado cripto, activo 24/7, los precios de SOL-USD y ETH-USD muestran una ligera consolidación bajo presión con RSI de 1 hora deprimidos pero estables tras casi 6-7 horas de tenencia. No se observan todavía los catalizadores de aceleración alcista necesarios para disparar el take-profit, y las posiciones mantienen pérdidas mínimas controladas muy lejos del stop-loss de -2.0%. Se mantiene la prudencia esperando un impulso en los activos digitales."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición en SOL-USD lleva poco más de 6 horas abierta, mostrando un PnL positivo moderado (+0.44%). El RSI de 1 hora se mantiene bajo (29.8) pero el precio se mantiene estable por encima del precio de entrada, por lo que se prefiere mantener y buscar el objetivo de take-profit sin alterar la operativa.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD se mantiene operando con un beneficio marginal del +0.20% tras 5.5 horas. El impulso de rebote técnico aún se está gestando y la posición está dentro de los márgenes normales de riesgo, por lo que se mantiene la exposición actual a la espera de mayor volumen.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en SOL-USD y ETH-USD supervisando la recuperación del RSI de 1 hora por encima de 40 para buscar el objetivo de ganancia de +2.0% a +3.5%. Conservar los 18.29 USD de liquidez para operar en cuanto el mercado cripto rompa a la baja o genere una fuerte vela de impulso alcista. Monitorear de cerca el comportamiento en los siguientes ciclos y estar listos para recortar si el soporte falla."
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
