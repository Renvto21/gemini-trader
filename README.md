# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 20:00:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.05 USD** | **$38.09 USD** | 🔴 **-4.76%** ($-1.91) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81230.23 | $10.01 | 📈 +0.07% | 59m |
| `SOL-USD` | 0.097418 | $102.65 | $102.88 | $10.02 | 📈 +0.22% | 49m |
| `ETH-USD` | 0.004193 | $2385.05 | $2389.34 | $10.02 | 📈 +0.18% | 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que el enfoque absoluto está en el sector de criptomonedas (ABIERTO 24/7). Las posiciones abiertas en BTC-USD, SOL-USD y ETH-USD muestran ligeras ganancias marginales tras haber capturado los rebotes iniciales desde zonas de sobreventa. Sin embargo, el impulso de 1 hora se ha desacelerado ligeramente y los precios se mantienen lateralizados dentro de un contexto diario bajista, por lo que se requiere paciencia para permitir que alcancen la zona objetivo de take-profit entre +2.0% y +3.5%."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD se mantiene estable con una pequeña ganancia del 0.07% tras casi una hora de mantener la posición. El impulso actual es neutro, por lo que se mantiene la posición a la espera del objetivo de take-profit o un aumento del momentum alcista.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD muestra un rendimiento positivo de 0.22% y se encuentra operando dentro del rango esperado para el rebote técnico. Se conserva la posición para buscar el objetivo de ganancia estipulado.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD registra una ganancia del 0.18% tras el rebote desde la sobreventa profunda. El activo se mantiene dentro de los parámetros de riesgo y objetivos establecidos, sin motivos para cerrar la posición anticipadamente.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (BTC-USD, SOL-USD, ETH-USD) vigilando de cerca el avance hacia el objetivo de take-profit (+2.0% a +3.5%) o un incremento en el RSI de 1H hacia la zona de sobrecompra (>70). El stop-loss se mantiene estricto en -2.0% para salvaguardar el portafolio. No se realizan nuevas compras en este ciclo debido a que la liquidez disponible se encuentra en el mínimo requerido y se prioriza consolidar las ganancias de las operaciones abiertas."
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
