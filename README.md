# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 18:00:55`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.23 USD** | **$19.87 USD** | **$39.10 USD** | 🔴 **-2.26%** ($-0.90) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 7h 10m |
| `SOL-USD` | 0.095785 | $104.40 | $104.00 | $9.96 | 📉 -0.38% | 1h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la acción y atención se desplaza a los criptoactivos que operan 24/7. Las principales criptomonedas muestran condiciones de sobreventa extrema en marcos de corto plazo (RSI 1h en zonas inferiores a 25), lo que representa oportunidades potenciales de rebote técnico por reversión a la media, aunque el sesgo general sigue siendo bajista bajo las medias móviles."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 60%): SOL-USD se encuentra bajo vigilancia estricta tras un leve retroceso en su RSI de 1h (25.0). Aunque el precio está cerca de nuestra entrada, le daremos un ciclo más para confirmar si respeta el soporte actual antes de recortar pérdidas.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos AAPL debido a que el mercado está cerrado. Para SOL-USD, el RSI de 1h ha caído nuevamente a 25.0 a pesar del intento de rebote previo, manteniéndose cerca del límite de stop-loss. Lo vigilaremos de cerca y si no muestra una recuperación rápida en el próximo ciclo, procederemos a vender para rotar el capital. Mantendremos la liquidez disponible de $19.23 dólares esperando una confirmación de giro alcista más clara en ETH-USD o BTC-USD antes de desplegar nuevas compras agresivas."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **52** | 🎯 **42.3%** (22W / 16L / 14BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 16:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.40 | SOL-USD presenta un RSI de 1h en 30.9 saliendo de la zona de compresión y un cambio positi... |
| `2026-10-14 15:20` | 🔴 SELL (-0.08$) | `SOL-USD` | $9.92 | $103.86 | SOL-USD lleva varias horas sin mostrar el rebote esperado, su RSI de 1h ha caído hasta 25.... |
| `2026-10-14 12:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.70 | SOL-USD presenta un RSI de 1h en 29.2 saliendo de sobreventa extrema y un cambio de 1h pos... |
| `2026-10-14 11:20` | 🔴 SELL (-0.09$) | `BTC-USD` | $5.89 | $81874.95 | BTC-USD lleva más de 14 horas abierto con un PnL negativo persistente (-1.51%) y un RSI de... |
| `2026-10-14 10:50` | 🟢 BUY | `AAPL` | $10.00 | $346.15 | AAPL se encuentra con un excelente momentum alcista intradiario, un incremento de 1.4% en ... |

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
