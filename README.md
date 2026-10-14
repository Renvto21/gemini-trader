# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 00:30:53`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.54 USD** | **$17.09 USD** | **$39.63 USD** | 🔴 **-0.92%** ($-0.37) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2515.67 | $5.01 | 📈 +0.29% | 7h 20m |
| `BTC-USD` | 0.000072 | $83128.62 | $83812.16 | $6.05 | 📈 +0.82% | 3h 30m |
| `SOL-USD` | 0.055840 | $107.45 | $107.93 | $6.03 | 📈 +0.45% | 1h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con un tono ligeramente positivo en las últimas horas (BTC-USD y SOL-USD con cambios positivos cercanos al 0.3% en 1h y +2.5% en 24h). Los activos tradicionales (acciones y ETFs) se encuentran cerrados, por lo que toda la atención táctica se centra en la gestión de nuestras posiciones abiertas en criptomonedas. Los indicadores de RSI en 1 hora se acercan a zonas de control sin sobrecompra extrema aún (alrededor de 59-64), permitiendo mantener las posiciones actuales a la espera de alcanzar el objetivo de take-profit entre +2.0% y +3.5%."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición muestra un rendimiento positivo (+0.82%) y un RSI de 1h en 63.3, acercándose al rango objetivo de take-profit sin mostrar signos de agotamiento bajista inmediato. Se mantiene para buscar la meta de ganancia.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD opera con un PnL positivo moderado (+0.29%) y un RSI de 1h en 59.4. Se mantiene en cartera a la espera de que el impulso alcista fortalezca el rebote técnico hacia la zona de beneficios.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD presenta un PnL de +0.45% y un RSI de 1h en 64.3, reflejando el rebote esperado desde la sobreventa diaria. Se mantiene la posición para capturar el objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales de BTC-USD, SOL-USD y ETH-USD ya que muestran un comportamiento estable con ganancias marginales. Monitorear de cerca el RSI de 1 hora de cada activo: si se acercan o superan los 70 o si el PnL alcanza el rango de +2.0% a +3.5%, ejecutar la toma de beneficios total o parcial para acumular efectivo. El stop-loss se mantiene estricto en -2.0% para proteger el capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **48** | 🎯 **45.8%** (22W / 12L / 14BE) | 🔴 **$-0.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |

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
