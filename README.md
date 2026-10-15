# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 11:50:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$16.12 USD** | **$22.52 USD** | **$38.65 USD** | 🔴 **-3.38%** ($-1.35) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $344.57 | $9.95 | 📉 -0.46% | 1d 1h |
| `ETH-USD` | 0.002539 | $2362.71 | $2384.28 | $6.05 | 📈 +0.91% | 10h 40m |
| `MSFT` | 0.012146 | $535.17 | $536.41 | $6.52 | 📈 +0.23% | 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un impulso alcista interesante de corto plazo en criptomonedas (SOL-USD y ETH-USD) tras activar los rebotes esperados. SOL-USD ha alcanzado un rendimiento de +2.11%, tocando el rango objetivo de toma de ganancias. En cuanto a Wall Street, los índices y acciones como MSFT y AAPL se mantienen estables pero con baja volatilidad intradiaria, permitiendo retener posiciones mientras se busca rotar capital hacia activos de mayor momentum dinámico."

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 90%): SOL-USD ha alcanzado un rendimiento de +2.11%, cumpliendo con la regla de toma rápida de ganancias (take-profit entre +2.0% y +3.5%). Procedo a vender la posición completa para asegurar el capital y rotar liquidez.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Se ha ejecutado la toma de ganancias en SOL-USD tras alcanzar el objetivo de +2.11% para asegurar liquidez. Mantener las posiciones en AAPL, ETH-USD y MSFT vigilando los stop-loss estrictos del -2.0%. Estar atentos a QQQ y NVDA para una posible entrada si confirman salida de sobreventa extrema en gráficos de 1 hora durante la siguiente sesión."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **56** | 🎯 **41.1%** (23W / 19L / 14BE) | 🔴 **$-1.26 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 11:50` | 🔴 SELL (+0.13$) | `SOL-USD` | $6.13 | $104.21 | SOL-USD ha alcanzado un rendimiento de +2.11%, cumpliendo con la regla de toma rápida de g... |
| `2026-10-15 10:50` | 🟢 BUY | `MSFT` | $6.50 | $535.17 | MSFT presenta un RSI de 1h ultra comprimido en sobreventa extrema (14.7) con un cambio pos... |
| `2026-10-15 10:30` | 🔴 SELL (-0.10$) | `BTC-USD` | $4.88 | $80081.22 | La posición en BTC-USD se acerca al límite de tolerancia de pérdida (-1.91%) y el activo p... |
| `2026-10-15 03:20` | 🟢 BUY | `SOL-USD` | $6.00 | $102.06 | SOL-USD muestra un RSI de 1h en 33.3 saliendo de zonas de compresión bajista, acompañado d... |
| `2026-10-15 01:10` | 🟢 BUY | `ETH-USD` | $6.00 | $2362.71 | ETH-USD presenta un RSI de 1h extremadamente bajo en 23.5 saliendo de sobreventa y un camb... |

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
