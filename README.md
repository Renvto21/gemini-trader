# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 17:30:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$34.62 USD** | **$38.61 USD** | 🔴 **-3.46%** ($-1.39) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 6h 50m |
| `ETH-USD` | 0.004178 | $2393.62 | $2398.92 | $10.02 | 📈 +0.22% | 4h 39m |
| `SOL-USD` | 0.096034 | $104.13 | $104.47 | $10.03 | 📈 +0.33% | 49m |
| `BTC-USD` | 0.000056 | $81874.05 | $81915.63 | $4.57 | 📈 +0.05% | 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto 24/7 mostrando ligeros signos de recuperación en el corto plazo, con SOL-USD, ETH-USD y BTC-USD registrando pequeños cambios positivos de 1 hora tras tocar zonas de sobreventa. Los activos tradicionales como QQQ y SPY se encuentran cerrados, por lo que la operativa actual se centra exclusivamente en gestionar las posiciones de cripto abiertas buscando capitalizar rebotes técnicos."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD muestra un cambio positivo de 1 hora de +0.59% y un RSI diario en niveles de sobreventa profunda (20.6), manteniendo intacto el potencial para un rebote técnico hacia el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD mantiene un comportamiento estable con un ligero incremento horaria, operando cerca de su precio de entrada y esperando confirmación de mayor volumen alcista.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en criptomonedas (SOL-USD, ETH-USD, BTC-USD) y la posición en QQQ a la espera de la apertura de Wall Street. Monitorear de cerca los objetivos de take-profit entre +2.0% y +3.5% o niveles de RSI de 1 hora cercanos a sobrecompra para rotar capital rápidamente. El stop-loss estricto se mantiene en -2.0% para proteger el capital ante cualquier fallo en el rebote."
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
