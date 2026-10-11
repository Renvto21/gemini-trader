# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 09:20:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.37 USD** | **$40.37 USD** | 🟢 **+0.93%** ($+0.37) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.330438 | $109.27 | $109.62 | $36.22 | 📈 +0.32% |
| `ETH-USD` | 0.001656 | $2500.14 | $2504.07 | $4.15 | 📈 +0.16% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un tono mixto con sesgo alcista en indices y tech tradicionales, mientras que las criptomonedas (SOL y ETH) se encuentran en condiciones extremas de sobreventa con RSI de 21.5 y 28.5 respectivamente, tras caídas semanales significativas. El portafolio actual se encuentra completamente invertido sin liquidez en efectivo, manteniendo posiciones estables en SOL-USD y ETH-USD."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en una situación de sobreventa extrema (RSI 21.5) tras una caída semanal del -9.22%. Aunque la tendencia es bajista a corto plazo, el nivel actual presenta un potencial claro de rebote técnico (mean reversion) hacia la zona de resistencia superior, por lo que se mantiene la posición para capturar el movimiento alcista inminente.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 08:40` | 🟢 BUY | `ETH-USD` | $4.14 | $2500.14 | ETH-USD se encuentra en clara sobreventa con un RSI de 28.2 y una caída de 7.78% en los úl... |
| `2026-10-11 08:00` | 🔴 SELL | `ETH-USD` | $4.14 | $2498.90 | Vendemos la posición completa de ETH-USD para liberar 4.14 USD en efectivo. Aunque está en... |
| `2026-10-11 05:00` | 🟢 BUY | `ETH-USD` | $4.14 | $2499.59 | ETH-USD presenta un RSI de 28.2, lo que indica una clara condición de sobreventa técnica t... |
| `2026-10-11 04:50` | 🟢 BUY | `SOL-USD` | $12.00 | $109.36 | Alta convicción en el rebote técnico de Solana tras una caída semanal del -9.43% y un RSI ... |
| `2026-10-11 04:50` | 🔴 SELL | `ETH-USD` | $16.12 | $2500.30 | Rotamos capital fuera de ETH-USD para asegurar una pequeña ganancia del +0.75% y liberar l... |

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
