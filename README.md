# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 00:00:51`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$37.28 USD** | **$41.28 USD** | 🟢 **+3.20%** ($+1.28) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.289416 | $111.58 | $111.76 | $32.35 | 📈 +0.16% |
| `ETH-USD` | 0.001940 | $2541.27 | $2542.74 | $4.93 | 📈 +0.06% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo mixto con los índices tradicionales y tecnológicas como QQQ y SPY con tendencias alcistas saludables, mientras que las criptomonedas (SOL-USD y ETH-USD) se encuentran en zonas de profunda sobreventa técnica con RSI de 27.7 y 34.5 respectivamente, tras caídas semanales significativas. Esto activa nuestra estrategia de Mean Reversion y búsqueda agresiva de rebotes alcistas de corto plazo. Mantendremos las posiciones actuales ya que muestran señales iniciales de estabilización con un cambio positivo de 24 horas y el efectivo disponible se encuentra en el límite mínimo establecido de $4.00, por lo que optamos por un enfoque HOLD en este ciclo para permitir que las posiciones maduren hacia nuestro objetivo de take-profit."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD está en condición de sobreventa extrema con un RSI de 27.7, pero muestra un rebote de 24 horas de 1.57%. Dado que nuestro capital y efectivo ya están optimizados y la posición está casi plana (0.16% PnL), mantenemos para capturar la reversión técnica hacia la media sin violar nuestros niveles de stop-loss.

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
