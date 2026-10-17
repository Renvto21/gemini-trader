# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 18:10:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.98 USD** | **$38.45 USD** | 🔴 **-3.87%** ($-1.55) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.95 | $10.00 | 📈 +0.01% | 7h 50m |
| `ETH-USD` | 0.004126 | $2423.75 | $2417.86 | $9.98 | 📉 -0.24% | 6h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general de criptomonedas se encuentra en un rango lateral bajista con baja volatilidad en el corto plazo. Los activos tradicionales (acciones y ETFs) están cerrados durante el fin de semana, por lo que toda la atención se centra en las cripto 24/7. Las posiciones actuales de SOL-USD y ETH-USD muestran consolidación prolongada tras más de 6-7 horas abiertas sin alcanzar el objetivo de rebote, aunque se mantienen firmes por encima de los límites de stop-loss estricto."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 60%): La posición lleva cerca de 8 horas abierta con un rendimiento plano (0.01%). Aunque el RSI diario está en sobreventa extrema, el RSI de 1 hora se mantiene tibio en 37. Mantendremos la posición vigilando el soporte y el stop-loss del -2.0%.
- **[HOLD] ETH-USD** (Confianza: 60%): ETH-USD registra una leve pérdida de -0.24% tras más de 6 horas de tenencia. El RSI diario muestra sobreventa profunda (28.4), pero el impulso a 1 hora sigue lateral. Mantenemos la posición a la espera de un gatillo alcista.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones de SOL-USD y ETH-USD un ciclo más ya que la pérdida no supera el umbral de -2.0%. Si el RSI de 1 hora no rompe al alza y el precio continúa estancado, procederemos a vender en el próximo ciclo para rotar el capital hacia oportunidades con mayor momentum."
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
