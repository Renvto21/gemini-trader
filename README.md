# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 09:50:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.29 USD** | **$40.29 USD** | 🟢 **+0.72%** ($+0.29) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.330438 | $109.27 | $109.38 | $36.14 | 📈 +0.10% |
| `ETH-USD` | 0.001656 | $2500.14 | $2502.32 | $4.14 | 📈 +0.09% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra señales mixtas, con un sesgo alcista moderado en índices tradicionales (SPY y QQQ) y acciones tecnológicas como MSFT que ha entrado en sobrecompra con un RSI de 72.3. Por otro lado, las criptomonedas principales se encuentran en zonas de marcada sobreventa técnica, destacando SOL-USD con un RSI extremadamente bajo de 21.2 y una caída del 7d_pct de -9.42%, y ETH-USD con un RSI de 28.4. Bajo nuestra estrategia agresiva de mean reversion y captura de rebotes, esto representa una oportunidad ideal de compra en los activos digitales sobrevendidos, manteniendo la exposición actual mientras se busca maximizar el potencial de rebote alcista."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en una situación clásica de sobreventa extrema con un RSI de 21.2 tras una caída semanal del 9.42%. Mantenemos la posición actual con alta convicción para capturar el rebote técnico inminente hacia la media, sin realizar ventas ya que aún no alcanza el objetivo de take-profit ni activa el stop-loss.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD presenta un RSI de 28.4, mostrando también condiciones de sobreventa técnica. Mantenemos la posición actual para aprovechar la recuperación esperada en el sector cripto junto con SOL-USD.

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
