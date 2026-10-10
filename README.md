# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 08:30:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.16 USD** | **$40.27 USD** | 🟢 **+0.68%** ($+0.27) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.50 | $20.09 | 📈 +0.44% |
| `ETH-USD` | 0.006448 | $2481.58 | $2492.91 | $16.07 | 📈 +0.46% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra resiliencia en los índices principales y tecnología, mientras que las criptomonedas (SOL-USD y ETH-USD) se encuentran en niveles extremos de sobreventa técnica con RSI en 22.3 y 26.0 respectivamente tras caídas semanales significativas. Mantenemos nuestras posiciones actuales esperando el rebote de reversión a la media, y con un efectivo de 4.11 USD cumplimos exactamente con la reserva mínima requerida, por lo que optamos por mantener (HOLD) para dejar que las posiciones maduren hacia nuestro objetivo de take-profit."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD presenta un RSI extremadamente bajo de 22.3, lo que indica una fuerte sobreventa y un potencial inminente de rebote técnico. Dado que nuestras ganancias actuales son marginales (+0.44%) y no hemos alcanzado el take-profit del 2.5%, mantenemos la posición para capturar el movimiento alcista.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD se mantiene en una zona de sobreventa profunda con un RSI de 26.0 tras una corrección semanal del -8.57%. Con el efectivo al límite de la reserva mínima permitida ($4.11 USD), la estrategia óptima es retener la posición para aprovechar la esperada recuperación de impulso en cripto.

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
