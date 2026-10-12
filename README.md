# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 12:50:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$36.18 USD** | **$40.18 USD** | 🟢 **+0.45%** ($+0.18) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001175 | $2553.82 | $2527.35 | $2.97 | 📉 -1.04% |
| `SOL-USD` | 0.305055 | $109.55 | $108.86 | $33.21 | 📉 -0.63% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un tono mixto con presiones bajistas en criptomonedas y activos tecnológicos de alto beta. SOL-USD presenta una condición extrema de sobreventa con un RSI de 27.1 y ETH-USD muestra un RSI de 32.5, lo cual activa nuestra estrategia de captura de rebotes por reversión a la media (Mean Reversion). Dado que nuestro efectivo actual es de apenas 4.0 USD y mantenemos una posición dominante en SOL-USD que acumula una leve pérdida pero se encuentra en zona de alta sobreventa, mantendremos las posiciones actuales para permitir el rebote técnico esperado, evitando realizar cierres anticipados en la zona de soporte y protegiendo el capital disponible según la reserva mínima establecida."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 82%): SOL-USD se encuentra en clara sobreventa técnica con un RSI de 27.1 tras una caída semanal del 9.87%. A pesar de la ligera pérdida actual (-0.63%), la regla de estrategia de rebotes técnicos nos dicta mantener y acumular en sobreventas extremas en lugar de vender en pánico, esperando el rebote de corto plazo hacia la zona de resistencia.
- **[HOLD] ETH-USD** (Confianza: 78%): ETH-USD registra un RSI de 32.5, aproximándose fuertemente a la zona de sobreventa técnica. Mantenemos la posición para capturar el movimiento de recuperación de la media junto con el ecosistema cripto.

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
