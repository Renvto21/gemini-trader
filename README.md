# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 15:20:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.26 USD** | **$34.40 USD** | **$38.67 USD** | 🔴 **-3.33%** ($-1.33) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.10 | $9.88 | 📉 -1.17% | 1d 4h |
| `MSFT` | 0.012146 | $535.17 | $539.23 | $6.55 | 📈 +0.76% | 4h 29m |
| `QQQ` | 0.013791 | $725.09 | $723.79 | $9.98 | 📉 -0.18% | 3h 0m |
| `NVDA` | 0.036812 | $217.32 | $217.05 | $7.99 | 📉 -0.12% | 2h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de acciones se mantiene operando con un sesgo bajista generalizado en el corto plazo, reflejado en caídas semanales de activos clave como QQQ y NVDA, aunque con indicadores de RSI de 1 hora profundamente sobrevendidos que sugieren una alta probabilidad de rebote técnico inminente (Mean Reversion). La liquidez disponible en efectivo es de $4.26 USD y mantenemos cuatro posiciones abiertas (AAPL, MSFT, QQQ, NVDA) con un PnL total acumulado de -3.33%. Monitoreamos de cerca los niveles de soporte y los umbrales de take-profit y stop-loss."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 75%): MSFT muestra una ganancia actual del +0.76% con un RSI de 1h en 31.1 y tendencia alcista diaria. Mantenemos la posición para buscar el objetivo de take-profit entre +2.0% y +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones actuales vigilando de cerca los niveles críticos. Para MSFT, buscar un take-profit si alcanza el rango del +2.0% al +3.5%. Para AAPL, QQQ y NVDA, mantener el stop-loss estricto en -2.0% y evaluar la rotación de capital si el impulso técnico falla en las próximas horas. La liquidez se mantendrá en reserva mínima ($4.26 USD) mientras esperamos la consolidación de los rebotes actuales."
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
