# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 22:20:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.61 USD** | **$30.26 USD** | **$38.87 USD** | 🔴 **-2.82%** ($-1.13) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.193324 | $103.45 | $104.21 | $20.15 | 📈 +0.73% |
| `ETH-USD` | 0.004136 | $2417.81 | $2445.62 | $10.12 | 📈 +1.15% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de extrema sobreventa técnica con SOL-USD (RSI en 22.3) y ETH-USD (RSI en 27.6) sufriendo caídas recientes pero manteniendo nuestras posiciones en ligero terreno positivo (+0.73% y +1.15% respectivamente). Aunque presentan tendencia bajista a corto plazo, el nivel de sobreventa abre una clara oportunidad de mean reversion para buscar rebotes rápidos. En cuanto a las acciones tecnológicas, NVDA muestra un retroceso interesante con RSI en 46.4, pero nuestra prioridad táctica actual es mantener liquidez ajustada para defender las posiciones existentes en cripto y evaluar un incremento si profundizan el rebote."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra en clara sobreventa (RSI 22.3) tras caídas recientes de -6.32% en 24h. Nuestra posición tiene una ganancia actual de +0.73%. Mantenemos la posición para capturar el rebote técnico hacia la zona de take-profit sin exceder los límites de riesgo.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 22:00` | 🟢 BUY | `SOL-USD` | $10.00 | $103.02 | SOL-USD presenta un RSI extremadamente bajo de 21.3 tras una caída del -7.39% en 24 horas.... |
| `2026-10-12 21:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2417.81 | ETH-USD se encuentra en una profunda corrección con una caída de -4.61% en 24h y un RSI de... |
| `2026-10-12 21:40` | 🟢 BUY | `SOL-USD` | $10.00 | $103.89 | SOL-USD se encuentra en una situación clara de sobreventa extrema (RSI de 22.0) tras caer ... |
| `2026-10-12 21:30` | 🔴 SELL | `ETH-USD` | $11.71 | $2419.82 | La posición registra una pérdida del -2.44% bajo una tendencia bajista marcada y un RSI de... |
| `2026-10-12 21:30` | 🔴 SELL | `SOL-USD` | $22.91 | $103.78 | La posición ha acumulado una pérdida del -2.64%, acercándose peligrosamente al stop-loss e... |

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
