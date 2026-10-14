# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 17:01:07`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.23 USD** | **$19.88 USD** | **$39.11 USD** | 🔴 **-2.22%** ($-0.89) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 6h 10m |
| `SOL-USD` | 0.095785 | $104.40 | $104.15 | $9.98 | 📉 -0.24% | 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de acciones tradicional se encuentra CERRADO, por lo que la liquidez activa se concentra en las criptomonedas (abiertas 24/7). Los activos digitales muestran un sesgo bajista en el corto plazo con RSI de 1 hora comprimidos en zonas de sobreventa (ETH-USD en 25.6, BTC-USD en 28.4 y SOL-USD en 29.2), lo que presenta oportunidades tácticas de rebote por mean reversion. Mantendremos las posiciones actuales para permitirles desarrollar el impulso técnico."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 75%): La posición en AAPL se mantiene con una pérdida menor del -0.92% tras 6 horas. Su mercado está cerrado y su RSI diario de 57.8 junto a una tendencia alcista justifican mantener el activo a la espera de su objetivo de take-profit.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD muestra un RSI de 1h en 29.2 saliendo de la zona de compresión y un cambio de 1h positivo, operando muy cerca del precio de entrada (-0.24%). Mantenemos la posición para capturar el rebote técnico esperado en criptomonedas.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones abiertas en AAPL y SOL-USD. AAPL está operando con normalidad a pesar del cierre y muestra un RSI saludable, mientras que SOL-USD se mantiene cerca de su precio de entrada con un RSI de 1h en 29.2 buscando un rebote alcista. Vigilaremos un stop-loss estricto a -2.0% y un take-profit entre +2.0% y +3.5%. No se realizan nuevas compras para conservar la liquidez mínima requerida."
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
