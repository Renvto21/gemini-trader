# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 16:10:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.57 USD** | **$20.01 USD** | **$38.58 USD** | 🔴 **-3.55%** ($-1.42) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $719.50 | $10.01 | 📈 +0.08% | 5h 29m |
| `ETH-USD` | 0.004178 | $2393.62 | $2394.94 | $10.01 | 📈 +0.06% | 3h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra mayormente plano con sesgo bajista en la tendencia general bajo las SMA20, aunque con indicios de consolidación en criptomonedas y tecnología. Las posiciones en QQQ y ETH-USD muestran ganancias mínimas estancadas (+0.08% y +0.06%) tras varias horas de holding, sin la fuerza de momentum esperada en el corto plazo. El efectivo disponible es de $18.57 USD, permitiendo flexibilidad táctica si surge un catalizador o cambio claro en el RSI de 1 hora."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 50%): La posición lleva más de 5 horas abierta con una ganancia marginal del +0.08%. Se mantiene temporalmente para buscar el objetivo de take-profit del +2.0%, vigilando el soporte y el stop-loss.
- **[HOLD] ETH-USD** (Confianza: 50%): Posición abierta con ligera ganancia (+0.06%). El RSI de 1 hora se mantiene en 33.3; esperamos el impulso de corto plazo hacia la zona de sobrecompra para asegurar utilidades.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de QQQ y ETH-USD un ciclo más monitoreando estrictamente el stop-loss del -2.0% y buscando el take-profit entre +2.0% y +3.5%. SOL-USD sigue mostrando un RSI diario extremadamente bajo (19.1) y un RSI de 1 hora en 30.3; esperaremos a que el cambio de 1h se torne positivo para ejecutar una compra agresiva por rebote de sobreventa. Mantendremos el colchón de liquidez mínimo."
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
