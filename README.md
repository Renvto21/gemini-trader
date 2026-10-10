# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 18:50:35`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.39 USD** | **$40.50 USD** | 🟢 **+1.24%** ($+0.50) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.26 | $20.23 | 📈 +1.14% |
| `ETH-USD` | 0.006448 | $2481.58 | $2506.39 | $16.16 | 📈 +1.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con el sector tecnológico y los principales índices (QQQ, SPY, MSFT) manteniendo tendencias alcistas sólidas. MSFT presenta un RSI de 72.3, entrando en zona de sobrecompra técnica. Por otro lado, las criptomonedas en cartera (SOL-USD y ETH-USD) se encuentran en condiciones extremas de sobreventa con RSI de 24.9 y 28.3 respectivamente, manteniendo ganancias moderadas del 1.14% y 1.0%. Nuestra reserva de liquidez se encuentra en $4.11 USD, alineada con la regla de mantener un mínimo operativo. Dado que nuestras posiciones en cripto siguen ganando tracción y buscan un rebote técnico mayor tras caídas semanales significativas, optamos por mantenerlas y no sobreoperar en este ciclo, dejando que el impulso continúe."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en clara sobreventa (RSI 24.9) y está experimentando un intento de recuperación con una ganancia actual de +1.14%. Mantenemos la posición para capturar el rebote técnico hacia la zona objetivo sin vender prematuramente.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD muestra un RSI extremadamente bajo de 28.3 y registra un PnL positivo de +1.0%. El activo busca recuperarse de la caída semanal. Mantenemos la posición a la espera de un mayor impulso alcista para asegurar beneficios.

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
