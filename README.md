# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 01:50:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.31 USD** | **$38.35 USD** | 🔴 **-4.12%** ($-1.65) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81688.15 | $10.06 | 📈 +0.64% | 6h 49m |
| `SOL-USD` | 0.097418 | $102.65 | $103.84 | $10.12 | 📈 +1.16% | 6h 39m |
| `ETH-USD` | 0.004193 | $2385.05 | $2414.98 | $10.13 | 📈 +1.25% | 6h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se encuentra abierto con un sesgo lateral a ligeramente bajista en la última hora, aunque nuestras posiciones abiertas mantienen ganancias moderadas pero por debajo del objetivo de take-profit del 2.0%. Los mercados tradicionales permanecen cerrados. El foco se mantiene en la gestión táctica de las criptomonedas para buscar la toma de beneficios o proteger el capital ante cualquier giro imprevisto."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): La posición muestra una ganancia actual de +0.64% con un holding time de casi 7 horas. El RSI 1H está en 54.8, por lo que se mantiene en cartera a la espera de alcanzar el objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD registra una ganancia de +1.16% y un RSI 1H de 47.4. Mantenemos la posición abierta para permitir que el rebote continúe hacia la zona de take-profit establecida.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD cuenta con un beneficio de +1.25% y un RSI 1H en 46.5. Continuamos operando la posición sin sobrepasar el stop-loss y esperando el objetivo de ganancia rápida.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (BTC-USD, SOL-USD, ETH-USD) vigilando de cerca que alcancen la zona objetivo de take-profit entre +2.0% y +3.5% o que el RSI 1H muestre signos de sobrecompra (>70). Los stop-loss se mantienen estrictos por debajo de -2.0%. Si el momentum decae y el tiempo de tenencia se prolonga sin avance, procederemos a rotar el capital hacia liquidez o nuevas oportunidades de rebote."
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
