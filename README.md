# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 14:30:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.37 USD** | **$19.87 USD** | **$38.24 USD** | 🔴 **-4.41%** ($-1.76) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.097172 | $102.91 | $101.95 | $9.91 | 📉 -0.93% | 3h 29m |
| `ETH-USD` | 0.004205 | $2377.97 | $2368.22 | $9.96 | 📉 -0.41% | 2h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se encuentra abierto 24/7 con un sesgo bajista temporal, pero presentando condiciones extremas de sobreventa en gráficos diarios y de 1 hora para activos clave como SOL-USD y ETH-USD (RSI diario debajo de 25 y RSI 1H en zona de compresión). Los mercados tradicionales (Wall Street) permanecen cerrados, por lo que toda la atención táctica se concentra en las criptomonedas para buscar oportunidades de rebote técnico tipo mean reversion."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD se mantiene abierta con una pérdida menor del -0.93%. A pesar de la debilidad reciente, el RSI diario en 15.9 indica una sobreventa extrema que sugiere un potencial rebote técnico inminente. Esperamos confirmación en el momentum de corto plazo.
- **[HOLD] ETH-USD** (Confianza: 75%): La posición en ETH-USD registra una pérdida leve del -0.41%. El RSI diario en 21.7 respalda una fuerte sobreventa y la estructura actual favorece mantener la posición a la espera de un impulso alcista de corto plazo hacia los objetivos de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en SOL-USD y ETH-USD ya que se encuentran en zonas de extrema sobreventa a la espera de un volumen de compra que active el rebote técnico. Monitorear de cerca el RSI de 1 hora: si cruza al alza superando los 40 y el change_1h_pct se torna positivo de manera sostenida, buscaremos la toma de ganancias (take-profit) entre +2.0% y +3.5%. En caso de que se acerquen al stop-loss estricto del -2.0%, ejecutaremos la venta inmediata para proteger el capital."
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
