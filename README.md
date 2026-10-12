# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 00:10:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$37.24 USD** | **$41.24 USD** | 🟢 **+3.10%** ($+1.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.289416 | $111.58 | $111.62 | $32.30 | 📈 +0.03% |
| `ETH-USD` | 0.001940 | $2541.27 | $2542.33 | $4.93 | 📈 +0.04% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo mixto con criptomonedas fuertemente sobrevendidas tras caídas semanales, destacando SOL-USD con un RSI de 27.3 y ETH-USD con un RSI de 34.4, lo cual activa nuestra estrategia de mean reversion y búsqueda de rebotes de corto plazo. Por otro lado, activos tecnológicos y de gran capitalización en EE.UU. como MSFT presentan un RSI de 72.3, entrando en zona de sobrecompra. Nuestra liquidez está ajustada al mínimo de $4.00 USD y nuestras posiciones actuales se mantienen estancadas con rendimientos cercanos a 0%."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 82%): SOL-USD presenta condiciones extremas de sobreventa con un RSI de 27.3 y un intento de rebote en 24 horas del +1.44%. Mantenemos la posición para capturar el rebote técnico objetivo hacia el +3% o +5% de ganancia.
- **[HOLD] ETH-USD** (Confianza: 78%): ETH-USD muestra un RSI de 34.4, cerca de la zona de sobreventa técnica. Mantenemos la posición actual valorada en $4.93 USD esperando una recuperación junto al resto del sector cripto.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 23:10` | 🟢 BUY | `ETH-USD` | $4.93 | $2541.27 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 34.2 y una caída semanal ... |
| `2026-10-11 23:00` | 🔴 SELL | `ETH-USD` | $3.92 | $2541.25 | La posicion en ETH-USD esta estancada y representa un monto muy pequeno ($3.92) sin sufici... |
| `2026-10-11 22:00` | 🔴 SELL | `ETH-USD` | $5.00 | $2542.93 | Vendemos parcialmente la posición en ETH-USD para liberar efectivo y cumplir con la regla ... |
| `2026-10-11 21:50` | 🟢 BUY | `ETH-USD` | $8.92 | $2542.73 | ETH-USD está en condiciones de clara sobreventa técnica (RSI de 34.5) tras una caída seman... |
| `2026-10-11 21:50` | 🔴 SELL | `SOL-USD` | $8.93 | $111.63 | Liberamos una fracción de la posición en SOL-USD que se encuentra estancada con rendimient... |

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
