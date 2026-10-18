# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 00:00:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.31 USD** | **$38.35 USD** | 🔴 **-4.12%** ($-1.65) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81721.63 | $10.07 | 📈 +0.68% | 4h 59m |
| `SOL-USD` | 0.097418 | $102.65 | $103.86 | $10.12 | 📈 +1.18% | 4h 50m |
| `ETH-USD` | 0.004193 | $2385.05 | $2413.88 | $10.12 | 📈 +1.21% | 4h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto muestra un comportamiento lateral a ligeramente alcista en las últimas horas, con nuestras posiciones en BTC-USD, SOL-USD y ETH-USD registrando ganancias moderadas pero sin alcanzar todavía el objetivo completo de take-profit del +2.0% al +3.5%. Los mercados tradicionales (Wall Street) se encuentran cerrados, por lo que toda la operativa se concentra exclusivamente en activos digitales abiertos 24/7."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición muestra un rendimiento positivo de +0.68% tras casi 5 horas de tenencia. El RSI de 1 hora se ubica en 58.6 y el precio mantiene la estructura de rebote esperada, por lo que se mantiene a la espera del objetivo de take-profit.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD registra una ganancia actual de +1.18%, acercándose al rango objetivo de toma de beneficios. El RSI de 1 hora en 50.2 indica estabilidad en el impulso de corto plazo.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD presenta una ganancia de +1.21% con un RSI de 1 hora en 47.4. La posición evoluciones favorablemente dentro del plan de recuperación técnica.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas actuales (BTC-USD, SOL-USD, ETH-USD) mientras continúan su proceso de recuperación desde los mínimos recientes. El RSI de 1 hora se mantiene en rangos estables sin sobrecompra extrema aún. Mantendré la observación estricta de las posiciones para asegurar beneficios en cuanto toquen el rango de +2.0% a +3.5% o ejecutar el stop-loss si el precio revierte hacia la zona de -2.0%. No se realizarán nuevas compras en este ciclo para preservar liquidez y permitir que las posiciones actuales maduren."
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
