# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 14:20:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.84 USD** | **$38.31 USD** | 🔴 **-4.22%** ($-1.69) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.16 | $9.92 | 📉 -0.75% | 4h 0m |
| `ETH-USD` | 0.004126 | $2423.75 | $2402.16 | $9.91 | 📉 -0.89% | 2h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto pero bajo presión bajista general y con un momentum de corto plazo muy débil. Los activos en cartera (SOL-USD y ETH-USD) muestran ligeras minusvalías que aún respetan nuestra tolerancia al riesgo, sin llegar al stop-loss estricto del -2.0%. Dado que el mercado tradicional está cerrado y las criptos muestran indicadores mixtos con RSI de 1 hora deprimidos pero sin un cambio de tendencia claro, la estrategia óptima es mantener la paciencia y vigilar de cerca la evolución del precio."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición se mantiene con una pérdida menor del -0.75%, dentro del rango de tolerancia y sin romper el soporte crítico. Esperamos confirmación de rebote alcista.
- **[HOLD] ETH-USD** (Confianza: 70%): La posición registra una caída de -0.89%, operando por encima de nuestro nivel de stop-loss estricto de -2.0%. Mantenemos la operativa a la espera de un flujo alcista.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales en SOL-USD y ETH-USD por este ciclo. Estableceremos un stop-loss estricto en -2.0% para ambas posiciones y buscaremos zonas de take-profit cuando el RSI de 1 hora supere los 70 puntos o el rendimiento alcance el rango de +2.0% a +3.5%. Si el mercado profundiza las pérdidas y toca el umbral de -2.0%, ejecutaremos venta inmediata para proteger capital."
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
