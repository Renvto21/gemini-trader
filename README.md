# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 10:40:36`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$28.48 USD** | **$9.99 USD** | **$38.46 USD** | 🔴 **-3.85%** ($-1.54) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.79 | $9.99 | 📉 -0.14% | 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado y las criptomonedas muestran un comportamiento plano con un sesgo ligeramente bajista en el corto plazo. SOL-USD mantiene un RSI diario profundamente sobrevendido en 22.4, pero su momentum en 1 hora se ha enfriado ligeramente con un RSI de 40.2 tras una apertura reciente de hace 19 minutos. La liquidez activa se enfoca exclusivamente en activos 24/7 mientras esperamos confirmación de volumen alcista."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD lleva apenas 19 minutos abierta con una ligera variación del -0.14%. El RSI diario en sobreventa extrema (22.4) respalda la tesis original de rebote técnico, por lo que mantendremos la posición esperando el impulso alcista necesario para alcanzar el take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos la posición actual en SOL-USD bajo vigilancia estricta. Monitorearemos un objetivo de take-profit entre +2.0% y +3.5% o una sobrecompra en el RSI de 1 hora (>70). El stop-loss se mantiene firme en -2.0%. Si el precio rompe el soporte o el holding time se extiende sin momentum positivo, evaluaremos rotar hacia ETH-USD o capitalizar nuevas oportunidades en cripto."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **65** | 🎯 **40.0%** (26W / 25L / 14BE) | 🔴 **$-1.41 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 10:20` | 🟢 BUY | `SOL-USD` | $10.00 | $103.94 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (22.5) y un cambio positiv... |
| `2026-10-17 04:30` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $104.94 | SOL-USD ha alcanzado un RSI de 1 hora de 70.4, entrando en zona de sobrecompra, y acumula ... |
| `2026-10-17 04:00` | 🔴 SELL (+0.07$) | `ETH-USD` | $10.07 | $2429.64 | ETH-USD ha alcanzado un RSI de 1 hora de 73.3, entrando en zona de sobrecompra. Siguiendo ... |
| `2026-10-16 16:30` | 🟢 BUY | `ETH-USD` | $10.00 | $2412.98 | ETH-USD muestra un RSI diario en niveles de sobreventa extrema (30.3) y un cambio positivo... |
| `2026-10-16 16:30` | 🔴 SELL (-0.11$) | `MSFT` | $6.39 | $526.18 | MSFT lleva más de 1 día y 5 horas abierto mostrando debilidad persistente y un rendimiento... |

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
