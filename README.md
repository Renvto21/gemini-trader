# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 07:30:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.17 USD** | **$34.58 USD** | **$38.74 USD** | 🔴 **-3.15%** ($-1.26) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 20h 40m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 19h 10m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 18h 40m |
| `ETH-USD` | 0.002855 | $2451.90 | $2451.09 | $7.00 | 📉 -0.03% | 2h 59m |
| `SOL-USD` | 0.028214 | $106.33 | $105.93 | $2.99 | 📉 -0.38% | 2h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional (Wall Street) se encuentra actualmente CERRADO, manteniendo los precios de las acciones congelados. Por su parte, el mercado de criptomonedas opera 24/7 y muestra un comportamiento lateral con ligeros sesgos positivos en ETH-USD y correcciones menores en SOL-USD. Mantenemos una postura defensiva pero alerta en cripto, mientras nos preparamos para buscar take-profits o ajustes en las posiciones de renta variable tan pronto abra la sesión bursátil."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): La posición en ETH-USD lleva poco tiempo abierta (menos de 3 horas) y muestra estabilidad con un cambio positivo de 1h del 0.15%. Mantenemos la posición a la espera de un mayor volumen de confirmación.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD presenta un RSI diario en zona de sobreventa extrema (28.0) y, aunque registra un pequeño retroceso en la última hora, el contexto de soporte macro justifica mantener la posición abierta para buscar el rebote técnico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca las posiciones abiertas en ETH-USD y SOL-USD para asegurar que no rompan soportes críticos. Mantener preparadas las órdenes de venta con objetivo de +2.0% a +3.5% para MSFT y QQQ en cuanto abra Wall Street. Vigilar la liquidez en efectivo ($4.17 USD) y evaluar la rotación de capital si alguna posición secundaria pierde momentum."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **58** | 🎯 **41.4%** (24W / 20L / 14BE) | 🔴 **$-1.22 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 05:10` | 🟢 BUY | `SOL-USD` | $3.00 | $106.33 | SOL-USD presenta un RSI diario en zona de sobreventa extrema (29.0) y un cambio positivo e... |
| `2026-10-16 04:30` | 🟢 BUY | `ETH-USD` | $7.00 | $2451.90 | Aprovechamos la liquidez disponible sobre la reserva mínima ($14.17 vs $4.00 requeridos) p... |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |

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
