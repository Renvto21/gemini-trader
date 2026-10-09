# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 18:37:04`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$20.00 USD** | **$4.09 USD** | **$16.03 USD** | **$20.12 USD** | 🟢 **+0.61%** ($+0.12) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.017822 | $336.67 | $336.62 | $6.00 | 📉 -0.01% |
| `SPY` | 0.006458 | $774.29 | $778.59 | $5.03 | 📈 +0.56% |
| `NVDA` | 0.021772 | $229.65 | $229.65 | $5.00 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un comportamiento mixto. Mientras que los índices de acciones (SPY, QQQ) y tecnológicas (NVDA, AAPL, MSFT) mantienen tendencias alcistas saludables, el oro (GLD) y las criptomonedas (BTC, ETH, SOL) muestran debilidad a corto plazo cotizando por debajo de sus medias móviles de 20 días. MSFT se encuentra en zona de sobrecompra (RSI > 72). Optamos por una rotación estratégica para salir de activos con tendencia bajista y posicionarnos en líderes tecnológicos con tendencia alcista y RSI saludable."*

**Operaciones del ciclo:**
- **[SELL] GLD** (Confianza: 80%): Rotamos fuera de GLD debido a su tendencia bajista actual por debajo de la SMA20. Aprovechamos para asegurar una ganancia del 1.9% y liberar liquidez para activos con mejor momentum.
- **[BUY] NVDA** (Confianza: 85%): Iniciamos posición en NVDA con $5.00 USD. El activo mantiene una tendencia alcista sólida sobre la SMA20 y un RSI saludable de 53.4, ofreciendo un excelente punto de entrada en comparación con otros gigantes tecnológicos sobrecomprados.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-09 18:37` | 🟢 BUY | `NVDA` | $5.00 | $229.65 | Iniciamos posición en NVDA con $5.00 USD. El activo mantiene una tendencia alcista sólida ... |
| `2026-10-09 18:37` | 🔴 SELL | `GLD` | $5.09 | $384.42 | Rotamos fuera de GLD debido a su tendencia bajista actual por debajo de la SMA20. Aprovech... |
| `2026-10-08 15:41` | 🟢 BUY | `GLD` | $5.00 | $377.27 | GLD presenta un RSI de 27.3, lo que indica condiciones de sobreventa extrema en un activo ... |
| `2026-10-08 15:23` | 🟢 BUY | `SPY` | $5.00 | $774.29 | SPY presenta una tendencia alcista sólida sobre su SMA20 y un RSI de 62.1, lo que indica q... |
| `2026-10-07 23:09` | 🟢 BUY | `AAPL` | $6.00 | $336.67 | AAPL es la opción más equilibrada del mercado actual: mantiene una tendencia alcista confi... |

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
