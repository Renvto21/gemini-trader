# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 14:30:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.31 USD** | **$40.42 USD** | 🟢 **+1.05%** ($+0.42) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.91 | $20.16 | 📈 +0.81% |
| `ETH-USD` | 0.006448 | $2481.58 | $2504.18 | $16.15 | 📈 +0.91% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra señales mixtas con criptomonedas fuertemente deprimidas en el corto plazo pero presentando condiciones extremas de sobreventa técnica (RSI de SOL en 23.7 y ETH en 28.0), lo cual representa una oportunidad ideal para nuestra estrategia agresiva de rebotes (mean reversion). Por otro lado, Microsoft (MSFT) ha entrado en zona de sobrecompra clara (RSI 72.3), mientras que activos tecnológicos de alto beta como NVDA y QQQ mantienen una tendencia estable alcista. Mantendremos nuestras posiciones actuales en cripto aprovechando el profundo descuento y la sobreventa, y esperaremos a que alcancen nuestro objetivo de take-profit o acumulaciones adicionales de efectivo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL se encuentra en un estado de sobreventa extrema con un RSI de 23.7 y una caída semanal de -9.56%. Nuestra posición actual muestra una ligera ganancia de +0.81%. Mantenemos la posición para capturar el rebote técnico esperado hacia la resistencia inmediata, cumpliendo con la estrategia de cazar sobreventas en cripto.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH muestra un RSI de 28.0, profundamente en territorio de sobreventa, alineado con nuestra tesis de rebote inminente. El rendimiento actual es de +0.91%. Conservamos la posición para buscar el objetivo de +2.5% o superior antes de rotar el capital.

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
