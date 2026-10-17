# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 17:40:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.97 USD** | **$38.44 USD** | 🔴 **-3.89%** ($-1.56) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.95 | $10.00 | 📈 +0.01% | 7h 20m |
| `ETH-USD` | 0.004126 | $2423.75 | $2415.72 | $9.97 | 📉 -0.33% | 5h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general muestra un sentimiento predominantemente bajista con los índices y acciones tradicionales cerrados. Las criptomonedas (SOL-USD, ETH-USD y BTC-USD) se mantienen operativas 24/7 pero muestran una consolidación lateral con bajo momentum de corto plazo en este ciclo. El RSI de 1 hora para Solana y Ethereum se sitúa cerca de 39, sin lograr romper con fuerza al alza, mientras que las caídas semanales se estabilizan pero sin catalizadores inmediatos de volumen."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 65%): La posición lleva abierta unas horas con un rendimiento neutro (0.01%). El RSI diario sigue en sobreventa extrema y el RSI de 1h se mantiene en 39, por lo que esperamos una confirmación de volumen para buscar el objetivo de take-profit sin incurrir en pérdidas innecesarias.
- **[HOLD] ETH-USD** (Confianza: 65%): ETH-USD muestra una ligera pérdida de -0.33%, manteniéndose dentro de un rango de tolerancia aceptable antes de activar el stop-loss estricto. Esperaremos un repunte del momentum técnico de 1 hora para intentar recuperar terreno y buscar rentabilidad.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de SOL-USD y ETH-USD durante este ciclo a pesar del bajo dinamismo, ya que se encuentran cerca de los precios de entrada y sus RSI diarios siguen en zonas de sobreventa profunda (22.6 y 28.3 respectivamente). Si en las próximas horas no se observa un incremento en el volumen y una ruptura del rsi_1h por encima de 50, procederemos a liquidarlas para buscar mayor volatilidad. Mantendremos una reserva de efectivo para reaccionar ante cualquier cambio abrupto en los criptoactivos."
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
