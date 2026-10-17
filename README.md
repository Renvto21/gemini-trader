# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 20:50:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.10 USD** | **$38.14 USD** | 🔴 **-4.64%** ($-1.86) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81279.36 | $10.01 | 📈 +0.13% | 1h 49m |
| `SOL-USD` | 0.097418 | $102.65 | $103.09 | $10.04 | 📈 +0.43% | 1h 39m |
| `ETH-USD` | 0.004193 | $2385.05 | $2394.71 | $10.04 | 📈 +0.41% | 1h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se encuentra operando en fin de semana con un sesgo lateral a bajista, manteniendo una tendencia general por debajo de la SMA20. Los activos en cartera (BTC-USD, SOL-USD y ETH-USD) muestran ligeras ganancias positivas pero aún no alcanzan el objetivo óptimo de take-profit entre +2.0% y +3.5%, ni sus indicadores RSI de 1H han superado la zona de sobrecompra (>70). El mercado tradicional permanece cerrado, por lo que toda la atención se concentra en gestionar las posiciones abiertas actuales."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD se mantiene estable con un PnL positivo del 0.13% y un RSI de 1H en 44.0. No ha alcanzado el objetivo de take-profit (+2.0%) ni ha roto el stop-loss, por lo que se mantiene la posición para capturar una mayor expansión del rebote técnico.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra un PnL positivo de 0.43% y un RSI de 1H en 37.3. Se mantiene la posición a la espera de que el impulso alcista de corto plazo acerque el precio al objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD registra un PnL positivo de 0.41% con un RSI de 1H recuperándose a 34.2. Se conserva la posición esperando una aceleración del rebote hacia la zona de objetivos.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (BTC-USD, SOL-USD, ETH-USD) ya que se encuentran en terreno positivo y sin tocar el stop-loss estricto (-2.0%). Esperar a que el RSI de 1H de alguno de los activos alcance niveles superiores a 60-70 o que el PnL se aproxime al objetivo de +2.0% para realizar tomas de beneficio y asegurar liquidez en efectivo. En el siguiente ciclo, si el momentum se debilita sin alcanzar el objetivo, evaluar la rotación parcial del capital."
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
