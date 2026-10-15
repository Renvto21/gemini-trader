# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 23:00:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.23 USD** | **$34.81 USD** | **$39.04 USD** | 🔴 **-2.41%** ($-0.96) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 12h 10m |
| `SOL-USD` | 0.095785 | $104.40 | $103.84 | $9.95 | 📉 -0.54% | 6h 29m |
| `ETH-USD` | 0.004135 | $2418.34 | $2409.36 | $9.96 | 📉 -0.37% | 3h 59m |
| `BTC-USD` | 0.000061 | $81640.68 | $81492.23 | $4.99 | 📉 -0.18% | 1h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se encuentra bajo presión bajista en los índices principales y criptomonedas, con los mercados bursátiles tradicionales cerrados. Las criptomonedas (BTC-USD, ETH-USD, SOL-USD) muestran RSI de 1 hora extremadamente deprimidos (<25), lo que indica una sobreventa profunda a corto plazo pero un riesgo continuo de continuación bajista debido a la tendencia macro. Mantenemos las posiciones abiertas evaluando los niveles de stop-loss y preparados para rotar capital si el impulso rebota."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 60%): El activo se encuentra en sobreventa extrema (RSI 1h en 23.5), pero la tendencia sigue siendo bajista. Mantenemos la posición actual a la espera de un cambio de impulso que confirme el rebote técnico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca los niveles de soporte actuales en SOL-USD, ETH-USD y BTC-USD. Si el RSI de 1 hora rompe hacia arriba de forma decisiva y el cambio de 1h se torna positivo, mantendremos las posiciones buscando el objetivo de take-profit entre +2.0% y +3.5%. Si alguna posición perfora el límite de stop-loss del -2.0% antes del rebote, ejecutaré la venta inmediata para proteger la liquidez y preservar el capital restante."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **52** | 🎯 **42.3%** (22W / 16L / 14BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 21:10` | 🟢 BUY | `BTC-USD` | $5.00 | $81640.68 | BTC-USD presenta un RSI de 1h en 24.9 (sobreventa extrema) y liquidez disponible suficient... |
| `2026-10-14 19:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2418.34 | ETH-USD presenta un RSI de 1h en 22.0 (sobreventa extrema) y un cambio de 1h que comienza ... |
| `2026-10-14 16:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.40 | SOL-USD presenta un RSI de 1h en 30.9 saliendo de la zona de compresión y un cambio positi... |
| `2026-10-14 15:20` | 🔴 SELL (-0.08$) | `SOL-USD` | $9.92 | $103.86 | SOL-USD lleva varias horas sin mostrar el rebote esperado, su RSI de 1h ha caído hasta 25.... |
| `2026-10-14 12:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.70 | SOL-USD presenta un RSI de 1h en 29.2 saliendo de sobreventa extrema y un cambio de 1h pos... |

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
