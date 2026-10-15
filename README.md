# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 10:50:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$10.00 USD** | **$28.38 USD** | **$38.38 USD** | 🔴 **-4.05%** ($-1.62) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $345.18 | $9.97 | 📉 -0.28% | 1d 0h |
| `ETH-USD` | 0.002539 | $2362.71 | $2338.65 | $5.94 | 📉 -1.02% | 9h 40m |
| `SOL-USD` | 0.058789 | $102.06 | $101.61 | $5.97 | 📉 -0.44% | 7h 30m |
| `MSFT` | 0.012146 | $535.17 | $535.17 | $6.50 | 📈 +0.00% | 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo general bajista en los principales índices, con caídas notables en QQQ y NVDA, mientras que las criptomonedas continúan con presión a la baja aunque con baja volatilidad en la última hora. MSFT muestra indicios de soporte técnico interesante con un RSI de 1h extremadamente bajo en sobreventa (14.7) y tendencia diaria alcista, lo que presenta una oportunidad táctica de rebote."

**Operaciones del ciclo:**
- **[BUY] MSFT** (Confianza: 85%): MSFT presenta un RSI de 1h ultra comprimido en sobreventa extrema (14.7) con un cambio positivo de 1h del 0.24% y tendencia diaria alcista sobre la SMA20, cumpliendo con la estrategia de rebote técnico de alta convicción.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener seguimiento estricto sobre AAPL, ETH-USD y SOL-USD para evaluar salidas si pierden soportes o alcanzan take-profit. Planificar la rotación de capital hacia MSFT aprovechando su sobreventa intradiaria en 1h para capturar un rebote técnico rápido. Monitorear de cerca los stop-loss en cripto si el momentum no repunta."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **55** | 🎯 **40.0%** (22W / 19L / 14BE) | 🔴 **$-1.39 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 10:50` | 🟢 BUY | `MSFT` | $6.50 | $535.17 | MSFT presenta un RSI de 1h ultra comprimido en sobreventa extrema (14.7) con un cambio pos... |
| `2026-10-15 10:30` | 🔴 SELL (-0.10$) | `BTC-USD` | $4.88 | $80081.22 | La posición en BTC-USD se acerca al límite de tolerancia de pérdida (-1.91%) y el activo p... |
| `2026-10-15 03:20` | 🟢 BUY | `SOL-USD` | $6.00 | $102.06 | SOL-USD muestra un RSI de 1h en 33.3 saliendo de zonas de compresión bajista, acompañado d... |
| `2026-10-15 01:10` | 🟢 BUY | `ETH-USD` | $6.00 | $2362.71 | ETH-USD presenta un RSI de 1h extremadamente bajo en 23.5 saliendo de sobreventa y un camb... |
| `2026-10-14 23:30` | 🔴 SELL (-0.30$) | `SOL-USD` | $9.70 | $101.32 | La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin ... |

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
