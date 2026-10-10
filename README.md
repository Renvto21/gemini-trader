# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 15:20:59`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.35 USD** | **$40.46 USD** | 🟢 **+1.16%** ($+0.46) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.04 | $20.19 | 📈 +0.93% |
| `ETH-USD` | 0.006448 | $2481.58 | $2507.18 | $16.17 | 📈 +1.03% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa con ETH-USD (RSI 28.5) y SOL-USD (RSI 24.2) recuperándose levemente tras caídas semanales significativas, encontrándose listos para un rebote técnico alcista. Mantenemos nuestras posiciones actuales dado que las ganancias no han alcanzado el objetivo de take-profit del +2.5% y la reserva de efectivo actual de $4.11 USD cumple estrictamente con el requisito de liquidez mínima."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en profunda sobreventa técnica con un RSI de 24.2, mostrando un intento de recuperación con +0.83% en 24h. Mantenemos la posición para capturar el rebote técnico hacia la zona de take-profit.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH-USD presenta un RSI de 28.5 en zona de sobreventa, operando en ligero beneficio (+1.03%). Esperamos a que alcance el objetivo del +2.5% para asegurar ganancias y rotar el capital.

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
