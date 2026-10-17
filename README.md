# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 11:00:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$28.48 USD** | **$10.00 USD** | **$38.47 USD** | 🔴 **-3.82%** ($-1.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.91 | $10.00 | 📉 -0.03% | 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra completamente cerrado, por lo que toda la actividad se concentra exclusivamente en el mercado cripto (24/7). SOL-USD muestra un holding time corto de 40 minutos con un PnL casi plano (-0.03%), un RSI de 1 hora recuperándose a 44.2 y un cambio de 1h positivo (+0.08%), manteniendo intacta nuestra tesis de rebote desde niveles de sobreventa diaria extrema (RSI diario en 22.5). ETH-USD también mantiene condiciones atractivas con RSI diario en 28.6. Continuamos enfocados en la disciplina táctica y la paciencia para capturar el take-profit en SOL-USD."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición en SOL-USD lleva solo 40 minutos abierta con un rendimiento plano (-0.03%). El RSI de 1 hora se sitúa en 44.2 con un cambio horario positivo del 0.08%, lo que indica que el rebote técnico desde la sobreventa diaria (RSI 22.5) sigue en desarrollo. Mantenemos la posición a la espera de alcanzar el objetivo de take-profit entre +2.0% y +3.5% o una sobrecompra en 1H.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos la posición actual en SOL-USD ya que lleva poco tiempo abierta (40m) y su comportamiento es estable. Establecemos nuestro objetivo de salida (take-profit) entre +2.0% y +3.5% o cuando el RSI de 1 hora supere los 70 puntos. El stop-loss estricto se mantiene en -2.0% para proteger el capital. Si el impulso se agota sin alcanzar el objetivo, consideraremos rotar hacia ETH-USD en los siguientes ciclos."
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
