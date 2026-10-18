# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 21:50:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.15 USD** | **$38.20 USD** | 🔴 **-4.51%** ($-1.80) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81371.61 | $10.02 | 📈 +0.25% | 2h 49m |
| `SOL-USD` | 0.097418 | $102.65 | $103.23 | $10.06 | 📈 +0.57% | 2h 39m |
| `ETH-USD` | 0.004193 | $2385.05 | $2401.39 | $10.07 | 📈 +0.69% | 2h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto muestra un ligero retroceso en la última hora tras el rebote inicial, con los activos (BTC-USD, ETH-USD, SOL-USD) manteniendo ganancias moderadas pero un momentum de corto plazo ligeramente debilitado (RSI 1H oscilando entre 31 y 40). Los mercados tradicionales permanecen cerrados. Nuestra prioridad es mantener las posiciones activas para capturar el take-profit entre +2.0% y +3.5% o salir preventivamente si el momentum se deteriora hacia el stop-loss."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 70%): BTC-USD muestra una ganancia leve de 0.25%. El RSI de 1H está en 40.2 y el precio se mantiene estable tras casi 3 horas de holding. No hay señales para vender ni justificación para rotar todavía.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD durante este ciclo. Vigilar estrictamente que el RSI de 1H no rompa soportes a la baja y activar stop-loss si alguna posición cae al umbral de -2.0%. Mantener la orden de take-profit lista si se alcanza el rango de +2.0% a +3.5% o si el RSI de 1H supera 70."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **67** | 🎯 **38.8%** (26W / 27L / 14BE) | 🔴 **$-1.84 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 19:10` | 🟢 BUY | `ETH-USD` | $10.00 | $2385.05 | ETH-USD muestra un RSI de 1H en 29.0 (sobreventa profunda) combinado con un cambio de 1h p... |
| `2026-10-17 19:10` | 🟢 BUY | `SOL-USD` | $10.00 | $102.65 | SOL-USD presenta un RSI de 1H en 31.5 saliendo de zona de sobreventa estricta y un cambio ... |
| `2026-10-17 19:00` | 🟢 BUY | `BTC-USD` | $10.00 | $81170.65 | BTC-USD muestra un RSI de 1H saliendo de niveles bajos (37.5) con un cambio positivo de 0.... |
| `2026-10-17 18:40` | 🔴 SELL (-0.22$) | `ETH-USD` | $9.78 | $2370.09 | La posición acumula una pérdida de -2.21%, excediendo el umbral de stop-loss del -2.0%. El... |
| `2026-10-17 18:40` | 🔴 SELL (-0.21$) | `SOL-USD` | $9.79 | $101.78 | La posición ha alcanzado una pérdida de -2.08%, rompiendo el límite de stop-loss estricto ... |

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
