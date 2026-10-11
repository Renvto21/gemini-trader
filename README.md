# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 02:30:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.36 USD** | **$40.36 USD** | 🟢 **+0.90%** ($+0.36) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.220969 | $109.11 | $109.54 | $24.20 | 📈 +0.39% |
| `ETH-USD` | 0.006448 | $2481.58 | $2505.22 | $16.15 | 📈 +0.95% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con sesgo alcista moderado en índices tradicionales (QQQ, SPY) y fortaleza en tecnológicas como MSFT, cuyo RSI se encuentra en zona de sobrecompra (72.3). Por otro lado, las criptomonedas principales como SOL-USD (RSI 22.4) y ETH-USD (RSI 28.1) se encuentran en condiciones claras de sobreventa técnica tras caídas semanales, lo que representa una oportunidad táctica de rebote por reversión a la media según la estrategia agresiva."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 90%): SOL-USD presenta un RSI extremadamente bajo de 22.4 y una caída semanal del -9.86%. Mantenemos la posición actual para cazar el rebote técnico hacia la media, ya que el precio actual de 109.54 USD ofrece un excelente descuento y el capital ya está invertido.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH-USD muestra un RSI de 28.1 en zona de sobreventa, con una ligera recuperación del 0.79% en 24 horas. Conservamos la posición para capturar el movimiento alcista impulsado por el rebote de criptoactivos.

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
