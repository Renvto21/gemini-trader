# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 03:01:00`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$6.92 USD** | **$34.72 USD** | **$41.64 USD** | 🟢 **+4.10%** ($+1.64) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.219306 | $111.68 | $112.74 | $24.72 | 📈 +0.95% |
| `ETH-USD` | 0.003904 | $2561.78 | $2561.78 | $10.00 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un tono mixto con sesgo alcista moderado en los índices principales (SPY y QQQ con tendencias firmes sobre sus medias móviles). En el sector cripto, observamos señales claras de sobreventa en ETH-USD (RSI 37) y SOL-USD (RSI 30.7) tras caídas semanales, lo que presenta una oportunidad ideal de rebote técnico. Nuestra posición actual en SOL-USD muestra un modesto beneficio del +0.95%, pero sin el impulso necesario a corto plazo. Conviene vender parte de SOL-USD para liberar liquidez y capturar una oportunidad fresca en ETH-USD, que muestra mayor fuerza en 24h (+2.31%) y está en zona óptima de reversión."*

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 82%): Vendemos parcialmente SOL-USD para capitalizar una pequeña ganancia y liberar efectivo, permitiendo la rotación dinámica de capital hacia un activo con mejor configuración de rebote técnico.
- **[BUY] ETH-USD** (Confianza: 88%): ETH-USD se encuentra en clara sobreventa técnica (RSI de 37) y muestra un repunte del 2.31% en las últimas 24 horas, lo que cumple perfectamente con nuestra estrategia de cazar rebotes en cripto con alta convicción.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 03:01` | 🟢 BUY | `ETH-USD` | $10.00 | $2561.78 | ETH-USD se encuentra en clara sobreventa técnica (RSI de 37) y muestra un repunte del 2.31... |
| `2026-10-12 03:01` | 🔴 SELL | `SOL-USD` | $16.91 | $112.74 | Vendemos parcialmente SOL-USD para capitalizar una pequeña ganancia y liberar efectivo, pe... |
| `2026-10-12 02:30` | 🟢 BUY | `SOL-USD` | $4.95 | $112.41 | SOL-USD mantiene un RSI en zona crítica de sobreventa (29.7) y un cambio positivo de 2.16%... |
| `2026-10-12 02:30` | 🔴 SELL | `ETH-USD` | $4.95 | $2553.65 | Tomamos beneficios totales en ETH-USD ya que se encuentra mostrando un rebote positivo per... |
| `2026-10-12 00:40` | 🟢 BUY | `SOL-USD` | $4.00 | $111.56 | SOL-USD muestra un RSI de 27.1, indicando una condición de sobreventa profunda tras una ca... |

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
