# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 10:01:01`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.39 USD** | **$39.39 USD** | 🔴 **-1.51%** ($-0.61) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $106.53 | $31.45 | 📉 -0.60% |
| `ETH-USD` | 0.003177 | $2505.44 | $2501.37 | $7.95 | 📉 -0.16% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones claras de sobreventa extrema, especialmente en Solana (SOL-USD) con un RSI de 25.7, ofreciendo una oportunidad clásica de rebote por reversión a la media. Ethereum también muestra un RSI bajo de 35.1 pero con un intento de recuperación en las últimas 24 horas (+2.33%). Dado nuestro enfoque de crecimiento acelerado y la regla de cazar rebotes en cripto, mantenemos nuestras posiciones actuales para permitirles capitalizar el rebote técnico y no realizamos ventas ya que las pérdidas están controladas y lejos de los límites estrictos de stop-loss."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en un estado de sobreventa extrema con un RSI de 25.7 y una caída semanal del -8.34%. Cumple perfectamente con la estrategia de cazar rebotes por mean reversion. Mantenemos la posición para capturar el movimiento alcista inminente hacia la media.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un RSI de 35.1 y un impulso positivo de 2.33% en las últimas 24 horas, lo que sugiere que el rebote técnico ya ha comenzado a gestarse. La mantenemos para acompañar el momentum.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 08:30` | 🟢 BUY | `ETH-USD` | $7.96 | $2505.44 | ETH-USD muestra un RSI de 35.6 en zona de sobreventa y un cambio positivo de 2.45% en 24 h... |
| `2026-10-13 08:30` | 🔴 SELL | `NVDA` | $7.96 | $226.32 | Liberamos capital de NVDA que se encuentra lateral y bajo su SMA20 sin momentum claro, par... |
| `2026-10-13 08:10` | 🟢 BUY | `NVDA` | $7.96 | $226.32 | Aprovechamos la corrección reciente de NVDA (caída de 7 días del -3.26% con un RSI de 46.4... |
| `2026-10-13 08:10` | 🔴 SELL | `ETH-USD` | $7.96 | $2494.07 | Ejecutamos rotación activa de capital vendiendo la posición completa de ETH-USD para liber... |
| `2026-10-13 02:30` | 🟢 BUY | `SOL-USD` | $4.00 | $108.19 | SOL-USD presenta un RSI extremadamente bajo de 26.3, lo que indica sobreventa técnica seve... |

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
