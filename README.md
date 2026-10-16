# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 07:00:51`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.17 USD** | **$34.56 USD** | **$38.73 USD** | 🔴 **-3.17%** ($-1.27) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 20h 10m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 18h 40m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 18h 10m |
| `ETH-USD` | 0.002855 | $2451.90 | $2446.11 | $6.98 | 📉 -0.24% | 2h 29m |
| `SOL-USD` | 0.028214 | $106.33 | $106.03 | $2.99 | 📉 -0.28% | 1h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra actualmente CERRADO, por lo que los precios de las acciones están congelados y no podemos operar en dichos activos según las reglas operativas. En el mercado de criptomonedas (que permanece abierto 24/7), los principales activos como ETH-USD y SOL-USD muestran consolidación tras las recientes entradas, manteniendo un sesgo neutral a bajista en el corto plazo pero respetando los niveles de soporte diario. Mantendremos las posiciones actuales a la espera de la apertura de los mercados tradicionales o de una mayor volatilidad en cripto que active nuestras condiciones de take-profit o stop-loss."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): La posición en ETH-USD lleva poco tiempo abierta (2h 29m) y se encuentra operando dentro de rangos normales con una pérdida mínima (-0.24%). No hay señales de sobrecompra ni se ha alcanzado el stop-loss, por lo que se mantiene para permitir que el rebote técnico se desarrolle.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones actuales en criptomonedas (ETH-USD y SOL-USD) y acciones (MSFT, QQQ, NVDA) mientras el mercado accionario esté cerrado. Vigilar de cerca el comportamiento de ETH-USD y SOL-USD para asegurar beneficios si se acercan al objetivo de +2.0% o cortar pérdidas si rompen soportes. En cuanto abra Wall Street, evaluar la rotación de capital de posiciones estancadas si surge mejor momentum."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **58** | 🎯 **41.4%** (24W / 20L / 14BE) | 🔴 **$-1.22 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 05:10` | 🟢 BUY | `SOL-USD` | $3.00 | $106.33 | SOL-USD presenta un RSI diario en zona de sobreventa extrema (29.0) y un cambio positivo e... |
| `2026-10-16 04:30` | 🟢 BUY | `ETH-USD` | $7.00 | $2451.90 | Aprovechamos la liquidez disponible sobre la reserva mínima ($14.17 vs $4.00 requeridos) p... |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |

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
