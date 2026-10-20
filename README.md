# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 02:50:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.66 USD** | **$38.66 USD** | 🔴 **-3.35%** ($-1.34) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 16h 10m |
| `ETH-USD` | 0.004178 | $2393.62 | $2401.79 | $10.03 | 📈 +0.34% | 13h 59m |
| `SOL-USD` | 0.096034 | $104.13 | $104.76 | $10.06 | 📈 +0.61% | 10h 10m |
| `BTC-USD` | 0.000105 | $81767.70 | $81856.73 | $8.57 | 📈 +0.11% | 9h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto 24/7 con una ligera consolidación tras los intentos de rebote recientes. Activos como SOL-USD y ETH-USD muestran rendimientos marginales positivos, mientras que los mercados tradicionales (QQQ) se encuentran cerrados con precios congelados. La liquidez total del portafolio se encuentra completamente invertida en este momento, por lo que la prioridad es la vigilancia de las posiciones activas para asegurar beneficios en cuanto alcancen los objetivos del 2% al 3.5%, o recortar pérdidas si se invalidan los soportes técnicos."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición muestra un rendimiento positivo de +0.61% y un RSI de 1 hora en 61.2, aproximándose a la zona de sobrecompra. Mantendremos la posición para buscar un take-profit óptimo entre +2.0% y +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (QQQ, ETH-USD, SOL-USD, BTC-USD) ya que se encuentran estables o con ligeras ganancias. Monitorear de cerca a SOL-USD y ETH-USD para asegurar beneficios si el RSI de 1 hora se acerca a la zona de sobrecompra (>70). No realizar nuevas compras hasta liberar liquidez mediante la toma de ganancias parcial o total de las posiciones con mejor desempeño."
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
