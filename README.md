# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 19:10:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$9.23 USD** | **$29.87 USD** | **$39.10 USD** | 🔴 **-2.26%** ($-0.90) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 8h 20m |
| `SOL-USD` | 0.095785 | $104.40 | $104.36 | $10.00 | 📉 -0.04% | 2h 39m |
| `ETH-USD` | 0.004135 | $2418.34 | $2409.81 | $9.96 | 📉 -0.35% | 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario de EE.UU. se encuentra cerrado con la mayoría de activos bajo presión y tendencia bajista de corto plazo. En el ecosistema de criptomonedas (abierto 24/7), tanto SOL-USD como ETH-USD muestran niveles de RSI de 1 hora deprimidos (32.3 y 20.4 respectivamente), manteniendo condiciones de sobreventa que sugieren una potencial consolidación antes de un rebote técnico. Mantendremos las posiciones actuales para permitir su desarrollo, vigilando de cerca los niveles de stop-loss y take-profit."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 65%): SOL-USD se mantiene operando dentro de un rango estrecho con un RSI de 1h en 32.3, consolidando tras la reciente entrada. Se mantiene la posición en busca del rebote técnico hacia la zona de take-profit.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD presenta un RSI de 1h extremadamente bajo en 20.4, reflejando sobreventa profunda. Mantendremos la posición para capturar el esperado rebote de reversión a la media sin sobreexponer el capital.
- **[HOLD] AAPL** (Confianza: 60%): El mercado de AAPL se encuentra cerrado. La posición se mantiene con una pérdida menor de -0.92% a la espera de la apertura para evaluar su comportamiento técnico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones en AAPL, SOL-USD y ETH-USD en vigilancia estricta. Monitorear los niveles de take-profit entre +2.0% y +3.5% para asegurar ganancias y activar stop-loss si alguna posición perfora el límite de -2.0%. La liquidez actual de efectivo se mantiene en $9.23 USD, cumpliendo con la reserva mínima requerida. Esperar la apertura de los mercados tradicionales para evaluar rotaciones adicionales en acciones."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **52** | 🎯 **42.3%** (22W / 16L / 14BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 19:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2418.34 | ETH-USD presenta un RSI de 1h en 22.0 (sobreventa extrema) y un cambio de 1h que comienza ... |
| `2026-10-14 16:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.40 | SOL-USD presenta un RSI de 1h en 30.9 saliendo de la zona de compresión y un cambio positi... |
| `2026-10-14 15:20` | 🔴 SELL (-0.08$) | `SOL-USD` | $9.92 | $103.86 | SOL-USD lleva varias horas sin mostrar el rebote esperado, su RSI de 1h ha caído hasta 25.... |
| `2026-10-14 12:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.70 | SOL-USD presenta un RSI de 1h en 29.2 saliendo de sobreventa extrema y un cambio de 1h pos... |
| `2026-10-14 11:20` | 🔴 SELL (-0.09$) | `BTC-USD` | $5.89 | $81874.95 | BTC-USD lleva más de 14 horas abierto con un PnL negativo persistente (-1.51%) y un RSI de... |

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
