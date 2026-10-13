# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 21:50:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.61 USD** | **$19.93 USD** | **$38.54 USD** | 🔴 **-3.64%** ($-1.46) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096256 | $103.89 | $103.18 | $9.93 | 📉 -0.68% |
| `ETH-USD` | 0.004136 | $2417.81 | $2417.81 | $10.00 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado de criptomonedas presenta una fuerte corrección reciente, con SOL-USD y ETH-USD en niveles de sobreventa extrema (RSI de 21.5 y 26.3 respectivamente), lo cual genera una oportunidad táctica de alta convicción para cazar un rebote técnico de tipo mean reversion. Mantenemos nuestra posición en SOL-USD y aprovechamos el efectivo disponible para sumar exposición en ETH-USD, respetando las reglas de gestión de riesgo y buscando capturar un rebote rápido."*

**Operaciones del ciclo:**
- **[BUY] ETH-USD** (Confianza: 88%): ETH-USD se encuentra en una profunda corrección con una caída de -4.61% en 24h y un RSI de 26.3, situándose en zona de sobreventa extrema. Aplicamos la regla táctica de cazar rebotes en cripto con alta convicción asignando $10.00 USD para buscar un rebote rápido del +3% al +5%.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD muestra un RSI extremo de 21.5 y una fuerte caída reciente, pero nos encontramos dentro de los límites del stop-loss estricto (-0.68%). Mantenemos la posición actual para permitir que se materialice el rebote técnico esperado hacia zonas de recuperación.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 21:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2417.81 | ETH-USD se encuentra en una profunda corrección con una caída de -4.61% en 24h y un RSI de... |
| `2026-10-12 21:40` | 🟢 BUY | `SOL-USD` | $10.00 | $103.89 | SOL-USD se encuentra en una situación clara de sobreventa extrema (RSI de 22.0) tras caer ... |
| `2026-10-12 21:30` | 🔴 SELL | `ETH-USD` | $11.71 | $2419.82 | La posición registra una pérdida del -2.44% bajo una tendencia bajista marcada y un RSI de... |
| `2026-10-12 21:30` | 🔴 SELL | `SOL-USD` | $22.91 | $103.78 | La posición ha acumulado una pérdida del -2.64%, acercándose peligrosamente al stop-loss e... |
| `2026-10-12 20:10` | 🟢 BUY | `SOL-USD` | $5.53 | $106.20 | SOL-USD presenta una condición de sobreventa extrema con un RSI de 24.1 y una caída de 7 d... |

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
