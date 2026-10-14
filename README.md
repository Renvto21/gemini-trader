# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 19:00:51`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$9.23 USD** | **$29.93 USD** | **$39.16 USD** | 🔴 **-2.10%** ($-0.84) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 8h 10m |
| `SOL-USD` | 0.095785 | $104.40 | $104.67 | $10.03 | 📈 +0.26% | 2h 30m |
| `ETH-USD` | 0.004135 | $2418.34 | $2418.34 | $10.00 | 📈 +0.00% | 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de acciones tradicionales se encuentra cerrado, limitando la operativa a criptomonedas que operan 24/7. SOL-USD mantiene un comportamiento lateral con un ligero repunte positivo (+0.06% en 1h y RSI de 1h en 34.0), cotizando ligeramente por encima de nuestro precio de entrada con un PnL de +0.26%. ETH-USD muestra un RSI de 1h extremadamente bajo en 22.0 con un cambio de 1h de +0.05%, lo que indica una potencial zona de sobreventa extrema óptima para cazar un rebote técnico inminente usando parte de la liquidez disponible."

**Operaciones del ciclo:**
- **[BUY] ETH-USD** (Confianza: 85%): ETH-USD presenta un RSI de 1h en 22.0 (sobreventa extrema) y un cambio de 1h que comienza a tornarse positivo (+0.05%), cumpliendo con la estrategia agresiva de mean reversion y captura de rebotes técnicos con alta convicción.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra un PnL positivo actual de +0.26% con un RSI de 1h en recuperación (34.0). Se mantiene en cartera a la espera de alcanzar el objetivo de take-profit de +2.0% a +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener SOL-USD en vigilancia estricta buscando la zona de take-profit entre +2.0% y +3.5% o protegiendo con stop-loss si perfora el soporte operativo. Ejecutar compra de ETH-USD aprovechando su RSI de 1h en sobreventa extrema (22.0) y su incipiente giro positivo de corto plazo. Conservar AAPL al estar su mercado cerrado. Asegurar que la reserva de efectivo se mantenga cercana al límite mínimo de $4.00 USD."
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
