# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 19:10:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.00 USD** | **$38.04 USD** | 🔴 **-4.89%** ($-1.96) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81150.01 | $10.00 | 📉 -0.03% | 9m |
| `SOL-USD` | 0.097418 | $102.65 | $102.65 | $10.00 | 📈 +0.00% | 0m |
| `ETH-USD` | 0.004193 | $2385.05 | $2385.05 | $10.00 | 📈 +0.00% | 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado por lo que la liquidez activa se concentra en criptomonedas. BTC-USD mantiene una posición estable con un PnL cercano a 0% tras una breve apertura de 9 minutos. Observamos que SOL-USD y ETH-USD muestran condiciones de sobreventa extrema en el RSI de 1H (31.5 y 29.0 respectivamente) acompañadas de variaciones horarias positivas, lo que activa nuestra estrategia de Mean Reversion y rebotes técnicos."

**Operaciones del ciclo:**
- **[BUY] SOL-USD** (Confianza: 86%): SOL-USD presenta un RSI de 1H en 31.5 saliendo de zona de sobreventa estricta y un cambio positivo de 0.1h en 0.5%, lo que indica un fuerte potencial de rebote táctico a corto plazo dentro de nuestra estrategia cuantitativa agresiva.
- **[BUY] ETH-USD** (Confianza: 85%): ETH-USD muestra un RSI de 1H en 29.0 (sobreventa profunda) combinado con un cambio de 1h positivo de 0.3%, cumpliendo perfectamente con los criterios de mean reversion y momentum de rebote para maximizar el rendimiento del portafolio.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantenemos la posición actual en BTC-USD monitoreando de cerca su evolución hacia el objetivo de take-profit del +2.5% o el stop-loss en -2.0%. Aprovechamos la liquidez disponible para reingresar en SOL-USD y ETH-USD capturando sus rebotes desde niveles de sobreventa extrema en temporalidad de 1H. Mantendremos la reserva mínima de efectivo requerida y seguiremos evaluando la rotación de capital para ciclos futuros."
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
