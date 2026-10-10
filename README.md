# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 06:20:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.26 USD** | **$40.37 USD** | 🟢 **+0.94%** ($+0.37) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.99 | $20.18 | 📈 +0.89% |
| `ETH-USD` | 0.006448 | $2481.58 | $2494.88 | $16.09 | 📈 +0.54% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra una divergencia clara entre las criptomonedas, que se encuentran fuertemente sobrevendidas (SOL con RSI de 24.0 y ETH con RSI de 26.4 tras caídas semanales cercanas al -9%), y los índices tradicionales o tecnológicas líderes como MSFT que ya presentan sobrecompra (RSI en 72.3). Dado nuestro enfoque cuantitativo de agresividad y mean reversion en cripto, mantenemos nuestras posiciones actuales en SOL-USD y ETH-USD aprovechando el profundo descuento técnico, mientras el efectivo disponible se encuentra en el límite mínimo establecido de $4.11 USD. No ejecutaremos ventas de ganancia aún porque ninguna posición ha alcanzado el umbral del +2.5% o RSI sobrecompra, y tampoco hay pérdidas que activen el stop-loss estricto."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD presenta un RSI extremadamente bajo de 24.0, lo que indica condiciones claras de sobreventa y un potencial rebote técnico inminente hacia nuestra meta de +2.5% a +6%. El PnL actual es de +0.89%, por lo que mantenemos la posición esperando capturar mayor impulso alcista.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD muestra un RSI de 26.4 y una caída semanal del -8.5%, configurando una sólida oportunidad de reversión a la media. Mantenemos la posición actual para dejar correr las ganancias y buscar el objetivo de toma de beneficios.

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
