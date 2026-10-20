# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 16:50:54`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.85 USD** | **$38.97 USD** | 🔴 **-2.56%** ($-1.03) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.32 | $9.96 | 📉 -0.39% | 4h 49m |
| `ETH-USD` | 0.004058 | $2452.17 | $2436.86 | $9.89 | 📉 -0.62% | 2h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento mixto con sesgo bajista en tendencias generales, pero con criptomonedas y algunos activos tecnológicos presentando oportunidades de rebote por sobreventa diaria y estabilización horaria. AAPL y ETH-USD se mantienen estables dentro de rangos manejables de pérdida sin tocar umbrales de stop-loss críticos."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 70%): La posición en AAPL tiene un holding time de casi 5 horas con una pérdida menor de -0.39%. El RSI de 1 hora se encuentra en 32.8 buscando estabilización y la tendencia diaria es alcista. Se mantiene para permitir que desarrolle el rebote esperado sin activar el stop-loss.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un comportamiento resiliente con un rendimiento de 24h positivo (+1.33%) y un RSI diario en zona de sobreventa (28.9) con potencial de reversión alcista. Mantenemos la posición para buscar el objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones abiertas en AAPL y ETH-USD mientras no rompan el soporte del -2.0%. Monitorear de cerca ETH-USD para capturar un take-profit si se aproxima al +2.0% o si el RSI de 1 hora entra en sobrecompra superior a 70. Preparado para rotar capital hacia criptomonedas con fuerte impulso si alguna posición lateraliza por más ciclos."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **82** | 🎯 **43.9%** (36W / 31L / 15BE) | 🔴 **$-0.79 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-20 13:51` | 🟢 BUY | `ETH-USD` | $9.95 | $2452.17 | ETH-USD muestra un excelente impulso de corto plazo con change_1h_pct positivo (+0.55%) y ... |
| `2026-10-20 13:51` | 🔴 SELL (-0.05$) | `GLD` | $9.95 | $377.90 | GLD se encuentra estancado con un rendimiento ligeramente negativo (-0.47%) y un rsi_1h de... |
| `2026-10-20 12:01` | 🟢 BUY | `GLD` | $10.00 | $379.70 | GLD presenta un RSI de 1 hora en 31.4, acercándose a la zona ideal de sobreventa para acti... |
| `2026-10-20 12:01` | 🟢 BUY | `AAPL` | $10.00 | $340.64 | AAPL se encuentra en tendencia alcista diaria con un RSI de 1 hora en 33.1 (cercano a sobr... |
| `2026-10-20 11:10` | 🔴 SELL (+0.12$) | `BTC-USD` | $8.69 | $82949.93 | BTC-USD muestra un RSI de 1 hora en 72.2 (sobrecompra) y un rendimiento positivo de +1.45%... |

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
