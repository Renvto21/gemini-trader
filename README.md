# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 12:00:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.52 USD** | **$40.52 USD** | 🟢 **+1.31%** ($+0.52) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.39 | $20.25 | 📈 +1.25% |
| `ETH-USD` | 0.006448 | $2481.58 | $2506.90 | $16.16 | 📈 +1.02% |
| `MSFT` | 0.007681 | $535.07 | $535.07 | $4.11 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema (RSI de SOL en 25.3 y ETH en 28.4), lo que presenta una oportunidad clásica de mean reversion para capturar rebotes técnicos rápidos. GLD se encuentra estancado y sin momentum, por lo que rotaremos su capital hacia MSFT, que presenta un fuerte impulso alcista con un RSI en sobrecompra moderada pero confirmando tendencia alcista."*

**Operaciones del ciclo:**
- **[SELL] GLD** (Confianza: 85%): Liberamos la totalidad de la posición en GLD ya que se encuentra estancada con 0% de PnL y sin momentum, permitiendo rotar este capital hacia oportunidades de mayor crecimiento en tech y cripto.
- **[BUY] MSFT** (Confianza: 88%): Aprovechamos el capital liberado de GLD para entrar en MSFT, que muestra un fuerte momentum alcista con un incremento del 2.38% en 24h y tendencia clara sobre la SMA20, alineándose con nuestra estrategia de alta convicción.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-10 12:00` | 🟢 BUY | `MSFT` | $4.11 | $535.07 | Aprovechamos el capital liberado de GLD para entrar en MSFT, que muestra un fuerte momentu... |
| `2026-10-10 12:00` | 🔴 SELL | `GLD` | $4.11 | $384.58 | Liberamos la totalidad de la posición en GLD ya que se encuentra estancada con 0% de PnL y... |
| `2026-10-10 11:50` | 🟢 BUY | `GLD` | $4.11 | $384.58 | Aprovechamos el efectivo disponible para cazar un rebote por sobreventa en GLD, cuyo RSI s... |
| `2026-10-09 19:00` | 🟢 BUY | `ETH-USD` | $5.00 | $2482.07 | ETH-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.0. Utilizando el c... |
| `2026-10-09 19:00` | 🔴 SELL | `NVDA` | $4.99 | $229.28 | Rotación activa de capital. NVDA se encuentra estancada con un rendimiento de -0.16% y un ... |

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
