# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 12:10:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.26 USD** | **$16.50 USD** | **$38.76 USD** | 🔴 **-3.10%** ($-1.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $344.81 | $9.96 | 📉 -0.39% | 1d 1h |
| `MSFT` | 0.012146 | $535.17 | $538.36 | $6.54 | 📈 +0.60% | 1h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra oportunidades de rebote técnico en activos tecnológicos y criptomonedas. ETH-USD ha alcanzado un rendimiento de +2.33%, cumpliendo con la regla de toma rápida de ganancias en el rango objetivo de +2.0% a +3.5%. QQQ y NVDA presentan condiciones de sobreventa extrema en 1h con indicios tempranos de reversión, mientras que AAPL se mantiene estable."

**Operaciones del ciclo:**
- **[SELL] ETH-USD** (Confianza: 90%): ETH-USD ha alcanzado un rendimiento del +2.33%, cumpliendo con el rango establecido para la toma rápida de ganancias (Take-Profit entre +2.0% y +3.5%) para asegurar efectivo y rotar capital.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Asegurar la toma de ganancias de ETH-USD para liberar liquidez. Vigilar de cerca a QQQ y NVDA para una potencial entrada en cuanto confirmen la aceleración del impulso alcista desde sus niveles actuales de sobreventa. Mantener la disciplina con el stop-loss y la reserva mínima de efectivo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **57** | 🎯 **42.1%** (24W / 19L / 14BE) | 🔴 **$-1.12 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 12:10` | 🔴 SELL (+0.14$) | `ETH-USD` | $6.14 | $2417.73 | ETH-USD ha alcanzado un rendimiento del +2.33%, cumpliendo con el rango establecido para l... |
| `2026-10-15 11:50` | 🔴 SELL (+0.13$) | `SOL-USD` | $6.13 | $104.21 | SOL-USD ha alcanzado un rendimiento de +2.11%, cumpliendo con la regla de toma rápida de g... |
| `2026-10-15 10:50` | 🟢 BUY | `MSFT` | $6.50 | $535.17 | MSFT presenta un RSI de 1h ultra comprimido en sobreventa extrema (14.7) con un cambio pos... |
| `2026-10-15 10:30` | 🔴 SELL (-0.10$) | `BTC-USD` | $4.88 | $80081.22 | La posición en BTC-USD se acerca al límite de tolerancia de pérdida (-1.91%) y el activo p... |
| `2026-10-15 03:20` | 🟢 BUY | `SOL-USD` | $6.00 | $102.06 | SOL-USD muestra un RSI de 1h en 33.3 saliendo de zonas de compresión bajista, acompañado d... |

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
