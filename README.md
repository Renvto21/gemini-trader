# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 22:10:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.13 USD** | **$40.24 USD** | 🟢 **+0.61%** ($+0.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.50 | $20.09 | 📈 +0.44% |
| `ETH-USD` | 0.006448 | $2481.58 | $2488.38 | $16.04 | 📈 +0.27% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto presenta una fuerte condición de sobreventa técnica con SOL-USD (RSI 20.9) y ETH-USD (RSI 26.1) en niveles extremos, sugiriendo un inminente rebote por reversión a la media. El sector tecnológico (QQQ, NVDA) se mantiene alcista pero extendido. Mantendremos la exposición máxima actual en SOL y ETH para capturar el rebote violento esperado, respetando el límite de reserva de efectivo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 90%): SOL-USD se encuentra en una sobreventa extrema con un RSI de 20.9. Actualmente nuestra posición está ligeramente en positivo (+0.44%). Dado que ya tenemos una asignación fuerte ($20.09) y el efectivo está al límite de la reserva mínima ($4.11), mantenemos la posición para capturar el rebote técnico esperado hacia la SMA20.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH-USD muestra un RSI de 26.1, lo que indica un claro agotamiento de la fuerza vendedora. Con un PnL plano (+0.27%) y sin liquidez extra para promediar (reserva en $4.11), la mejor decisión táctica es mantener la posición para maximizar el retorno del rebote inminente.

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
