# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 18:20:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.02 USD** | **$36.74 USD** | **$40.77 USD** | 🟢 **+1.91%** ($+0.77) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.260810 | $111.80 | $110.21 | $28.74 | 📉 -1.42% |
| `ETH-USD` | 0.003174 | $2520.20 | $2520.20 | $8.00 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra una divergencia interesante: mientras los índices generales y acciones tecnológicas como MSFT y QQQ se mantienen estables o alcistas, activos cripto clave como SOL-USD y ETH-USD se encuentran profundamente en zona de sobreventa técnica con RSI de 22.5 y 31.1 respectivamente. Esto presenta una oportunidad clásica de reversión a la media (mean reversion) para cazar rebotes agresivos. Nuestra posición actual en SOL-USD registra una pérdida leve de -1.42%, manteniéndose muy por encima de nuestro límite de stop-loss estricto (-3.0%), y dado su RSI extremadamente bajo, el escenario sigue siendo propicio para acumular o mantener a la espera del rebote técnico."*

**Operaciones del ciclo:**
- **[BUY] ETH-USD** (Confianza: 88%): ETH-USD presenta un RSI de 31.1 y una caída acumulada del 7.04% en los últimos 7 días, situándose en una clara zona de sobreventa con alta probabilidad de un rebote técnico rápido. Aprovechamos nuestra liquidez disponible para capturar este movimiento de alta beta en línea con nuestra estrategia de cazar rebotes en cripto.

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
