# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 09:00:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$37.13 USD** | **$41.13 USD** | 🟢 **+2.83%** ($+1.13) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.307862 | $111.77 | $110.90 | $34.14 | 📉 -0.78% |
| `ETH-USD` | 0.001175 | $2553.82 | $2543.23 | $2.99 | 📉 -0.41% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con sesgo alcista en los índices principales y acciones tecnológicas como MSFT, la cual ha entrado en sobrecompra (RSI 72.3). Por otro lado, las criptomonedas continúan con caídas semanales y SOL-USD se encuentra claramente en zona de sobreventa extrema con un RSI de 29.9, lo que representa una oportunidad ideal de rebote por mean reversion. Mantendremos SOL-USD y aprovecharemos la sobreventa para buscar el rebote técnico hacia la media."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 82%): SOL-USD está en condiciones de sobreventa extrema con un RSI de 29.9, cumpliendo nuestra regla táctica de cazar rebotes en cripto. Aunque registra una pequeña pérdida actual de -0.78%, el nivel técnico es ideal para mantener y esperar el rebote alcista hacia el objetivo del +3%.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 07:40` | 🟢 BUY | `ETH-USD` | $3.00 | $2553.82 | ETH-USD presenta un RSI de 35.7 indicando condiciones cercanas a la sobreventa, lo que act... |
| `2026-10-12 07:30` | 🔴 SELL | `ETH-USD` | $7.00 | $2553.60 | ETH-USD se encuentra estancado con un PnL cercano a 0% sin momentum inmediato. Vendemos la... |
| `2026-10-12 07:00` | 🟢 BUY | `SOL-USD` | $4.00 | $111.65 | SOL-USD está en zona de sobreventa profunda con un RSI de 31.8 y una caída semanal de -7.5... |
| `2026-10-12 06:10` | 🟢 BUY | `ETH-USD` | $2.00 | $2552.03 | ETH-USD presenta un RSI de 35.5 en clara zona de sobreventa tras caídas semanales del -5.3... |
| `2026-10-12 05:50` | 🟢 BUY | `ETH-USD` | $5.00 | $2553.65 | ETH-USD presenta un RSI de 35.7 en clara zona de sobreventa técnica tras una caída semanal... |

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
