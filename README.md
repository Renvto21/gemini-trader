# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 16:00:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$37.03 USD** | **$41.03 USD** | 🟢 **+2.58%** ($+1.03) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.004740 | $2531.44 | $2531.85 | $12.00 | 📈 +0.02% |
| `SOL-USD` | 0.224836 | $111.90 | $111.33 | $25.03 | 📉 -0.51% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra resiliencia general con los índices principales y valores tecnológicos (QQQ, SPY, MSFT) operando en tendencia alcista. En particular, MSFT ha entrado en zona de sobrecompra (RSI 72.3), lo que indica fortaleza pero también proximidad a una pausa. Por otro lado, las criptomonedas continúan con caídas acumuladas en 7 días pero muestran fuertes señales de rebote por sobreventa técnica: SOL-USD tiene un RSI de 26.4 y ETH-USD de 32.9. Mantengo mis posiciones actuales en cripto buscando aprovechar este rebote táctico de mean reversion, y opero con la liquidez disponible para capitalizar oportunidades puntuales."*

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD se encuentra en clara sobreventa técnica con un RSI de 32.9 y comenzando a mostrar un repunte del 1.11% en 24 horas. Mantengo la posición para capturar el rebote alcista esperado.
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD registra un RSI extremadamente bajo de 26.4, lo que representa una oportunidad clásica de mean reversion y rebote técnico de alta convicción a pesar de la ligera caída acumulada de la semana.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 14:10` | 🟢 BUY | `SOL-USD` | $5.16 | $111.90 | SOL-USD presenta un RSI de 28.2 indicando sobreventa clara tras una caída semanal del 7.33... |
| `2026-10-11 14:00` | 🟢 BUY | `SOL-USD` | $10.00 | $112.02 | SOL-USD se encuentra en clara sobreventa tecnica con un RSI de 28.5 tras una caida semanal... |
| `2026-10-11 13:40` | 🟢 BUY | `SOL-USD` | $10.00 | $111.79 | SOL-USD presenta una excelente oportunidad de rebote técnico de alta convicción al encontr... |
| `2026-10-11 13:30` | 🔴 SELL | `SOL-USD` | $19.04 | $111.95 | SOL-USD ha alcanzado un rendimiento cercano a nuestra meta de take-profit del 2.5% (+2.43%... |
| `2026-10-11 13:20` | 🟢 BUY | `ETH-USD` | $12.00 | $2531.44 | ETH-USD se encuentra en zona de profunda sobreventa técnica con un RSI de 32.8 y una caída... |

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
