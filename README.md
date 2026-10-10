# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 10:10:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.21 USD** | **$40.32 USD** | 🟢 **+0.80%** ($+0.32) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.72 | $20.13 | 📈 +0.64% |
| `ETH-USD` | 0.006448 | $2481.58 | $2494.14 | $16.08 | 📈 +0.51% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto se encuentra en una fase de profunda sobreventa técnica, con SOL-USD y ETH-USD mostrando un RSI de 23.0 y 26.3 respectivamente, tras caídas semanales cercanas al -9% y -8%. Estas condiciones de extrema sobreventa presentan una oportunidad clásica de rebote técnico (mean reversion) para capturar movimientos alcistas rápidos. Por otro lado, los índices generales y el sector tecnológico (SPY, QQQ, NVDA) muestran estabilidad y tendencias alcistas moderadas, destacando a MSFT en zona de sobrecompra (RSI 72.3). Dado nuestro efectivo actual de $4.11 USD, mantendremos nuestras posiciones actuales en SOL-USD y ETH-USD ya que se están preparando para el rebote esperado, operando en modo HOLD para maximizar la captura del impulso sin sobreextender la liquidez."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD registra un RSI extremadamente bajo de 23.0 tras una corrección semanal del -9.72%, situándose en una clara zona de sobreventa que anticipa un rebote técnico inminente. Mantenemos la posición para capturar la recuperación de precio hacia los niveles de media.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH-USD muestra un RSI de 26.3 en condiciones de fuerte sobreventa y un retroceso semanal del -8.52%. Conservamos los títulos actuales para aprovechar la inminente reversión a la media y buscar el objetivo de ganancia rápida.

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
