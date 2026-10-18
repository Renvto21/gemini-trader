# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 13:00:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.37 USD** | **$19.90 USD** | **$38.27 USD** | 🔴 **-4.31%** ($-1.73) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.097172 | $102.91 | $102.05 | $9.92 | 📉 -0.84% | 1h 59m |
| `ETH-USD` | 0.004205 | $2377.97 | $2374.83 | $9.99 | 📉 -0.13% | 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional (Wall Street) se encuentra cerrado, por lo que toda la operativa activa se concentra exclusivamente en el mercado de criptomonedas (ABIERTO 24/7). Las criptomonedas principales (SOL-USD, ETH-USD y BTC-USD) muestran un comportamiento lateral a ligeramente bajista en el muy corto plazo, con RSI de 1 hora comprimidos cerca de la zona de sobreventa pero sin romper todavía al alza. El portafolio mantiene dos posiciones abiertas (SOL-USD y ETH-USD) con ligeras pérdidas no realizadas (-0.84% y -0.13% respectivamente), manteniendo un tiempo en cartera prudente y por debajo de las dos horas. Dado que no se ha alcanzado ni el objetivo de take-profit ni el stop-loss estricto del -2.0%, y los indicadores diarios se mantienen en niveles de sobreventa profunda, se decide mantener las posiciones actuales a la espera de un impulso alcista que active el rebote técnico."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición lleva menos de dos horas abierta y presenta una pérdida menor de -0.84%, manteniéndose muy por encima del stop-loss de -2.0%. El RSI diario en 16.0 indica sobreventa extrema, por lo que se espera un rebote técnico próximamente.
- **[HOLD] ETH-USD** (Confianza: 75%): La posición en ETH-USD registra una pérdida insignificante de -0.13% con un tiempo en cartera de apenas 59 minutos. El contexto diario muestra un RSI en 21.9, lo que justifica mantener la posición a la espera del impulso alcista de corto plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas de SOL-USD y ETH-USD debido a que el tiempo en cartera sigue siendo bajo y los fundamentos técnicos de sobreventa diaria extrema siguen intactos. Monitorear de cerca el RSI de 1 hora: si el RSI de 1 hora supera los 55-60 y las posiciones logran una ganancia de +2.0% a +3.5%, ejecutar la toma de beneficios. Mantener estricto el stop-loss en -2.0% para cada posición abierta y proteger el capital ante cualquier extensión bajista inesperada."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **70** | 🎯 **41.4%** (29W / 27L / 14BE) | 🔴 **$-1.49 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 12:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2377.97 | ETH-USD presenta un RSI diario extremadamente bajo en 22.0 y un RSI de 1 hora saliendo de ... |
| `2026-10-18 11:01` | 🟢 BUY | `SOL-USD` | $10.00 | $102.91 | SOL-USD muestra un RSI diario extremadamente bajo (16.4) en zona de sobreventa profunda y ... |
| `2026-10-18 08:00` | 🔴 SELL (+0.13$) | `ETH-USD` | $10.13 | $2415.11 | ETH-USD registra un RSI de 1H en 72.1 (sobrecompra) y una ganancia de +1.26%. Se procede a... |
| `2026-10-18 08:00` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $103.84 | SOL-USD presenta un RSI de 1H en 67.6 acercándose a zona de sobrecompra con una ganancia d... |
| `2026-10-18 08:00` | 🔴 SELL (+0.10$) | `BTC-USD` | $10.08 | $81974.15 | BTC-USD ha alcanzado un RSI de 1H en 78.8 (sobrecompra profunda) tras el rebote esperado, ... |

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
