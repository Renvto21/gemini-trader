# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 21:00:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.17 USD** | **$24.68 USD** | **$38.85 USD** | 🔴 **-2.88%** ($-1.15) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $533.69 | $6.48 | 📉 -0.28% | 10h 10m |
| `QQQ` | 0.013791 | $725.09 | $728.95 | $10.05 | 📈 +0.53% | 8h 40m |
| `NVDA` | 0.036812 | $217.32 | $221.30 | $8.15 | 📈 +1.83% | 8h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional (Wall Street) se encuentra actualmente CERRADO, por lo que los activos tecnológicos e índices como MSFT, QQQ, NVDA y SPY muestran precios congelados y no permiten operar. Por otro lado, los mercados de criptomonedas operan 24/7 y muestran un tono neutral a ligeramente alcista en el corto plazo, con SOL y ETH presentando un RSI de 1h elevado (cercano a sobrecompra alrededor de 70) pero con RSI diario en zona de sobreventa, lo que indica que aún no ofrecen el punto de entrada ideal para un rebote inminente. Mantendremos las posiciones actuales de NVDA, QQQ y MSFT hasta la apertura del mercado bursátil para buscar nuestros objetivos de take-profit."

**Operaciones del ciclo:**
- **[HOLD] NVDA** (Confianza: 80%): La posición en NVDA muestra una ganancia actual del +1.83%, acercándose al rango objetivo de take-profit (+2.0% a +3.5%). Dado que el mercado está cerrado, se mantiene la posición esperando la apertura para asegurar beneficios.
- **[HOLD] QQQ** (Confianza: 75%): QQQ se encuentra con una ganancia marginal del +0.53% tras el rebote técnico. Con el mercado cerrado, se mantiene a la espera de mayor tracción alcista en la próxima sesión.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones vigentes en NVDA, QQQ y MSFT durante el cierre del mercado bursátil, esperando la apertura de Wall Street para asegurar beneficios en cuanto alcancen el rango de take-profit entre +2.0% y +3.5%, o para aplicar stop-loss en caso de movimientos adversos. La liquidez de $14.17 USD se mantendrá reservada a la espera de una corrección intradiaria más clara en Cripto (SOL-USD o ETH-USD) o hasta la apertura de los mercados tradicionales para buscar nuevas oportunidades de momentum."
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
