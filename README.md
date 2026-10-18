# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 21:20:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.13 USD** | **$38.18 USD** | 🔴 **-4.56%** ($-1.82) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81363.18 | $10.02 | 📈 +0.24% | 2h 19m |
| `SOL-USD` | 0.097418 | $102.65 | $103.15 | $10.05 | 📈 +0.49% | 2h 9m |
| `ETH-USD` | 0.004193 | $2385.05 | $2398.97 | $10.06 | 📈 +0.58% | 2h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra completamente CERRADO (fines de semana/fuera de horario), por lo que la liquidez activa se concentra estrictamente en el mercado cripto 24/7. Las criptomonedas principales (BTC-USD, ETH-USD y SOL-USD) muestran un comportamiento lateral a ligeramente bajista en la última hora, con los indicadores RSI de 1H comprimiéndose cerca o por debajo de 40 tras el rebote inicial. Mantenemos nuestras posiciones abiertas con ganancias marginales (entre +0.24% y +0.58%), sin alcanzar aún los objetivos de take-profit (+2.0%) ni activar los stop-loss."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 70%): La posición en BTC-USD registra una ganancia moderada de +0.24% tras más de 2 horas de tenencia. Aunque el cambio de 1h es ligeramente negativo (-0.22%), el precio se mantiene estable y por encima del precio de entrada, por lo que se prefiere mantener a la espera de un mayor impulso alcista.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD mantiene una rentabilidad positiva de +0.58% con un RSI de 1H en 30.5. No ha alcanzado el objetivo de take-profit del +2.0% pero se mantiene firme sobre el soporte inicial, por lo que se mantiene la posición.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD presenta un PnL positivo de +0.49%. El precio muestra estabilidad a corto plazo y el sesgo operativo actual sugiere mantener para buscar una extensión del rebote hacia la zona de sobrecompra.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD durante este ciclo ya que se encuentran estables y dentro de rangos operativos seguros. Monitorear de cerca el RSI de 1H y la acción de precio; si alguna posición alcanza la zona de take-profit entre +2.0% y +3.5% o su RSI supera los 70 puntos, procederemos a vender para asegurar capital en efectivo. Si el momentum se deteriora y rompe los soportes actuales, aplicaremos stop-loss inmediato."
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
