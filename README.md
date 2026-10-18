# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 03:50:35`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.24 USD** | **$38.28 USD** | 🔴 **-4.29%** ($-1.72) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81600.96 | $10.05 | 📈 +0.53% | 8h 49m |
| `SOL-USD` | 0.097418 | $102.65 | $103.51 | $10.08 | 📈 +0.84% | 8h 39m |
| `ETH-USD` | 0.004193 | $2385.05 | $2408.98 | $10.10 | 📈 +1.00% | 8h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 mostrando una estabilidad relativa con ligeras ganancias en nuestras posiciones actuales de BTC-USD, SOL-USD y ETH-USD, las cuales han estado abiertas por casi 9 horas. Aunque muestran retornos positivos entre +0.53% y +1.00%, aún no alcanzan el objetivo de take-profit de +2.0% a +3.5%. Los activos tradicionales están cerrados, por lo que toda la atención táctica sigue centrada en el mercado cripto."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD muestra una ganancia actual de +0.53% tras casi 9 horas de tenencia. El RSI de 1h se encuentra en 61.7, alejándose de zonas de peligro y consolidándose. Mantenemos la posición a la espera del objetivo de take-profit de +2.0% a +3.5%.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD registra un rendimiento positivo de +0.84% con un RSI de 1h en 53.5. Continuamos con la operación abierta buscando el objetivo de take-profit estipulado en la estrategia de momentum.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD es la posición con mejor desempeño actual con un +1.00% y un RSI de 1h en 53.5. Está avanzando adecuadamente hacia la zona de take-profit, por lo que se mantiene sin cambios.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD esperando que continúen el impulso alcista hacia el objetivo de take-profit de +2.0% a +3.5%. Si el RSI de 1 hora de cualquiera de estas posiciones supera 70 o se acerca al rango objetivo, procederemos a vender para asegurar ganancias. Mantener activo el stop-loss estricto a -2.0% ante cualquier reversión imprevista."
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
