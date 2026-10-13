# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 06:50:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.57 USD** | **$39.57 USD** | 🔴 **-1.08%** ($-0.43) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $106.92 | $31.56 | 📉 -0.24% |
| `ETH-USD` | 0.003192 | $2506.03 | $2508.51 | $8.01 | 📈 +0.10% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra claras señales de sobreventa extrema en SOL-USD (RSI de 26.8) y un intento de rebote en ETH-USD (RSI en 35.9). Dado nuestro enfoque agresivo de mean reversion y captura de momentum, SOL-USD se encuentra en una zona óptima para acumular más debido al descuento acumulado de -8% en los últimos 7 días. Por otro lado, ETH-USD muestra un rendimiento positivo del 2.62% en 24h, indicando el inicio del rebote técnico esperado, pero se mantiene estable mientras priorizamos la consolidación de nuestra apuesta fuerte en Solana."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD tiene un RSI de 26.8, lo que indica sobreventa profunda, y una caída semanal del -8%. Mantenemos la posición actual valorada en $31.56 USD esperando el rebote técnico agresivo hacia la resistencia superior, alineado con nuestra estrategia de buscar retornos rápidos del +2% al +6%.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD está rebotando con un +2.62% en las últimas 24 horas y un RSI saliendo de zonas de sobreventa a 35.9. Mantenemos la posición actual para dejar que capture más impulso antes de tomar beneficios.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 02:30` | 🟢 BUY | `SOL-USD` | $4.00 | $108.19 | SOL-USD presenta un RSI extremadamente bajo de 26.3, lo que indica sobreventa técnica seve... |
| `2026-10-13 01:30` | 🟢 BUY | `SOL-USD` | $6.23 | $107.75 | SOL-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.8 tras una caída s... |
| `2026-10-13 01:10` | 🟢 BUY | `ETH-USD` | $8.00 | $2506.03 | ETH-USD se encuentra en clara sobreventa técnica con un RSI de 31.1 tras una caída semanal... |
| `2026-10-13 01:10` | 🔴 SELL | `SOL-USD` | $16.14 | $107.57 | Vendemos parcialmente SOL-USD para liberar liquidez y poder financiar la entrada en ETH-US... |
| `2026-10-13 01:00` | 🟢 BUY | `SOL-USD` | $12.00 | $107.31 | Aprovechamos la sobreventa extrema de SOL-USD (RSI 25.3 y caída semanal de -11.16%) para i... |

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
