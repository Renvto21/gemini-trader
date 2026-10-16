# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 06:40:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.17 USD** | **$34.58 USD** | **$38.75 USD** | 🔴 **-3.12%** ($-1.25) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 19h 49m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 18h 20m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 17h 50m |
| `ETH-USD` | 0.002855 | $2451.90 | $2448.92 | $6.99 | 📉 -0.12% | 2h 9m |
| `SOL-USD` | 0.028214 | $106.33 | $106.44 | $3.00 | 📈 +0.10% | 1h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores se encuentra actualmente cerrado, por lo que toda la atención táctica se desplaza exclusivamente hacia los activos cripto que operan 24/7. Las posiciones en renta variable (MSFT, QQQ, NVDA) permanecen con precios congelados y con rendimientos cercanos a cero o ligeramente positivos/negativos. En el segmento cripto, ETH-USD y SOL-USD se mantienen estables tras las compras recientes, operando con un sesgo lateral a la espera de mayor volumen y confirmación de momentum en el corto plazo."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): La posición en ETH-USD lleva poco tiempo abierta (2 horas) y se encuentra estable con una ligera variación del -0.12%. El RSI diario en 32.5 respalda la tesis de rebote por mean reversion, por lo que se mantiene a la espera de un impulso alcista que acerque el precio al objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca el rendimiento de ETH-USD y SOL-USD. Como el efectivo disponible se encuentra en $4.17 (cerca de la reserva mínima de $4.00), no realizaremos nuevas compras en este ciclo. Mantener las posiciones actuales y esperar a la apertura de Wall Street para evaluar la rotación o toma de beneficios si las acciones tecnológicas muestran rebotes hacia la zona objetivo de +2.0% a +3.5%."
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
