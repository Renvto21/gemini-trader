# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 06:10:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$12.00 USD** | **$39.53 USD** | 🔴 **-1.18%** ($-0.47) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83424.20 | $6.02 | 📈 +0.36% | 9h 9m |
| `SOL-USD` | 0.055840 | $107.45 | $107.13 | $5.98 | 📉 -0.30% | 6h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto y operando en un rango lateral estrecho con ligeros sesgos positivos. BTC-USD muestra estabilidad con un RSI de 1H en 55.3 y una ligera ganancia del 0.36% en cartera, mientras que SOL-USD se mantiene cerca de su precio de entrada con un PnL de -0.30% y un RSI diario profundamente deprimido en 28.6. Los activos tradicionales se encuentran cerrados, por lo que toda la atención táctica se centra en gestionar y rotar el capital dentro de los criptoactivos disponibles."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD muestra un rendimiento positivo constante (+0.36%) y un RSI de 1H neutral-saludable (55.3). Mantenemos la posición a la espera de que el impulso acerque el precio a nuestra zona objetivo de toma de ganancias (+2.0% a +3.5%).
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD se mantiene estable a pesar de la ligera pérdida actual (-0.30%). Su RSI diario se encuentra en sobreventa extrema (28.6), lo que respalda la tesis de un rebote técnico pendiente. Daremos un ciclo más de margen antes de evaluar rotación si no hay tracción alcista.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales de BTC-USD y SOL-USD vigilando de cerca los niveles de take-profit entre +2.0% y +3.5%. Si BTC-USD se acerca al objetivo o su RSI de 1H cruza por encima de 70, realizaremos toma de ganancias. Para SOL-USD, evaluaremos su comportamiento en los próximos ciclos; si no muestra un repunte claro hacia terreno positivo y rompe soporte, rotaremos el capital hacia oportunidades con mayor inercia alcista. Mantener la reserva mínima de efectivo."
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
