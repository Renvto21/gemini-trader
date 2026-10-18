# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 02:50:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.20 USD** | **$38.25 USD** | 🔴 **-4.38%** ($-1.75) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81608.63 | $10.05 | 📈 +0.54% | 7h 49m |
| `SOL-USD` | 0.097418 | $102.65 | $103.24 | $10.06 | 📈 +0.57% | 7h 39m |
| `ETH-USD` | 0.004193 | $2385.05 | $2407.00 | $10.09 | 📈 +0.92% | 7h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto 24/7 mostrando un comportamiento lateral con ligeros retrocesos en la última hora (-0.11% a -0.44%), mientras que los activos tradicionales de Wall Street permanecen cerrados. Las posiciones actuales en BTC, ETH y SOL se encuentran en territorio positivo leve (entre +0.54% y +0.92%), aún sin alcanzar el objetivo de take-profit óptimo (+2.0% a +3.5%), pero manteniéndose alejadas de los límites de stop-loss. El RSI de 1 hora se ha enfriado moderadamente tras el rebote inicial, por lo que la postura táctica adecuada es mantener las posiciones actuales y dejar que el precio evolucione."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): La posición muestra un rendimiento positivo de +0.54% tras el rebote inicial. El RSI de 1 hora se sitúa en 59.1 y aún no alcanza la zona de sobrecompra para tomar beneficios, ni ha perforado los niveles de stop-loss. Mantenemos la posición activa.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD registra una ganancia del +0.92% con un RSI de 1 hora neutral en 50.0. Continuamos operando el rebote técnico a la espera de que el precio se acerque al objetivo de take-profit del +2.0%.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD presenta un rendimiento estable de +0.57% y un RSI de 1 hora en 48.1. La tendencia de corto plazo sigue consolidándose, por lo que no hay señales de salida anticipada ni de stop-loss.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré las posiciones abiertas en BTC-USD, ETH-USD y SOL-USD para permitirles buscar la zona objetivo de take-profit entre +2.0% y +3.5%. Vigilaré de cerca el RSI de 1 hora; si alguno se acerca a niveles de sobrecompra (>70), procederé a vender para asegurar ganancias. Mantendré la reserva mínima de efectivo de $4.00 y no abriré nuevas posiciones hasta el próximo ciclo."
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
