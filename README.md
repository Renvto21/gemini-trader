# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 16:30:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.44 USD** | **$40.55 USD** | 🟢 **+1.37%** ($+0.55) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.36 | $20.25 | 📈 +1.23% |
| `ETH-USD` | 0.006448 | $2481.58 | $2511.16 | $16.19 | 📈 +1.19% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema con SOL-USD (RSI 25.2) y ETH-USD (RSI 29.1) operando en niveles atractivos para un rebote técnico de reversión a la media. Nuestras posiciones actuales están experimentando un leve beneficio positivo pero aún no alcanzan el objetivo de take-profit del 2.5%. Dado que mantenemos nuestra reserva de liquidez operativa en el efectivo actual ($4.11 USD), la mejor estrategia es mantener las posiciones actuales de criptomonedas mientras se desarrolla el rebote y conservar la liquidez sin forzar nuevas compras en este ciclo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL se encuentra en condiciones de sobreventa profunda (RSI 14 en 25.2) con un inicio de recuperación del 1.12% en las últimas 24 horas. Mantenemos la posición para capturar el rebote técnico hacia el objetivo del +2.5% o superior.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH presenta un RSI de 29.1, también en zona de sobreventa, mostrando un intento de estabilización. Conservamos la posición actual para aprovechar la recuperación de la tendencia a corto plazo.

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
