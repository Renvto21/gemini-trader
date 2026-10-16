# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 13:10:52`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$17.07 USD** | **$21.35 USD** | **$38.41 USD** | 🔴 **-3.96%** ($-1.59) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $528.65 | $6.42 | 📉 -1.22% | 1d 2h |
| `NVDA` | 0.036812 | $217.32 | $217.02 | $7.99 | 📉 -0.14% | 1d 0h |
| `ETH-USD` | 0.002855 | $2451.90 | $2430.58 | $6.94 | 📉 -0.87% | 8h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo bajista general con la mayoría de los activos cotizando bajo sus medias móviles de 20 períodos, aunque con indicios de sobreventa en gráficos de 1 hora que podrían propiciar rebotes técnicos de corto plazo. Wall Street y los mercados de criptomonedas se encuentran abiertos, permitiendo operar tanto acciones tecnológicas como criptoactivos 24/7."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 60%): La posición en MSFT presenta una pérdida moderada de -1.22% tras 1 día de tenencia, manteniendo su tendencia alcista diaria sobre la SMA20. Se mantiene a la espera de un rebote técnico que permita cerrar en positivo o alcanzar el take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener monitoreo estricto sobre las posiciones abiertas (MSFT, NVDA, ETH-USD). Ejecutar stop-loss preventivo si alguna posición supera el -2.0% de pérdida o si el momentum se deteriora. Prepararse para rotar capital hacia oportunidades de alta convicción con rsi_1h cruzando al alza desde niveles de sobreventa."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **60** | 🎯 **40.0%** (24W / 22L / 14BE) | 🔴 **$-1.32 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 12:50` | 🔴 SELL (-0.06$) | `SOL-USD` | $2.94 | $104.34 | SOL-USD lleva varias horas abierto sin generar el rebote esperado, acumulando una pérdida ... |
| `2026-10-16 10:50` | 🔴 SELL (-0.04$) | `QQQ` | $9.95 | $721.83 | QQQ lleva más de 22 horas abierto operando bajo la SMA20 con un RSI de 1 hora en 30.2 y un... |
| `2026-10-16 05:10` | 🟢 BUY | `SOL-USD` | $3.00 | $106.33 | SOL-USD presenta un RSI diario en zona de sobreventa extrema (29.0) y un cambio positivo e... |
| `2026-10-16 04:30` | 🟢 BUY | `ETH-USD` | $7.00 | $2451.90 | Aprovechamos la liquidez disponible sobre la reserva mínima ($14.17 vs $4.00 requeridos) p... |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |

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
