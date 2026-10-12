# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 11:50:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.42 USD** | **$12.96 USD** | **$40.39 USD** | 🟢 **+0.97%** ($+0.39) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001175 | $2553.82 | $2523.45 | $2.96 | 📉 -1.19% |
| `SOL-USD` | 0.090909 | $110.00 | $110.00 | $10.00 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo correctivo a corto plazo, pero con criptomonedas clave como SOL-USD y ETH-USD entrando profundamente en zonas de sobreventa técnica (RSI de 28.6 y 32.2 respectivamente). Esto activa nuestra estrategia táctica de mean reversion y búsqueda de rebotes rápidos en alta volatilidad. Mantenemos nuestra posición en ETH y aprovechamos la liquidez disponible para abrir una nueva posición en SOL-USD con alta convicción para capturar un rebote técnico inminente."*

**Operaciones del ciclo:**
- **[BUY] SOL-USD** (Confianza: 88%): SOL-USD presenta un RSI de 28.6 indicando sobreventa extrema y una caída acumulada semanal del 8.93%. Bajo nuestra estrategia agresiva de mean reversion, este es un punto de entrada excelente para cazar un rebote rápido del 3% al 5%.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 11:50` | 🟢 BUY | `SOL-USD` | $10.00 | $110.00 | SOL-USD presenta un RSI de 28.6 indicando sobreventa extrema y una caída acumulada semanal... |
| `2026-10-12 11:40` | 🔴 SELL | `SOL-USD` | $37.42 | $108.72 | Activación del stop-loss estricto debido a que la posición ha caído un -2.58%, rompiendo e... |
| `2026-10-12 11:10` | 🟢 BUY | `SOL-USD` | $4.00 | $110.16 | SOL-USD presenta un RSI extremadamente bajo de 28.8 y una caída acumulada del 8.8% en 7 dí... |
| `2026-10-12 07:40` | 🟢 BUY | `ETH-USD` | $3.00 | $2553.82 | ETH-USD presenta un RSI de 35.7 indicando condiciones cercanas a la sobreventa, lo que act... |
| `2026-10-12 07:30` | 🔴 SELL | `ETH-USD` | $7.00 | $2553.60 | ETH-USD se encuentra estancado con un PnL cercano a 0% sin momentum inmediato. Vendemos la... |

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
