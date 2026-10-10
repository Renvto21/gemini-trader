# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 19:30:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.37 USD** | **$40.48 USD** | 🟢 **+1.21%** ($+0.48) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.23 | $20.22 | 📈 +1.11% |
| `ETH-USD` | 0.006448 | $2481.58 | $2505.00 | $16.15 | 📈 +0.94% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo alcista moderado en índices tradicionales (QQQ, SPY) y acciones tecnológicas de peso como MSFT, la cual ha entrado en sobrecompra con un RSI de 72.3. Por otro lado, las criptomonedas (SOL-USD y ETH-USD) se encuentran en condiciones claras de sobreventa técnica (RSI de 24.8 y 28.1 respectivamente), manteniendo una tendencia bajista de corto plazo pero preparadas para un potencial rebote de reversión a la media. Mantenemos nuestras posiciones actuales esperando un impulso alcista que nos permita tomar ganancias o rotar capital eficientemente."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD está profundamente en sobreventa (RSI 24.8) mostrando un ligero repunte del 1.0% en 24h. Mantenemos la posición para capturar el rebote técnico esperado hacia la resistencia local, cumpliendo con la estrategia de cazar sobreventas en cripto.
- **[HOLD] ETH-USD** (Confianza: 78%): ETH-USD presenta un RSI de 28.1, también en zona de sobreventa. Mantenemos la posición actual con una ganancia flotante pequeña, esperando que acompañe el movimiento de recuperación del mercado cripto sin disparar aún un stop-loss.

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
