# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 00:30:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.22 USD** | **$40.33 USD** | 🟢 **+0.83%** ($+0.33) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.47 | $20.08 | 📈 +0.41% |
| `ETH-USD` | 0.006448 | $2481.58 | $2503.24 | $16.14 | 📈 +0.87% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra resiliencia en los principales índices tecnológicos (QQQ, SPY) con tendencias alcistas estables, mientras que el sector cripto (ETH-USD y SOL-USD) se encuentra en niveles de profunda sobreventa técnica con RSI en 27.8 y 22.1 respectivamente, tras caídas semanales significativas. Mantenemos nuestras posiciones actuales en cripto a la espera de un fuerte rebote técnico (mean reversion) respaldado por la agresiva estrategia de crecimiento. Dado que nuestra liquidez actual se encuentra en el límite mínimo deseado ($4.11 USD) y nuestras posiciones actuales operan con ganancias estables pero aún sin alcanzar el objetivo de take-profit del +2.5%, decidimos mantener la estructura actual para maximizar la captura del rebote en curso."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD presenta un RSI extremadamente bajo de 22.1 y una caída de casi -10% en 7 días, lo que configura una oportunidad perfecta de rebote técnico por sobreventa. Mantenemos la posición para capturar el movimiento alcista inminente hacia nuestra meta de take-profit.

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
