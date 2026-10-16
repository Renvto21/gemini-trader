# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 14:20:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.05 USD** | **$13.21 USD** | **$38.26 USD** | 🔴 **-4.35%** ($-1.74) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $524.94 | $6.38 | 📉 -1.91% | 1d 3h |
| `ETH-USD` | 0.002855 | $2451.90 | $2395.44 | $6.84 | 📉 -2.30% | 9h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se encuentra bajo presión bajista con la mayoría de los activos operando por debajo de sus medias móviles de 20 períodos. Las criptomonedas y las grandes tecnológicas muestran niveles de RSI de 1 hora cercanos a la zona de sobreventa (menores a 35), lo que sugiere la proximidad de posibles rebotes técnicos, aunque el sesgo macro continúa siendo de cautela."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 60%): La posición acumula una pérdida de -1.91% con un tiempo de tenencia de más de un día. Aunque el RSI de 1 hora está en 30.1, la tendencia diaria se mantiene alcista sobre la SMA20, por lo que mantengo la posición buscando un rebote hacia la zona de recuperación sin superar el stop-loss del -2.0%.
- **[HOLD] ETH-USD** (Confianza: 50%): ETH-USD presenta una pérdida de -2.30% y opera bajo la SMA20. Sin embargo, el RSI diario se encuentra en 29.5 (sobreventa extrema), lo que justifica mantener la posición temporalmente a la espera de una reacción alcista de corto plazo antes de considerar un cierre por stop-loss.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener la disciplina ante las caídas. MSFT acumula una pérdida cercana al -1.91% tras más de un día abierta, pero su tendencia diaria sigue siendo alcista sobre la SMA20; mantendré el stop-loss estricto en -2.0%. ETH-USD muestra un PnL de -2.3% con holding time de casi 10 horas, operando en tendencia bajista pero con RSI diario en zona de sobreventa extrema (29.5); evaluaré su salida si rompe soportes adicionales. No realizaré nuevas compras en este ciclo debido a la debilidad generalizada del mercado y la prioridad de proteger la liquidez disponible."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **61** | 🎯 **39.3%** (24W / 23L / 14BE) | 🔴 **$-1.34 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 13:40` | 🔴 SELL (-0.02$) | `NVDA` | $7.98 | $216.80 | NVDA lleva más de 24 horas abierto operando bajo la SMA20 con un momentum débil, acumula u... |
| `2026-10-16 12:50` | 🔴 SELL (-0.06$) | `SOL-USD` | $2.94 | $104.34 | SOL-USD lleva varias horas abierto sin generar el rebote esperado, acumulando una pérdida ... |
| `2026-10-16 10:50` | 🔴 SELL (-0.04$) | `QQQ` | $9.95 | $721.83 | QQQ lleva más de 22 horas abierto operando bajo la SMA20 con un RSI de 1 hora en 30.2 y un... |
| `2026-10-16 05:10` | 🟢 BUY | `SOL-USD` | $3.00 | $106.33 | SOL-USD presenta un RSI diario en zona de sobreventa extrema (29.0) y un cambio positivo e... |
| `2026-10-16 04:30` | 🟢 BUY | `ETH-USD` | $7.00 | $2451.90 | Aprovechamos la liquidez disponible sobre la reserva mínima ($14.17 vs $4.00 requeridos) p... |

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
