# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 06:40:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$11.96 USD** | **$39.49 USD** | 🔴 **-1.28%** ($-0.51) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83218.61 | $6.01 | 📈 +0.11% | 9h 39m |
| `SOL-USD` | 0.055840 | $107.45 | $106.62 | $5.95 | 📉 -0.77% | 7h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra completamente cerrado durante el fin de semana, por lo que toda la actividad se concentra en las criptomonedas (BTC-USD y SOL-USD). Ambas criptomonedas muestran un comportamiento lateral con ligeros sesgos bajistas en el corto plazo, pero manteniendo sus soportes diarios. El portafolio actual se mantiene estable con pérdidas mínimas y sin la necesidad de activar un stop-loss estricto ya que ninguna posición ha tocado el límite del -2.0%."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 70%): BTC-USD se mantiene en rango con un PnL ligeramente positivo (+0.11%) tras casi 10 horas. El RSI de 1H se sitúa en 50.3 y la tendencia diaria sigue consolidando. No hay razones para vender ni comprar más en este momento, mantenemos la posición esperando el objetivo de take-profit.
- **[HOLD] SOL-USD** (Confianza: 65%): SOL-USD muestra un PnL de -0.77% y un holding time de más de 7 horas. Aunque el momentum de corto plazo es débil, el RSI diario en 27.3 respalda el soporte macro de sobreventa. Mantenemos la posición a la espera de un rebote técnico sin alcanzar aún el stop-loss.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales de BTC-USD y SOL-USD vigilando de cerca los niveles de take-profit entre +2.0% y +3.5% o sobrecompra en RSI de 1H (> 70). Dado que las posiciones llevan varias horas con poco movimiento, nos mantendremos pacientes esperando el próximo impulso alcista. No se realizarán nuevas compras en este ciclo para preservar la liquidez mínima y observar la evolución del precio en las criptomonedas principales."
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
