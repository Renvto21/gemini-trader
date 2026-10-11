# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 08:40:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.29 USD** | **$40.29 USD** | 🟢 **+0.73%** ($+0.29) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.330438 | $109.27 | $109.40 | $36.15 | 📈 +0.12% |
| `ETH-USD` | 0.001656 | $2500.14 | $2500.14 | $4.14 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra oportunidades claras de reversión a la media (mean reversion) en criptomonedas debido a condiciones extremas de sobreventa. Específicamente, ETH-USD presenta un RSI de 28.2 y una caída semanal del 7.78%, situándose en una posición ideal para un rebote técnico rápido. Por otro lado, SOL-USD se mantiene en cartera con un rendimiento estancado y un RSI extremadamente deprimido en 21.3; sin embargo, para diversificar y aprovechar el fuerte descuento en ETH, mantendremos la posición de SOL por ahora y rotaremos parte de la liquidez para cazar el rebote de Ethereum."*

**Operaciones del ciclo:**
- **[BUY] ETH-USD** (Confianza: 88%): ETH-USD se encuentra en clara sobreventa con un RSI de 28.2 y una caída de 7.78% en los últimos 7 días. Cumple perfectamente con la regla táctica de cazar rebotes en cripto con alta convicción. Utilizo la totalidad del efectivo disponible para capturar este movimiento alcista de corto plazo.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 08:40` | 🟢 BUY | `ETH-USD` | $4.14 | $2500.14 | ETH-USD se encuentra en clara sobreventa con un RSI de 28.2 y una caída de 7.78% en los úl... |
| `2026-10-11 08:00` | 🔴 SELL | `ETH-USD` | $4.14 | $2498.90 | Vendemos la posición completa de ETH-USD para liberar 4.14 USD en efectivo. Aunque está en... |
| `2026-10-11 05:00` | 🟢 BUY | `ETH-USD` | $4.14 | $2499.59 | ETH-USD presenta un RSI de 28.2, lo que indica una clara condición de sobreventa técnica t... |
| `2026-10-11 04:50` | 🟢 BUY | `SOL-USD` | $12.00 | $109.36 | Alta convicción en el rebote técnico de Solana tras una caída semanal del -9.43% y un RSI ... |
| `2026-10-11 04:50` | 🔴 SELL | `ETH-USD` | $16.12 | $2500.30 | Rotamos capital fuera de ETH-USD para asegurar una pequeña ganancia del +0.75% y liberar l... |

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
