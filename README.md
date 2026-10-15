# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 12:20:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$12.26 USD** | **$26.47 USD** | **$38.73 USD** | 🔴 **-3.17%** ($-1.27) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $343.53 | $9.92 | 📉 -0.76% | 1d 1h |
| `MSFT` | 0.012146 | $535.17 | $538.84 | $6.54 | 📈 +0.69% | 1h 29m |
| `QQQ` | 0.013791 | $725.09 | $725.09 | $10.00 | 📈 +0.00% | 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra señales mixtas pero con claros indicios de rebote técnico en activos tecnológicos y de alto beta. QQQ y NVDA presentan condiciones de sobreventa extrema en RSI de 1 hora acompañadas de un inicio de recuperación en su cambio de la última hora, lo que activa nuestra estrategia de Mean Reversion. Mantenemos una posición sólida en MSFT con ganancias moderadas, mientras que AAPL se mantiene estable. La liquidez disponible permite realizar nuevas entradas tácticas agresivas para capturar el impulso alcista actual."

**Operaciones del ciclo:**
- **[BUY] QQQ** (Confianza: 88%): QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio positivo de 0.69% en la última hora. Es una clara oportunidad de rebote técnico (Mean Reversion) con alta convicción para aprovechar la recuperación del índice tecnológico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener MSFT buscando el objetivo de take-profit entre +2.0% y +3.5% o salida por ruptura de soporte si el RSI de 1h vuelve a caer. Vigilar AAPL por si muestra debilidad y decidir rotación de capital. Aprovechar la liquidez actual para abrir posición en QQQ y/o NVDA capitalizando su rebote por sobreventa."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **57** | 🎯 **42.1%** (24W / 19L / 14BE) | 🔴 **$-1.12 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |
| `2026-10-15 12:10` | 🔴 SELL (+0.14$) | `ETH-USD` | $6.14 | $2417.73 | ETH-USD ha alcanzado un rendimiento del +2.33%, cumpliendo con el rango establecido para l... |
| `2026-10-15 11:50` | 🔴 SELL (+0.13$) | `SOL-USD` | $6.13 | $104.21 | SOL-USD ha alcanzado un rendimiento de +2.11%, cumpliendo con la regla de toma rápida de g... |
| `2026-10-15 10:50` | 🟢 BUY | `MSFT` | $6.50 | $535.17 | MSFT presenta un RSI de 1h ultra comprimido en sobreventa extrema (14.7) con un cambio pos... |
| `2026-10-15 10:30` | 🔴 SELL (-0.10$) | `BTC-USD` | $4.88 | $80081.22 | La posición en BTC-USD se acerca al límite de tolerancia de pérdida (-1.91%) y el activo p... |

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
