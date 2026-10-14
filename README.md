# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 21:20:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$28.54 USD** | **$11.01 USD** | **$39.55 USD** | 🔴 **-1.12%** ($-0.45) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2505.13 | $4.99 | 📉 -0.13% | 4h 10m |
| `BTC-USD` | 0.000072 | $83128.62 | $83363.34 | $6.02 | 📈 +0.28% | 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que el foco operativo se mantiene exclusivamente en las criptomonedas que operan 24/7. BTC-USD y ETH-USD muestran signos iniciales de estabilización tras tocar zonas de sobreventa en gráficos de 1 hora, con pequeños repuntes en su cambio de 1h y 24h. Mantenemos las posiciones actuales mientras esperamos la consolidación del rebote técnico o la consecución del objetivo de take-profit."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD muestra un pequeño rendimiento positivo del 0.28% y un RSI de 1H en 41.7, recuperándose desde la zona de sobreventa donde fue comprado. Mantenemos la posición a la espera de un mayor impulso hacia el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD se encuentra estable con una pérdida marginal del -0.13% y un RSI de 1H en 34.2 saliendo de la zona de sobreventa. Daremos más margen de tiempo para consolidar el rebote técnico esperado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones abiertas en BTC-USD y ETH-USD supervisando de cerca el cumplimiento de nuestros objetivos de take-profit entre +2.0% y +3.5%, o si su RSI de 1H supera 70 para asegurar ganancias de inmediato. El stop-loss estricto se mantiene en -2.0% para proteger el capital. No realizaremos nuevas entradas en este ciclo para preservar la liquidez mínima y observar el desarrollo del momentum en cripto."
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
