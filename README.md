# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 03:30:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.19 USD** | **$40.30 USD** | 🟢 **+0.76%** ($+0.30) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.67 | $20.12 | 📈 +0.59% |
| `ETH-USD` | 0.006448 | $2481.58 | $2492.89 | $16.07 | 📈 +0.46% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra oportunidades claras de rebote técnico en el sector cripto debido a niveles extremos de sobreventa (RSI de ETH en 26.9 y SOL en 21.5), cumpliendo con nuestra estrategia de cazar reversiones. Por otro lado, MSFT ha entrado en zona de sobrecompra (RSI 72.3), pero dado que nuestro portafolio actual se compone de SOL-USD y ETH-USD manteniendo ganancias moderadas pero estables y el efectivo se encuentra en el límite mínimo ($4.11 USD), decidimos mantener las posiciones actuales para capturar el rebote alcista esperado sin realizar operaciones de venta ni compra en este ciclo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL se encuentra en una condición extrema de sobreventa con un RSI de 21.5 y una fuerte caída semanal de -8.34%. Mantenemos la posición para capturar el rebote técnico agresivo hacia nuestro objetivo de take-profit, ya que aún no alcanza el umbral de +2.5% ni el stop-loss.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH muestra un RSI de 26.9, indicando clara sobreventa y potencial de reversión alcista inminente. La posición está en positivo (+0.46%) y esperamos la aceleración del precio para ejecutar ganancias.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-09 19:00` | 🟢 BUY | `ETH-USD` | $5.00 | $2482.07 | ETH-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.0. Utilizando el c... |
| `2026-10-09 19:00` | 🔴 SELL | `NVDA` | $4.99 | $229.28 | Rotación activa de capital. NVDA se encuentra estancada con un rendimiento de -0.16% y un ... |
| `2026-10-09 18:50` | 🟢 BUY | `SOL-USD` | $5.00 | $108.91 | Oportunidad de alta convicción por sobreventa extrema. SOL-USD tiene un RSI de 20.2 tras u... |
| `2026-10-09 18:50` | 🔴 SELL | `QQQ` | $5.00 | $751.27 | Rotación de capital activo. QQQ se encuentra estancado con rendimiento plano (-0.06%) y si... |
| `2026-10-09 18:40` | 🟢 BUY | `SOL-USD` | $5.00 | $109.02 | SOL-USD está extremadamente sobrevendido con un RSI de 20.3. Ejecutamos una compra agresiv... |

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
