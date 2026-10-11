# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 16:30:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$37.02 USD** | **$41.02 USD** | 🟢 **+2.55%** ($+1.02) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.004740 | $2531.44 | $2532.64 | $12.01 | 📈 +0.05% |
| `SOL-USD` | 0.224836 | $111.90 | $111.26 | $25.02 | 📉 -0.58% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado general muestra un tono mixto con sesgo alcista moderado en índices tradicionales (SPY, QQQ), mientras que las criptomonedas (SOL, ETH) han sufrido caídas recientes en los últimos 7 días pero presentan condiciones técnicas claras de sobreventa extrema (RSI de SOL en 26.1 y ETH en 33.0). Mantenemos nuestra tesis de cazar rebotes en estos activos altamente volátiles para capturar movimientos rápidos de recuperación."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): A pesar de una ligera baja, SOL-USD se encuentra en clara sobreventa técnica con un RSI de 26.1, lo que activa nuestra regla de cazar rebotes por mean reversion. Mantenemos la posición para capturar el rebote alcista inminente hacia nuestro objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un RSI de 33.0 en zona de sobreventa y un ligero repunte del 1.14% en 24 horas. La posición está prácticamente plana y esperamos la continuación del rebote técnico para rotar capital o asegurar beneficios.

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
