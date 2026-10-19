# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 14:00:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.57 USD** | **$20.04 USD** | **$38.60 USD** | 🔴 **-3.49%** ($-1.40) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $720.00 | $10.02 | 📈 +0.15% | 3h 20m |
| `ETH-USD` | 0.004178 | $2393.62 | $2399.48 | $10.02 | 📈 +0.24% | 1h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra mayoritariamente lateral o con ligeros retrocesos en el corto plazo. Los índices y activos tecnológicos como QQQ y criptomonedas como ETH-USD muestran consolidación tras los recientes intentos de rebote técnico, manteniéndose cerca de los precios de entrada sin alcanzar aún los objetivos de take-profit ni activar los stop-loss."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 75%): La posición lleva pocas horas abierta y se mantiene estable con una pequeña ganancia del +0.15%. Esperamos a que el momentum se reactive hacia la zona de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un comportamiento lateral con una ligera ganancia del +0.24%. Mantenemos la posición para capturar el rebote esperado en el corto plazo sin forzar salidas anticipadas.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en QQQ y ETH-USD mientras se mantengan dentro del rango de tolerancia y no rompan los soportes clave. Vigilar de cerca el RSI de 1 hora para asegurar ganancias si se acercan al objetivo de +2.0% o cortar pérdidas estrictamente si bajan de -2.0%. Preservar liquidez operativa para el próximo ciclo."
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
