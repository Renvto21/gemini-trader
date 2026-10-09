# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 19:19:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.09 USD** | **$21.07 USD** | **$40.16 USD** | 🟢 **+0.41%** ($+0.16) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.017822 | $336.67 | $338.50 | $6.03 | 📈 +0.54% |
| `SPY` | 0.006458 | $774.29 | $778.98 | $5.03 | 📈 +0.61% |
| `NVDA` | 0.021772 | $229.65 | $229.83 | $5.00 | 📈 +0.08% |
| `QQQ` | 0.006656 | $751.21 | $751.48 | $5.00 | 📈 +0.04% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado de renta variable (SPY, QQQ, AAPL, NVDA) mantiene una tendencia alcista saludable por encima de sus medias móviles de 20 días, con niveles de RSI neutrales a moderados (entre 49 y 58), lo que sugiere continuidad pero sin euforia extrema. Por otro lado, el sector de criptomonedas (BTC, ETH, SOL) y el oro (GLD) muestran debilidad técnica a corto plazo con tendencias bajistas, aunque con niveles de sobreventa notables en el caso de las altcoins. Adoptamos una postura prudente de mantener nuestras posiciones actuales para consolidar ganancias y preservar un nivel elevado de liquidez (cercano al 47% del portafolio) ante posibles repuntes de volatilidad."*

**Operaciones del ciclo:**
- **[HOLD] SPY** (Confianza: 90%): Mantenemos nuestra posición en el SPY y el resto del portafolio sin cambios. El mercado accionario sigue en tendencia alcista con un RSI saludable de 56.0, pero dado que ya contamos con una exposición diversificada en tecnología y mercado general (AAPL, NVDA, QQQ, SPY) y que los activos alternativos muestran tendencias bajistas, la opción más prudente y cuantitativa es no forzar nuevas operaciones y conservar nuestra sólida reserva de efectivo de $19.09 USD.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-09 19:13` | 🟢 BUY | `QQQ` | $5.00 | $751.21 | QQQ se encuentra en una tendencia alcista sólida sobre su SMA20 y con un RSI de 57.8, lo q... |
| `2026-10-09 19:07` | 💵 DEPOSIT | `CASH` | $20.00 | $1.00 | Inyección adicional de $20.00 USD de efectivo para ampliar la capacidad operativa y permit... |
| `2026-10-09 18:37` | 🟢 BUY | `NVDA` | $5.00 | $229.65 | Iniciamos posición en NVDA con $5.00 USD. El activo mantiene una tendencia alcista sólida ... |
| `2026-10-09 18:37` | 🔴 SELL | `GLD` | $5.09 | $384.42 | Rotamos fuera de GLD debido a su tendencia bajista actual por debajo de la SMA20. Aprovech... |
| `2026-10-08 15:41` | 🟢 BUY | `GLD` | $5.00 | $377.27 | GLD presenta un RSI de 27.3, lo que indica condiciones de sobreventa extrema en un activo ... |

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
