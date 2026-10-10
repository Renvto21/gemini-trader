# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 04:50:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.20 USD** | **$40.31 USD** | 🟢 **+0.78%** ($+0.31) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.75 | $20.13 | 📈 +0.67% |
| `ETH-USD` | 0.006448 | $2481.58 | $2491.80 | $16.07 | 📈 +0.41% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra una divergencia interesante con criptomonedas fuertemente sobrevendidas tras caídas semanales significativas (ETH-USD con RSI en 25.8 y SOL-USD con RSI en 23.1), lo que presenta una oportunidad clásica de rebote por reversión a la media (Mean Reversion). Por otro lado, activos tecnológicos y índices como MSFT entran en zonas de sobrecompra técnica (RSI 72.3), mientras que QQQ y SPY mantienen una tendencia alcista saludable. Mantendremos nuestras posiciones actuales en cripto esperando que el rebote técnico se acelere, y utilizaremos nuestro efectivo disponible para capturar momentum en activos de alta beta si es necesario, o mantener liquidez táctica."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en un estado de sobreventa extrema (RSI de 23.1) tras una caída semanal del -9.69%. Mantenemos la posición para cazar el rebote inminente hacia la media, respetando estrictamente nuestro stop-loss del -3% en caso de fallo.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD registra un RSI de 25.8 con caídas acumuladas recientes. La estructura técnica sugiere que el precio está listo para un rebote de alivio de corto plazo. Conservamos la posición para capturar la ganancia táctica.

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
