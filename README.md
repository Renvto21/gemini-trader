# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 19:00:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.02 USD** | **$36.81 USD** | **$40.84 USD** | 🟢 **+2.09%** ($+0.84) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.260810 | $111.80 | $110.42 | $28.80 | 📉 -1.23% |
| `ETH-USD` | 0.003174 | $2520.20 | $2525.18 | $8.02 | 📈 +0.20% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo técnico mixto con oportunidades claras de rebote en criptoactivos debido a condiciones extremas de sobreventa. SOL-USD presenta un RSI crítico de 23.3 y ETH-USD muestra un RSI de 31.9, ideales para estrategias de Mean Reversion. Mantenemos una postura agresiva para aprovechar estos niveles de descuento mientras preservamos liquidez."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): A pesar de la ligera caída de -1.23%, SOL-USD tiene un RSI extremadamente bajo de 23.3, lo que indica sobreventa profunda y un potencial rebote técnico inminente hacia la zona de recuperación. Mantenemos la posición para capturar el impulso alcista.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD se encuentra en una zona de sobreventa con un RSI de 31.9 y registra una pequeña ganancia del 0.2%. Mantenemos la posición a la espera de un movimiento alcista más fuerte alineado con nuestra estrategia de rotación y captura de rebotes.

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
