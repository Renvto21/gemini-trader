# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 10:50:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$9.92 USD** | **$28.62 USD** | **$38.54 USD** | 🔴 **-3.66%** ($-1.46) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.004178 | $2393.62 | $2397.61 | $10.02 | 📈 +0.17% | 21h 59m |
| `SOL-USD` | 0.096034 | $104.13 | $104.50 | $10.04 | 📈 +0.36% | 18h 9m |
| `BTC-USD` | 0.000105 | $81767.70 | $81790.44 | $8.57 | 📈 +0.03% | 17h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo bajista generalizado en renta variable y criptomonedas, con la mayoría de los activos cotizando por debajo de sus medias móviles de 20 días. Sin embargo, las criptomonedas se mantienen abiertas y muestran ligeros intentos de recuperación en el corto plazo (cambio de 1h positivo en BTC, ETH y SOL), mientras que los índices tradicionales como QQQ acumulan más de 24 horas sin el momentum alcista esperado y con tendencia bajista."

**Operaciones del ciclo:**
- **[SELL] QQQ** (Confianza: 85%): QQQ lleva más de 24 horas abierto sin momentum alcista, con un rendimiento de -0.82% y bajo la SMA20. Aplicamos la regla de rotación de capital para evitar posiciones estancadas y proteger el portafolio.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Las posiciones en criptomonedas (ETH-USD, SOL-USD, BTC-USD) muestran estabilidad y ligeros rebotes técnicos, por lo que se mantendrán buscando alcanzar el objetivo de take-profit del +2.0% al +3.5%. Por otro lado, la posición en QQQ lleva 24 horas estancada con tendencia bajista bajo la SMA20 y sin el rebote esperado; procederemos a liquidarla para cortar pérdidas mínimas y liberar capital hacia alternativas de mayor dinamismo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **78** | 🎯 **42.3%** (33W / 30L / 15BE) | 🔴 **$-1.37 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-20 10:50` | 🔴 SELL (-0.08$) | `QQQ` | $9.92 | $713.02 | QQQ lleva más de 24 horas abierto sin momentum alcista, con un rendimiento de -0.82% y baj... |
| `2026-10-19 23:00` | 🟢 BUY | `BTC-USD` | $4.00 | $81646.39 | BTC-USD presenta un RSI de 1 hora en 27.7, nivel de sobreventa profunda ideal para un rebo... |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |

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
