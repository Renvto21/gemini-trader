# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 02:30:53`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.24 USD** | **$38.29 USD** | 🔴 **-4.28%** ($-1.71) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81655.05 | $10.06 | 📈 +0.60% | 7h 30m |
| `SOL-USD` | 0.097418 | $102.65 | $103.46 | $10.08 | 📈 +0.79% | 7h 20m |
| `ETH-USD` | 0.004193 | $2385.05 | $2409.62 | $10.10 | 📈 +1.03% | 7h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se encuentra abierto 24/7 mostrando un rebote moderado desde los niveles de sobreventa previos. Las posiciones actuales en BTC-USD, SOL-USD y ETH-USD registran ganancias moderadas pero estables entre +0.6% y +1.03%, con un tiempo en cartera cercano a las 7.5 horas. El RSI de 1 hora se mantiene neutral-saludable sin alcanzar todavía la zona de take-profit (>70) ni el objetivo de +2.0%. Los mercados tradicionales (Wall Street) permanecen cerrados, por lo que toda la atención táctica se centra en la gestión de estas tres posiciones abiertas."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): La posición mantiene un rendimiento positivo de +0.6% y un RSI de 1H en 60.5. No se han alcanzado los objetivos de take-profit (+2.0%) ni se ha activado el stop-loss, por lo que se mantiene la posición para capturar la continuación del impulso.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra un rendimiento positivo de +0.79% y un comportamiento estable. Se mantiene abierta a la espera de que el precio continúe su recuperación hacia el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 78%): ETH-USD lidera las ganancias actuales con un +1.03%. Se mantiene operando activamente mientras se aproxima de forma gradual a la zona objetivo de take-profit entre +2.0% y +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré las posiciones de BTC-USD, SOL-USD y ETH-USD durante este ciclo ya que se encuentran en terreno positivo y operando dentro de parámetros normales. Vigilaré de cerca el RSI de 1 hora y el porcentaje de beneficio: en cuanto alcancen el rango de +2.0% a +3.5% o crucen la zona de sobrecompra (>70), realizaré la venta total para asegurar ganancias y liberar liquidez. El stop-loss se mantiene estricto en -2.0% para proteger el capital ante cualquier giro repentino del mercado."
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
