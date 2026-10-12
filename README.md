# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 21:50:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.01 USD** | **$41.23 USD** | **$41.24 USD** | 🟢 **+3.10%** ($+1.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.289416 | $111.58 | $111.63 | $32.31 | 📈 +0.04% |
| `ETH-USD` | 0.003508 | $2542.73 | $2542.73 | $8.92 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo mixto con oportunidades claras de rebote técnico en criptomonedas fuertemente castigadas durante la semana. SOL-USD mantiene un RSI en zona de extrema sobreventa (27.3), pero se encuentra estancado cerca de su precio de entrada sin momentum inmediato. Por otro lado, ETH-USD presenta una excelente oportunidad de entrada por mean reversion con un RSI de 34.5 y una fuerte caída semanal del -6.21%. Dado que operamos con capital limitado y requerimos rotación dinámica, venderemos parcialmente SOL-USD para liberar liquidez y cazar el rebote de alta convicción en ETH-USD."*

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 85%): Liberamos una fracción de la posición en SOL-USD que se encuentra estancada con rendimiento cercano a 0% para capitalizar liquidez y financiar la entrada en ETH-USD que muestra mejores condiciones de rebote inminente.
- **[BUY] ETH-USD** (Confianza: 90%): ETH-USD está en condiciones de clara sobreventa técnica (RSI de 34.5) tras una caída semanal del -6.21%, ideal para una estrategia agresiva de mean reversion buscando un rebote rápido del 3% al 5%.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 21:50` | 🟢 BUY | `ETH-USD` | $8.92 | $2542.73 | ETH-USD está en condiciones de clara sobreventa técnica (RSI de 34.5) tras una caída seman... |
| `2026-10-11 21:50` | 🔴 SELL | `SOL-USD` | $8.93 | $111.63 | Liberamos una fracción de la posición en SOL-USD que se encuentra estancada con rendimient... |
| `2026-10-11 21:20` | 🟢 BUY | `SOL-USD` | $4.24 | $111.11 | Aprovechamos el capital liberado para incrementar la exposición en SOL-USD. Se encuentra e... |
| `2026-10-11 21:20` | 🔴 SELL | `ETH-USD` | $4.24 | $2534.63 | Vendemos la totalidad de la posición en ETH-USD (valorada en aproximadamente 4.24 USD) par... |
| `2026-10-11 21:10` | 🟢 BUY | `SOL-USD` | $3.82 | $111.13 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 25.7 y una caída semanal de... |

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
