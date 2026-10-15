# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 07:40:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.89 USD** | **$38.50 USD** | 🔴 **-3.74%** ($-1.50) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 20h 50m |
| `BTC-USD` | 0.000061 | $81640.68 | $81039.80 | $4.96 | 📉 -0.74% | 10h 30m |
| `ETH-USD` | 0.002539 | $2362.71 | $2366.54 | $6.01 | 📈 +0.16% | 6h 30m |
| `SOL-USD` | 0.058789 | $102.06 | $102.26 | $6.01 | 📈 +0.20% | 4h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto 24/7 con una ligera consolidación bajista en el corto plazo (cambios de 1h negativos en BTC, ETH y SOL), mientras que los mercados tradicionales permanecen cerrados. Las posiciones en ETH-USD y SOL-USD muestran ligeras ganancias marginales pero el momentum de 1h se está enfriando. Mantendremos la disciplina táctica sin forzar salidas anticipadas ya que no han alcanzado el take-profit de +2% a +3.5% ni han roto el stop-loss de -2.0%."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): La posición mantiene una ganancia leve de 0.16% tras haber entrado por rebote técnico. Aunque el cambio de 1h es ligeramente negativo (-0.25%), el RSI diario está en niveles de sobreventa profunda (25.3), por lo que debemos darle espacio para buscar el objetivo de take-profit entre +2.0% y +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca ETH-USD y SOL-USD para capturar un take-profit si el RSI de 1h rebota hacia la zona de sobrecompra (>70) o si alcanzan el rango objetivo de +2.0% a +3.5%. Proteger el capital manteniendo el stop-loss estricto a -2.0%. Esperar la apertura de los mercados tradicionales para evaluar la rotación o salida de AAPL si pierde tracción."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **54** | 🎯 **40.7%** (22W / 18L / 14BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 03:20` | 🟢 BUY | `SOL-USD` | $6.00 | $102.06 | SOL-USD muestra un RSI de 1h en 33.3 saliendo de zonas de compresión bajista, acompañado d... |
| `2026-10-15 01:10` | 🟢 BUY | `ETH-USD` | $6.00 | $2362.71 | ETH-USD presenta un RSI de 1h extremadamente bajo en 23.5 saliendo de sobreventa y un camb... |
| `2026-10-14 23:30` | 🔴 SELL (-0.30$) | `SOL-USD` | $9.70 | $101.32 | La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin ... |
| `2026-10-14 23:30` | 🔴 SELL (-0.32$) | `ETH-USD` | $9.68 | $2340.86 | 🚨 STOP-LOSS AUTOMÁTICO (CIRCUIT BREAKER): Pérdida de -3.20% superó el límite de seguridad ... |
| `2026-10-14 21:10` | 🟢 BUY | `BTC-USD` | $5.00 | $81640.68 | BTC-USD presenta un RSI de 1h en 24.9 (sobreventa extrema) y liquidez disponible suficient... |

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
