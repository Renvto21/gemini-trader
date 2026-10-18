# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 06:20:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.31 USD** | **$38.35 USD** | 🔴 **-4.12%** ($-1.65) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81836.09 | $10.08 | 📈 +0.82% | 11h 19m |
| `SOL-USD` | 0.097418 | $102.65 | $103.65 | $10.10 | 📈 +0.97% | 11h 9m |
| `ETH-USD` | 0.004193 | $2385.05 | $2415.01 | $10.13 | 📈 +1.26% | 11h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene abierto y operando con un sesgo alcista moderado de corto plazo, donde nuestras posiciones actuales en BTC-USD, SOL-USD y ETH-USD muestran rendimientos positivos (+0.82%, +0.97% y +1.26% respectivamente) tras el rebote técnico esperado. Los mercados tradicionales permanecen cerrados. Mantenemos la vigilancia sobre los niveles de RSI de 1H, que se acercan a zonas de consolidación sin alcanzar todavía los objetivos extremos de take-profit (+2.0% a +3.5%), por lo que decidimos mantener las posiciones actuales para permitirles seguir madurando."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición muestra un rendimiento positivo de +0.82% y un RSI de 1h en 59.3. El impulso continúa desarrollándose hacia el objetivo de take-profit sin activar ninguna alerta de stop-loss.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD lidera las ganancias actuales con +1.26% y un RSI de 1h en 49.7. Mantenemos la posición para capturar el beneficio completo dentro del rango objetivo de take-profit.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD registra un PnL de +0.97% con un RSI de 1h en 47.6. El rebote técnico sigue su curso de manera saludable y no hay razones para cerrar la operación prematuramente.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD. Monitorear de cerca los niveles de RSI de 1H en busca del rango objetivo de take-profit (+2.0% a +3.5%) o señales de sobrecompra (>70) para proceder con la venta y asegurar beneficios. El stop-loss se mantiene rigurosamente en -2.0%."
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
