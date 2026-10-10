# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 06:40:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.25 USD** | **$40.36 USD** | 🟢 **+0.91%** ($+0.36) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.94 | $20.17 | 📈 +0.84% |
| `ETH-USD` | 0.006448 | $2481.58 | $2494.60 | $16.08 | 📈 +0.52% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto se encuentra en niveles extremos de sobreventa técnica tras caídas semanales importantes, destacando SOL-USD con un RSI de 23.8 y ETH-USD con 26.3, lo cual representa una oportunidad clara de rebote por reversión a la media. Mantendremos nuestras posiciones actuales ya que muestran ligeras ganancias y están listas para capturar el impulso alcista inminente. Por otro lado, la liquidez actual está al límite mínimo requerido ($4.11 USD), por lo que no realizaremos nuevas compras en este momento y nos enfocaremos en dejar madurar las posiciones actuales en cripto."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD presenta un RSI sobrevendido de 23.8 y acumula una caída semanal del -9.54%, ideal para un rebote técnico rápido. Nuestra posición ya está en positivo (+0.84%) y mantenemos la operativa para buscar el objetivo de +2.5% o superior.

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
