# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 17:10:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.43 USD** | **$40.54 USD** | 🟢 **+1.35%** ($+0.54) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.34 | $20.24 | 📈 +1.21% |
| `ETH-USD` | 0.006448 | $2481.58 | $2510.51 | $16.19 | 📈 +1.17% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con sesgo alcista en índices tradicionales y tecnología de gran capitalización (QQQ, SPY), mientras que el sector cripto ha estado bajo presión la última semana pero presenta condiciones de sobreventa extrema (RSI de ETH en 29.0 y SOL en 25.2), lo cual activa nuestra estrategia de mean reversion y caza de rebotes rápidos. Mantenemos nuestras posiciones actuales esperando que el impulso alcista en cripto continúe consolidando ganancias."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra en sobreventa extrema con un RSI de 25.2, mostrando un intento de recuperación con un +1.1% en las últimas 24 horas. Mantenemos la posición para capturar el rebote técnico esperado hacia la resistencia de corto plazo.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD presenta un RSI de 29.0 reflejando clara sobreventa tras caídas recientes de la semana. Está rebotando un +1% en 24h y mantenemos la posición para buscar el objetivo de toma de ganancias del +2.5%.

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
