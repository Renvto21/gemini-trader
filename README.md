# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 01:40:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.23 USD** | **$40.34 USD** | 🟢 **+0.85%** ($+0.34) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.47 | $20.08 | 📈 +0.41% |
| `ETH-USD` | 0.006448 | $2481.58 | $2504.66 | $16.15 | 📈 +0.93% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un tono mixto con sesgo alcista en índices tradicionales como SPY y QQQ, mientras que el sector cripto (SOL-USD y ETH-USD) se encuentra bajo presión con caídas semanales marcadas. Específicamente, ETH-USD muestra un RSI de 28.0 y SOL-USD un RSI de 22.1, lo cual los sitúa en una zona extrema de sobreventa (mean reversion). Dado que mantenemos una postura táctica agresiva y buscamos rebotes rápidos, estas condiciones de sobreventa son ideales para buscar ganancias de corto plazo, a pesar de la tendencia bajista de corto plazo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra profundamente en sobreventa con un RSI de 22.1 tras una caída semanal del 9.92%. Nuestra posición actual muestra una ganancia leve del 0.41%. Mantenemos la posición para capturar el rebote inminente hacia la media, aprovechando el alto potencial de recuperación de la altcoin.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD registra un RSI de 28.0 en zona de sobreventa técnica tras una caída semanal del 8.14%. La posición actual arroja un PnL positivo del 0.93%. Mantenemos la inversión para permitir que el precio rebote y alcance nuestro objetivo de toma de beneficios antes de rotar el capital.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-10 12:10` | 🔴 SELL | `MSFT` | $4.11 | $535.07 | MSFT ha alcanzado un RSI de 72.3 (sobrecompra) cumpliendo con la regla táctica de toma de ... |
| `2026-10-10 12:00` | 🟢 BUY | `MSFT` | $4.11 | $535.07 | Aprovechamos el capital liberado de GLD para entrar en MSFT, que muestra un fuerte momentu... |
| `2026-10-10 12:00` | 🔴 SELL | `GLD` | $4.11 | $384.58 | Liberamos la totalidad de la posición en GLD ya que se encuentra estancada con 0% de PnL y... |
| `2026-10-10 11:50` | 🟢 BUY | `GLD` | $4.11 | $384.58 | Aprovechamos el efectivo disponible para cazar un rebote por sobreventa en GLD, cuyo RSI s... |
| `2026-10-09 19:00` | 🟢 BUY | `ETH-USD` | $5.00 | $2482.07 | ETH-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.0. Utilizando el c... |

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
