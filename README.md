# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 18:40:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.02 USD** | **$36.82 USD** | **$40.84 USD** | 🟢 **+2.11%** ($+0.84) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.260810 | $111.80 | $110.46 | $28.81 | 📉 -1.20% |
| `ETH-USD` | 0.003174 | $2520.20 | $2524.32 | $8.01 | 📈 +0.16% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de profunda sobreventa técnica, destacando SOL-USD con un RSI de 23.4 y ETH-USD con 31.7, lo cual activa nuestra estrategia de cazar rebotes por mean reversion. En el sector tecnológico y general, MSFT se encuentra en sobrecompra (RSI 72.3), mientras que el efectivo disponible está en los niveles mínimos requeridos, permitiéndonos mantener el foco en la gestión de nuestras posiciones actuales de alta volatilidad."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): A pesar de encontrarse en una ligera pérdida del -1.2%, el RSI de 23.4 indica una sobreventa extrema que favorece un rebote técnico inminente en el corto plazo. Mantenemos la posición para capturar la recuperación.
- **[HOLD] ETH-USD** (Confianza: 80%): La posición se mantiene prácticamente estable con una ganancia marginal del 0.16%. Con un RSI de 31.7, el activo está listo para acompañar el rebote técnico general del sector cripto.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 18:20` | 🟢 BUY | `ETH-USD` | $8.00 | $2520.20 | ETH-USD presenta un RSI de 31.1 y una caída acumulada del 7.04% en los últimos 7 días, sit... |
| `2026-10-11 17:50` | 🔴 SELL | `ETH-USD` | $12.02 | $2536.22 | ETH-USD se encuentra estancado con una ganancia mínima de +0.19% y bajo una tendencia baji... |
| `2026-10-11 17:40` | 🟢 BUY | `SOL-USD` | $4.00 | $111.14 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 25.7 y una... |
| `2026-10-11 14:10` | 🟢 BUY | `SOL-USD` | $5.16 | $111.90 | SOL-USD presenta un RSI de 28.2 indicando sobreventa clara tras una caída semanal del 7.33... |
| `2026-10-11 14:00` | 🟢 BUY | `SOL-USD` | $10.00 | $112.02 | SOL-USD se encuentra en clara sobreventa tecnica con un RSI de 28.5 tras una caida semanal... |

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
