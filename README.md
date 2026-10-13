# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 05:20:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.12 USD** | **$40.12 USD** | 🟢 **+0.30%** ($+0.12) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $108.56 | $32.05 | 📈 +1.29% |
| `ETH-USD` | 0.003192 | $2506.03 | $2529.04 | $8.07 | 📈 +0.92% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un rebote técnico interesante en el sector cripto. SOL-USD y ETH-USD están recuperando terreno tras caídas semanales, con SOL registrando un RSI de 31.2 y ETH en 38.0, lo que confirma oportunidades de sobreventa. Por otro lado, MSFT presenta un RSI de 77.9 (sobrecompra clara), pero no lo tenemos en cartera. Mantendremos la exposición actual en criptomonedas ya que están generando un momentum positivo a corto plazo y acercándose a nuestros objetivos de take-profit."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD muestra un incremento del 2.84% en 24h y un RSI de 31.2 tras una fuerte caída semanal, ideal para cazar rebotes. Está cerca de la zona de take-profit (+2.5%), por lo que decidimos mantener para maximizar la ganancia.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD sube un 3.46% en 24h con un RSI de 38.0. La posición está ganando tracción alcista tras tocar niveles de sobreventa, por lo que merece la pena mantenerla en busca de un mayor recorrido.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 02:30` | 🟢 BUY | `SOL-USD` | $4.00 | $108.19 | SOL-USD presenta un RSI extremadamente bajo de 26.3, lo que indica sobreventa técnica seve... |
| `2026-10-13 01:30` | 🟢 BUY | `SOL-USD` | $6.23 | $107.75 | SOL-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.8 tras una caída s... |
| `2026-10-13 01:10` | 🟢 BUY | `ETH-USD` | $8.00 | $2506.03 | ETH-USD se encuentra en clara sobreventa técnica con un RSI de 31.1 tras una caída semanal... |
| `2026-10-13 01:10` | 🔴 SELL | `SOL-USD` | $16.14 | $107.57 | Vendemos parcialmente SOL-USD para liberar liquidez y poder financiar la entrada en ETH-US... |
| `2026-10-13 01:00` | 🟢 BUY | `SOL-USD` | $12.00 | $107.31 | Aprovechamos la sobreventa extrema de SOL-USD (RSI 25.3 y caída semanal de -11.16%) para i... |

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
