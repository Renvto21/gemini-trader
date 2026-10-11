# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 06:30:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.24 USD** | **$40.24 USD** | 🟢 **+0.61%** ($+0.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.330438 | $109.27 | $109.26 | $36.10 | 📉 -0.01% |
| `ETH-USD` | 0.001656 | $2499.59 | $2498.40 | $4.14 | 📉 -0.05% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un fuerte contraste: las criptomonedas (SOL-USD y ETH-USD) se encuentran en condiciones extremas de sobreventa con niveles de RSI de 21.1 y 28.1 respectivamente, lo que presenta una oportunidad clásica de rebote técnico (Mean Reversion). Por otro lado, activos tecnológicos como MSFT presentan un RSI de sobrecompra en 72.3 tras fuertes ganancias. Mantenemos una postura agresiva para aprovechar los descuentos profundos en cripto y rotar capital si es necesario."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD está en un nivel de sobreventa extrema (RSI de 21.1) tras una caída semanal del 9.52%. Mantenemos la posición para cazar el rebote técnico inminente hacia la zona del +4%.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 05:00` | 🟢 BUY | `ETH-USD` | $4.14 | $2499.59 | ETH-USD presenta un RSI de 28.2, lo que indica una clara condición de sobreventa técnica t... |
| `2026-10-11 04:50` | 🟢 BUY | `SOL-USD` | $12.00 | $109.36 | Alta convicción en el rebote técnico de Solana tras una caída semanal del -9.43% y un RSI ... |
| `2026-10-11 04:50` | 🔴 SELL | `ETH-USD` | $16.12 | $2500.30 | Rotamos capital fuera de ETH-USD para asegurar una pequeña ganancia del +0.75% y liberar l... |
| `2026-10-11 03:20` | 🟢 BUY | `SOL-USD` | $12.00 | $109.35 | SOL-USD se encuentra en una situación de sobreventa técnica masiva con un RSI de 14 en 21.... |
| `2026-10-11 03:20` | 🔴 SELL | `MSFT` | $12.00 | $535.07 | MSFT ha entrado en zona de sobrecompra técnica con un RSI de 72.3. Aplicando la regla táct... |

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
