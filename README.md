# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 16:00:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.72 USD** | **$39.72 USD** | 🔴 **-0.69%** ($-0.28) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001175 | $2553.82 | $2511.12 | $2.95 | 📉 -1.67% |
| `SOL-USD` | 0.342237 | $109.34 | $107.44 | $36.77 | 📉 -1.74% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto y tecnológico muestra una corrección a corto plazo, con activos como SOL-USD y ETH-USD en niveles de sobreventa extrema (RSI de 25.4 y 31.4 respectivamente). Las posiciones actuales registran pérdidas menores pero controladas, sin alcanzar aún el stop-loss estricto del -2.5%. Dado el enfoque agresivo de mean reversion y captura de rebotes, mantenemos las posiciones actuales ya que presentan sobreventa atractiva y esperamos una recuperación técnica inminente para capitalizar ganancias."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra en clara sobreventa con un RSI de 25.4 tras una caída semanal del 11.05%. Aunque registra una pérdida temporal de -1.74%, la estrategia dicta cazar rebotes en sobreventa. Mantener la posición para aprovechar el rebote técnico hacia la resistencia inmediata.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un RSI de 31.4, acercándose a la zona de sobreventa profunda. La caída actual es del -1.67%, muy lejos del stop-loss estricto. Esperamos consolidación y un posterior rebote alcista dentro de la alta volatilidad del mercado cripto.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 15:40` | 🟢 BUY | `SOL-USD` | $4.00 | $107.58 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 25.6 y una caída acumulada ... |
| `2026-10-12 12:20` | 🟢 BUY | `SOL-USD` | $3.42 | $108.91 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 27.1 y una caída acumulada ... |
| `2026-10-12 12:10` | 🟢 BUY | `SOL-USD` | $10.00 | $108.93 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 27.2 y una... |
| `2026-10-12 12:01` | 🟢 BUY | `SOL-USD` | $10.00 | $109.96 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 28.5 y una caída semanal de... |
| `2026-10-12 11:50` | 🟢 BUY | `SOL-USD` | $10.00 | $110.00 | SOL-USD presenta un RSI de 28.6 indicando sobreventa extrema y una caída acumulada semanal... |

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
