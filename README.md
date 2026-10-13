# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 00:00:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$17.43 USD** | **$22.04 USD** | **$39.47 USD** | 🔴 **-1.34%** ($-0.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.112803 | $106.38 | $106.51 | $12.01 | 📈 +0.12% |
| `ETH-USD` | 0.004032 | $2480.01 | $2486.37 | $10.03 | 📈 +0.26% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra una correccion a corto plazo con criptomonedas como SOL-USD y ETH-USD fuertemente sobrevendidas, con RSI de 24.4 y 29.9 respectivamente, lo que representa una oportunidad ideal para cazar rebotes tecnicos siguiendo la estrategia de mean reversion. Mantenemos liquidez suficiente de 17.43 USD y decidimos retener nuestras posiciones actuales ya que muestran estabilidad inicial tras la caida."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en zona de sobreventa extrema con un RSI de 24.4. Aunque el rendimiento actual es plano, la alta volatilidad y la caida reciente de -4.25% en 24h configuran un escenario perfecto para un rebote inminente hacia la resistencia cercana.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 23:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2480.01 | Ethereum se encuentra en clara sobreventa con un RSI de 29.5 y una caída semanal del 8.06%... |
| `2026-10-12 23:40` | 🟢 BUY | `SOL-USD` | $12.00 | $106.38 | SOL-USD presenta una clara condición de sobreventa técnica extrema con RSI de 24.3 tras un... |
| `2026-10-12 23:40` | 🔴 SELL | `GLD` | $12.00 | $382.15 | Posición estancada con rendimiento de 0% sin momentum alcista. Vendo la totalidad para lib... |
| `2026-10-12 23:30` | 🟢 BUY | `GLD` | $12.00 | $382.15 | Aprovechamos la liquidez liberada y el efectivo disponible para cazar un rebote técnico en... |
| `2026-10-12 23:30` | 🔴 SELL | `ETH-USD` | $10.26 | $2479.99 | La posición registra un beneficio del +2.57%, alcanzando el objetivo de toma rápida de gan... |

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
