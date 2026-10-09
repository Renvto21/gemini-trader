# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 19:13:08`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.09 USD** | **$21.06 USD** | **$40.15 USD** | 🟢 **+0.39%** ($+0.15) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.017822 | $336.67 | $338.26 | $6.03 | 📈 +0.47% |
| `SPY` | 0.006458 | $774.29 | $778.96 | $5.03 | 📈 +0.60% |
| `NVDA` | 0.021772 | $229.65 | $229.71 | $5.00 | 📈 +0.03% |
| `QQQ` | 0.006656 | $751.21 | $751.21 | $5.00 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado general presenta un comportamiento mixto pero mayoritariamente alcista en los índices principales (SPY y QQQ), los cuales se mantienen sobre su SMA20 con niveles de RSI saludables (56.0 y 57.8 respectivamente). El sector tecnológico muestra fortaleza, aunque activos individuales como MSFT muestran señales de sobrecompra (RSI 72.7). Por otro lado, el sector de criptomonedas (BTC, ETH, SOL) experimenta una corrección bajista a corto plazo con niveles de RSI en zona de sobreventa extrema, lo que sugiere cautela antes de buscar reversiones. Mantenemos una postura prudente, aprovechando la alta liquidez disponible ($24.09 USD) para diversificar moderadamente sin comprometer nuestra reserva de seguridad."*

**Operaciones del ciclo:**
- **[BUY] QQQ** (Confianza: 80%): QQQ se encuentra en una tendencia alcista sólida sobre su SMA20 y con un RSI de 57.8, lo que representa un punto de entrada técnicamente favorable y sin riesgo inminente de sobrecompra. Esta adquisición de $5.00 USD nos permite diversificar el portafolio en el sector tecnológico de manera indexada, complementando nuestras posiciones individuales en AAPL y NVDA, mientras mantenemos una reserva de efectivo muy superior al mínimo requerido de $3.00 USD.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-09 19:13` | 🟢 BUY | `QQQ` | $5.00 | $751.21 | QQQ se encuentra en una tendencia alcista sólida sobre su SMA20 y con un RSI de 57.8, lo q... |
| `2026-10-09 19:07` | 💵 DEPOSIT | `CASH` | $20.00 | $1.00 | Inyección adicional de $20.00 USD de efectivo para ampliar la capacidad operativa y permit... |
| `2026-10-09 18:37` | 🟢 BUY | `NVDA` | $5.00 | $229.65 | Iniciamos posición en NVDA con $5.00 USD. El activo mantiene una tendencia alcista sólida ... |
| `2026-10-09 18:37` | 🔴 SELL | `GLD` | $5.09 | $384.42 | Rotamos fuera de GLD debido a su tendencia bajista actual por debajo de la SMA20. Aprovech... |
| `2026-10-08 15:41` | 🟢 BUY | `GLD` | $5.00 | $377.27 | GLD presenta un RSI de 27.3, lo que indica condiciones de sobreventa extrema en un activo ... |

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
