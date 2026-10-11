# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 13:50:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.16 USD** | **$22.11 USD** | **$41.27 USD** | 🟢 **+3.16%** ($+1.27) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.004740 | $2531.44 | $2548.62 | $12.08 | 📈 +0.68% |
| `SOL-USD` | 0.089453 | $111.79 | $112.08 | $10.03 | 📈 +0.26% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo alcista moderado en los índices y en las grandes tecnológicas como MSFT y QQQ, mientras que las criptomonedas (SOL y ETH) están rebotando desde niveles de sobreventa técnica tras caídas semanales significativas. SOL se encuentra en un RSI de 28.7 y ETH en 35.3, lo que representa una excelente oportunidad de mean reversion. Mantendremos nuestras posiciones actuales ya que muestran ganancias iniciales y un buen momentum de recuperación a corto plazo, aprovechando el efectivo disponible para una nueva entrada táctica en cripto o rotación si fuera necesario, pero respetando la reserva mínima de liquidez."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL se encuentra en plena zona de rebote por sobreventa técnica (RSI 28.7) tras una caída semanal del -7.18%. Muestra un intento de recuperación del +1.86% en 24h. Mantenemos la posición para capturar el objetivo de +3% a +6% de ganancia rápida.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 13:40` | 🟢 BUY | `SOL-USD` | $10.00 | $111.79 | SOL-USD presenta una excelente oportunidad de rebote técnico de alta convicción al encontr... |
| `2026-10-11 13:30` | 🔴 SELL | `SOL-USD` | $19.04 | $111.95 | SOL-USD ha alcanzado un rendimiento cercano a nuestra meta de take-profit del 2.5% (+2.43%... |
| `2026-10-11 13:20` | 🟢 BUY | `ETH-USD` | $12.00 | $2531.44 | ETH-USD se encuentra en zona de profunda sobreventa técnica con un RSI de 32.8 y una caída... |
| `2026-10-11 13:10` | 🔴 SELL | `ETH-USD` | $9.99 | $2530.10 | ETH-USD se encuentra estancado con un P&L cercano a 0% (-0.06%) y bajo tendencia bajista e... |
| `2026-10-11 13:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2531.65 | ETH-USD se encuentra en clara sobreventa técnica con un RSI de 32.8 y una fuerte caída sem... |

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
