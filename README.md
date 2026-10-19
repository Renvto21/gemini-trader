# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 18:30:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$34.66 USD** | **$38.65 USD** | 🔴 **-3.36%** ($-1.35) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 7h 50m |
| `ETH-USD` | 0.004178 | $2393.62 | $2402.74 | $10.04 | 📈 +0.38% | 5h 39m |
| `SOL-USD` | 0.096034 | $104.13 | $104.68 | $10.05 | 📈 +0.53% | 1h 50m |
| `BTC-USD` | 0.000056 | $81874.05 | $81974.46 | $4.58 | 📈 +0.12% | 1h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con un sesgo de consolidación lateral alcista tras las recientes condiciones de sobreventa profunda en los marcos diarios. Los activos tradicionales como QQQ se encuentran cerrados. Las posiciones en ETH-USD, SOL-USD y BTC-USD muestran ligeras ganancias positivas pero aún no alcanzan el objetivo de take-profit del 2.0% al 3.5%. El momentum de corto plazo muestra estabilidad en el RSI de 1 hora, por lo que se decide mantener las posiciones actuales y conservar liquidez para futuros impulsos."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): La posición se mantiene en terreno positivo (+0.38%) y el RSI de 1 hora se recupera gradualmente (38.7). Mantenemos para buscar el objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD muestra la mayor fuerza relativa del portafolio con un rendimiento actual de +0.53% y un RSI diario profundamente sobrevendido (21.2) que respalda el rebote técnico a mediano plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones activas en ETH-USD, SOL-USD y BTC-USD vigilando de cerca la evolución del RSI de 1 hora hacia la zona de sobrecompra (>70) para ejecutar tomas de ganancias progresivas (Take-Profit). QQQ permanece cerrado y sin cambios. El stop-loss se mantiene estrictamente en -2.0% para proteger el capital. Si el momentum se desacelera sin alcanzar el objetivo, se evaluará rotar capital en el siguiente ciclo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |
| `2026-10-19 01:50` | 🔴 SELL (+0.09$) | `ETH-USD` | $8.09 | $2428.97 | ETH-USD registra una ganancia acumulada y su RSI de 1 hora ha alcanzado 68.3, acercándose ... |

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
