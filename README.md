# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 05:10:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.18 USD** | **$38.23 USD** | 🔴 **-4.42%** ($-1.77) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81581.51 | $10.05 | 📈 +0.51% | 10h 9m |
| `SOL-USD` | 0.097418 | $102.65 | $103.14 | $10.05 | 📈 +0.48% | 9h 59m |
| `ETH-USD` | 0.004193 | $2385.05 | $2405.71 | $10.09 | 📈 +0.87% | 9h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con un comportamiento lateral a ligeramente alcista. Las posiciones abiertas (BTC, SOL, ETH) muestran ganancias marginales tras 10 horas de consolidación, con el RSI de 1 hora neutralizándose alrededor de 45-55. Los mercados tradicionales permanecen cerrados, por lo que el capital activo está concentrado en criptomonedas esperando un catalizador de volumen para buscar los objetivos de take-profit cercanos al +2.0%."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 65%): La posición se mantiene en terreno positivo (+0.51%) tras 10 horas. El RSI de 1 hora se encuentra en una zona neutral saludable (55.4) y el precio sostiene el nivel de entrada esperando mayor volumen alcista.
- **[HOLD] SOL-USD** (Confianza: 65%): SOL-USD registra una ganancia moderada de +0.48%. Mantiene la posición abierta mientras consolida por encima del precio de compra a la espera de un impulso de corto plazo.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD lidera las ganancias actuales con un +0.87% y un RSI diario muy deprimido (23.6), lo que sugiere un excelente potencial de rebote continuado hacia la zona de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones vigentes en BTC, SOL y ETH por este ciclo mientras muestran ligeras ganancias. Monitorearemos de cerca el nivel de take-profit entre +2.0% y +3.5% para asegurar beneficios, manteniendo el stop-loss estricto en -2.0% para proteger el capital ante cualquier reversión imprevista."
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
