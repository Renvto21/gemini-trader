# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 15:00:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$35.80 USD** | **$39.80 USD** | 🔴 **-0.50%** ($-0.20) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001175 | $2553.82 | $2509.09 | $2.95 | 📉 -1.75% |
| `SOL-USD` | 0.305055 | $109.55 | $107.69 | $32.85 | 📉 -1.70% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo bajista temporal en activos de alto beta y criptomonedas debido a caídas recientes, pero esto genera excelentes oportunidades de sobreventa técnica (mean reversion). ETH-USD y SOL-USD se encuentran con RSI profundamente deprimidos (31.3 y 25.7 respectivamente), acumulando caídas semanales importantes. Aunque estamos cerca del stop-loss en SOL-USD (-1.7%), la sobreventa extrema sugiere un rebote inminente. Por otro lado, MSFT ha entrado en clara sobrecompra (RSI 77.6) y GLD muestra debilidad con RSI en 34.7. Mantendremos nuestras posiciones actuales en cripto aprovechando el descuento y la volatilidad para buscar el rebote alcista rápido."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 82%): A pesar de una pérdida actual de -1.7%, el RSI de SOL-USD se encuentra en un nivel extremadamente bajista de 25.7, lo que indica sobreventa profunda. Esto activa nuestra estrategia de captura de rebotes técnicos (mean reversion). Mantendremos la posición para capturar el repunte inminente hacia la media.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 12:20` | 🟢 BUY | `SOL-USD` | $3.42 | $108.91 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 27.1 y una caída acumulada ... |
| `2026-10-12 12:10` | 🟢 BUY | `SOL-USD` | $10.00 | $108.93 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 27.2 y una... |
| `2026-10-12 12:01` | 🟢 BUY | `SOL-USD` | $10.00 | $109.96 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 28.5 y una caída semanal de... |
| `2026-10-12 11:50` | 🟢 BUY | `SOL-USD` | $10.00 | $110.00 | SOL-USD presenta un RSI de 28.6 indicando sobreventa extrema y una caída acumulada semanal... |
| `2026-10-12 11:40` | 🔴 SELL | `SOL-USD` | $37.42 | $108.72 | Activación del stop-loss estricto debido a que la posición ha caído un -2.58%, rompiendo e... |

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
