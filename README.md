# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 18:56:07`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$20.00 USD** | **$4.09 USD** | **$16.04 USD** | **$20.14 USD** | 🟢 **+0.69%** ($+0.14) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.017822 | $336.67 | $337.53 | $6.02 | 📈 +0.26% |
| `SPY` | 0.006458 | $774.29 | $778.83 | $5.03 | 📈 +0.59% |
| `NVDA` | 0.021772 | $229.65 | $229.57 | $5.00 | 📉 -0.03% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"Error al consultar Gemini (503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}). Se aplica regla de seguridad HOLD."*

**Operaciones del ciclo:**
- **[HOLD] PORTFOLIO** (Confianza: 100%): Error de conexión o API, manteniendo posiciones.

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
