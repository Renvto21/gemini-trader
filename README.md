# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 07:50:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.35 USD** | **$38.40 USD** | 🔴 **-4.00%** ($-1.60) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $82013.77 | $10.10 | 📈 +1.04% | 12h 49m |
| `SOL-USD` | 0.097418 | $102.65 | $103.89 | $10.12 | 📈 +1.21% | 12h 39m |
| `ETH-USD` | 0.004193 | $2385.05 | $2415.70 | $10.13 | 📈 +1.29% | 12h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene abierto y operando con estabilidad moderada, con nuestras posiciones actuales en BTC-USD, SOL-USD y ETH-USD registrando ganancias ligeras entre +1.0% y +1.3%. Aunque las ganancias aún no alcanzan el objetivo de take-profit óptimo (+2.0% a +3.5%), el momentum se mantiene contenido pero estable. Los mercados tradicionales continúan cerrados, por lo que toda la actividad se concentra en mantener y proteger las posiciones actuales en criptomonedas."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD muestra una ganancia actual de +1.04% con un RSI de 1H en 61.5. Mantiene estabilidad y el impulso sigue vivo, por lo que se mantiene en cartera a la espera de la zona de take-profit.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD presenta un beneficio de +1.21% y un RSI de 1H en 48.8. Sin señales de salida o debilidad, se conserva operativamente.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD registra una ganancia del +1.29% con RSI de 1H en 48.8. La posición está evolucionando favorablemente dentro del canal esperado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré las posiciones abiertas de BTC-USD, SOL-USD y ETH-USD ya que se encuentran en terreno positivo. Monitorearé el RSI de 1H en busca de acercamientos a sobrecompra (>70) para ejecutar tomas de beneficio y asegurar liquidez. Mantendré el stop-loss estricto en -2.0% para proteger el capital ante cualquier giro repentino."
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
