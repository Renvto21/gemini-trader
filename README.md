# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 20:10:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.37 USD** | **$40.48 USD** | 🟢 **+1.21%** ($+0.48) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.19 | $20.21 | 📈 +1.07% |
| `ETH-USD` | 0.006448 | $2481.58 | $2506.01 | $16.16 | 📈 +0.98% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un rebote técnico moderado en las criptomonedas principales que se encontraban en profunda sobreventa, mientras que los índices tecnológicos (QQQ, SPY) mantienen una tendencia alcista saludable. Ethereum (ETH-USD) y Solana (SOL-USD) presentan RSI de 28.3 y 24.7 respectivamente, lo que confirma condiciones extremas de sobreventa y un potencial de rebote alcista agresivo. Mantendremos nuestras posiciones actuales y el efectivo disponible ya que estamos cerca de la reserva mínima de liquidez, permitiendo que las criptomonedas capturen el movimiento de recuperación esperado."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en zona de sobreventa extrema (RSI de 24.7) mostrando los primeros signos de recuperación tras caídas semanales. Mantenemos la posición para capturar el rebote técnico hacia la zona objetivo de ganancia del +3%.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD registra un RSI de 28.3, manteniendo una clara oportunidad de reversión a la media. Conservamos la posición para aprovechar el impulso alcista inminente en el sector cripto.

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
