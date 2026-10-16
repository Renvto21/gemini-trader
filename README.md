# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 21:30:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.17 USD** | **$24.68 USD** | **$38.85 USD** | 🔴 **-2.88%** ($-1.15) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $533.69 | $6.48 | 📉 -0.28% | 10h 40m |
| `QQQ` | 0.013791 | $725.09 | $728.95 | $10.05 | 📈 +0.53% | 9h 10m |
| `NVDA` | 0.036812 | $217.32 | $221.30 | $8.15 | 📈 +1.83% | 8h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado bursátil tradicional se encuentra actualmente CERRADO, manteniendo congelados los precios de activos clave como NVDA, QQQ y MSFT. Por otro lado, las criptomonedas operan 24/7 con un ligero sesgo positivo y rebotes técnicos moderados, destacando SOL-USD y ETH-USD con RSI de 1h tocando zonas de sobrecompra (>70). Dado que nuestras posiciones principales en acciones están cerradas y NVDA acumula una ganancia de +1.83% cerca de la zona objetivo, debemos esperar la reapertura de Wall Street para asegurar beneficios, mientras mantenemos la liquidez intacta."

**Operaciones del ciclo:**
- **[HOLD] NVDA** (Confianza: 80%): NVDA se encuentra en un mercado cerrado con una ganancia actual de +1.83%, muy cerca de nuestra zona objetivo de take-profit (+2.0% a +3.5%). Mantenemos la posición a la espera de la apertura del mercado para asegurar ganancias de manera óptima.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear la apertura de Wall Street para asegurar ganancias en NVDA si cruza el umbral del +2.0% o muestra sobrecompra. Mantener MSFT y QQQ evaluando su comportamiento inicial. Conservar la liquidez actual en efectivo para reaccionar ante cualquier volatilidad en la apertura o buscar oportunidades de rotación hacia activos con mayor momentum."
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
