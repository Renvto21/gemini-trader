# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 12:20:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.93 USD** | **$38.40 USD** | 🔴 **-4.00%** ($-1.60) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.69 | $9.98 | 📉 -0.24% | 2h 0m |
| `ETH-USD` | 0.004126 | $2423.75 | $2411.57 | $9.95 | 📉 -0.50% | 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario de Wall Street se encuentra completamente cerrado, por lo que la operativa se concentra exclusivamente en el mercado de criptomonedas (abierto 24/7). Las criptomonedas principales como SOL-USD y ETH-USD muestran consolidación lateral con ligeros retrocesos en la última hora, manteniendo sus RSI en niveles neutrales de corto plazo mientras el contexto diario permanece en sobreventa profunda. No hay señales inmediatas de pánico ni de un rebote explosivo confirmado, por lo que la estrategia adecuada es mantener posiciones actuales y permitir que maduren."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD lleva poco tiempo abierta (2 horas) y se mantiene estable con una ligera variación del -0.24%. Mantenemos la posición a la espera de un impulso alcista que acerque el precio a la zona de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un comportamiento similar, con una pérdida temporal de -0.5% en 30 minutos de holding. El RSI diario se mantiene en zona de sobreventa profunda, por lo que conservamos la posición para capturar el rebote esperado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de SOL-USD y ETH-USD ya que se encuentran estables dentro del rango de tolerancia y con poco tiempo de apertura. Monitorearemos la evolución del RSI de 1 hora buscando que supere los 70 puntos para asegurar take-profit o que se acerque al stop-loss estricto en -2.0%. La liquidez se mantiene segura en $18.48 USD esperando la próxima confirmación de momentum alcista."
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
