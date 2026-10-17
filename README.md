# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 18:30:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.79 USD** | **$38.27 USD** | 🔴 **-4.33%** ($-1.73) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $102.85 | $9.90 | 📉 -1.05% | 8h 10m |
| `ETH-USD` | 0.004126 | $2423.75 | $2398.95 | $9.90 | 📉 -1.02% | 6h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado durante el fin de semana, por lo que la operativa se concentra exclusivamente en criptomonedas (ABIERTO 24/7). Las criptomonedas principales (SOL-USD, ETH-USD y BTC-USD) muestran una ligera presión a la baja en el corto plazo con caídas en el cambio de 1 hora y 24 horas, situándose en tendencias bajistas bajo la SMA20. Sin embargo, nuestros activos en cartera (SOL-USD y ETH-USD) se mantienen relativamente estables con pérdidas controladas (-1.05% y -1.02%) tras varias horas de tenencia. No se ha alcanzado aún el stop-loss estricto del -2.0% ni el rebote esperado para tomar ganancias, por lo que decidimos mantener la postura actual y seguir vigilando de cerca."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición en SOL-USD muestra una pérdida moderada del -1.05% tras 8 horas abierta. El RSI de 1 hora está en 28.9 (sobreventa de corto plazo) y el RSI diario en 21.7, manteniendo la expectativa de un rebote técnico inminente sin haber tocado el stop-loss del -2.0%.
- **[HOLD] ETH-USD** (Confianza: 70%): La posición en ETH-USD acumula una pérdida del -1.02% con un tiempo abierto de casi 7 horas. El RSI de 1 hora se sitúa en 31.1 y el diario en 27.5, manteniendo intacto el soporte macro y la posibilidad de un repunte a corto plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos SOL-USD y ETH-USD un ciclo más ya que las pérdidas se mantienen acotadas alrededor del -1.0% y no han tocado el stop-loss de -2.0%. El RSI de 1 hora se encuentra en niveles cercanos a sobreventa (28.9 para SOL y 31.1 para ETH), lo que podría anticipar un rebote técnico inminente. Si en el próximo ciclo las pérdidas superan el -1.5% o el impulso bajista continúa sin respetarse el soporte, procederemos a vender para cortar pérdidas y proteger el capital. Take-profit objetivo entre +2.0% y +3.5%."
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
