# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 22:50:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.28 USD** | **$38.32 USD** | 🔴 **-4.19%** ($-1.68) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81660.45 | $10.06 | 📈 +0.60% | 3h 49m |
| `SOL-USD` | 0.097418 | $102.65 | $103.76 | $10.11 | 📈 +1.08% | 3h 39m |
| `ETH-USD` | 0.004193 | $2385.05 | $2410.67 | $10.11 | 📈 +1.07% | 3h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con un tono moderadamente constructivo en el corto plazo, aunque el contexto macro diario sigue bajo presión bajista general (por debajo de la SMA20). Las posiciones abiertas en BTC-USD, SOL-USD y ETH-USD muestran ganancias moderadas entre 0.6% y 1.08%, acercándose al rango objetivo de take-profit pero sin alcanzar todavía la zona óptima de +2.0% a +3.5% o niveles de sobrecompra en el RSI de 1 hora. Los mercados tradicionales continúan cerrados, por lo que la liquidez activa permanece dedicada por completo a la criptoesfera."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición mantiene un rendimiento positivo de +0.6% con un RSI de 1h en 52.0. El rebote técnico sigue su curso dentro de lo esperado, por lo que conviene mantenerla activa a la espera de la zona objetivo de take-profit (+2.0% a +3.5%).
- **[HOLD] SOL-USD** (Confianza: 80%): La posición registra una ganancia del +1.08% con un momentum de corto plazo favorable y un RSI de 1h en 37.9. Se mantiene abierta para buscar la extensión del rebote hacia la meta de take-profit.
- **[HOLD] ETH-USD** (Confianza: 80%): La posición presenta un rendimiento de +1.07% con un cambio positivo de 0.32% en la última hora. Se conserva en cartera para capturar la continuidad del movimiento alcista técnico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD mientras conserven el impulso de corto plazo. Vigilar de cerca el RSI de 1 hora para asegurar beneficios parciales o totales tan pronto como alcancen el rango de take-profit de +2.0% a +3.5% o crucen el umbral de sobrecompra (>70). El stop-loss estricto se mantiene anclado en -2.0% para blindar la cuenta ante cualquier reversión abrupta. No se requieren nuevas compras en este ciclo para preservar la reserva mínima de efectivo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **67** | 🎯 **38.8%** (26W / 27L / 14BE) | 🔴 **$-1.84 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 19:10` | 🟢 BUY | `ETH-USD` | $10.00 | $2385.05 | ETH-USD muestra un RSI de 1H en 29.0 (sobreventa profunda) combinado con un cambio de 1h p... |
| `2026-10-17 19:10` | 🟢 BUY | `SOL-USD` | $10.00 | $102.65 | SOL-USD presenta un RSI de 1H en 31.5 saliendo de zona de sobreventa estricta y un cambio ... |
| `2026-10-17 19:00` | 🟢 BUY | `BTC-USD` | $10.00 | $81170.65 | BTC-USD muestra un RSI de 1H saliendo de niveles bajos (37.5) con un cambio positivo de 0.... |
| `2026-10-17 18:40` | 🔴 SELL (-0.22$) | `ETH-USD` | $9.78 | $2370.09 | La posición acumula una pérdida de -2.21%, excediendo el umbral de stop-loss del -2.0%. El... |
| `2026-10-17 18:40` | 🔴 SELL (-0.21$) | `SOL-USD` | $9.79 | $101.78 | La posición ha alcanzado una pérdida de -2.08%, rompiendo el límite de stop-loss estricto ... |

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
