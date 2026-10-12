# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 15:50:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.72 USD** | **$39.73 USD** | 🔴 **-0.68%** ($-0.27) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001175 | $2553.82 | $2506.29 | $2.94 | 📉 -1.86% |
| `SOL-USD` | 0.342237 | $109.34 | $107.47 | $36.78 | 📉 -1.71% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema, destacando SOL-USD con un RSI de 25.4 y ETH-USD con un RSI de 31.1, lo cual activa nuestra estrategia de búsqueda de rebotes técnicos (mean reversion). Nuestras posiciones actuales están experimentando una ligera contracción dentro del rango permitido antes de activar el stop-loss estricto. Mantendremos el capital en cripto aprovechando la alta volatilidad para cazar un rebote rápido, sin realizar operaciones de venta en este momento ya que aún no alcanzamos el umbral de pérdida del -3.0% ni tenemos exceso de efectivo inactivo para rotar."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD presenta un RSI de 25.4 en profunda sobreventa y una caída del 11% en 7 días. Mantenemos la posición para capturar el rebote técnico inminente sin tocar el stop-loss del -3.0%.

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
