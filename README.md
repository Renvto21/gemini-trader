# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 21:00:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$41.08 USD** | **$41.08 USD** | 🟢 **+2.70%** ($+1.08) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.296859 | $111.70 | $111.21 | $33.01 | 📉 -0.44% |
| `ETH-USD` | 0.001674 | $2520.20 | $2533.84 | $4.24 | 📈 +0.54% |
| `MSFT` | 0.007144 | $535.07 | $535.07 | $3.82 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con sesgo alcista moderado en los índices y acciones tecnológicas (SPY y QQQ sobre SMA20), mientras que las criptomonedas como SOL-USD y ETH-USD presentan condiciones técnicas de sobreventa extrema (RSI de 26.0 y 33.2 respectivamente) tras caídas semanales significativas. Esto representa una oportunidad ideal para cazar rebotes técnicos (mean reversion) manteniendo una postura táctica agresiva."*

**Operaciones del ciclo:**
- **[SELL] ETH-USD** (Confianza: 80%): Tomamos una ganancia parcial en ETH-USD (que muestra un PnL de +0.54%) para liberar capital en efectivo y financiar nuevas oportunidades de alto rendimiento o asegurar liquidez.
- **[BUY] MSFT** (Confianza: 85%): MSFT muestra un fuerte momentum alcista con un incremento de 2.38% en 24 horas y un RSI en zona de sobrecompra técnica (72.3), alineado con nuestra estrategia de capturar movimientos rápidos de crecimiento acelerado y alta beta.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 21:00` | 🟢 BUY | `MSFT` | $3.82 | $535.07 | MSFT muestra un fuerte momentum alcista con un incremento de 2.38% en 24 horas y un RSI en... |
| `2026-10-11 21:00` | 🔴 SELL | `ETH-USD` | $3.80 | $2533.84 | Tomamos una ganancia parcial en ETH-USD (que muestra un PnL de +0.54%) para liberar capita... |
| `2026-10-11 20:00` | 🟢 BUY | `SOL-USD` | $4.00 | $110.96 | SOL-USD se encuentra en una clara condicion de sobreventa tecnica profunda con un RSI de 2... |
| `2026-10-11 18:20` | 🟢 BUY | `ETH-USD` | $8.00 | $2520.20 | ETH-USD presenta un RSI de 31.1 y una caída acumulada del 7.04% en los últimos 7 días, sit... |
| `2026-10-11 17:50` | 🔴 SELL | `ETH-USD` | $12.02 | $2536.22 | ETH-USD se encuentra estancado con una ganancia mínima de +0.19% y bajo una tendencia baji... |

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
