# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 00:10:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$7.43 USD** | **$32.06 USD** | **$39.49 USD** | 🔴 **-1.28%** ($-0.51) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.206603 | $106.48 | $106.61 | $22.03 | 📈 +0.12% |
| `ETH-USD` | 0.004032 | $2480.01 | $2488.96 | $10.04 | 📈 +0.36% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un tono de cautela con criptomonedas fuertemente presionadas a la baja en la última semana. SOL-USD presenta un RSI extremadamente bajo de 24.5 y ETH-USD se sitúa en 30.0, lo que representa condiciones claras de sobreventa y una oportunidad perfecta para cazar rebotes de reversión a la media. Mantendremos las posiciones actuales ya que están cerca del punto de entrada y el efectivo disponible se desplegará en la mejor oportunidad técnica."*

**Operaciones del ciclo:**
- **[BUY] SOL-USD** (Confianza: 90%): SOL-USD se encuentra en una clara condición de sobreventa con un RSI de 24.5 y una caída del -11.74% en los últimos 7 días. Bajo nuestra estrategia agresiva de Mean Reversion, este nivel ofrece una excelente oportunidad para acumular en el dip y capturar un rebote rápido del 3% al 5%.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 00:10` | 🟢 BUY | `SOL-USD` | $10.00 | $106.61 | SOL-USD se encuentra en una clara condición de sobreventa con un RSI de 24.5 y una caída d... |
| `2026-10-12 23:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2480.01 | Ethereum se encuentra en clara sobreventa con un RSI de 29.5 y una caída semanal del 8.06%... |
| `2026-10-12 23:40` | 🟢 BUY | `SOL-USD` | $12.00 | $106.38 | SOL-USD presenta una clara condición de sobreventa técnica extrema con RSI de 24.3 tras un... |
| `2026-10-12 23:40` | 🔴 SELL | `GLD` | $12.00 | $382.15 | Posición estancada con rendimiento de 0% sin momentum alcista. Vendo la totalidad para lib... |
| `2026-10-12 23:30` | 🟢 BUY | `GLD` | $12.00 | $382.15 | Aprovechamos la liquidez liberada y el efectivo disponible para cazar un rebote técnico en... |

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
