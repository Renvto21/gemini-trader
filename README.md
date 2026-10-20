# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 04:50:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.52 USD** | **$38.52 USD** | 🔴 **-3.71%** ($-1.48) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 18h 9m |
| `ETH-USD` | 0.004178 | $2393.62 | $2388.37 | $9.98 | 📉 -0.22% | 15h 59m |
| `SOL-USD` | 0.096034 | $104.13 | $104.28 | $10.01 | 📈 +0.14% | 12h 9m |
| `BTC-USD` | 0.000105 | $81767.70 | $81441.78 | $8.53 | 📉 -0.40% | 11h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional (Wall Street) se encuentra cerrado, por lo que toda la liquidez y enfoque operativo se concentran en el mercado de criptomonedas (abierto 24/7). Las posiciones actuales se encuentran estables pero con un ligero sesgo bajista lateral de corto plazo. Mantenemos la vigilancia sobre los niveles de soporte diario y RSI en cripto para buscar take-profits o rotación de capital según las reglas de momentum."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra un RSI diario en niveles de sobreventa profunda (21.3) y mantiene un valor positivo leve en la posición actual. Esperamos que el rebote técnico se acelere para buscar la zona de take-profit objetivo entre +2.0% y +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas (QQQ, ETH-USD, SOL-USD, BTC-USD) monitoreando de cerca su comportamiento de precio. Establecer take-profit estricto entre +2.0% y +3.5% o RSI 1H superior a 70. Vigilar el stop-loss en -2.0% para evitar pérdidas mayores. Si alguna cripto se estanca sin momentum, rotar el capital hacia activos con mayor dinamismo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 23:00` | 🟢 BUY | `BTC-USD` | $4.00 | $81646.39 | BTC-USD presenta un RSI de 1 hora en 27.7, nivel de sobreventa profunda ideal para un rebo... |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |

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
