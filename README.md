# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 15:01:05`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$21.90 USD** | **$16.40 USD** | **$38.30 USD** | 🔴 **-4.26%** ($-1.70) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $526.88 | $6.40 | 📉 -1.55% | 1d 4h |
| `SOL-USD` | 0.096423 | $103.71 | $103.71 | $10.00 | 📈 +0.00% | 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se encuentra bajo presión con la mayoría de los activos cotizando en tendencia bajista bajo la SMA20. Sin embargo, observamos condiciones interesantes de sobreventa en el corto plazo (RSI de 1 hora bajo 35) que sugieren oportunidades potenciales de rebote técnico. MSFT se mantiene en cartera con una pérdida menor de -1.55% y un holding time superior a 1 día; dado que su RSI de 1 hora está cruzando al alza hacia 35 y muestra un cambio positivo de 0.21%, mantenemos la posición esperando la extensión hacia la zona de take-profit. En cuanto a la liquidez disponible, activos como SOL-USD muestran un RSI de 1 hora en 34.3 saliendo de sobreventa con un cambio positivo de 0.14%, lo que activa nuestra estrategia agresiva de mean reversion."

**Operaciones del ciclo:**
- **[BUY] SOL-USD** (Confianza: 85%): SOL-USD presenta un RSI de 1 hora en 34.3 saliendo de la zona de sobreventa extrema, acompañado de un cambio positivo de 0.14% en la última hora. Aprovechamos la oportunidad de alta convicción para cazar un rebote técnico rápido (mean reversion) asignando $10.0 USD de la liquidez disponible.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantengo MSFT vigilando el soporte y esperando el objetivo de take-profit (+2.0%). Si rompe el stop-loss estricto de -2%, venderé inmediatamente. Con el efectivo restante, he abierto una posición en SOL-USD aprovechando el rebote técnico desde la sobreventa; estableceré un stop-loss estricto de -2.0% y buscaré un take-profit rápido del +2.5%."
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
