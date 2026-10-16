# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 16:30:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$19.97 USD** | **$38.25 USD** | 🔴 **-4.37%** ($-1.75) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $103.35 | $9.97 | 📉 -0.35% | 1h 29m |
| `ETH-USD` | 0.004144 | $2412.98 | $2412.98 | $10.00 | 📈 +0.00% | 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general muestra una tendencia bajista de corto plazo con la mayoría de los activos tecnológicos y criptomonedas operando por debajo de sus medias móviles de 20 días. Sin embargo, se observan señales incipientes de recuperación y rebote por sobreventa en algunos activos cripto (como BTC-USD y SOL-USD) y estabilidad en valores de renta variable seleccionados."

**Operaciones del ciclo:**
- **[SELL] MSFT** (Confianza: 85%): MSFT lleva más de 1 día y 5 horas abierto mostrando debilidad persistente y un rendimiento estancado sin lograr romper al alza. Vendo la posición para cortar la pérdida menor (-1.68%) y liberar capital para rotarlo hacia oportunidades con mayor impulso en cripto.
- **[BUY] ETH-USD** (Confianza: 82%): ETH-USD muestra un RSI diario en niveles de sobreventa extrema (30.3) y un cambio positivo en la última hora (0.4%), lo que indica una sólida oportunidad táctica de rebote por mean reversion (reversión a la media) aprovechando la liquidez liberada.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré la posición en SOL-USD ya que continúa consolidando su base tras salir de sobreventa, monitoreando de cerca su evolución y aplicando un stop-loss estricto si pierde el soporte de 101 USD o buscando take-profit cerca del +2.5%. Respecto a MSFT, al llevar más de un día sin momentum alcista claro y acercarse al límite de tolerancia de pérdida (-1.68%), he decidido liquidarla para liberar efectivo y capturar oportunidades de mayor dinamismo en criptoactivos como ETH-USD."
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
