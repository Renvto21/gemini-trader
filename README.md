# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 15:50:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.41 USD** | **$40.52 USD** | 🟢 **+1.30%** ($+0.52) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.24 | $20.22 | 📈 +1.12% |
| `ETH-USD` | 0.006448 | $2481.58 | $2510.39 | $16.19 | 📈 +1.16% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un tono mixto con sesgo alcista en los índices principales y tecnológicas de gran capitalización. Destaca la situación de sobreventa extrema en criptomonedas clave como SOL-USD (RSI de 24.8) y ETH-USD (RSI de 29.0), lo cual representa una oportunidad clara de rebote técnico (mean reversion). Nuestras posiciones actuales en SOL-USD y ETH-USD muestran ganancias moderadas (+1.12% y +1.16% respectivamente), pero aún no alcanzan el objetivo de take-profit del +2.5% ni están en sobrecompra, por lo que se mantienen para capturar mayor impulso. Dado que nuestra liquidez en efectivo es de $4.11 USD (alineada con la regla de mantener una reserva mínima de $4.00 USD), no disponemos de capital libre adicional para nuevas compras sin liquidar posiciones existentes. Por lo tanto, mantenemos el portafolio actual esperando que el rebote en cripto alcance la zona objetivo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): La posición tiene un RSI extremadamente bajo de 24.8, indicando sobreventa profunda y potencial de rebote alcista. Aunque muestra una ganancia leve de +1.12%, el objetivo es capturar un movimiento completo hacia el +2.5% o superior antes de tomar ganancias.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD se encuentra en condiciones de sobreventa técnica (RSI de 29.0). Mantenemos la posición actual con un PnL positivo del +1.16% a la espera de un mayor impulso alcista que permita asegurar beneficios.

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
