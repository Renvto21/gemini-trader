# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 18:00:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.99 USD** | **$38.47 USD** | 🔴 **-3.82%** ($-1.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $104.09 | $10.01 | 📈 +0.14% | 7h 40m |
| `ETH-USD` | 0.004126 | $2423.75 | $2418.90 | $9.98 | 📉 -0.20% | 6h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado por fin de semana/horario inhábil, por lo que toda la operativa activa se concentra en el mercado de criptomonedas (abierto 24/7). Las criptomonedas principales (SOL-USD y ETH-USD) se mantienen operando en rangos estrechos y sin el impulso alcista esperado en el corto plazo tras varias horas de tenencia. El sentimiento macro sigue cauteloso y bajista por debajo de las medias móviles, pero los niveles diarios de RSI en cripto siguen profundamente deprimidos, lo que sugiere paciencia a la espera de un catalizador de volumen o rotación."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 60%): La posición en SOL-USD se mantiene estable con un P&L marginal de +0.14% tras 7 horas y 40 minutos. Aunque el movimiento ha sido lateral, el RSI diario se encuentra en niveles de sobreventa extrema (22.7), por lo que mantenemos la posición esperando un impulso de volumen que active nuestro objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] ETH-USD** (Confianza: 60%): La posición en ETH-USD muestra una leve pérdida actual de -0.20% tras 6 horas de tenencia. El comportamiento es plano pero se mantiene dentro del margen de tolerancia antes de activar un stop-loss estricto. Mantendremos la exposición a la espera de una ruptura del RSI de 1 hora por encima de 50 que confirme el rebote.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Las posiciones actuales de SOL-USD y ETH-USD llevan más de 6-7 horas con movimientos laterales mínimos (P&L cercano a 0%). Dado que no muestran el momentum de rebote esperado en el RSI de 1 hora, mantendremos las posiciones por un ciclo más vigilando de cerca el soporte. Si el RSI de 1 hora rompe a la baja o la posición se acerca al stop-loss del -2.0%, procederemos a cortar pérdidas de inmediato para liberar efectivo y buscar mejores setups en activos con mayor volatilidad y momento técnico."
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
