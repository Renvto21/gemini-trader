# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 21:10:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$28.54 USD** | **$10.99 USD** | **$39.53 USD** | 🔴 **-1.17%** ($-0.47) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2500.47 | $4.98 | 📉 -0.31% | 4h 0m |
| `BTC-USD` | 0.000072 | $83128.62 | $83223.37 | $6.01 | 📈 +0.11% | 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "Los mercados tradicionales (Wall Street) se encuentran cerrados, por lo que toda la actividad se concentra exclusivamente en las criptomonedas (abiertas 24/7). BTC-USD muestra un comportamiento estable con una ligera ganancia del 0.11% en nuestra posición y un RSI de 1H en 36.9, manteniendo el sesgo de rebote técnico. ETH-USD se mantiene cerca de su precio de entrada con una pequeña pérdida de -0.31% y un RSI de 1H en 32.1. Ambas posiciones se encuentran dentro de los márgenes permitidos de stop-loss (-2.0%) y take-profit (+2.0% a +3.5%), por lo que decidimos mantenerlas y dejar correr el impulso."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición en BTC-USD muestra un rendimiento positivo de +0.11% y mantiene su estructura de rebote de corto plazo con un RSI de 1H en 36.9. Se mantiene activa dentro de los parámetros esperados hacia el take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): La posición en ETH-USD registra una pérdida leve de -0.31%, muy lejos del stop-loss estricto de -2.0%. El RSI de 1H se sitúa en 32.1, lo que indica que continúa en zona de soporte y con probabilidades de buscar el rebote alcista.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones abiertas en BTC-USD y ETH-USD supervisando de cerca el cumplimiento de nuestros objetivos. Si BTC-USD o ETH-USD alcanzan la zona de take-profit entre +2.0% y +3.5%, o si su RSI de 1H supera 70, procederemos a asegurar ganancias inmediatamente. Si alguna de las posiciones rompe el stop-loss estricto de -2.0%, cortaremos la pérdida de inmediato y rotaremos el capital hacia oportunidades con mayor dinamismo en cripto."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **48** | 🎯 **45.8%** (22W / 12L / 14BE) | 🔴 **$-0.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |
| `2026-10-13 16:30` | 🟢 BUY | `ETH-USD` | $9.68 | $2507.92 | ETH-USD muestra un RSI de 35.8 en zona de fuerte sobreventa y un impulso alcista diario de... |

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
