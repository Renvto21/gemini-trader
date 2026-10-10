# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 10:40:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.22 USD** | **$40.33 USD** | 🟢 **+0.83%** ($+0.33) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.74 | $20.13 | 📈 +0.66% |
| `ETH-USD` | 0.006448 | $2481.58 | $2495.75 | $16.09 | 📈 +0.57% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un tono mixto con fortaleza en acciones tecnológicas e índices como MSFT, QQQ y SPY, mientras que las criptomonedas se mantienen en zonas de profunda sobreventa técnica (RSI inferior a 30 en SOL-USD y ETH-USD). Nuestro portafolio se mantiene operando con ambas criptomonedas en busca del rebote por mean reversion. Dado que la reserva de efectivo actual es de 4.11 USD (alineada con la regla de mantener solo una reserva mínima de $4.00 USD) y ninguna de nuestras posiciones actuales ha alcanzado el take-profit del +2.5% ni el stop-loss, la estrategia óptima en este ciclo es mantener las posiciones activas para permitir que el rebote técnico en cripto madure."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra en condición de extrema sobreventa (RSI de 23.1). Mantenemos la posición para capturar el esperado rebote técnico hacia la zona de resistencia tras la caída semanal.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD presenta un RSI de 26.5, reflejando sobreventa clara. Sostenemos la posición actual para aprovechar la reversión a la media sin comprometer más liquidez.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-09 19:00` | 🟢 BUY | `ETH-USD` | $5.00 | $2482.07 | ETH-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.0. Utilizando el c... |
| `2026-10-09 19:00` | 🔴 SELL | `NVDA` | $4.99 | $229.28 | Rotación activa de capital. NVDA se encuentra estancada con un rendimiento de -0.16% y un ... |
| `2026-10-09 18:50` | 🟢 BUY | `SOL-USD` | $5.00 | $108.91 | Oportunidad de alta convicción por sobreventa extrema. SOL-USD tiene un RSI de 20.2 tras u... |
| `2026-10-09 18:50` | 🔴 SELL | `QQQ` | $5.00 | $751.27 | Rotación de capital activo. QQQ se encuentra estancado con rendimiento plano (-0.06%) y si... |
| `2026-10-09 18:40` | 🟢 BUY | `SOL-USD` | $5.00 | $109.02 | SOL-USD está extremadamente sobrevendido con un RSI de 20.3. Ejecutamos una compra agresiv... |

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
