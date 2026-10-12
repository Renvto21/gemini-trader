# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 10:20:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$36.83 USD** | **$40.83 USD** | 🟢 **+2.08%** ($+0.83) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.307862 | $111.77 | $110.00 | $33.86 | 📉 -1.59% |
| `ETH-USD` | 0.001175 | $2553.82 | $2523.95 | $2.96 | 📉 -1.17% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto se encuentra en zona de sobreventa extrema (SOL-USD con RSI de 28.6 y ETH-USD con RSI de 32.3), lo cual representa una oportunidad ideal de mean reversion. Por otro lado, MSFT ha entrado en sobrecompra con un RSI de 72.3 y un excelente rendimiento, pero dado que nuestro portafolio está invertido en criptoactivos, mantendremos la posición actual en SOL-USD aprovechando su bajo costo y alta probabilidad de rebote técnico rápido, mientras evaluamos la gestión de liquidez."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD muestra un RSI de 28.6 en profunda sobreventa y una caída semanal de casi 9%. Estamos cerca del gatillo de stop-loss pero la alta probabilidad de un rebote técnico a corto plazo nos invita a mantener y sostener la posición para capturar el movimiento alcista.

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
