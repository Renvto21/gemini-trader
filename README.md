# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 18:25:26`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.09 USD** | **$36.02 USD** | **$40.11 USD** | 🟢 **+0.28%** ($+0.11) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.017822 | $336.67 | $336.64 | $6.00 | 📉 -0.01% |
| `SPY` | 0.006458 | $774.29 | $778.57 | $5.03 | 📈 +0.55% |
| `NVDA` | 0.021772 | $229.65 | $229.28 | $4.99 | 📉 -0.16% |
| `QQQ` | 0.006652 | $751.70 | $751.27 | $5.00 | 📉 -0.06% |
| `SOL-USD` | 0.091676 | $109.08 | $109.08 | $10.00 | 📈 +0.00% |
| `ETH-USD` | 0.002015 | $2481.72 | $2481.72 | $5.00 | 📈 -0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado tecnológico (QQQ, SPY) mantiene una tendencia alcista saludable sobre la SMA20, mientras que el sector cripto ha sufrido una fuerte corrección reciente, dejando a activos de alta beta como SOL-USD y ETH-USD en niveles de sobreventa extrema (RSI de 20.3 y 24.9 respectivamente). Esta divergencia presenta una oportunidad de oro para aplicar nuestra estrategia de reversión a la media (Mean Reversion) de alta convicción, desplegando la liquidez ociosa en busca de rebotes rápidos del +2% al +6%. Mantendremos las posiciones actuales de acciones estables y rotaremos el efectivo hacia el riesgo cripto sobrevendido."*

**Operaciones del ciclo:**
- **[BUY] SOL-USD** (Confianza: 90%): SOL-USD se encuentra en una condición de sobreventa extrema con un RSI de 20.3 tras caer un 8.83% en la última semana. Al ser un activo de alto beta y fuerte momentum histórico, la probabilidad de un rebote técnico violento hacia la media es sumamente alta. Asignamos $10.00 USD (alta convicción) para maximizar el retorno rápido.
- **[BUY] ETH-USD** (Confianza: 85%): ETH-USD muestra un RSI de 24.9, confirmando una capitulación de corto plazo en el mercado cripto. Entramos con una posición estándar de $5.00 USD para capturar el rebote técnico coordinado con el resto del mercado de activos digitales.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-09 18:25` | 🟢 BUY | `ETH-USD` | $5.00 | $2481.72 | ETH-USD muestra un RSI de 24.9, confirmando una capitulación de corto plazo en el mercado ... |
| `2026-10-09 18:25` | 🟢 BUY | `SOL-USD` | $10.00 | $109.08 | SOL-USD se encuentra en una condición de sobreventa extrema con un RSI de 20.3 tras caer u... |
| `2026-10-09 16:26` | 🟢 BUY | `QQQ` | $5.00 | $751.70 | QQQ se encuentra en una tendencia alcista clara sobre su SMA20 y con un RSI de 58.1 que su... |
| `2026-10-09 16:07` | 💵 DEPOSIT | `CASH` | $20.00 | $1.00 | Inyección adicional de $20.00 USD de efectivo para ampliar la capacidad operativa y permit... |
| `2026-10-09 15:37` | 🟢 BUY | `NVDA` | $5.00 | $229.65 | Iniciamos posición en NVDA con $5.00 USD. El activo mantiene una tendencia alcista sólida ... |

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
