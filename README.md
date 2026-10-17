# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 12:30:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.96 USD** | **$38.43 USD** | 🔴 **-3.92%** ($-1.57) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.91 | $10.00 | 📉 -0.03% | 2h 10m |
| `ETH-USD` | 0.004126 | $2423.75 | $2414.12 | $9.96 | 📉 -0.40% | 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario tradicional (Wall Street) se encuentra cerrado, por lo que toda la actividad se concentra exclusivamente en los activos cripto disponibles 24/7. Tanto SOL-USD como ETH-USD muestran consolidación lateral tras sus recientes aperturas, con ligeras variaciones negativas de corto plazo (-0.43% y -0.28% en la última hora) pero manteniendo un fuerte soporte potencial gracias a sus RSI diarios en niveles de sobreventa profunda (28.2 y 22.5). El momentum alcista inmediato aún no se dispara, por lo que la estrategia dicta mantener y vigilar de cerca."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD lleva poco tiempo abierta (2h 10m) y presenta una pérdida marginal (-0.03%). El RSI diario de 22.5 respalda la tesis de sobreventa macro, por lo que mantenemos la posición esperando un rebote que dispare el RSI de 1 hora hacia zona de sobrecompra.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD se encuentra estable con una pérdida no realizada mínima del -0.4%. Su RSI diario en 28.2 indica un atractivo soporte por rebote técnico. Daremos tiempo a que el activo desarrolle momentum alcista en las próximas horas.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones de SOL-USD y ETH-USD durante este ciclo ya que llevan poco tiempo abiertas y sus caídas actuales son mínimas (-0.03% y -0.4%). El plan táctico para el próximo ciclo es monitorear el RSI de 1 hora: si supera los 70 puntos o el rendimiento alcanza el rango de +2.0% a +3.5%, ejecutaremos un take-profit total o parcial. Si alguna posición rompe a la baja superando el límite de -2.0%, aplicaremos el stop-loss estricto para proteger el capital."
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
