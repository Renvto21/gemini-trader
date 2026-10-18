# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 03:00:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.23 USD** | **$38.27 USD** | 🔴 **-4.32%** ($-1.73) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81625.22 | $10.06 | 📈 +0.56% | 8h 0m |
| `SOL-USD` | 0.097418 | $102.65 | $103.40 | $10.07 | 📈 +0.73% | 7h 50m |
| `ETH-USD` | 0.004193 | $2385.05 | $2408.42 | $10.10 | 📈 +0.98% | 7h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas continúa abierto 24/7, mientras que los activos tradicionales están cerrados. Las posiciones actuales en BTC-USD, SOL-USD y ETH-USD se encuentran estables con ganancias moderadas entre 0.56% y 0.98%, mostrando signos positivos de recuperación tras el rebote técnico pero sin alcanzar todavía la zona objetivo de take-profit de +2.0% a +3.5%. El RSI de 1 hora se mantiene en niveles neutrales saludables y el capital se encuentra debidamente posicionado."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición en BTC-USD muestra una ganancia de 0.56% con un RSI de 1h en 62.5. Aunque hay progreso, aún no alcanza el objetivo de take-profit de +2.0% a +3.5%, por lo que es óptimo mantener y dejar correr las ganancias.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD registra un rendimiento positivo de 0.98% con un RSI de 1h en 53.3. Mantendremos la posición abierta para buscar la zona de take-profit establecida.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD mantiene una ganancia de 0.73% con un RSI de 1h en 52.7. La tendencia de corto plazo es estable y no hay motivos para cerrar anticipadamente la posición.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré las posiciones abiertas en BTC-USD, ETH-USD y SOL-USD ya que muestran un comportamiento técnico favorable aunque moderado. Esperaré al siguiente ciclo para evaluar si alcanzan el objetivo de take-profit (+2.0% a +3.5%) o si el RSI de 1 hora se aproxima a la zona de sobrecompra (>70) para realizar ventas parciales o totales. Conservaré la liquidez actual y vigilaré de cerca cualquier cambio de momentum."
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
