# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 21:30:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.23 USD** | **$34.88 USD** | **$39.11 USD** | 🔴 **-2.23%** ($-0.89) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $341.27 | $9.86 | 📉 -1.41% | 10h 40m |
| `SOL-USD` | 0.095785 | $104.40 | $104.36 | $10.00 | 📉 -0.04% | 4h 59m |
| `ETH-USD` | 0.004135 | $2418.34 | $2424.30 | $10.02 | 📈 +0.25% | 2h 29m |
| `BTC-USD` | 0.000061 | $81640.68 | $81647.17 | $5.00 | 📈 +0.01% | 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la actividad se concentra exclusivamente en los criptoactivos (BTC-USD, ETH-USD y SOL-USD), que operan 24/7. Las criptomonedas muestran signos de sobreventa en gráficos de 1 hora pero con intentos incipientes de recuperación en el corto plazo (cambio de 1h positivo). Mantendremos la postura en cripto buscando el rebote técnico y conservaremos AAPL dado que está en mercado cerrado y su caída no ha tocado el stop-loss estricto."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un ligero repunte en el cambio de 1h (+0.49%) tras estar en sobreventa extrema. Mantenemos la posición para capturar el rebote esperado hacia la zona del +2.0%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones actuales en cripto (BTC, ETH, SOL) vigilando que alcancen el objetivo de take-profit entre +2.0% y +3.5%. Proteger AAPL con el stop-loss del -2.0% para cuando abra el mercado de valores. Si ETH o SOL pierden impulso o caen por debajo de los soportes, ejecutar ventas inmediatas para rotar capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **52** | 🎯 **42.3%** (22W / 16L / 14BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 21:10` | 🟢 BUY | `BTC-USD` | $5.00 | $81640.68 | BTC-USD presenta un RSI de 1h en 24.9 (sobreventa extrema) y liquidez disponible suficient... |
| `2026-10-14 19:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2418.34 | ETH-USD presenta un RSI de 1h en 22.0 (sobreventa extrema) y un cambio de 1h que comienza ... |
| `2026-10-14 16:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.40 | SOL-USD presenta un RSI de 1h en 30.9 saliendo de la zona de compresión y un cambio positi... |
| `2026-10-14 15:20` | 🔴 SELL (-0.08$) | `SOL-USD` | $9.92 | $103.86 | SOL-USD lleva varias horas sin mostrar el rebote esperado, su RSI de 1h ha caído hasta 25.... |
| `2026-10-14 12:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.70 | SOL-USD presenta un RSI de 1h en 29.2 saliendo de sobreventa extrema y un cambio de 1h pos... |

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
