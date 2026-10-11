# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 10:10:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.27 USD** | **$40.27 USD** | 🟢 **+0.67%** ($+0.27) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.330438 | $109.27 | $109.32 | $36.12 | 📈 +0.04% |
| `ETH-USD` | 0.001656 | $2500.14 | $2502.06 | $4.14 | 📈 +0.08% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa técnica con SOL-USD (RSI en 21.2) y ETH-USD (RSI en 28.3) tras caídas semanales significativas, lo que activa nuestra estrategia agresiva de mean reversion y búsqueda de rebotes rápidos. El portafolio actual se encuentra totalmente invertido y sin efectivo disponible ($0.00 cash). Para poder cazar el fuerte rebote técnico inminente en ETH-USD, optamos por vender parcialmente su pequeña posición para liberar liquidez o mantener nuestras posiciones actuales si no superan los umbrales de stop-loss. Dado que ETH-USD está extremadamente sobrevendido pero estancado en este ciclo exacto con un PnL neutral, y SOL-USD concentra el mayor peso con un RSI crítico de 21.2, mantendremos SOL-USD para capturar el rebote alcista del +3% al +6%, y realizaremos un HOLD general mientras esperamos rotación de capital."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD se encuentra en una condición técnica de extrema sobreventa con un RSI de 21.2 y una caída semanal del -9.47%. Esto representa una oportunidad ideal de rebote por reversión a la media. Mantenemos la posición para capturar el movimiento alcista esperado.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD registra un RSI de 28.3, también en zona de sobreventa profunda. Mantenemos la posición actual para aprovechar la recuperación conjunta del mercado cripto sin activar ventas innecesarias con PnL cercano a cero.

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
