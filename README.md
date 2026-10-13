# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 01:10:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$10.23 USD** | **$29.56 USD** | **$39.79 USD** | 🔴 **-0.53%** ($-0.21) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.200407 | $106.82 | $107.57 | $21.56 | 📈 +0.70% |
| `ETH-USD` | 0.003192 | $2506.03 | $2506.03 | $8.00 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de fuerte sobreventa, destacando a ETH-USD con un RSI de 31.1 y una caída semanal del 7.1%, y SOL-USD con un RSI extremo de 25.6 tras una fuerte corrección. Nuestra posición actual en SOL-USD se mantiene estable con una pequeña ganancia del 0.7%, pero las condiciones de sobreventa generalizadas en cripto abren una excelente oportunidad de rotación táctica para capturar un rebote inminente en ETH-USD, aprovechando la alta volatilidad para buscar ganancias rápidas."*

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 85%): Vendemos parcialmente SOL-USD para liberar liquidez y poder financiar la entrada en ETH-USD, cumpliendo con la regla de rotación activa de capital hacia oportunidades con fuerte potencial de rebote técnico.
- **[BUY] ETH-USD** (Confianza: 88%): ETH-USD se encuentra en clara sobreventa técnica con un RSI de 31.1 tras una caída semanal del 7.1%. Esto activa nuestra estrategia agresiva de Mean Reversion para cazar un rebote rápido del 2% al 6%.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 01:10` | 🟢 BUY | `ETH-USD` | $8.00 | $2506.03 | ETH-USD se encuentra en clara sobreventa técnica con un RSI de 31.1 tras una caída semanal... |
| `2026-10-13 01:10` | 🔴 SELL | `SOL-USD` | $16.14 | $107.57 | Vendemos parcialmente SOL-USD para liberar liquidez y poder financiar la entrada en ETH-US... |
| `2026-10-13 01:00` | 🟢 BUY | `SOL-USD` | $12.00 | $107.31 | Aprovechamos la sobreventa extrema de SOL-USD (RSI 25.3 y caída semanal de -11.16%) para i... |
| `2026-10-13 01:00` | 🔴 SELL | `ETH-USD` | $10.10 | $2504.55 | Vendemos la totalidad de ETH-USD para liberar capital líquido de inmediato y redirigirlo h... |
| `2026-10-13 00:40` | 🟢 BUY | `SOL-USD` | $3.43 | $107.26 | SOL-USD se encuentra en profunda sobreventa técnica con un RSI de 25.2 y una caída del 11.... |

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
