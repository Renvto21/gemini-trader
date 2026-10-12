# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 21:10:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$41.06 USD** | **$41.06 USD** | 🟢 **+2.64%** ($+1.06) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.331256 | $111.64 | $111.13 | $36.81 | 📉 -0.45% |
| `ETH-USD` | 0.001674 | $2520.20 | $2534.99 | $4.24 | 📈 +0.59% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un tono mixto con sesgo alcista en índices tecnológicos y tradicionales como QQQ y SPY, mientras que las criptomonedas presentan condiciones ideales de sobreventa (RSI de SOL-USD en 25.7 y ETH-USD en 33.3), lo que activa nuestra estrategia táctica de rebote por reversión a la media. En acciones, MSFT ha entrado en sobrecompra con un RSI de 72.3, cumpliendo nuestra regla de toma rápida de ganancias."*

**Operaciones del ciclo:**
- **[SELL] MSFT** (Confianza: 90%): MSFT ha alcanzado un RSI de 72.3 en zona de sobrecompra y acumula un avance sólido. Ejecutamos la toma de ganancias según las reglas operativas para liberar efectivo y rotar capital.
- **[BUY] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en clara sobreventa técnica con un RSI de 25.7 y una caída semanal del 7.97%. Aprovechamos el efectivo recién liberado para cazar un rebote agresivo por mean reversion.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 21:10` | 🟢 BUY | `SOL-USD` | $3.82 | $111.13 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 25.7 y una caída semanal de... |
| `2026-10-11 21:10` | 🔴 SELL | `MSFT` | $3.82 | $535.07 | MSFT ha alcanzado un RSI de 72.3 en zona de sobrecompra y acumula un avance sólido. Ejecut... |
| `2026-10-11 21:00` | 🟢 BUY | `MSFT` | $3.82 | $535.07 | MSFT muestra un fuerte momentum alcista con un incremento de 2.38% en 24 horas y un RSI en... |
| `2026-10-11 21:00` | 🔴 SELL | `ETH-USD` | $3.80 | $2533.84 | Tomamos una ganancia parcial en ETH-USD (que muestra un PnL de +0.54%) para liberar capita... |
| `2026-10-11 20:00` | 🟢 BUY | `SOL-USD` | $4.00 | $110.96 | SOL-USD se encuentra en una clara condicion de sobreventa tecnica profunda con un RSI de 2... |

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
