# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 12:00:56`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$16.12 USD** | **$22.57 USD** | **$38.69 USD** | 🔴 **-3.27%** ($-1.31) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $344.92 | $9.96 | 📉 -0.36% | 1d 1h |
| `ETH-USD` | 0.002539 | $2362.71 | $2395.71 | $6.08 | 📈 +1.40% | 10h 50m |
| `MSFT` | 0.012146 | $535.17 | $536.76 | $6.52 | 📈 +0.30% | 1h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento mixto con el sector cripto estabilizándose y los índices tradicionales operando en sesgo bajista pero con claras señales de sobreventa en gráficos de 1 hora. QQQ, SPY y NVDA presentan indicadores RSI de 1 hora comprimidos por debajo de 30, lo que abre una ventana excelente para capturar rebotes técnicos por mean reversion. En nuestra cartera actual, ETH-USD se acerca a la zona objetivo con un +1.4% de ganancia, mientras que MSFT y AAPL se mantienen estables con ligeras variaciones."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD registra un PnL positivo de +1.4% y se encamina hacia nuestra zona de toma rápida de ganancias (+2.0% a +3.5%). Mantenemos la posición para capturar el objetivo establecido.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener la vigilancia estricta sobre ETH-USD para asegurar ganancias si alcanza el rango de +2.0% a +3.5%. Monitorear de cerca a QQQ y NVDA para una potencial entrada en cuanto confirmen la reversión alcista desde la sobreventa extrema de 1h. Preservar la liquidez requerida de $4.00 USD y utilizar el efectivo disponible remanente para oportunidades de alto impulso técnico."
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
