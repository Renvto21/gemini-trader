# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 16:40:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.57 USD** | **$30.05 USD** | **$38.61 USD** | 🔴 **-3.47%** ($-1.39) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $720.84 | $10.03 | 📈 +0.27% | 6h 0m |
| `ETH-USD` | 0.004178 | $2393.62 | $2398.40 | $10.02 | 📈 +0.20% | 3h 49m |
| `SOL-USD` | 0.096034 | $104.13 | $104.13 | $10.00 | 📈 +0.00% | 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento mixto con sesgo bajista en el corto plazo, pero con claros indicios de agotamiento vendedor en activos digitales y criptomonedas. SOL-USD presenta una oportunidad excelente de reverso a la media con un RSI diario extremadamente deprimido en 19.7 y un cambio de 1h ya volviéndose positivo (+0.23%). Las posiciones actuales en QQQ y ETH-USD se mantienen estables con ligeras ganancias del +0.27% y +0.20%, por lo que continuaremos esperando a que alcancen nuestra zona objetivo de take-profit entre +2.0% y +3.5%."

**Operaciones del ciclo:**
- **[BUY] SOL-USD** (Confianza: 88%): SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profunda, y su cambio de 1h se ha tornado positivo (+0.23%) con un RSI de 34.9 saliendo de mínimos, lo que activa nuestra estrategia de rebote por mean reversion.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones de QQQ y ETH-USD vigilando el stop-loss en -2.0% y preparándonos para asegurar beneficios si rozan +2.0% de ganancia o sobrecompra en 1h. Hemos desplegado capital fresco en SOL-USD aprovechando su sobreventa extrema diaria. En el siguiente ciclo evaluaremos la rotación de posiciones si el momentum se debilita."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |
| `2026-10-19 01:50` | 🔴 SELL (+0.09$) | `ETH-USD` | $8.09 | $2428.97 | ETH-USD registra una ganancia acumulada y su RSI de 1 hora ha alcanzado 68.3, acercándose ... |
| `2026-10-19 01:00` | 🔴 SELL (-0.00$) | `SOL-USD` | $8.00 | $105.08 | SOL-USD ha entrado en sobrecompra con un RSI de 1 hora en 72.7, cumpliendo estrictamente c... |

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
