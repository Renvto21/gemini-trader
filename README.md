# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 02:50:33`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.01 USD** | **$41.64 USD** | **$41.64 USD** | 🟢 **+4.11%** ($+1.64) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.369306 | $111.68 | $112.75 | $41.64 | 📈 +0.96% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un repunte técnico en el sector cripto con SOL-USD y ETH-USD mostrando condiciones de sobreventa previa y comenzando rebotes alcistas de corto plazo (RSI de 30.7 y 37.1 respectivamente). SOL-USD se mantiene en cartera con ganancias moderadas, mientras que MSFT muestra signos de sobrecompra (RSI en 72.3). La liquidez actual es muy baja y mantenemos una posición activa para capturar más impulso."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD muestra un RSI en zona de rebote alcista (30.7) y un cambio positivo en 24 horas del 2.47%. Aunque la ganancia actual es del 0.96%, el activo tiene espacio para continuar su recuperación técnica hacia la resistencia inmediata, por lo que decidimos mantener la posición.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 02:30` | 🟢 BUY | `SOL-USD` | $4.95 | $112.41 | SOL-USD mantiene un RSI en zona crítica de sobreventa (29.7) y un cambio positivo de 2.16%... |
| `2026-10-12 02:30` | 🔴 SELL | `ETH-USD` | $4.95 | $2553.65 | Tomamos beneficios totales en ETH-USD ya que se encuentra mostrando un rebote positivo per... |
| `2026-10-12 00:40` | 🟢 BUY | `SOL-USD` | $4.00 | $111.56 | SOL-USD muestra un RSI de 27.1, indicando una condición de sobreventa profunda tras una ca... |
| `2026-10-12 00:30` | 🟢 BUY | `ETH-USD` | $4.93 | $2542.03 | ETH-USD se encuentra en zona de clara sobreventa técnica con un RSI de 34.4 tras una caída... |
| `2026-10-12 00:20` | 🔴 SELL | `ETH-USD` | $4.93 | $2542.39 | ETH-USD se encuentra estancado con una ganancia marginal del 0.04% y bajo momentum inmedia... |

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
