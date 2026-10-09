# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 17:00:58`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.09 USD** | **$21.02 USD** | **$40.11 USD** | 🟢 **+0.28%** ($+0.11) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.017822 | $336.67 | $336.64 | $6.00 | 📉 -0.01% |
| `SPY` | 0.006458 | $774.29 | $778.54 | $5.03 | 📈 +0.55% |
| `NVDA` | 0.021772 | $229.65 | $229.28 | $4.99 | 📉 -0.16% |
| `QQQ` | 0.006652 | $751.70 | $751.27 | $5.00 | 📉 -0.06% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"Aviso temporal de Gemini (The read operation timed out). Se aplica regla de seguridad HOLD para proteger posiciones."*

**Operaciones del ciclo:**
- **[HOLD] PORTFOLIO** (Confianza: 100%): Error temporal de conexión, manteniendo posiciones de forma segura.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-09 16:26` | 🟢 BUY | `QQQ` | $5.00 | $751.70 | QQQ se encuentra en una tendencia alcista clara sobre su SMA20 y con un RSI de 58.1 que su... |
| `2026-10-09 16:07` | 💵 DEPOSIT | `CASH` | $20.00 | $1.00 | Inyección adicional de $20.00 USD de efectivo para ampliar la capacidad operativa y permit... |
| `2026-10-09 15:37` | 🟢 BUY | `NVDA` | $5.00 | $229.65 | Iniciamos posición en NVDA con $5.00 USD. El activo mantiene una tendencia alcista sólida ... |
| `2026-10-09 15:37` | 🔴 SELL | `GLD` | $5.09 | $384.42 | Rotamos fuera de GLD debido a su tendencia bajista actual por debajo de la SMA20. Aprovech... |
| `2026-10-08 12:41` | 🟢 BUY | `GLD` | $5.00 | $377.27 | GLD presenta un RSI de 27.3, lo que indica condiciones de sobreventa extrema en un activo ... |

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
