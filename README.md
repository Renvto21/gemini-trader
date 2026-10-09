# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 16:26:58`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.09 USD** | **$21.05 USD** | **$40.14 USD** | 🟢 **+0.35%** ($+0.14) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.017822 | $336.67 | $337.31 | $6.01 | 📈 +0.19% |
| `SPY` | 0.006458 | $774.29 | $779.08 | $5.03 | 📈 +0.62% |
| `NVDA` | 0.021772 | $229.65 | $229.82 | $5.00 | 📈 +0.07% |
| `QQQ` | 0.006652 | $751.70 | $751.70 | $5.00 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado de renta variable estadounidense mantiene una estructura alcista sólida, con índices como SPY y QQQ cotizando por encima de su SMA20 y con niveles de RSI saludables (56.1 y 58.1 respectivamente), lo que indica fuerza sin llegar a la sobrecompra. Las criptomonedas (ETH, SOL) muestran una fuerte corrección técnica con niveles de sobreventa extrema (RSI < 25), pero debido a su tendencia bajista actual, preferimos priorizar la estabilidad de la renta variable. Mantendremos nuestras posiciones actuales en AAPL, SPY y NVDA, las cuales se encuentran en terreno positivo, y añadiremos una posición moderada en QQQ para diversificar el portafolio tecnológico aprovechando su tendencia favorable."*

**Operaciones del ciclo:**
- **[BUY] QQQ** (Confianza: 85%): QQQ se encuentra en una tendencia alcista clara sobre su SMA20 y con un RSI de 58.1 que sugiere espacio para continuar al alza. La compra de $5.00 USD respeta los límites de gestión de riesgo, diversifica nuestra exposición tecnológica y mantiene un nivel de efectivo muy saludable de $19.09 USD, muy por encima del mínimo requerido de $3.00 USD.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-09 16:26` | 🟢 BUY | `QQQ` | $5.00 | $751.70 | QQQ se encuentra en una tendencia alcista clara sobre su SMA20 y con un RSI de 58.1 que su... |
| `2026-10-09 16:07` | 💵 DEPOSIT | `CASH` | $20.00 | $1.00 | Inyección adicional de $20.00 USD de efectivo para ampliar la capacidad operativa y permit... |
| `2026-10-09 15:37` | 🟢 BUY | `NVDA` | $5.00 | $229.65 | Iniciamos posición en NVDA con $5.00 USD. El activo mantiene una tendencia alcista sólida ... |
| `2026-10-09 15:37` | 🔴 SELL | `GLD` | $5.09 | $384.42 | Rotamos fuera de GLD debido a su tendencia bajista actual por debajo de la SMA20. Aprovech... |
| `2026-10-08 12:41` | 🟢 BUY | `GLD` | $5.00 | $377.27 | GLD presenta un RSI de 27.3, lo que indica condiciones de sobreventa extrema en un activo ... |

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
