# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 04:40:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$38.48 USD** | **$0.00 USD** | **$38.48 USD** | 🔴 **-3.81%** ($-1.52) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *(Ninguna posición abierta - 100% en efectivo)* | - | - | - | - | - | - |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "Los mercados tradicionales se encuentran cerrados, por lo que la liquidez y la operativa se centran exclusivamente en el mercado de criptomonedas (24/7). Observamos que ETH-USD y SOL-USD se encuentran actualmente en zonas de sobrecompra en el corto plazo (RSI de 1 hora por encima de 70), lo cual confirma que el rebote anterior fue exitoso y se debieron tomar ganancias. Bitcoin (BTC-USD) muestra un RSI de 1 hora de 67.9, acercándose también a niveles de resistencia a corto plazo sin ofrecer un punto de entrada claro por retroceso en este momento. Dado que mantenemos una saludable reserva de efectivo y los activos disponibles muestran señales de sobrecompra tras recientes rebotes, la estrategia actual exige paciencia para evitar compras en máximos locales y esperar una corrección intrahabituaria."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD presenta un RSI de 1 hora en 74.4, encontrándose en territorio de sobrecompra tras el reciente rebote. No es momento de comprar; mantengo liquidez en espera de un retroceso intradiario hacia zonas de soporte para cazar una nueva oportunidad de mean reversion.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantengo una sólida reserva de efectivo de $38.48 USD. Los activos cripto abiertos (ETH-USD, SOL-USD, BTC-USD) se encuentran en zonas de sobrecompra técnica a 1 hora (RSI > 70 o muy cercano), descartando entradas inmediatas. Mi plan táctico para los siguientes ciclos es vigilar de cerca una corrección o retroceso intrahorario en ETH-USD o BTC-USD que devuelva el RSI de 1 hora a niveles inferiores a 35-40, permitiendo reingresar con una confianza superior al 85% y cumpliendo estrictamente con la reserva de efectivo mínima de $4.00 USD."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **65** | 🎯 **40.0%** (26W / 25L / 14BE) | 🔴 **$-1.41 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 04:30` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $104.94 | SOL-USD ha alcanzado un RSI de 1 hora de 70.4, entrando en zona de sobrecompra, y acumula ... |
| `2026-10-17 04:00` | 🔴 SELL (+0.07$) | `ETH-USD` | $10.07 | $2429.64 | ETH-USD ha alcanzado un RSI de 1 hora de 73.3, entrando en zona de sobrecompra. Siguiendo ... |
| `2026-10-16 16:30` | 🟢 BUY | `ETH-USD` | $10.00 | $2412.98 | ETH-USD muestra un RSI diario en niveles de sobreventa extrema (30.3) y un cambio positivo... |
| `2026-10-16 16:30` | 🔴 SELL (-0.11$) | `MSFT` | $6.39 | $526.18 | MSFT lleva más de 1 día y 5 horas abierto mostrando debilidad persistente y un rendimiento... |
| `2026-10-16 15:01` | 🟢 BUY | `SOL-USD` | $10.00 | $103.71 | SOL-USD presenta un RSI de 1 hora en 34.3 saliendo de la zona de sobreventa extrema, acomp... |

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
