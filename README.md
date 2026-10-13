# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 19:20:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.68 USD** | **$34.84 USD** | **$39.52 USD** | 🔴 **-1.20%** ($-0.48) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.279466 | $107.20 | $106.78 | $29.84 | 📉 -0.39% | 5h 19m |
| `ETH-USD` | 0.001993 | $2508.37 | $2506.14 | $5.00 | 📉 -0.09% | 2h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando en régimen 24/7 con un tono lateral a bajista en el corto plazo (tendencias bajo la SMA20). Los activos tradicionales (SPY, QQQ, AAPL, MSFT, NVDA, GLD) se encuentran cerrados, por lo que la liquidez activa debe centrarse exclusivamente en las posiciones abiertas en criptomonedas (SOL-USD y ETH-USD). Ambas posiciones se encuentran con variaciones moderadas cercanas al 0% de PnL tras varias horas de tenencia, sin mostrar el impulso alcista necesario para alcanzar el take-profit. Se mantendrán temporalmente en espera de un catalizador o incremento en el volumen."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 60%): La posición en SOL-USD lleva más de 5 horas abierta con una pérdida marginal de -0.39%. Aunque el momentum es débil, el RSI diario está profundamente en sobreventa (26.4), por lo que se mantiene a la espera de un rebote técnico inminente respetando el límite estricto de stop-loss.
- **[HOLD] ETH-USD** (Confianza: 60%): ETH-USD registra un PnL casi plano (-0.09%) con un RSI de 1 hora en 44.0. Se mantiene activa para capturar el rebote alcista diario una vez que el mercado rompa el rango lateral actual.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener SOL-USD y ETH-USD vigiladas estrechamente. El tiempo de tenencia de SOL-USD supera las 5 horas sin el rebote esperado; si el RSI de 1 hora perfora soportes o las pérdidas se acercan al -2.0%, se procederá a vender para liberar liquidez. Si surge un repunte en el RSI por encima de 60-70, se buscará la toma de beneficios."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **47** | 🎯 **46.8%** (22W / 11L / 14BE) | 🔴 **$-0.28 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |
| `2026-10-13 16:30` | 🟢 BUY | `ETH-USD` | $9.68 | $2507.92 | ETH-USD muestra un RSI de 35.8 en zona de fuerte sobreventa y un impulso alcista diario de... |
| `2026-10-13 16:30` | 🔴 SELL | `SOL-USD` | $9.69 | $107.65 | Realizamos una toma parcial de beneficios y rotación de capital liberando aproximadamente ... |
| `2026-10-13 14:01` | 🟢 BUY | `SOL-USD` | $7.97 | $107.29 | SOL-USD presenta una condición de sobreventa extrema con un RSI de 27.9 y un desplome sema... |

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
