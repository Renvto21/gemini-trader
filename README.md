# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 19:20:36`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$29.98 USD** | **$38.03 USD** | 🔴 **-4.93%** ($-1.97) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81125.86 | $9.99 | 📉 -0.06% | 19m |
| `SOL-USD` | 0.097418 | $102.65 | $102.55 | $9.99 | 📉 -0.10% | 9m |
| `ETH-USD` | 0.004193 | $2385.05 | $2384.40 | $10.00 | 📉 -0.03% | 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se encuentra abierto 24/7 con un sesgo bajista generalizado en el corto plazo, pero mostrando intentos de consolidación y rebotes técnicos moderados tras caídas recientes. Los activos tradicionales como acciones y ETFs están cerrados. Mantenemos nuestras posiciones recientes en cripto mientras evaluamos su evolución técnica."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): La posición fue abierta hace pocos minutos y muestra un comportamiento estable con una ligera variación del -0.06%. Mantenemos la posición a la espera de un mayor impulso alcista que confirme el rebote.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD mantiene un RSI de 1H en zona de recuperación (30.4) y un cambio positivo reciente del 0.4%. Esperamos que el momentum continúe hacia nuestro objetivo de ganancia.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD permanece cerca de su precio de entrada con un PnL de -0.03%. Continuamos vigilando la sobreventa en temporalidad diaria y de 1H para buscar una salida con beneficios.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitoreando las posiciones abiertas en BTC-USD, SOL-USD y ETH-USD que llevan pocos minutos de ejecución. Esperaremos a que alcancen nuestro objetivo de take-profit entre +2.0% y +3.5%, o activaremos el stop-loss si alguna posición perfora el límite de -2.0%. La liquidez en efectivo se mantiene en niveles mínimos para maximizar la exposición en los activos abiertos 24/7."
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
