# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 07:10:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$41.33 USD** | **$41.33 USD** | 🟢 **+3.33%** ($+1.33) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.307862 | $111.77 | $111.50 | $34.33 | 📉 -0.25% |
| `ETH-USD` | 0.002742 | $2553.19 | $2553.62 | $7.00 | 📈 +0.02% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con sesgo alcista moderado en los índices principales (QQQ, SPY), mientras que el sector cripto (SOL-USD, ETH-USD) se encuentra en niveles de sobreventa técnica (RSI de 31.3 y 35.7 respectivamente) tras caídas semanales significativas, lo que presenta una oportunidad ideal para cazar rebotes por reversión a la media según la estrategia agresiva de crecimiento."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 82%): SOL-USD tiene un RSI de 31.3, muy cerca de la zona óptima de sobreventa, y aunque registra una ligera pérdida de -0.25%, el contexto técnico indica un inminente rebote alcista para capturar el objetivo de +2% a +6%. Mantenemos la posición para dejar madurar el movimiento.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD presenta un RSI de 35.7 en zona de sobreventa con un rendimiento plano actual. Mantenemos la posición esperando el impulso alcista del sector cripto para rotar o tomar ganancias rápidamente una vez alcanzado el objetivo de corto plazo.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 07:00` | 🟢 BUY | `SOL-USD` | $4.00 | $111.65 | SOL-USD está en zona de sobreventa profunda con un RSI de 31.8 y una caída semanal de -7.5... |
| `2026-10-12 06:10` | 🟢 BUY | `ETH-USD` | $2.00 | $2552.03 | ETH-USD presenta un RSI de 35.5 en clara zona de sobreventa tras caídas semanales del -5.3... |
| `2026-10-12 05:50` | 🟢 BUY | `ETH-USD` | $5.00 | $2553.65 | ETH-USD presenta un RSI de 35.7 en clara zona de sobreventa técnica tras una caída semanal... |
| `2026-10-12 05:50` | 🔴 SELL | `SOL-USD` | $5.00 | $111.85 | Liberamos una pequeña porción de SOL-USD para rescatar liquidez y financiar una entrada tá... |
| `2026-10-12 05:30` | 🔴 SELL | `ETH-USD` | $5.98 | $2553.85 | Rotación activa de capital. ETH se encuentra estancado y bajo su SMA20 con un PnL de -0.33... |

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
