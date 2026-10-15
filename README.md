# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 14:10:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.26 USD** | **$34.50 USD** | **$38.76 USD** | 🔴 **-3.10%** ($-1.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $344.49 | $9.95 | 📉 -0.48% | 1d 3h |
| `MSFT` | 0.012146 | $535.17 | $539.29 | $6.55 | 📈 +0.77% | 3h 19m |
| `QQQ` | 0.013791 | $725.09 | $724.51 | $9.99 | 📉 -0.08% | 1h 50m |
| `NVDA` | 0.036812 | $217.32 | $217.38 | $8.00 | 📈 +0.03% | 1h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El portafolio se encuentra con una ligera pérdida global del -3.1%, mientras los mercados principales muestran señales mixtas con sesgo técnico bajista en marcos diarios pero con intentos de rebote en marcos de 1 hora. Las posiciones actuales (AAPL, MSFT, QQQ, NVDA) operan con fluctuaciones reducidas sin alcanzar aún los objetivos ambiciosos de take-profit (+2.0% a +3.5%) ni activar los stop-loss restrictivos. El efectivo disponible se mantiene en un nivel bajo ($4.26 USD), cumpliendo con la regla de máxima exposición y rotación activa."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 70%): MSFT muestra una ganancia leve del +0.77% y se mantiene con tendencia alcista sobre la SMA20. Se mantiene la posición a la espera de alcanzar el objetivo de take-profit entre +2.0% y +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas actuales (AAPL, MSFT, QQQ, NVDA) evaluando su evolución en busca del take-profit entre +2.0% y +3.5% o protegiendo con el stop-loss en -2.0% si el impulso se deteriora. Monitorear de cerca los mercados cripto y tecnológicos para futuras rotaciones de capital en cuanto alguna posición lateralice o alcance su objetivo de salida."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **57** | 🎯 **42.1%** (24W / 19L / 14BE) | 🔴 **$-1.12 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |
| `2026-10-15 12:10` | 🔴 SELL (+0.14$) | `ETH-USD` | $6.14 | $2417.73 | ETH-USD ha alcanzado un rendimiento del +2.33%, cumpliendo con el rango establecido para l... |
| `2026-10-15 11:50` | 🔴 SELL (+0.13$) | `SOL-USD` | $6.13 | $104.21 | SOL-USD ha alcanzado un rendimiento de +2.11%, cumpliendo con la regla de toma rápida de g... |
| `2026-10-15 10:50` | 🟢 BUY | `MSFT` | $6.50 | $535.17 | MSFT presenta un RSI de 1h ultra comprimido en sobreventa extrema (14.7) con un cambio pos... |

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
