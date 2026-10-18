# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 06:40:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.41 USD** | **$38.45 USD** | 🔴 **-3.86%** ($-1.55) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $82103.01 | $10.11 | 📈 +1.15% | 11h 39m |
| `SOL-USD` | 0.097418 | $102.65 | $104.04 | $10.14 | 📈 +1.35% | 11h 29m |
| `ETH-USD` | 0.004193 | $2385.05 | $2422.66 | $10.16 | 📈 +1.58% | 11h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto muestra un comportamiento positivo de rebote tras la sobreventa previa. BTC-USD, SOL-USD y ETH-USD se encuentran abiertos 24/7 y registrando ganancias moderadas, con rendimientos actuales en cartera de entre +1.15% y +1.58%. Las posiciones están cerca pero aún no alcanzan el objetivo óptimo de take-profit del +2.0% al +3.5%, o la zona de sobrecompra estricta en RSI 1H (>70). Los mercados tradicionales (Wall Street) permanecen cerrados, por lo que la liquidez y operativa se concentran exclusivamente en criptoactivos."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): La posición acumula una ganancia de +1.15% y un RSI de 1H en 64.3. Todavía no alcanza el umbral objetivo de take-profit (+2.0% a +3.5%) ni sobrecompra extrema (>70), por lo que se mantiene para permitir que continúe el rebote técnico.
- **[HOLD] SOL-USD** (Confianza: 75%): La posición registra un rendimiento positivo de +1.35% con un RSI de 1H en 50.6. Mantiene la tendencia de recuperación y se conserva a la espera de alcanzar el objetivo de take-profit establecido.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un comportamiento favorable con una ganancia actual de +1.58% y un RSI de 1H en 52.9. Está muy cerca de la zona de toma de beneficios, por lo que se mantiene abierta en este ciclo para maximizar el tramo final del rebote.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en BTC-USD, SOL-USD y ETH-USD en este ciclo, monitoreando de cerca su aproximación al rango objetivo de take-profit (+2.0% a +3.5%) o señales de RSI 1H superior a 70 para asegurar beneficios en efectivo. El stop-loss estricto se mantiene operando en -2.0%. Si alguna posición pierde momentum o retrocede hacia los soportes críticos, procederé a vender inmediatamente para proteger el capital y rotar liquidez."
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
