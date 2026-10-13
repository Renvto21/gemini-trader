# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 02:50:35`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.99 USD** | **$39.99 USD** | 🔴 **-0.03%** ($-0.01) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $108.15 | $31.92 | 📈 +0.91% |
| `ETH-USD` | 0.003192 | $2506.03 | $2526.26 | $8.06 | 📈 +0.81% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema con Solana (SOL-USD) en un RSI de 26.2 y Ethereum (ETH-USD) en 32.4, lo que representa una oportunidad ideal para cazar rebotes de reversión a la media. En el sector tecnológico y tradicional, MSFT ha entrado en clara sobrecompra con un RSI de 77.9. Nuestro portafolio se encuentra totalmente invertido y con ganancias marginales en SOL y ETH, por lo que mantendremos estas posiciones a la espera de un mayor impulso alcista técnico."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): A pesar de la caída semanal, SOL se encuentra en un nivel de sobreventa extrema (RSI 26.2) perfecto para buscar un rebote técnico rápido. Mantenemos la posición para capturar el movimiento alcista.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH muestra un RSI de 32.4 en zona de sobreventa, acompañando el potencial de rebote en el mercado cripto. Conservamos la posición actual para maximizar la rentabilidad en la recuperación.

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
