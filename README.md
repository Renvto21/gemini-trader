# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 02:30:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.65 USD** | **$38.65 USD** | 🔴 **-3.38%** ($-1.35) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 15h 50m |
| `ETH-USD` | 0.004178 | $2393.62 | $2402.06 | $10.04 | 📈 +0.35% | 13h 39m |
| `SOL-USD` | 0.096034 | $104.13 | $104.59 | $10.04 | 📈 +0.44% | 9h 50m |
| `BTC-USD` | 0.000105 | $81767.70 | $81858.07 | $8.57 | 📈 +0.11% | 9h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que la liquidez activa se concentra en el mercado de criptomonedas que opera 24/7. Las posiciones actuales en cripto muestran una estabilidad moderada con ganancias ligeras pero sin alcanzar el objetivo de take-profit del +2% al +3.5%. QQQ se mantiene cerrado con una ligera pérdida temporal. Mantendremos las posiciones actuales ya que no han tocado niveles de stop-loss ni muestran señales de agotamiento bajista extremo que ameriten una venta de pánico."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición muestra un rendimiento positivo de +0.44% y un RSI de 1h en 58.2. Esperamos que el impulso continúe acercándose al rango objetivo de take-profit del +2% al +3.5%.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD se mantiene estable con un PnL de +0.35% y un RSI de 1h en 57.8. Mantenemos la posición a la espera de un mayor despegue alcista.
- **[HOLD] BTC-USD** (Confianza: 75%): La posición se encuentra estable con una ganancia marginal del +0.11% y RSI de 1h en 50.7. Sin razones técnicas para vender o comprar más por el momento.
- **[HOLD] QQQ** (Confianza: 70%): El activo se encuentra en mercado cerrado. La pérdida es mínima (-0.08%) y está dentro de los márgenes de tolerancia antes de la apertura del mercado tradicional.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear las posiciones de SOL-USD, ETH-USD y BTC-USD en busca de un incremento en el RSI de 1 hora hacia zonas de sobrecompra (>70) para realizar tomas de beneficios parciales o totales. Mantener la vigilancia sobre QQQ y otros activos tradicionales para la apertura del mercado bursátil. No ejecutar nuevas compras hasta liberar liquidez mediante la toma de ganancias."
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
