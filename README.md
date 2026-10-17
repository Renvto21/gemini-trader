# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 15:00:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.89 USD** | **$38.36 USD** | 🔴 **-4.09%** ($-1.64) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.37 | $9.95 | 📉 -0.55% | 4h 40m |
| `ETH-USD` | 0.004126 | $2423.75 | $2409.58 | $9.94 | 📉 -0.58% | 3h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "Los mercados tradicionales se encuentran cerrados, por lo que la liquidez y las operaciones activas se concentran exclusivamente en el mercado de criptomonedas (24/7). Tanto SOL-USD como ETH-USD muestran consolidación lateral con ligeros cambios positivos recientes en 1 hora, pero se mantienen operando dentro de una tendencia bajista de mayor temporalidad. Mantenemos la paciencia mientras los indicadores técnicos digieren la sobreventa diaria."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 65%): La posición mantiene un comportamiento técnico neutral-positivo de corto plazo con un cambio de 1h positivo (0.03%) y un RSI de 1h en recuperación (32.1). No ha alcanzado el stop-loss de -2.0% ni el objetivo de take-profit, por lo que continuamos manteniendo para permitir que se desarrolle el rebote.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Las posiciones en SOL-USD y ETH-USD se mantienen estables con pérdidas mínimas de -0.55% y -0.58%, respectivamente. El tiempo abierto aún es moderado (menos de 5 horas), por lo que no rotaremos el capital todavía. Monitorearemos el RSI de 1 hora buscando la aceleración hacia la zona de +2.0% o +3.5% para tomar beneficios, o ejecutaremos un stop-loss estricto en -2.0% si el impulso bajista retoma fuerza."
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
