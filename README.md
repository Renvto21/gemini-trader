# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 18:00:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$12.02 USD** | **$28.99 USD** | **$41.01 USD** | 🟢 **+2.52%** ($+1.01) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.260810 | $111.80 | $111.14 | $28.99 | 📉 -0.59% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con sesgo alcista moderado en el sector tecnológico y el S&P 500, mientras que las criptomonedas como SOL y ETH se encuentran en niveles de sobreventa técnica profunda (RSI de 25.7 y 33.3 respectivamente) tras caídas recientes de 7 días. Nuestra posición actual en SOL-USD registra una leve pérdida del -0.59%, manteniéndose muy por encima de nuestro stop-loss estricto del -3.0%. Con un RSI extremadamente bajo en SOL y un intento de rebote diario del +1.01%, se presentan condiciones óptimas para mantener la posición y buscar la reversión alcista hacia el objetivo del +3% al +5%, manteniendo la disciplina de liquidez y rotación."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 82%): La posición en SOL-USD muestra un RSI de 25.7 indicando clara sobreventa y un inicio de recuperación en 24 horas (+1.01%). La pérdida actual de -0.59% está muy lejos de nuestro límite de stop-loss (-3.0%). Mantenemos la posición para capturar el rebote técnico esperado hacia la resistencia inmediata.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 17:50` | 🔴 SELL | `ETH-USD` | $12.02 | $2536.22 | ETH-USD se encuentra estancado con una ganancia mínima de +0.19% y bajo una tendencia baji... |
| `2026-10-11 17:40` | 🟢 BUY | `SOL-USD` | $4.00 | $111.14 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 25.7 y una... |
| `2026-10-11 14:10` | 🟢 BUY | `SOL-USD` | $5.16 | $111.90 | SOL-USD presenta un RSI de 28.2 indicando sobreventa clara tras una caída semanal del 7.33... |
| `2026-10-11 14:00` | 🟢 BUY | `SOL-USD` | $10.00 | $112.02 | SOL-USD se encuentra en clara sobreventa tecnica con un RSI de 28.5 tras una caida semanal... |
| `2026-10-11 13:40` | 🟢 BUY | `SOL-USD` | $10.00 | $111.79 | SOL-USD presenta una excelente oportunidad de rebote técnico de alta convicción al encontr... |

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
