# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 05:00:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.22 USD** | **$40.33 USD** | 🟢 **+0.83%** ($+0.33) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.82 | $20.15 | 📈 +0.73% |
| `ETH-USD` | 0.006448 | $2481.58 | $2492.97 | $16.07 | 📈 +0.46% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa técnica con ETH (RSI 26.0) y SOL (RSI 23.4) operando profundamente deprimidos tras caídas semanales cercanas al 10%. Esto activa nuestra estrategia cuantitativa de cazar rebotes por mean reversion. En el sector tecnológico y general, observamos fortaleza alcista en QQQ, SPY y MSFT, este último entrando en zona de sobrecompra (RSI 72.3). Dado nuestro capital actual y la reserva mínima requerida de $4.11 USD en efectivo, mantenemos nuestras posiciones actuales con alta convicción en cripto para capturar el rebote inminente, operando sin ventas precipitadas ya que ninguna posición activa ha alcanzado el objetivo de take-profit ni ha violado el stop-loss."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL se encuentra en condiciones de sobreventa extrema (RSI de 23.4) y una fuerte caída semanal del -9.63%. Mantenemos la posición para capturar el rebote técnico agresivo esperado hacia la media, cumpliendo con nuestra tesis de mean reversion.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH presenta un RSI de 26.0 y acumula un retroceso semanal del -8.57%. Las condiciones técnicas favorecen un rebote inminente, por lo que conservamos la posición para maximizar el rendimiento al alza.

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
