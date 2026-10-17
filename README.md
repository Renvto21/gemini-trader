# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 12:40:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.94 USD** | **$38.41 USD** | 🔴 **-3.96%** ($-1.59) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.81 | $9.99 | 📉 -0.13% | 2h 20m |
| `ETH-USD` | 0.004126 | $2423.75 | $2412.00 | $9.95 | 📉 -0.48% | 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional (Wall Street) se encuentra cerrado, por lo que toda la liquidez y atención se centran en las criptomonedas, que operan 24/7. Las criptomonedas principales como SOL-USD y ETH-USD muestran una consolidación de corto plazo tras las recientes compras en zonas de sobreventa diaria, con variaciones mínimas de 1 hora y un RSI de 1 hora neutral (en torno a 44-46). El sentimiento macro en cripto sigue bajo presión bajista pero con buenos soportes diarios."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD lleva poco tiempo abierta (2h 20m) y su pérdida es insignificante (-0.13%). El RSI de 1 hora se encuentra en 44.6, mostrando estabilidad mientras esperamos el impulso alcista hacia nuestros objetivos de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): La posición en ETH-USD mantiene un comportamiento similar con una leve variación de -0.48% y un RSI de 1 hora en 46.0. No hay señales de ruptura de soporte ni activación de stop-loss, por lo que se mantiene para buscar el rebote esperado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de SOL-USD y ETH-USD ya que se encuentran estables con pérdidas marginales y un tiempo de retención corto. El plan táctico para el próximo ciclo es vigilar de cerca el RSI de 1 hora y el cambio porcentual: si alguna posición alcanza el rango de take-profit de +2.0% a +3.5% o cruza el RSI de sobrecompra (>70), realizaremos beneficios. Si rompen a la baja superando el -2.0%, aplicaremos el stop-loss de inmediato."
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
