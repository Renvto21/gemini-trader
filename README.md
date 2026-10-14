# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 20:20:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$9.23 USD** | **$29.89 USD** | **$39.11 USD** | 🔴 **-2.22%** ($-0.89) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 9h 30m |
| `SOL-USD` | 0.095785 | $104.40 | $104.30 | $9.99 | 📉 -0.10% | 3h 49m |
| `ETH-USD` | 0.004135 | $2418.34 | $2415.38 | $9.99 | 📉 -0.12% | 1h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se encuentra mayoritariamente cerrado, con los índices tradicionales y acciones en pausa. Las criptomonedas operan 24/7 mostrando un sesgo bajista continuado de corto plazo con niveles de sobreventa profundos (RSI de 1h muy bajos en BTC, ETH y SOL), aunque sin un momentum positivo confirmado en la última hora que valide un rebote inmediato. Mantenemos una postura defensiva pero pacientes ante nuestras posiciones abiertas recientes en cripto y acciones."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición lleva pocas horas abierta con una pérdida marginal de -0.1%. Aunque el RSI de 1h está bajo (33.7), la tendencia general sigue bajista; sin embargo, no amerita corte de pérdida prematuro al estar muy cerca del precio de entrada y mantenernos dentro del plan táctico.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD presenta sobreventa extrema en RSI de 1h (22.5) pero sin confirmación de giro alcista en la última hora. Mantenemos la posición a la espera del desarrollo del rebote técnico sin sobrepasar los límites de riesgo.
- **[HOLD] AAPL** (Confianza: 70%): El mercado de acciones está cerrado, congelando el precio de AAPL con una ligera pérdida del -0.92%. Se mantiene en cartera a la espera de la reapertura de Wall Street para evaluar su comportamiento frente al soporte.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en AAPL, SOL-USD y ETH-USD mientras respeten el umbral de pérdida del -2.0%. Estar atentos a la apertura del mercado bursátil para evaluar la evolución de AAPL y vigilar de cerca el RSI de 1h en SOL y ETH buscando el catalizador de volumen alcista que confirme el rebote por sobreventa. Si alguna posición rompe soportes críticos, procederemos a la venta inmediata."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **52** | 🎯 **42.3%** (22W / 16L / 14BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 19:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2418.34 | ETH-USD presenta un RSI de 1h en 22.0 (sobreventa extrema) y un cambio de 1h que comienza ... |
| `2026-10-14 16:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.40 | SOL-USD presenta un RSI de 1h en 30.9 saliendo de la zona de compresión y un cambio positi... |
| `2026-10-14 15:20` | 🔴 SELL (-0.08$) | `SOL-USD` | $9.92 | $103.86 | SOL-USD lleva varias horas sin mostrar el rebote esperado, su RSI de 1h ha caído hasta 25.... |
| `2026-10-14 12:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.70 | SOL-USD presenta un RSI de 1h en 29.2 saliendo de sobreventa extrema y un cambio de 1h pos... |
| `2026-10-14 11:20` | 🔴 SELL (-0.09$) | `BTC-USD` | $5.89 | $81874.95 | BTC-USD lleva más de 14 horas abierto con un PnL negativo persistente (-1.51%) y un RSI de... |

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
