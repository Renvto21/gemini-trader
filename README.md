# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 02:40:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.34 USD** | **$40.34 USD** | 🟢 **+0.86%** ($+0.34) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.220969 | $109.11 | $109.47 | $24.19 | 📈 +0.33% |
| `ETH-USD` | 0.006448 | $2481.58 | $2505.27 | $16.15 | 📈 +0.95% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un contraste claro: las criptomonedas (SOL-USD con RSI de 22.1 y ETH-USD con RSI de 28.1) se encuentran en condiciones extremas de sobreventa técnica tras caídas semanales significativas, lo que presenta una oportunidad ideal para cazar rebotes de reversión a la media. Por otro lado, activos tecnológicos como MSFT han entrado en sobrecompra (RSI 72.3). Dado que nuestro capital está totalmente invertido en SOL y ETH y con ganancias mínimas, y cumpliendo con la regla de mantener solo $4.00 USD de efectivo libre, decidimos mantener nuestras posiciones actuales para capturar el fuerte rebote inminente en cripto sin realizar operaciones de venta por ahora."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 90%): SOL-USD se encuentra en un estado de sobreventa extrema con un RSI de 22.1 y una caída semanal cercana al -10%. Mantenemos la posición para capturar el rebote técnico agresivo esperado hacia la media.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH-USD muestra un RSI de 28.1 indicando sobreventa técnica profunda. Aunque la tendencia es bajista, las condiciones son perfectas para un rebote de alivio de corto plazo.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 02:20` | 🟢 BUY | `SOL-USD` | $4.11 | $109.54 | SOL-USD se encuentra en extrema sobreventa técnica con un RSI de 22.4 y una caída semanal ... |
| `2026-10-10 12:10` | 🔴 SELL | `MSFT` | $4.11 | $535.07 | MSFT ha alcanzado un RSI de 72.3 (sobrecompra) cumpliendo con la regla táctica de toma de ... |
| `2026-10-10 12:00` | 🟢 BUY | `MSFT` | $4.11 | $535.07 | Aprovechamos el capital liberado de GLD para entrar en MSFT, que muestra un fuerte momentu... |
| `2026-10-10 12:00` | 🔴 SELL | `GLD` | $4.11 | $384.58 | Liberamos la totalidad de la posición en GLD ya que se encuentra estancada con 0% de PnL y... |
| `2026-10-10 11:50` | 🟢 BUY | `GLD` | $4.11 | $384.58 | Aprovechamos el efectivo disponible para cazar un rebote por sobreventa en GLD, cuyo RSI s... |

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
