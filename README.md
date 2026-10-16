# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 23:40:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.17 USD** | **$24.59 USD** | **$38.76 USD** | 🔴 **-3.11%** ($-1.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 12h 49m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 11h 19m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 10h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario de Wall Street se encuentra actualmente CERRADO, manteniendo los precios de MSFT, QQQ y NVDA congelados. Por su parte, los mercados de criptomonedas (BTC-USD, ETH-USD, SOL-USD) están ABIERTOS 24/7 mostrando un sesgo alcista de corto plazo con indicadores RSI de 1 hora en zona de sobrecompra, recuperándose de caídas semanales previas pero operando aún bajo la SMA20 en el gráfico diario."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 75%): La posición en MSFT se mantiene con una ganancia actual de +0.8%. El mercado está cerrado, por lo que mantendremos la posición operativa a la espera de la apertura para buscar take-profit si alcanza el rango del 2.0% al 3.5%.
- **[HOLD] QQQ** (Confianza: 75%): QQQ se encuentra con mercado cerrado registrando una leve ganancia de +0.4%. Mantenemos la posición a la espera de que Wall Street abra para capturar el rebote técnico desde la sobreventa.
- **[HOLD] NVDA** (Confianza: 70%): NVDA muestra un PnL casi plano (-0.04%) con mercado cerrado. El RSI diario se mantiene estable y esperaremos la sesión regular para definir si rompemos el soporte o ejecutamos la ganancia.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Dado que los mercados de acciones están cerrados, mantendré las posiciones de MSFT, QQQ y NVDA hasta la apertura de Wall Street, vigilando estrictamente el objetivo de take-profit en el rango de +2.0% a +3.5% o el stop-loss a -2.0%. En cuanto al mercado cripto, ETH y SOL se encuentran con RSI de 1h en sobrecompra (>70), por lo que no es momento óptimo de entrada para rebotes; esperaré una corrección intradiaria o la apertura del mercado tradicional para evaluar rotaciones de capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **58** | 🎯 **41.4%** (24W / 20L / 14BE) | 🔴 **$-1.22 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |
| `2026-10-15 12:10` | 🔴 SELL (+0.14$) | `ETH-USD` | $6.14 | $2417.73 | ETH-USD ha alcanzado un rendimiento del +2.33%, cumpliendo con el rango establecido para l... |
| `2026-10-15 11:50` | 🔴 SELL (+0.13$) | `SOL-USD` | $6.13 | $104.21 | SOL-USD ha alcanzado un rendimiento de +2.11%, cumpliendo con la regla de toma rápida de g... |

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
