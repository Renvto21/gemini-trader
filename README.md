# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 08:30:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.14 USD** | **$36.13 USD** | **$40.27 USD** | 🟢 **+0.67%** ($+0.27) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.330438 | $109.27 | $109.33 | $36.13 | 📈 +0.05% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra divergencias interesantes con un sector cripto fuertemente castigado en el corto plazo (SOL con RSI de 21.2 y ETH con RSI de 28.2), lo cual representa una oportunidad clásica de rebote técnico por sobreventa extrema (Mean Reversion). Por otro lado, MSFT ha entrado en sobrecompra con un RSI de 72.3 y un fuerte impulso alcista reciente. Mantenemos nuestra posición en SOL-USD ya que el RSI extremadamente bajo sugiere un rebote inminente hacia la media."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en un estado de sobreventa técnica masiva con un RSI de 21.2 y una caída del 9.46% en los últimos 7 días. Aunque está bajo la SMA20, las condiciones para un rebote técnico inminente son óptimas según nuestra estrategia de caza de rebotes. Mantenemos la posición para capturar el movimiento alcista de recuperación.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 08:00` | 🔴 SELL | `ETH-USD` | $4.14 | $2498.90 | Vendemos la posición completa de ETH-USD para liberar 4.14 USD en efectivo. Aunque está en... |
| `2026-10-11 05:00` | 🟢 BUY | `ETH-USD` | $4.14 | $2499.59 | ETH-USD presenta un RSI de 28.2, lo que indica una clara condición de sobreventa técnica t... |
| `2026-10-11 04:50` | 🟢 BUY | `SOL-USD` | $12.00 | $109.36 | Alta convicción en el rebote técnico de Solana tras una caída semanal del -9.43% y un RSI ... |
| `2026-10-11 04:50` | 🔴 SELL | `ETH-USD` | $16.12 | $2500.30 | Rotamos capital fuera de ETH-USD para asegurar una pequeña ganancia del +0.75% y liberar l... |
| `2026-10-11 03:20` | 🟢 BUY | `SOL-USD` | $12.00 | $109.35 | SOL-USD se encuentra en una situación de sobreventa técnica masiva con un RSI de 14 en 21.... |

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
