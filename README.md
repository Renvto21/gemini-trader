# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 09:10:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$12.05 USD** | **$39.57 USD** | 🔴 **-1.07%** ($-0.43) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83667.60 | $6.04 | 📈 +0.65% | 12h 9m |
| `SOL-USD` | 0.055840 | $107.45 | $107.58 | $6.01 | 📈 +0.12% | 9h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra cerrado, por lo que la liquidez activa se concentra en el sector de criptomonedas (ABIERTO 24/7). Tanto BTC-USD como SOL-USD muestran ligeras ganancias con un momentum positivo en el corto plazo y RSI de 1H en zona neutral-saludable, sin alcanzar aún la sobrecompra extrema (>70) que active una toma de beneficios inmediata. Mantenemos las posiciones activas mientras respeten los niveles de stop-loss."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): La posición en BTC-USD mantiene un PnL positivo de 0.65% con un RSI de 1H en 54.4 y un cambio horario positivo. No ha alcanzado el objetivo de take-profit ni ha roto el stop-loss, por lo que mantenemos la operación abierta.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener BTC-USD y SOL-USD vigentes. Monitorear de cerca el RSI de 1H en busca de niveles superiores a 70 para realizar tomas de beneficios parciales o totales. Si el holding time supera las 15-20 horas sin incrementos de momentum, procederemos a rotar el capital hacia oportunidades de mayor dinamismo."
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
