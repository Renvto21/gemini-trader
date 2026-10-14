# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 21:40:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$28.54 USD** | **$11.05 USD** | **$39.59 USD** | 🔴 **-1.03%** ($-0.41) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2515.89 | $5.01 | 📈 +0.30% | 4h 30m |
| `BTC-USD` | 0.000072 | $83128.62 | $83607.37 | $6.03 | 📈 +0.58% | 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra cerrado, por lo que toda la actividad se concentra en los criptoactivos (24/7). Las posiciones actuales en ETH-USD y BTC-USD muestran ligeras ganancias (+0.3% y +0.58% respectivamente) con un comportamiento estable, manteniéndose lejos tanto del stop-loss de -2.0% como de los objetivos de take-profit entre +2.0% y +3.5%. Los indicadores de 1H muestran un momentum neutral a ligeramente positivo sin alcanzar aún la sobrecompra (>70). Mantenemos la cautela y la vigilancia activa sobre los activos abiertos."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD muestra un rendimiento positivo constante (+0.3%) tras el rebote inicial. Se mantiene operando por debajo del take-profit objetivo y sin señales de debilidad que ameriten recortar la posición, por lo que se decide mantener.
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD presenta un avance estable de +0.58% con un buen comportamiento del RSI de 1H. Está dentro de los parámetros esperados de la estrategia de rebote y lejos del stop-loss, por lo que se mantiene la posición.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Continuaremos manteniendo ETH-USD y BTC-USD en este ciclo, esperando que alcancen el objetivo de take-profit entre +2.0% y +3.5% o que el RSI de 1H supere 70 para asegurar beneficios. El stop-loss se mantiene firme en -2.0%. Dado que el efectivo disponible de reserva se sitúa en $28.54 USD, guardaremos liquidez para futuras oportunidades de alta convicción cuando se presenten entradas claras por sobreventa."
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
