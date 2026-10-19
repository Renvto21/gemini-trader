# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 16:20:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.57 USD** | **$20.03 USD** | **$38.60 USD** | 🔴 **-3.50%** ($-1.40) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $720.22 | $10.02 | 📈 +0.18% | 5h 40m |
| `ETH-USD` | 0.004178 | $2393.62 | $2397.12 | $10.01 | 📈 +0.15% | 3h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo general bajista en los principales índices y criptomonedas, encontrándose por debajo de sus medias móviles de 20 períodos, pero con señales incipientes de sobreventa extrema en ciertos activos digitales como SOL-USD y ETH-USD. Las acciones tecnológicas como QQQ y MSFT se mantienen estables pero sin un momentum claro de continuación. El enfoque se mantiene en cazar rebotes técnicos estrictos de corto plazo y asegurar ganancias rápidas."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 70%): QQQ se encuentra con una ganancia marginal del +0.18% tras 5 horas abierto. Mantiene un RSI de 1 hora en 40.0 y un cambio positivo de 1h del +0.23%. Se mantiene la posición buscando alcanzar el objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD se mantiene estable con una ganancia de +0.15% y un RSI de 1 hora en 34.1, cerca de la zona de sobreventa. Se conserva la posición a la espera de un impulso alcista que active la toma de beneficios rápida.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones de QQQ y ETH-USD un ciclo más monitoreando el stop-loss en -2.0% y buscando un take-profit agresivo entre +2.0% y +3.5%. SOL-USD mantiene un RSI diario extremadamente bajo (19.3) y un RSI de 1 hora en 32.4; se evaluará una entrada en cuanto su cambio de 1h vire a terreno positivo para aprovechar el rebote por sobreventa. Conservaremos la liquidez mínima de reserva."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |
| `2026-10-19 01:50` | 🔴 SELL (+0.09$) | `ETH-USD` | $8.09 | $2428.97 | ETH-USD registra una ganancia acumulada y su RSI de 1 hora ha alcanzado 68.3, acercándose ... |
| `2026-10-19 01:00` | 🔴 SELL (-0.00$) | `SOL-USD` | $8.00 | $105.08 | SOL-USD ha entrado en sobrecompra con un RSI de 1 hora en 72.7, cumpliendo estrictamente c... |
| `2026-10-18 23:20` | 🟢 BUY | `SOL-USD` | $8.00 | $105.11 | SOL-USD presenta un RSI diario en 21.8 (sobreventa extrema) y un momentum de 24 horas alci... |

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
