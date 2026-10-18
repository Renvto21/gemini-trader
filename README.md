# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 17:40:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$29.98 USD** | **$8.00 USD** | **$37.99 USD** | 🔴 **-5.03%** ($-2.01) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.079341 | $100.83 | $100.88 | $8.00 | 📈 +0.05% | 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra completamente cerrado durante el fin de semana, por lo que toda la acción y liquidez activa se concentra en el mercado de criptomonedas (abierto 24/7). Las criptomonedas principales (BTC-USD, ETH-USD, SOL-USD) muestran condiciones de sobreventa extrema en sus gráficos diarios, aunque persisten tendencias bajistas de corto plazo bajo la SMA20. Nuestra única posición activa en SOL-USD muestra estabilidad con un beneficio marginal del +0.05% tras 39 minutos de holding, manteniendo el pulso a la espera de un rebote técnico firme impulsado por su RSI diario extremadamente deprimido."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD lleva poco tiempo abierta (39 minutos) con un rendimiento plano (+0.05%). Mantiene un RSI diario extremadamente bajo (15.3), lo que justifica conservar la posición a la espera del rebote técnico esperado hacia el objetivo de take-profit de +2.0% a +3.5%, manteniendo activo el stop-loss a -2.0%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos la posición actual en SOL-USD monitoreando de cerca su evolución. Establecemos un objetivo de take-profit entre +2.0% y +3.5% (aproximadamente $103.00) y un stop-loss estricto a -2.0% ($98.86) para proteger el capital. Evaluaremos una entrada adicional en ETH-USD si su RSI de 1 hora rompe al alza con un cambio positivo confirmado. El efectivo disponible se mantendrá a la espera de confirmación de momentum."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **72** | 🎯 **40.3%** (29W / 29L / 14BE) | 🔴 **$-1.88 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 17:00` | 🟢 BUY | `SOL-USD` | $8.00 | $100.83 | SOL-USD muestra un RSI diario extremadamente deprimido en 15.3 y un RSI de 1 hora en 23.4 ... |
| `2026-10-18 16:40` | 🔴 SELL (-0.19$) | `ETH-USD` | $9.81 | $2332.39 | ETH-USD registra una pérdida del -1.92% con un RSI de 1 hora en 18.5 que refleja debilidad... |
| `2026-10-18 16:40` | 🔴 SELL (-0.20$) | `SOL-USD` | $9.80 | $100.90 | La posición en SOL-USD lleva casi 6 horas abierta con una pérdida del -1.95% y un RSI de 1... |
| `2026-10-18 12:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2377.97 | ETH-USD presenta un RSI diario extremadamente bajo en 22.0 y un RSI de 1 hora saliendo de ... |
| `2026-10-18 11:01` | 🟢 BUY | `SOL-USD` | $10.00 | $102.91 | SOL-USD muestra un RSI diario extremadamente bajo (16.4) en zona de sobreventa profunda y ... |

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
