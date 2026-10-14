# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 03:31:17`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$12.00 USD** | **$39.53 USD** | 🔴 **-1.18%** ($-0.47) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83407.97 | $6.02 | 📈 +0.34% | 6h 30m |
| `SOL-USD` | 0.055840 | $107.45 | $107.10 | $5.98 | 📉 -0.33% | 4h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra cerrado, por lo que toda la actividad se concentra en las criptomonedas (BTC-USD y SOL-USD), que operan 24/7. Ambas posiciones se mantienen estables pero con ganancias y pérdidas moderadas cercanas al 0%, con el RSI de 1 hora normalizado y el RSI diario de SOL en niveles de sobreventa extrema (27.3). Mantenemos la disciplina sin forzar operaciones de compra nuevas ya que buscamos confirmación de mayor impulso antes de desplegar más liquidez."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 60%): La posición muestra un rendimiento positivo marginal (+0.34%) con un holding time de poco más de 6 horas. Mantenemos la posición a la espera de que alcance el objetivo de take-profit del +2.0% al +3.5%.
- **[HOLD] SOL-USD** (Confianza: 60%): La posición de SOL-USD se mantiene cerca de la paridad (-0.33%) respaldada por un RSI diario profundamente en sobreventa (27.3). Esperaremos a que desarrolle el rebote técnico esperado hacia nuestra zona de beneficios.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de BTC-USD y SOL-USD. Monitorearemos que alcancen la zona objetivo de take-profit entre +2.0% y +3.5% o activaremos el stop-loss en caso de caída mayor a -2.0%. Si el mercado de criptomonedas continúa lateralizando sin alcanzar los objetivos en las próximas horas, rotaremos parte del capital hacia activos con mayor momentum."
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
