# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 21:30:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$28.54 USD** | **$11.03 USD** | **$39.57 USD** | 🔴 **-1.08%** ($-0.43) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2511.26 | $5.01 | 📈 +0.12% | 4h 20m |
| `BTC-USD` | 0.000072 | $83128.62 | $83439.46 | $6.02 | 📈 +0.37% | 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas continúa operando en un rango de recuperación moderada 24/7, con BTC-USD y ETH-USD mostrando ligeras ganancias diarias del 2.05% y 2.74% respectivamente, aunque aún operan bajo sus medias móviles de 20 días en un contexto técnico general bajista. Los mercados tradicionales de Wall Street se encuentran cerrados, por lo que toda la atención operativa se concentra en mantener el capital activo en las criptomonedas y proteger las pequeñas ganancias actuales."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): La posición en ETH-USD se mantiene en terreno positivo (+0.12%) tras 4 horas y 20 minutos de retención. Su RSI de 1H se ubica en 38.7 con un cambio positivo de 1H del 0.27%, lo que indica que el rebote sigue gestándose sin alcanzar todavía el objetivo de take-profit (+2.0% a +3.5%) ni activar el stop-loss. Mantenemos la posición.
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD opera con una ganancia de +0.37% tras su reciente entrada, con un RSI de 1H en 44.1 y un cambio positivo constante. Permanece dentro de los parámetros esperados de acumulación del rebote técnico, por lo que conservamos la posición a la espera del objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales en ETH-USD y BTC-USD mientras se aproximan a nuestros objetivos de take-profit entre +2.0% y +3.5%, o hasta que el RSI de 1H supere 70 para asegurar beneficios. El stop-loss estricto se mantiene firme en -2.0%. Dado que el efectivo disponible de reserva se mantiene saludable en $28.54 USD y las posiciones actuales muestran un rendimiento estable, no realizaremos nuevas compras en este ciclo para evitar sobreexponer el portafolio en una tendencia bajista de marco temporal diario."
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
