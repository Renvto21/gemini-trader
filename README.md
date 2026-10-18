# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 05:00:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.18 USD** | **$38.23 USD** | 🔴 **-4.43%** ($-1.77) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81563.23 | $10.05 | 📈 +0.48% | 9h 59m |
| `SOL-USD` | 0.097418 | $102.65 | $103.15 | $10.05 | 📈 +0.49% | 9h 49m |
| `ETH-USD` | 0.004193 | $2385.05 | $2404.90 | $10.08 | 📈 +0.83% | 9h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto muestra un estancamiento en las últimas horas tras el rebote inicial, con los activos (BTC-USD, SOL-USD, ETH-USD) operando con ganancias marginales menores al 1% tras casi 10 horas de retención. Los mercados tradicionales permanecen cerrados. El momentum de corto plazo se ha enfriado, situándose en zonas neutrales sin la fuerza necesaria para alcanzar los objetivos de take-profit inmediatos, pero manteniéndose seguros lejos del stop-loss."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 70%): La posición se mantiene en terreno positivo (+0.48%) tras casi 10 horas. Aunque el momentum de 1h se ha enfriado, no ha roto soportes y se mantiene dentro de los parámetros de la estrategia a la espera de una extensión alcista.
- **[HOLD] SOL-USD** (Confianza: 70%): Se mantiene con una ganancia marginal del +0.49%. El RSI de 1h se estabiliza en 45.0, por lo que conservamos la posición para permitir que el rebote diario desarrolle su curso completo.
- **[HOLD] ETH-USD** (Confianza: 75%): Es la posición con mejor desempeño actual (+0.83%). Se mantiene activa buscando alcanzar la zona objetivo de take-profit entre +2.0% y +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Las posiciones llevan casi 10 horas abiertas con rendimientos muy planos y RSI de 1 hora neutralizado. Mantendremos las posiciones vigentes (BTC, SOL, ETH) por un ciclo más esperando la aceleración del volumen, pero si en el siguiente ciclo no muestran avance hacia la zona de +2.0%, procederemos a rotar el capital hacia activos con mayor dinamismo. Los niveles de stop-loss se mantienen estrictos en -2.0% de pérdida por posición."
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
