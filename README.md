# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 18:50:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.01 USD** | **$39.50 USD** | **$39.51 USD** | 🔴 **-1.23%** ($-0.49) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.369549 | $109.24 | $106.89 | $39.50 | 📉 -2.15% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto se encuentra bajo presión bajista a corto plazo, destacando SOL-USD con un RSI extremadamente de sobreventa en 24.8 y una caída del -11.51% en 7 días, rozando nuestro límite de stop-loss estricto (-2.15%). ETH-USD también muestra sobreventa con RSI de 30.2. En el sector tecnológico, MSFT está en sobrecompra (RSI 77.9), mientras que QQQ y NVDA se mantienen neutrales con sesgo bajista. Mantendremos la posición en SOL buscando su rebote técnico o ejecutaremos el stop-loss si profundiza la caída, sin realizar nuevas compras en este ciclo para preservar liquidez."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición actual en SOL-USD registra un PnL de -2.15%, acercándose al límite de stop-loss (-2.5% a -3.0%). Sin embargo, su RSI de 24.8 indica una sobreventa masiva que históricamente precede a fuertes rebotes por reversión a la media. Mantendremos la posición para capturar el rebote técnico esperado, vigilando de cerca el nivel de pérdida para cortar de inmediato si perfora el soporte.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 16:40` | 🟢 BUY | `SOL-USD` | $2.95 | $108.01 | Aprovechamos el capital liberado de Ethereum para incrementar la exposición en SOL-USD. Su... |
| `2026-10-12 16:40` | 🔴 SELL | `ETH-USD` | $2.95 | $2515.02 | Vendemos la posición completa en ETH-USD para liberar liquidez y concentrar el capital dis... |
| `2026-10-12 15:40` | 🟢 BUY | `SOL-USD` | $4.00 | $107.58 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 25.6 y una caída acumulada ... |
| `2026-10-12 12:20` | 🟢 BUY | `SOL-USD` | $3.42 | $108.91 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 27.1 y una caída acumulada ... |
| `2026-10-12 12:10` | 🟢 BUY | `SOL-USD` | $10.00 | $108.93 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 27.2 y una... |

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
