# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 16:50:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$37.07 USD** | **$41.07 USD** | 🟢 **+2.68%** ($+1.07) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.004740 | $2531.44 | $2535.40 | $12.02 | 📈 +0.16% |
| `SOL-USD` | 0.224836 | $111.90 | $111.43 | $25.05 | 📉 -0.42% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo positivo general con los índices principales como SPY y QQQ operando alcistas sobre la SMA20. En el sector cripto, SOL-USD y ETH-USD presentan condiciones extremas de sobreventa con RSI de 26.7 y 33.4 respectivamente, lo cual activa nuestra estrategia de reversión a la media (mean reversion) para buscar rebotes rápidos. Dado que estamos totalmente investidos y con la liquidez mínima de $4.00 USD, y ninguna posición actual cumple el criterio de take-profit superior al +2.5% o stop-loss estricto, mantenemos nuestras posiciones actuales para permitirles desarrollar su rebote técnico."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en clara sobreventa técnica con un RSI de 26.7 y una caída semanal del -7.72%, pero mostrando un intento de recuperación de +1.27% en 24h. Mantenemos la posición para capturar el rebote esperado según la estrategia de reversión a la media.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 14:10` | 🟢 BUY | `SOL-USD` | $5.16 | $111.90 | SOL-USD presenta un RSI de 28.2 indicando sobreventa clara tras una caída semanal del 7.33... |
| `2026-10-11 14:00` | 🟢 BUY | `SOL-USD` | $10.00 | $112.02 | SOL-USD se encuentra en clara sobreventa tecnica con un RSI de 28.5 tras una caida semanal... |
| `2026-10-11 13:40` | 🟢 BUY | `SOL-USD` | $10.00 | $111.79 | SOL-USD presenta una excelente oportunidad de rebote técnico de alta convicción al encontr... |
| `2026-10-11 13:30` | 🔴 SELL | `SOL-USD` | $19.04 | $111.95 | SOL-USD ha alcanzado un rendimiento cercano a nuestra meta de take-profit del 2.5% (+2.43%... |
| `2026-10-11 13:20` | 🟢 BUY | `ETH-USD` | $12.00 | $2531.44 | ETH-USD se encuentra en zona de profunda sobreventa técnica con un RSI de 32.8 y una caída... |

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
