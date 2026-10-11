# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 07:50:41`

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
| `ETH-USD` | 0.001656 | $2499.59 | $2498.12 | $4.14 | 📉 -0.06% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra una divergencia interesante: mientras que los índices y acciones tecnológicas como SPY, QQQ y MSFT se mantienen en tendencia alcista (MSFT en sobrecompra con RSI de 72.3), las criptomonedas principales como SOL-USD y ETH-USD se encuentran en niveles extremos de sobreventa técnica (RSI de 21.1 y 28.1 respectivamente) tras caídas semanales significativas. Nuestro portafolio actual está invertido al 100% en estas dos criptomonedas, las cuales están planas en el muy corto plazo pero listas para un rebote explosivo por reversión a la media (Mean Reversion) debido a su profunda sobreventa."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD presenta un RSI extremadamente bajo de 21.1 y una caída de -9.52% en los últimos 7 días. Según la estrategia de caza de rebotes, estamos ante una clara oportunidad de sobreventa técnica con alta probabilidad de un rebote rápido del +2% al +6%. Mantenemos la posición para capturar este movimiento sin vender en el suelo.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH-USD muestra un RSI de 28.1, también en zona de clara sobreventa técnica tras una caída semanal del -7.85%. Al estar nuestra liquidez en cero y la posición con un rendimiento cercano a cero sin haber roto los niveles de stop-loss, mantenemos la posición para aprovechar el inminente rebote alcista del sector cripto.

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
