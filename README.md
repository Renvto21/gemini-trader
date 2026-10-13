# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 20:40:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$34.54 USD** | **$4.98 USD** | **$39.52 USD** | 🔴 **-1.19%** ($-0.48) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2499.59 | $4.98 | 📉 -0.35% | 3h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que la liquidez y la actividad operativa se concentran exclusivamente en el mercado de criptomonedas (24/7). Los principales activos cripto (ETH, SOL, BTC) muestran un sesgo bajista a corto plazo bajo la SMA20, con un momentum neutral a ligeramente débil en la última hora. Nuestra posición actual en ETH-USD registra una leve pérdida (-0.35%) tras más de tres horas de holding, manteniéndose muy por encima de nuestro stop-loss estricto (-2.0%)."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): La posición en ETH-USD se mantiene estable con una pérdida marginal del -0.35%, muy lejos de nuestro límite de stop-loss (-2.0%). El holding time es de aproximadamente 3 horas y medio, por lo que aún cuenta con margen para desarrollar el rebote técnico esperado sin necesidad de forzar una venta prematura.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos la posición en ETH-USD mientras respete el soporte actual y no alcance el stop-loss del -2.0%. Buscaremos la toma de beneficios si el precio rebota hacia el rango de +2.0% a +3.5% o si el RSI de 1H supera los 70 puntos. Si la posición permanece estancada sin volumen de compra en las próximas horas, rotaremos el capital hacia liquidez o hacia otra oportunidad en activos abiertos."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **48** | 🎯 **45.8%** (22W / 12L / 14BE) | 🔴 **$-0.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |
| `2026-10-13 16:30` | 🟢 BUY | `ETH-USD` | $9.68 | $2507.92 | ETH-USD muestra un RSI de 35.8 en zona de fuerte sobreventa y un impulso alcista diario de... |
| `2026-10-13 16:30` | 🔴 SELL | `SOL-USD` | $9.69 | $107.65 | Realizamos una toma parcial de beneficios y rotación de capital liberando aproximadamente ... |

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
