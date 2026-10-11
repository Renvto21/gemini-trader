# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 13:40:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.16 USD** | **$22.05 USD** | **$41.21 USD** | 🟢 **+3.02%** ($+1.21) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.004740 | $2531.44 | $2541.93 | $12.05 | 📈 +0.41% |
| `SOL-USD` | 0.089453 | $111.79 | $111.79 | $10.00 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo alcista moderado en índices principales como SPY y QQQ, mientras que el sector tecnológico muestra fortaleza general, destacando MSFT en zona de sobrecompra con un RSI de 72.3. En el ámbito cripto, SOL-USD se encuentra en clara sobreventa técnica con un RSI de 27.8 tras caídas recientes de 7.42% en la última semana, lo que representa una oportunidad ideal de rebote por reversión a la media (Mean Reversion). ETH-USD se mantiene en cartera con ganancias modestas pero sin el momentum explosivo deseado, mientras que disponemos de un sólido colchón de liquidez para cazar nuevas oportunidades."*

**Operaciones del ciclo:**
- **[BUY] SOL-USD** (Confianza: 88%): SOL-USD presenta una excelente oportunidad de rebote técnico de alta convicción al encontrarse en condición de sobreventa profunda (RSI de 27.8) y acumulando una caída semanal de -7.42%. Aplicamos una asignación agresiva de $10.00 USD para capturar el movimiento alcista de corto plazo.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 13:40` | 🟢 BUY | `SOL-USD` | $10.00 | $111.79 | SOL-USD presenta una excelente oportunidad de rebote técnico de alta convicción al encontr... |
| `2026-10-11 13:30` | 🔴 SELL | `SOL-USD` | $19.04 | $111.95 | SOL-USD ha alcanzado un rendimiento cercano a nuestra meta de take-profit del 2.5% (+2.43%... |
| `2026-10-11 13:20` | 🟢 BUY | `ETH-USD` | $12.00 | $2531.44 | ETH-USD se encuentra en zona de profunda sobreventa técnica con un RSI de 32.8 y una caída... |
| `2026-10-11 13:10` | 🔴 SELL | `ETH-USD` | $9.99 | $2530.10 | ETH-USD se encuentra estancado con un P&L cercano a 0% (-0.06%) y bajo tendencia bajista e... |
| `2026-10-11 13:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2531.65 | ETH-USD se encuentra en clara sobreventa técnica con un RSI de 32.8 y una fuerte caída sem... |

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
