# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 21:20:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.17 USD** | **$24.68 USD** | **$38.85 USD** | 🔴 **-2.88%** ($-1.15) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $533.69 | $6.48 | 📉 -0.28% | 10h 29m |
| `QQQ` | 0.013791 | $725.09 | $728.95 | $10.05 | 📈 +0.53% | 9h 0m |
| `NVDA` | 0.036812 | $217.32 | $221.30 | $8.15 | 📈 +1.83% | 8h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado bursátil se encuentra cerrado con precios congelados, por lo que las operaciones se limitan a mantener las posiciones actuales en NVDA, QQQ y MSFT, o buscar entradas tácticas en los activos cripto 24/7. NVDA muestra un excelente rendimiento acumulando +1.83% de ganancia, acercándose a nuestra zona objetivo de toma de beneficios, mientras que QQQ se mantiene positivo en +0.53%. MSFT registra una leve baja de -0.28%. En el ecosistema cripto, ETH-USD y SOL-USD muestran fuertes RSI de 1 hora cercanos a la sobrecompra con tendencias bajistas macro, por lo que priorizamos conservar la liquidez actual y vigilar de cerca la apertura de Wall Street."

**Operaciones del ciclo:**
- **[HOLD] NVDA** (Confianza: 80%): La posición en NVDA acumula un +1.83% de ganancia, cerca de nuestra regla de take-profit (+2.0% a +3.5%). Como el mercado está cerrado, se mantiene la posición para asegurar beneficios en cuanto abra Wall Street.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca a NVDA ya que su ganancia actual está en +1.83%, muy cerca de la zona de take-profit objetivo (+2.0% a +3.5%). Si NVDA o QQQ alcanzan sobrecompra en la apertura del mercado o cruzan el umbral de ganancia deseado, ejecutaremos la venta para asegurar liquidez. Mantendremos la liquidez en efectivo ($14.17) intacta para aprovechar movimientos en la apertura bursátil o posibles correcciones profundas en cripto."
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
