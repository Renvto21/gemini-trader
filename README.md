# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 15:20:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.37 USD** | **$19.86 USD** | **$38.23 USD** | 🔴 **-4.42%** ($-1.77) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.097172 | $102.91 | $102.13 | $9.92 | 📉 -0.76% | 4h 19m |
| `ETH-USD` | 0.004205 | $2377.97 | $2362.87 | $9.94 | 📉 -0.63% | 3h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto 24/7 mostrando un sesgo lateral a bajista de corto plazo, con ETH-USD y SOL-USD consolidando tras sus recientes caídas. Los mercados tradicionales permanecen cerrados. Las posiciones actuales en SOL-USD y ETH-USD se encuentran con ligeras pérdidas latentes (~-0.7%), pero mantienen RSI diarios en zonas de sobreventa extrema, lo que valida la tesis de rebote a la espera de un gatillo alcista de volumen."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD mantiene un RSI diario extremadamente bajo (16.0) y un RSI de 1 hora en 31.1 con un ligero cambio positivo (+0.11%). La posición muestra una pérdida menor (-0.76%) y el holding time es de aproximadamente 4 horas. Continuamos esperando el desarrollo del rebote técnico hacia la zona de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD presenta un RSI diario en 21.5 y un RSI de 1 hora en 23.2, encontrándose en una zona clara de sobreventa profunda. La pérdida actual es marginal (-0.63%) y se mantendrá la posición mientras se espera la recuperación del impulso de corto plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones abiertas de SOL-USD y ETH-USD durante este ciclo para permitir que el rebote técnico se desarrolle, ya que el holding time sigue siendo corto (~4h). El stop-loss estricto se mantiene en -2.0% y buscaremos tomar beneficios (take-profit) si el RSI de 1 hora supera 70 o la ganancia alcanza el rango de +2.0% a +3.5%. La liquidez actual de $18.37 USD se reservará para posibles entradas adicionales o para cubrir cualquier contingencia táctica."
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
