# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 11:50:34`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.51 USD** | **$40.51 USD** | 🟢 **+1.29%** ($+0.51) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.39 | $20.25 | 📈 +1.25% |
| `ETH-USD` | 0.006448 | $2481.58 | $2505.26 | $16.15 | 📈 +0.95% |
| `GLD` | 0.010687 | $384.58 | $384.58 | $4.11 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema con ETH-USD (RSI 28.1) y SOL-USD (RSI 25.3), manteniendo un sesgo bajista a corto plazo pero preparado para un fuerte rebote técnico (mean reversion). Por otro lado, MSFT presenta un RSI de 72.3 en zona de sobrecompra. Nuestras posiciones actuales en cripto se encuentran con ganancias moderadas pero sin alcanzar todavía el objetivo del +2.5%, por lo que decidimos mantenerlas y aprovechar el efectivo disponible para una nueva entrada táctica en GLD, que muestra un RSI de sobreventa técnica (37.9) y un impulso diario positivo del +1.57%."*

**Operaciones del ciclo:**
- **[BUY] GLD** (Confianza: 85%): Aprovechamos el efectivo disponible para cazar un rebote por sobreventa en GLD, cuyo RSI se encuentra en 37.9 con un repunte diario de 1.57%, cumpliendo perfectamente con la estrategia de alta convicción y rotación dinámica para maximizar el rendimiento del portafolio.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-10 11:50` | 🟢 BUY | `GLD` | $4.11 | $384.58 | Aprovechamos el efectivo disponible para cazar un rebote por sobreventa en GLD, cuyo RSI s... |
| `2026-10-09 19:00` | 🟢 BUY | `ETH-USD` | $5.00 | $2482.07 | ETH-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.0. Utilizando el c... |
| `2026-10-09 19:00` | 🔴 SELL | `NVDA` | $4.99 | $229.28 | Rotación activa de capital. NVDA se encuentra estancada con un rendimiento de -0.16% y un ... |
| `2026-10-09 18:50` | 🟢 BUY | `SOL-USD` | $5.00 | $108.91 | Oportunidad de alta convicción por sobreventa extrema. SOL-USD tiene un RSI de 20.2 tras u... |
| `2026-10-09 18:50` | 🔴 SELL | `QQQ` | $5.00 | $751.27 | Rotación de capital activo. QQQ se encuentra estancado con rendimiento plano (-0.06%) y si... |

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
