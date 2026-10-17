# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 16:10:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.93 USD** | **$38.41 USD** | 🔴 **-3.98%** ($-1.59) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.73 | $9.98 | 📉 -0.20% | 5h 50m |
| `ETH-USD` | 0.004126 | $2423.75 | $2412.57 | $9.95 | 📉 -0.46% | 4h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado bursátil tradicional se encuentra cerrado, por lo que toda la atención se concentra en el mercado de criptomonedas (abierto 24/7). Los activos principales como SOL-USD y ETH-USD muestran una consolidación en rangos estrechos tras haber buscado rebotes por sobreventa diaria, con variaciones de 1 hora prácticamente planas y RSI de 1 hora neutrales (~35-40). No se observan todavía los impulsos de volumen ni los quiebres alcistas necesarios para activar el take-profit, pero se mantienen estables muy cerca de sus precios de entrada sin alcanzar los niveles de stop-loss."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD acumula un rendimiento estable de -0.2% tras casi 6 horas abierta. El RSI de 1 hora se sitúa en 35.3 y el mercado de criptomonedas está activo, pero aún no se produce el momentum alcista necesario para realizar una toma de beneficios. Mantenemos la posición a la espera del rebote técnico.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD se encuentra con una pérdida menor de -0.46% y un RSI de 1 hora en 40.6. Dado que el mercado tradicional está cerrado y no hay señales de debilidad extrema que ameriten un corte de pérdidas anticipado, mantenemos la posición esperando la confirmación de impulso alcista.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones de SOL-USD y ETH-USD durante este ciclo ya que se encuentran con pérdidas mínimas (-0.2% y -0.46%) y los mercados tradicionales cerrados limitan otras opciones líquidas. Seguiremos vigilando el RSI de 1 hora y el cambio porcentual de corto plazo para identificar el momento en que se dispare el volumen y el rebote técnico hacia la zona objetivo de +2.0% a +3.5%. Si alguna de las posiciones vulnera el soporte crítico y se acerca al límite de -2.0%, ejecutaremos la venta inmediata para proteger el capital disponible."
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
