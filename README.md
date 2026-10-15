# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 02:30:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$17.61 USD** | **$20.86 USD** | **$38.47 USD** | 🔴 **-3.83%** ($-1.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 15h 40m |
| `BTC-USD` | 0.000061 | $81640.68 | $80992.47 | $4.96 | 📉 -0.79% | 5h 20m |
| `ETH-USD` | 0.002539 | $2362.71 | $2358.10 | $5.99 | 📉 -0.20% | 1h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario de EE. UU. se encuentra cerrado, por lo que toda la atención se desplaza al mercado de criptomonedas (abierto 24/7). Las criptomonedas muestran presiones bajistas continuas con tendencias por debajo de sus medias móviles de 20 periodos, pero ETH-USD y SOL-USD presentan niveles de RSI diario extremadamente bajos que sugieren posibles rebotes por sobreventa a medida que avance la sesión. Mantenemos una postura defensiva pero flexible para rotar capital hacia activos con mayor dinamismo cripto."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 60%): La posición en BTC-USD lleva pocas horas abierta (-0.79% PnL) y se encuentra dentro de parámetros normales de fluctuación. Esperamos confirmación de volumen y rebote en el corto plazo.
- **[HOLD] ETH-USD** (Confianza: 65%): ETH-USD muestra un RSI de 1h en 29.2, cerca de la zona de sobreventa previa. Mantenemos la posición buscando el rebote técnico hacia la zona del +2% de beneficio antes de tomar ganancias.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones abiertas en BTC-USD y ETH-USD supervisando de cerca un cambio positivo en el cambio porcentual de 1h y RSI superior a 40 para asegurar ganancias o cortar pérdidas si bajan del -2.0%. Dado que AAPL está en mercado cerrado, no se puede operar, pero se evaluará su salida en cuanto abra la sesión si el momentum decae. Vigilar SOL-USD para una posible entrada si rompe la resistencia intradía con un RSI en recuperación."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **54** | 🎯 **40.7%** (22W / 18L / 14BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 01:10` | 🟢 BUY | `ETH-USD` | $6.00 | $2362.71 | ETH-USD presenta un RSI de 1h extremadamente bajo en 23.5 saliendo de sobreventa y un camb... |
| `2026-10-14 23:30` | 🔴 SELL (-0.30$) | `SOL-USD` | $9.70 | $101.32 | La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin ... |
| `2026-10-14 23:30` | 🔴 SELL (-0.32$) | `ETH-USD` | $9.68 | $2340.86 | 🚨 STOP-LOSS AUTOMÁTICO (CIRCUIT BREAKER): Pérdida de -3.20% superó el límite de seguridad ... |
| `2026-10-14 21:10` | 🟢 BUY | `BTC-USD` | $5.00 | $81640.68 | BTC-USD presenta un RSI de 1h en 24.9 (sobreventa extrema) y liquidez disponible suficient... |
| `2026-10-14 19:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2418.34 | ETH-USD presenta un RSI de 1h en 22.0 (sobreventa extrema) y un cambio de 1h que comienza ... |

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
