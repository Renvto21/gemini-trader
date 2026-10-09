# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 18:31:09`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.09 USD** | **$36.01 USD** | **$40.10 USD** | 🟢 **+0.26%** ($+0.10) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SPY` | 0.006458 | $774.29 | $778.57 | $5.03 | 📈 +0.55% |
| `NVDA` | 0.021772 | $229.65 | $229.28 | $4.99 | 📉 -0.16% |
| `QQQ` | 0.006652 | $751.70 | $751.27 | $5.00 | 📉 -0.06% |
| `SOL-USD` | 0.091676 | $109.08 | $109.01 | $9.99 | 📉 -0.06% |
| `ETH-USD` | 0.004433 | $2481.36 | $2481.06 | $11.00 | 📉 -0.01% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra una clara divergencia: mientras las acciones tecnológicas y los índices tradicionales (SPY, QQQ) mantienen una tendencia alcista moderada, el sector cripto ha sufrido una fuerte corrección de corto plazo, llevando a activos de alto beta como SOL y ETH a niveles extremos de sobreventa técnica (RSI de 20.2 y 24.8 respectivamente). Esta capitulación representa una oportunidad inmejorable de reversión a la media (Mean Reversion). Decidimos rotar capital de forma agresiva vendiendo una posición estancada y de menor momentum (AAPL) para duplicar nuestra apuesta en el rebote inminente de ETH-USD, manteniendo intacta nuestra reserva mínima de liquidez."*

**Operaciones del ciclo:**
- **[SELL] AAPL** (Confianza: 90%): Rotación estratégica de capital. AAPL se encuentra estancada con un rendimiento de -0.01% y un RSI neutral de 47.3. Liquidamos la posición para liberar $6.00 USD de capital y redirigirlos a un activo con mayor momentum y descuento técnico.
- **[BUY] ETH-USD** (Confianza: 92%): Oportunidad de alta convicción por sobreventa extrema (RSI de 24.8). Con los $6.00 USD liberados de AAPL, incrementamos nuestra exposición en ETH-USD para buscar un rebote rápido del +2.5% al +6.0%, acumulando una posición total de alta convicción cercana a los $11.00 USD.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-09 18:31` | 🟢 BUY | `ETH-USD` | $6.00 | $2481.06 | Oportunidad de alta convicción por sobreventa extrema (RSI de 24.8). Con los $6.00 USD lib... |
| `2026-10-09 18:31` | 🔴 SELL | `AAPL` | $6.00 | $336.64 | Rotación estratégica de capital. AAPL se encuentra estancada con un rendimiento de -0.01% ... |
| `2026-10-09 18:25` | 🟢 BUY | `ETH-USD` | $5.00 | $2481.72 | ETH-USD muestra un RSI de 24.9, confirmando una capitulación de corto plazo en el mercado ... |
| `2026-10-09 18:25` | 🟢 BUY | `SOL-USD` | $10.00 | $109.08 | SOL-USD se encuentra en una condición de sobreventa extrema con un RSI de 20.3 tras caer u... |
| `2026-10-09 16:26` | 🟢 BUY | `QQQ` | $5.00 | $751.70 | QQQ se encuentra en una tendencia alcista clara sobre su SMA20 y con un RSI de 58.1 que su... |

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
