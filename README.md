# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 02:20:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$41.66 USD** | **$41.67 USD** | 🟢 **+4.17%** ($+1.67) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.325271 | $111.58 | $112.82 | $36.70 | 📈 +1.11% |
| `ETH-USD` | 0.001939 | $2542.03 | $2561.41 | $4.97 | 📈 +0.76% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo técnico mixto con criptomonedas repuntando desde zonas de sobreventa (SOL con RSI en 30.9 y ETH en 37.0), lo cual activa nuestras señales de rebote (mean reversion). Ambas posiciones actuales tienen ganancias modestas pero estables, y dado que buscamos una rotación dinámica y toma de beneficios rápida, mantendremos SOL-USD mientras evaluamos el mercado o liberamos liquidez si es necesario. No se realizan ventas masivas porque las criptos están mostrando un impulso positivo de 24 horas interesante (+2.53% en SOL y +2.29% en ETH), alineándose con nuestra estrategia agresiva."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición en SOL-USD muestra un rebote técnico incipiente tras estar en sobreventa extrema (RSI 30.9). Mantenemos la posición para capturar el objetivo del +2.5% a +6% de ganancia rápida según la estrategia de momentum.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 00:40` | 🟢 BUY | `SOL-USD` | $4.00 | $111.56 | SOL-USD muestra un RSI de 27.1, indicando una condición de sobreventa profunda tras una ca... |
| `2026-10-12 00:30` | 🟢 BUY | `ETH-USD` | $4.93 | $2542.03 | ETH-USD se encuentra en zona de clara sobreventa técnica con un RSI de 34.4 tras una caída... |
| `2026-10-12 00:20` | 🔴 SELL | `ETH-USD` | $4.93 | $2542.39 | ETH-USD se encuentra estancado con una ganancia marginal del 0.04% y bajo momentum inmedia... |
| `2026-10-11 23:10` | 🟢 BUY | `ETH-USD` | $4.93 | $2541.27 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 34.2 y una caída semanal ... |
| `2026-10-11 23:00` | 🔴 SELL | `ETH-USD` | $3.92 | $2541.25 | La posicion en ETH-USD esta estancada y representa un monto muy pequeno ($3.92) sin sufici... |

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
