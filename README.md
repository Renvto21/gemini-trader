# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 02:10:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.54 USD** | **$16.99 USD** | **$39.53 USD** | 🔴 **-1.18%** ($-0.47) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2501.34 | $4.99 | 📉 -0.28% | 9h 0m |
| `BTC-USD` | 0.000072 | $83128.62 | $83379.56 | $6.02 | 📈 +0.30% | 5h 9m |
| `SOL-USD` | 0.055840 | $107.45 | $107.14 | $5.98 | 📉 -0.29% | 2h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se encuentra abierto operando 24/7 con un sesgo lateral a bajista en el corto plazo, mientras que los mercados tradicionales (Wall Street) permanecen cerrados. Las posiciones actuales en BTC-USD, ETH-USD y SOL-USD muestran variaciones mínimas y se mantienen dentro de rangos normales de consolidación tras intentar rebotes técnicos, sin disparar aún los objetivos de take-profit del 2.0% al 3.5% ni los stop-loss."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD muestra una ligera ganancia de +0.3% y un RSI de 1 hora estable en 51.0. Se mantiene la posición esperando que alcance el objetivo de take-profit sin señales de invalidación del rebote.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas actuales (ETH-USD, BTC-USD, SOL-USD) vigilando de cerca su evolución. Establecer objetivo estricto de take-profit entre +2.0% y +3.5% y stop-loss defensivo ante cualquier caída mayor a -2.0%. Mantener la reserva de efectivo actual y esperar confirmaciones de momentum más fuertes en cripto antes de rotar capital o abrir nuevas operaciones."
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
