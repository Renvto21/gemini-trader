# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 15:10:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.57 USD** | **$20.05 USD** | **$38.62 USD** | 🔴 **-3.46%** ($-1.38) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $719.38 | $10.01 | 📈 +0.06% | 4h 29m |
| `ETH-USD` | 0.004178 | $2393.62 | $2404.01 | $10.04 | 📈 +0.43% | 2h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo mixto con la mayoría de los índices y criptomonedas bajo sus medias móviles de 20 períodos, consolidando tras recientes caídas semanales. Las posiciones actuales de QQQ y ETH-USD se mantienen estables con ligeras ganancias pero sin el impulso de aceleración esperado. La liquidez en efectivo se mantiene adecuada y el mercado cripto permanece activo operando 24/7."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 70%): QQQ se encuentra con una pequeña ganancia del +0.06% tras 4 horas y media de holding. El momentum de 1h se ha enfriado ligeramente, pero la tendencia intradiaria y el contexto de rebote técnico justifican mantener la posición a la espera del objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un comportamiento positivo con una ganancia actual de +0.43% y un RSI de 1h recuperándose hasta 39.5. Mantendremos la posición buscando que alcance el rango de take-profit del +2.0% al +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de QQQ y ETH-USD mientras se acercan de manera controlada al objetivo de take-profit entre +2.0% y +3.5%. Monitorearemos de cerca el RSI de 1 hora de BTC-USD y SOL-USD para identificar un rompimiento alcista con volumen si deciden acelerar el rebote. Mantendremos la disciplina con el stop-loss en -2.0% y la reserva mínima de efectivo de $4.00 USD."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |
| `2026-10-19 01:50` | 🔴 SELL (+0.09$) | `ETH-USD` | $8.09 | $2428.97 | ETH-USD registra una ganancia acumulada y su RSI de 1 hora ha alcanzado 68.3, acercándose ... |
| `2026-10-19 01:00` | 🔴 SELL (-0.00$) | `SOL-USD` | $8.00 | $105.08 | SOL-USD ha entrado en sobrecompra con un RSI de 1 hora en 72.7, cumpliendo estrictamente c... |
| `2026-10-18 23:20` | 🟢 BUY | `SOL-USD` | $8.00 | $105.11 | SOL-USD presenta un RSI diario en 21.8 (sobreventa extrema) y un momentum de 24 horas alci... |

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
