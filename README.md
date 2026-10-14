# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 10:00:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$11.86 USD** | **$39.38 USD** | 🔴 **-1.54%** ($-0.62) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $82698.75 | $5.97 | 📉 -0.52% | 12h 59m |
| `SOL-USD` | 0.055840 | $107.45 | $105.47 | $5.89 | 📉 -1.84% | 10h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado por lo que la liquidez opera en criptomonedas 24/7. BTC-USD y SOL-USD se mantienen con momentum débil pero sin romper el soporte crítico de stop-loss del -2.0%, aunque SOL-USD se encuentra muy cerca con una pérdida de -1.84% y un holding time superior a las 10 horas."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 65%): BTC-USD se mantiene cerca del precio de entrada con un PnL de -0.52%. El RSI de 1H está en 42.2 y no ha alcanzado los niveles de stop-loss del -2.0%, por lo que mantenemos la posición esperando una mejora en el momentum.
- **[HOLD] SOL-USD** (Confianza: 60%): SOL-USD presenta un PnL de -1.84%, acercándose al límite estricto de stop-loss del -2.0%. Dado que el holding time supera las 10 horas y el RSI diario está en sobreventa extrema (26.1), le daremos un margen adicional en este ciclo antes de ejecutar el corte de pérdidas.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos BTC-USD y SOL-USD vigilando de cerca el stop-loss estricto del -2.0%. Si SOL-USD rompe a la baja procederemos a liquidar inmediatamente para proteger efectivo y buscar nuevas entradas."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **49** | 🎯 **44.9%** (22W / 13L / 14BE) | 🔴 **$-0.39 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |

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
