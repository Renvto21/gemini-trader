# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 13:50:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.57 USD** | **$20.05 USD** | **$38.62 USD** | 🔴 **-3.46%** ($-1.38) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $720.67 | $10.02 | 📈 +0.24% | 3h 10m |
| `ETH-USD` | 0.004178 | $2393.62 | $2400.09 | $10.03 | 📈 +0.27% | 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra mayoritariamente lateral con sesgo bajista en el marco diario, pero con oportunidades de rebote técnico en activos específicos de cripto y tecnología que muestran ligera recuperación intradiaria. Las posiciones abiertas en QQQ y ETH-USD muestran ganancias menores que aún no alcanzan el objetivo de take-profit del +2.0%, por lo que se mantienen bajo estrecha vigilancia."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 70%): La posición en QQQ muestra una ganancia leve del +0.24% con un holding time de poco más de 3 horas. El RSI de 1h se encuentra neutral (45.1) y no ha alcanzado el objetivo de take-profit, por lo que se mantiene la posición.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD presenta un comportamiento estable con una ganancia del +0.27% y un cambio de 1h positivo (+0.35%). Esperaremos a que se acerque a la zona de sobrecompra o al objetivo de take-profit para asegurar beneficios.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones de QQQ y ETH-USD mientras no alcancen la zona de take-profit (+2.0% a +3.5%) o activen el stop-loss en -2.0%. Monitorear de cerca el RSI de 1 hora y el momentum de ETH-USD para asegurar ganancias rápidamente y rotar capital si se estanca."
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
