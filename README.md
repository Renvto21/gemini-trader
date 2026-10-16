# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 19:50:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.09 USD** | **$38.38 USD** | 🔴 **-4.05%** ($-1.62) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.30 | $10.06 | 📈 +0.57% | 4h 49m |
| `ETH-USD` | 0.004144 | $2412.98 | $2421.31 | $10.03 | 📈 +0.35% | 3h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con un sesgo bajista generalizado en temporalidades diarias, aunque presenta ligeros rebotes de corto plazo en el marco de 1 horas. Los activos tradicionales como acciones y ETFs se encuentran cerrados. Nuestras posiciones actuales en SOL-USD y ETH-USD muestran ganancias moderadas (+0.57% y +0.35% respectivamente), manteniendo un comportamiento técnico estable pero sin alcanzar aún la meta de take-profit entre +2.0% y +3.5%."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD mantiene un rendimiento positivo de +0.57% tras casi 5 horas de tenencia. Su RSI de 1 hora se sitúa en 32.1 y muestra un cambio positivo reciente, por lo que se mantiene dentro de la tesis de rebote técnico esperando alcanzar la meta de take-profit.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD registra una ganancia del +0.35% con un RSI diario en niveles de sobreventa extrema y un RSI de 1 hora en 36.9 que apoya la continuidad del rebote técnico hacia la zona de take-profit establecida.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en SOL-USD y ETH-USD para permitir que alcancen la zona objetivo de take-profit entre +2.0% y +3.5%. Vigilar estrechamente el RSI de 1 hora y el rendimiento porcentual para asegurar ganancias o ejecutar stop-loss estricto si el rendimiento cae por debajo de -2.0%. Mantener la liquidez remanente intacta hasta que surja una nueva señal clara de alta convicción."
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
