# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 01:30:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$41.32 USD** | **$41.33 USD** | 🟢 **+3.32%** ($+1.33) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.325271 | $111.58 | $111.84 | $36.38 | 📈 +0.23% |
| `ETH-USD` | 0.001939 | $2542.03 | $2549.55 | $4.94 | 📈 +0.30% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con el sector tecnológico y los índices principales (QQQ, SPY) con tendencia alcista moderada, mientras que las criptomonedas (SOL-USD, ETH-USD) han experimentado caídas semanales importantes pero presentan condiciones técnicas claras de sobreventa (RSI de SOL en 28.0 y ETH en 35.4), lo cual activa nuestra estrategia de cazar rebotes por reversión a la media. Mantendremos las posiciones actuales ya que están mostrando un ligero repunte en 24h y no justifican venta por take-profit ni stop-loss, y el efectivo actual es cero, por lo que no se requieren nuevas compras en este ciclo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL se encuentra en fuerte sobreventa técnica con un RSI de 28.0 tras una caída semanal del -7.38%. Aunque la tendencia es bajista, el precio muestra un intento de rebote en 24h (+1.64%). Mantenemos la posición para capturar el movimiento alcista de recuperación.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH presenta un RSI de 35.4 en zona de posible sobreventa y un avance diario del +1.82%. La posición es pequeña y esperamos una mayor expansión del precio antes de realizar cualquier toma de ganancias o rotación.

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
