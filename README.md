# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 18:40:56`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$20.00 USD** | **$4.09 USD** | **$16.03 USD** | **$20.12 USD** | 🟢 **+0.62%** ($+0.12) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.017822 | $336.67 | $336.94 | $6.00 | 📈 +0.08% |
| `SPY` | 0.006458 | $774.29 | $778.56 | $5.03 | 📈 +0.55% |
| `NVDA` | 0.021772 | $229.65 | $229.52 | $5.00 | 📉 -0.06% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado general (SPY, QQQ) mantiene una tendencia alcista saludable con niveles de RSI moderados (alrededor de 55), lo que sugiere estabilidad. Las criptomonedas (BTC, SOL, ETH) muestran debilidad a corto plazo y tendencias bajistas, mientras que MSFT se encuentra en zona de sobrecompra (RSI > 72). Dado que nuestro portafolio actual está compuesto por activos sólidos en tendencia alcista (AAPL, SPY, NVDA) y nuestro efectivo disponible ($4.09) está muy cerca del límite mínimo de reserva de seguridad ($3.00), la estrategia más prudente es mantener las posiciones actuales sin realizar nuevas compras para preservar la liquidez."*

**Operaciones del ciclo:**
- **[HOLD] SPY** (Confianza: 95%): Mantenemos la posición en SPY y el resto del portafolio. El mercado se encuentra en tendencia alcista y con RSI saludable. No disponemos de suficiente efectivo libre para realizar nuevas compras significativas sin comprometer la reserva mínima de seguridad de $3.00 (actualmente tenemos $4.09 en efectivo).

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-09 18:37` | 🟢 BUY | `NVDA` | $5.00 | $229.65 | Iniciamos posición en NVDA con $5.00 USD. El activo mantiene una tendencia alcista sólida ... |
| `2026-10-09 18:37` | 🔴 SELL | `GLD` | $5.09 | $384.42 | Rotamos fuera de GLD debido a su tendencia bajista actual por debajo de la SMA20. Aprovech... |
| `2026-10-08 15:41` | 🟢 BUY | `GLD` | $5.00 | $377.27 | GLD presenta un RSI de 27.3, lo que indica condiciones de sobreventa extrema en un activo ... |
| `2026-10-08 15:23` | 🟢 BUY | `SPY` | $5.00 | $774.29 | SPY presenta una tendencia alcista sólida sobre su SMA20 y un RSI de 62.1, lo que indica q... |
| `2026-10-07 23:09` | 🟢 BUY | `AAPL` | $6.00 | $336.67 | AAPL es la opción más equilibrada del mercado actual: mantiene una tendencia alcista confi... |

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
