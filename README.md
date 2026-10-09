# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 18:53:31`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$20.00 USD** | **$4.09 USD** | **$16.02 USD** | **$20.12 USD** | 🟢 **+0.59%** ($+0.12) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.017822 | $336.67 | $336.75 | $6.00 | 📈 +0.02% |
| `SPY` | 0.006458 | $774.29 | $778.46 | $5.03 | 📈 +0.54% |
| `NVDA` | 0.021772 | $229.65 | $229.44 | $5.00 | 📉 -0.09% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado de renta variable estadounidense (SPY, QQQ) mantiene una tendencia técnica alcista sólida por encima de sus medias móviles de 20 días con osciladores RSI en terreno neutral y saludable (47 a 58), a excepción de MSFT que muestra signos de sobrecompra (RSI 72.6). En contraste, el sector cripto y el oro permanecen bajo presión técnica con tendencias bajistas debajo de la SMA20. Dado que el efectivo disponible ($4.09 USD) debe mantener un colchón mínimo de seguridad de $3.00 USD, el capital libre operable es de apenas $1.09 USD, insuficiente para una nueva asignación responsable sin desbalancear la cartera."*

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 85%): AAPL mantiene una estructura alcista por encima de su SMA20 con un RSI neutral de 47.4. La posición se encuentra prácticamente a precio de entrada sin justificación técnica ni fundamental para tomar pérdidas o cerrar la posición.
- **[HOLD] SPY** (Confianza: 90%): SPY continúa marcando tendencia positiva por encima de la SMA20 con un RSI saludable de 55.5 y leve rendimiento acumulado a favor. Actúa como el pilar diversificado del portafolio, por lo que se mantiene la posición.

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
