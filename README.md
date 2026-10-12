# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 01:10:32`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$41.22 USD** | **$41.23 USD** | 🟢 **+3.07%** ($+1.23) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.325271 | $111.58 | $111.58 | $36.29 | 📈 -0.00% |
| `ETH-USD` | 0.001939 | $2542.03 | $2542.12 | $4.93 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo positivo general con QQQ, SPY y MSFT manteniendo tendencias alcistas, aunque algunas tecnológicas y criptomonedas han sufrido caídas recientes de 7 días. Destaca MSFT con un RSI de 72.3 en zona de sobrecompra. En cripto, SOL-USD muestra un RSI fuertemente en sobreventa (27.2) y ETH-USD también está deprimido con RSI de 34.4, lo que representa una excelente oportunidad para acumular en el dip bajo nuestra estrategia de agresividad y mean reversion."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD se encuentra en un estado de sobreventa extrema (RSI de 27.2) tras una caída semanal del 7.59%. Mantenemos la posición para capturar el rebote técnico inminente hacia la zona de recuperación rápida.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 00:40` | 🟢 BUY | `SOL-USD` | $4.00 | $111.56 | SOL-USD muestra un RSI de 27.1, indicando una condición de sobreventa profunda tras una ca... |
| `2026-10-12 00:30` | 🟢 BUY | `ETH-USD` | $4.93 | $2542.03 | ETH-USD se encuentra en zona de clara sobreventa técnica con un RSI de 34.4 tras una caída... |
| `2026-10-12 00:20` | 🔴 SELL | `ETH-USD` | $4.93 | $2542.39 | ETH-USD se encuentra estancado con una ganancia marginal del 0.04% y bajo momentum inmedia... |
| `2026-10-11 23:10` | 🟢 BUY | `ETH-USD` | $4.93 | $2541.27 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 34.2 y una caída semanal ... |
| `2026-10-11 23:00` | 🔴 SELL | `ETH-USD` | $3.92 | $2541.25 | La posicion en ETH-USD esta estancada y representa un monto muy pequeno ($3.92) sin sufici... |

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
