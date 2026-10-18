# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 02:10:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.27 USD** | **$38.31 USD** | 🔴 **-4.22%** ($-1.69) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81669.83 | $10.06 | 📈 +0.61% | 7h 9m |
| `SOL-USD` | 0.097418 | $102.65 | $103.60 | $10.09 | 📈 +0.93% | 6h 59m |
| `ETH-USD` | 0.004193 | $2385.05 | $2411.55 | $10.11 | 📈 +1.11% | 6h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas continúa operando en fin de semana con un comportamiento lateral a ligeramente correctivo en el corto plazo (cambios de 1h cercanos a 0), mientras que los mercados tradicionales permanecen cerrados. Nuestras posiciones en cripto (BTC-USD, SOL-USD y ETH-USD) se mantienen estables con pequeñas ganancias acumuladas entre +0.61% y +1.11%, acercándose progresivamente a nuestra zona objetivo de take-profit sin alcanzar todavía el umbral óptimo del +2.0%. Mantendremos la disciplina y el monitoreo continuo del RSI de 1 hora."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición muestra un rendimiento positivo del 0.61% tras 7 horas abierta. El RSI de 1H se sitúa en 61.0, aproximándose a zonas de sobrecompra pero sin alcanzar el objetivo de take-profit. Mantenemos la posición esperando el impulso final.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (BTC-USD, SOL-USD, ETH-USD) a la espera de que el RSI de 1 hora supere la zona de 70 o que las ganancias alcancen el rango objetivo de +2.0% a +3.5% para proceder a la toma de beneficios y liberar liquidez. Los stop-loss se mantienen estrictos por debajo de -2.0% para proteger el portafolio ante cualquier volatilidad imprevista."
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
