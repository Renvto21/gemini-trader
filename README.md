# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 21:10:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.10 USD** | **$38.15 USD** | 🔴 **-4.62%** ($-1.85) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81291.58 | $10.01 | 📈 +0.15% | 2h 9m |
| `SOL-USD` | 0.097418 | $102.65 | $103.12 | $10.05 | 📈 +0.46% | 1h 59m |
| `ETH-USD` | 0.004193 | $2385.05 | $2395.54 | $10.04 | 📈 +0.44% | 1h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "Los mercados bursátiles tradicionales se encuentran cerrados, por lo que toda la actividad se centra en el mercado cripto 24/7. Las principales criptomonedas (BTC, ETH, SOL) muestran un ligero retroceso en la última hora con caídas cercanas al -0.89% y RSI de 1H rondando zonas de sobreventa o cerca de soportes. Nuestras posiciones actuales muestran ganancias muy ligeras (entre +0.15% y +0.46%), manteniéndose seguras lejos del stop-loss, pero aún sin alcanzar la meta de take-profit del +2.0%."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD se mantiene estable con un PnL positivo de +0.15% tras dos horas de retención. Aunque el cambio de 1h es ligeramente negativo (-0.29%), el precio respeta los rangos de entrada y no ha activado ninguna señal de salida ni de take-profit.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD registra un PnL de +0.46%. A pesar de un retroceso menor en la última hora, el activo se mantiene en zona operativa saludable, por lo que se mantiene la posición buscando el objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD durante este ciclo mientras se encuentran estables. Establecer objetivos estrictos de take-profit en +2.0% de PnL o si el RSI de 1H supera los 65-70 puntos para asegurar capital. Mantener la vigilancia sobre los niveles de soporte actuales; si el momentum se deteriora y rompen a la baja, se procederá a recortar pérdidas para proteger el efectivo."
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
