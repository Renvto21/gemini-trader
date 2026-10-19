# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 17:00:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.57 USD** | **$29.96 USD** | **$38.53 USD** | 🔴 **-3.68%** ($-1.47) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 6h 20m |
| `ETH-USD` | 0.004178 | $2393.62 | $2392.43 | $10.00 | 📉 -0.05% | 4h 9m |
| `SOL-USD` | 0.096034 | $104.13 | $103.89 | $9.98 | 📉 -0.23% | 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra CERRADO, por lo que toda la atención operativa se concentra en las criptomonedas (ABIERTO 24/7). ETH-USD y SOL-USD muestran condiciones extremas de sobreventa con RSI diarios muy deprimidos (23.9 y 19.2 respectivamente) y RSI de 1 hora saliendo de niveles mínimos con ligeros cambios positivos de 1h, lo que valida la continuidad de nuestra tesis de rebote técnico (mean reversion). Mantenemos la cautela y vigilamos de cerca los niveles de stop-loss y take-profit."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD se mantiene en cartera con una pérdida menor de -0.05%. El RSI de 1h está en 32.8 y el RSI diario en 23.9, mostrando una sobreventa profunda ideal para un rebote. Mantenemos la posición a la espera de que el momentum alcista se acelere.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD presenta un RSI diario extremo de 19.2 y un RSI de 1h en 31.0 con un ligero cambio positivo de 1h (+0.03%). La pérdida actual es de solo -0.23%, por lo que el setup técnico de rebote sigue intacto y dentro de los parámetros de riesgo permitidos.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales en QQQ, ETH-USD y SOL-USD ya que las pérdidas no han alcanzado el stop-loss estricto del -2.0%. Dado que el mercado tradicional está cerrado, operaremos solo sobre los activos cripto si muestran un cambio de momentum más claro. Establecemos objetivos de salida entre +2.0% y +3.5% para asegurar beneficios rápidamente, y mantendremos el stop-loss ajustado a -2.0%."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |
| `2026-10-19 01:50` | 🔴 SELL (+0.09$) | `ETH-USD` | $8.09 | $2428.97 | ETH-USD registra una ganancia acumulada y su RSI de 1 hora ha alcanzado 68.3, acercándose ... |
| `2026-10-19 01:00` | 🔴 SELL (-0.00$) | `SOL-USD` | $8.00 | $105.08 | SOL-USD ha entrado en sobrecompra con un RSI de 1 hora en 72.7, cumpliendo estrictamente c... |

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
