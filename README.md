# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 14:30:51`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.84 USD** | **$38.32 USD** | 🔴 **-4.20%** ($-1.68) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.16 | $9.92 | 📉 -0.75% | 4h 10m |
| `ETH-USD` | 0.004126 | $2423.75 | $2404.28 | $9.92 | 📉 -0.80% | 2h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se encuentra mayoritariamente cerrado por ser fin de semana o fuera de horario, por lo que la liquidez activa se concentra en las criptomonedas (24/7). Los activos principales de cripto como SOL-USD y ETH-USD muestran niveles de sobreventa extrema tanto en gráficos diarios como de 1 hora, pero mantienen una tendencia bajista de corto plazo. Nuestras posiciones actuales registran pérdidas menores (-0.75% y -0.8%), manteniéndose seguras muy por encima de nuestro umbral de stop-loss estricto de -2.0%."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición en SOL-USD se mantiene estable con una pérdida leve de -0.75%, muy por encima del stop-loss del -2.0%. El RSI de 1 hora sigue bajo, por lo que esperamos una señal clara de recuperación para buscar el take-profit.
- **[HOLD] ETH-USD** (Confianza: 80%): La posición en ETH-USD registra una pérdida menor de -0.8%, respetando los parámetros de riesgo. Mantenemos la posición para capturar el rebote técnico cuando el impulso de corto plazo se torne favorable.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales en SOL-USD y ETH-USD durante este ciclo, ya que se encuentran estables dentro de los rangos de riesgo permitidos y lejos del stop-loss de -2.0%. Monitorearemos de cerca el RSI de 1 hora para buscar zonas de take-profit en cuanto alcancen ganancias de +2.0% a +3.5% o superen los 70 puntos. No realizaremos nuevas compras hasta ver una ruptura clara de la tendencia bajista actual en los gráficos de 1 hora."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **65** | 🎯 **40.0%** (26W / 25L / 14BE) | 🔴 **$-1.41 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 11:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2423.75 | ETH-USD presenta un RSI diario en niveles de sobreventa profunda (28.9) y un cambio positi... |
| `2026-10-17 10:20` | 🟢 BUY | `SOL-USD` | $10.00 | $103.94 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (22.5) y un cambio positiv... |
| `2026-10-17 04:30` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $104.94 | SOL-USD ha alcanzado un RSI de 1 hora de 70.4, entrando en zona de sobrecompra, y acumula ... |
| `2026-10-17 04:00` | 🔴 SELL (+0.07$) | `ETH-USD` | $10.07 | $2429.64 | ETH-USD ha alcanzado un RSI de 1 hora de 73.3, entrando en zona de sobrecompra. Siguiendo ... |
| `2026-10-16 16:30` | 🟢 BUY | `ETH-USD` | $10.00 | $2412.98 | ETH-USD muestra un RSI diario en niveles de sobreventa extrema (30.3) y un cambio positivo... |

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
