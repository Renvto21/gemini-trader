# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 12:30:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$12.26 USD** | **$26.45 USD** | **$38.71 USD** | 🔴 **-3.22%** ($-1.29) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $344.08 | $9.94 | 📉 -0.60% | 1d 1h |
| `MSFT` | 0.012146 | $535.17 | $537.29 | $6.53 | 📈 +0.40% | 1h 39m |
| `QQQ` | 0.013791 | $725.09 | $724.08 | $9.99 | 📉 -0.14% | 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo bajista general en los principales índices, con la mayoría de activos cotizando por debajo de su SMA20 en gráfico diario, aunque persisten condiciones de sobreventa extrema en marcos de tiempo de 1 hora (como en NVDA y QQQ). Los mercados tradicionales están abiertos y el efectivo disponible se mantiene en niveles operativos."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 80%): La posición en QQQ fue abierta recientemente aprovechando una sobreventa en 1h; el precio se mantiene estable y esperamos el desarrollo del rebote técnico hacia la zona de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener QQQ y MSFT buscando take-profit entre +2.0% y +3.5% o controlando stop-loss ante ruptura de soportes de corto plazo. Vigilar AAPL y evaluar rotación si se estanca. Mantener liquidez reservada mínima y buscar entradas en criptomonedas o rebotes técnicos extremos si se confirma el momentum."
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
