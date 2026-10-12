# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 09:20:34`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$37.07 USD** | **$41.08 USD** | 🟢 **+2.70%** ($+1.08) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.307862 | $111.77 | $110.74 | $34.09 | 📉 -0.93% |
| `ETH-USD` | 0.001175 | $2553.82 | $2538.59 | $2.98 | 📉 -0.60% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto se encuentra en condiciones de sobreventa extrema a corto plazo (SOL-USD con RSI de 29.6 y ETH-USD con RSI de 33.6), lo cual representa una oportunidad táctica de reversión a la media según nuestra estrategia agresiva. Por otro lado, los mercados de renta variable (QQQ, SPY, MSFT) muestran resiliencia y tendencia alcista, destacando MSFT en zona de sobrecompra (RSI 72.3). Mantendremos nuestra posición en cripto para capturar el rebote técnico y no realizaremos ventas en este ciclo ya que ninguna posición ha tocado el stop-loss estricto ni el take-profit, encontrándose con ligeras pérdidas temporales dentro del rango aceptable."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD está profundamente sobrevendido con un RSI de 29.6 tras una caída semanal del 8.32%. Aunque presenta una pérdida no realizada de -0.93%, la estrategia agresiva de caza de rebotes dicta mantener y esperar la reversión alcista hacia la media sin vender prematuramente.

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
