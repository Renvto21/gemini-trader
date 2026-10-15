# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 09:00:54`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.85 USD** | **$38.46 USD** | 🔴 **-3.85%** ($-1.54) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 22h 10m |
| `BTC-USD` | 0.000061 | $81640.68 | $80852.10 | $4.95 | 📉 -0.97% | 11h 50m |
| `ETH-USD` | 0.002539 | $2362.71 | $2359.01 | $5.99 | 📉 -0.16% | 7h 50m |
| `SOL-USD` | 0.058789 | $102.06 | $102.00 | $6.00 | 📉 -0.06% | 5h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se encuentra bajo presión con los principales índices de Wall Street cerrados y las criptomonedas mostrando un sesgo lateral bajista. Las criptomonedas en cartera (BTC-USD, ETH-USD, SOL-USD) presentan variaciones mínimas recientes tras los rebotes iniciados previamente, manteniendo un comportamiento técnico estable pero sin la fuerza alcista esperada en el muy corto plazo. El efectivo disponible es limitado ($11.61), por lo que la prioridad es consolidar posiciones y esperar confirmaciones de momentum antes de comprometer más capital."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 65%): ETH-USD muestra un RSI de 1h en 33.6 manteniéndose estable tras la entrada reciente. No ha alcanzado el objetivo de take-profit ni ha roto el stop-loss, por lo que se mantiene en cartera esperando un nuevo impulso alcista.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (AAPL, BTC-USD, ETH-USD, SOL-USD) ya que se encuentran dentro de rangos tolerables de pérdida y respetan el stop-loss estricto de -2.0%. Monitorear de cerca el comportamiento de ETH-USD y SOL-USD en las próximas horas: si logran romper al alza con un RSI de 1h superior a 60-70 o alcanzan una ganancia del +2.0%, proceder a realizar tomas de beneficios parciales para liberar liquidez. Evitar nuevas compras hasta observar una ruptura clara o hasta que la apertura de los mercados tradicionales ofrezca mejores oportunidades tácticas."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **54** | 🎯 **40.7%** (22W / 18L / 14BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 03:20` | 🟢 BUY | `SOL-USD` | $6.00 | $102.06 | SOL-USD muestra un RSI de 1h en 33.3 saliendo de zonas de compresión bajista, acompañado d... |
| `2026-10-15 01:10` | 🟢 BUY | `ETH-USD` | $6.00 | $2362.71 | ETH-USD presenta un RSI de 1h extremadamente bajo en 23.5 saliendo de sobreventa y un camb... |
| `2026-10-14 23:30` | 🔴 SELL (-0.30$) | `SOL-USD` | $9.70 | $101.32 | La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin ... |
| `2026-10-14 23:30` | 🔴 SELL (-0.32$) | `ETH-USD` | $9.68 | $2340.86 | 🚨 STOP-LOSS AUTOMÁTICO (CIRCUIT BREAKER): Pérdida de -3.20% superó el límite de seguridad ... |
| `2026-10-14 21:10` | 🟢 BUY | `BTC-USD` | $5.00 | $81640.68 | BTC-USD presenta un RSI de 1h en 24.9 (sobreventa extrema) y liquidez disponible suficient... |

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
