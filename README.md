# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 10:20:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$33.41 USD** | **$5.94 USD** | **$39.36 USD** | 🔴 **-1.61%** ($-0.64) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $82334.59 | $5.94 | 📉 -0.96% | 13h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se encuentra operando en fin de semana/fuera de horario principal con una tendencia general bajista y ligera presión vendedora. BTC-USD mantiene una posición abierta con un PnL moderadamente negativo (-0.96%) tras más de 13 horas de holding, acercándose a nuestra zona de vigilancia pero sin romper soportes críticos. ETH-USD y SOL-USD muestran condiciones de sobreventa en gráficos de 1 hora (RSI en 33 y 32.5 respectivamente), pero dado que el mercado accionario tradicional se encuentra CERRADO, enfocaremos toda nuestra atención en gestionar la posición actual y mantener liquidez para entradas tácticas si el impulso de rebote se confirma."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): La posición en BTC-USD lleva más de 13 horas abierta con una pérdida no realizada menor (-0.96%). El precio se mantiene por encima de nuestro nivel crítico de stop-loss del -2.0%. Mantendremos la posición a la espera de una recuperación del RSI de 1H por encima de 45 que confirme un rebote técnico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos la posición de BTC-USD vigilando de cerca el soporte actual. Si BTC-USD perfora el soporte y se acerca al límite de stop-loss del -2.0%, procederemos a vender inmediatamente para proteger el capital. Dado que los mercados de valores están cerrados, conservaremos el efectivo restante ($33.41 USD) a la espera de señales de volumen alcista y un RSI de 1H superior a 45 en criptoactivos antes de desplegar nuevo capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **50** | 🎯 **44.0%** (22W / 14L / 14BE) | 🔴 **$-0.50 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 10:10` | 🔴 SELL (-0.11$) | `SOL-USD` | $5.89 | $105.41 | La posición en SOL-USD acumula una pérdida cercana al -1.9%, rozando nuestro stop-loss est... |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |

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
