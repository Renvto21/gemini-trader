# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 19:50:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.07 USD** | **$40.18 USD** | 🟢 **+0.45%** ($+0.18) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.18 | $20.03 | 📈 +0.14% |
| `ETH-USD` | 0.006448 | $2481.58 | $2487.59 | $16.04 | 📈 +0.24% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto presenta condiciones extremas de sobreventa técnica con RSI en niveles altamente deprimidos (SOL en 20.4 y ETH en 25.9), lo que configura un escenario propicio para un rebote por reversión a la media (mean reversion). Mientras los índices de renta variable tradicional (QQQ y SPY) muestran fortaleza moderada, el mayor potencial asimétrico de corto plazo (+2% a +6%) reside en sostener la exposición en criptoactivos castigados. Con el efectivo en $4.11 USD, alineado estrictamente a la reserva mínima obligatoria de $4.00 USD, no hay margen de liquidez adicional sin liquidar activos, por lo que la postura táctica óptima es mantener posiciones a la espera del catalizador de rebote."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 90%): SOL se ubica en sobreventa profunda con RSI 14 de 20.4 y una contracción de -8.75% a 7 días. La posición está en ligera ganancia (+0.14%) y tiene un ratio riesgo-beneficio altamente favorable para capturar el rebote hacia los objetivos de toma de ganancias de +2.5% a +6%.
- **[HOLD] ETH-USD** (Confianza: 88%): ETH mantiene RSI en 25.9 con un inicio de recuperación intradía (+0.63%). La posición acumula +0.24% de beneficio, lejos de los niveles de stop-loss y con alta probabilidad de continuar la recuperación técnica hacia la resistencia inmediata.

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
