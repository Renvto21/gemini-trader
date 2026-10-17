# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 17:10:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.98 USD** | **$38.45 USD** | 🔴 **-3.87%** ($-1.55) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.95 | $10.00 | 📈 +0.01% | 6h 50m |
| `ETH-USD` | 0.004126 | $2423.75 | $2417.48 | $9.97 | 📉 -0.26% | 5h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario tradicional se encuentra cerrado por lo que la liquidez y operativa se concentran exclusivamente en las criptomonedas. SOL-USD y ETH-USD muestran consolidación lateral tras haber abierto posiciones basadas en sobreventa diaria, manteniendo un comportamiento plano sin activar aún los objetivos de take-profit ni perforar el stop-loss estricto."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición se encuentra estable con un PnL de 0.01% tras casi 7 horas de holding. El RSI de 1 hora se sitúa en 39 y el diario en 22.6, manteniendo la tesis de rebote técnico sin romper los límites del stop-loss.
- **[HOLD] ETH-USD** (Confianza: 70%): La posición registra una ligera baja de -0.26% tras más de 5 horas activa, manteniéndose muy por encima del límite estricto de stop-loss de -2.0%. Esperamos que el impulso intradiario reactive el rebote técnico hacia la zona objetivo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones de SOL-USD y ETH-USD por unos ciclos adicionales dado que se mantienen estables dentro de los rangos de riesgo permitidos. Monitorearemos de cerca un incremento en el volumen o RSI de 1 hora para asegurar ganancias si rozan el +2%, o cortar de inmediato si las pérdidas se acercan al -2%. No se abrirán nuevas posiciones en este momento para preservar el efectivo mínimo."
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
