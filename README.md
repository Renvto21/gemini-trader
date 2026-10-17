# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 14:00:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.82 USD** | **$38.29 USD** | 🔴 **-4.27%** ($-1.71) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.03 | $9.91 | 📉 -0.88% | 3h 40m |
| `ETH-USD` | 0.004126 | $2423.75 | $2400.31 | $9.90 | 📉 -0.97% | 2h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado por lo que el foco se centra exclusivamente en criptomonedas. Los activos digitales como SOL-USD y ETH-USD muestran presiones bajistas y caídas recientes, con indicadores técnicos en niveles de sobreventa pero sin un impulso claro de rebote intradiario en la última hora. El portafolio actual se mantiene con pérdidas menores (-0.88% en SOL y -0.97% en ETH) pero dentro de los márgenes tolerables de stop-loss, esperando el catalizador de volumen o un cambio en el RSI de 1 hora."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición en SOL-USD acumula una pérdida de -0.88%, manteniéndose por encima del límite de stop-loss de -2.0%. Aunque el momentum de 1 hora es débil, el RSI diario está profundamente en sobreventa (21.8) y se espera una reversión a la media en cuanto el mercado active compras.
- **[HOLD] ETH-USD** (Confianza: 70%): La posición en ETH-USD registra una pérdida leve de -0.97%, respetando el umbral defensivo. El activo está consolidando en niveles de soporte diario y se mantiene la expectativa de capturar el rebote técnico en las siguientes horas.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones abiertas en SOL-USD y ETH-USD durante este ciclo actual mientras no rompan el stop-loss estricto del -2.0%. Si el RSI de 1 hora rompe al alza con fuerza superando los 50 puntos o se acerca a la zona de sobrecompra (>70), ejecutaremos take-profit. Si por el contrario el precio perfora los soportes y las pérdidas superan el -2.0%, procederemos a vender inmediatamente para proteger el capital y buscar liquidez."
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
