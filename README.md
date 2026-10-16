# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 18:20:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.05 USD** | **$38.34 USD** | 🔴 **-4.14%** ($-1.66) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.22 | $10.05 | 📈 +0.49% | 3h 19m |
| `ETH-USD` | 0.004144 | $2412.98 | $2414.22 | $10.01 | 📈 +0.05% | 1h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto 24/7 con un tono lateral a ligeramente bajista, mientras que los mercados bursátiles tradicionales permanecen cerrados. SOL-USD y ETH-USD muestran signos tempranos de estabilización tras caídas recientes, con RSI de 1 hora recuperándose lentamente de zonas de sobreventa, aunque aún operan bajo sus medias móviles de 20 períodos."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD mantiene una ganancia moderada de +0.49% con un holding time de poco más de 3 horas. El RSI de 1 hora sube a 35.8 y el cambio de la última hora es positivo, por lo que se mantiene en cartera a la espera de un mayor impulso hacia el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD se encuentra estable con una ligera ganancia de +0.05% y un RSI diario en niveles de sobreventa extrema de 30.3. Continuamos con la posición abierta para capturar el rebote técnico anticipado en el corto plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en SOL-USD y ETH-USD mientras continúan consolidando tras sus rebotes desde la sobreventa. Monitorear de cerca los objetivos de take-profit cercanos al +2.5% o si el RSI de 1 hora supera los 70 puntos. Mantener un stop-loss estricto a -2.0%. La liquidez en efectivo disponible de $18.29 USD se mantendrá temporalmente a la espera de una ruptura alcista más clara o una confirmación de momentum en BTC-USD."
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
