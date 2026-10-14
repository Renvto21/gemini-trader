# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 18:30:52`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.23 USD** | **$19.90 USD** | **$39.13 USD** | 🔴 **-2.18%** ($-0.87) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 7h 40m |
| `SOL-USD` | 0.095785 | $104.40 | $104.34 | $9.99 | 📉 -0.06% | 2h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general muestra un sentimiento predominantemente bajista en temporalidades diarias, con los principales índices y acciones tecnológicas cerrados y operando por debajo de sus medias móviles de 20 periodos. En el ecosistema cripto, que permanece abierto 24/7, observamos condiciones de sobreventa generalizadas con RSI de 1 hora deprimidos, lo que presenta oportunidades tácticas de rebote para activos como SOL-USD, aunque con alta volatilidad y presión bajista macro."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD muestra un cambio de 1h positivo (+0.35%) y un RSI de 1h en 28.6 intentando estabilizarse tras la reciente compra. Mantenemos la posición para permitir que desarrolle el rebote técnico esperado, respetando estrictamente nuestro nivel de stop-loss.
- **[HOLD] AAPL** (Confianza: 75%): El mercado de Wall Street se encuentra cerrado, por lo que no es posible operar acciones tradicionales. AAPL se mantiene en cartera bajo una tendencia macro alcista sólida sobre la SMA20.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos SOL-USD ya que muestra un ligero cambio positivo de 1h (+0.35%) y se mantiene estable cerca de nuestra zona de entrada, vigilando de cerca el stop-loss estricto en -2.0% y un objetivo de take-profit entre +2.0% y +3.5%. AAPL sigue en cartera por estar el mercado cerrado y mantener una tendencia macro alcista sólida. Para el próximo ciclo, si SOL-USD rompe a la baja o se estanca sin momentum, procederemos a liquidarla para liberar capital hacia criptomonedas con mejor impulso alcista."
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
