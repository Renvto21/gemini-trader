# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 00:10:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.35 USD** | **$38.39 USD** | 🔴 **-4.02%** ($-1.61) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81789.00 | $10.08 | 📈 +0.76% | 5h 9m |
| `SOL-USD` | 0.097418 | $102.65 | $104.01 | $10.13 | 📈 +1.32% | 4h 59m |
| `ETH-USD` | 0.004193 | $2385.05 | $2417.63 | $10.14 | 📈 +1.37% | 4h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con un tono de recuperación moderada tras los mínimos recientes. Las posiciones abiertas en BTC-USD, SOL-USD y ETH-USD muestran ganancias no realizadas modestas (entre +0.76% y +1.37%), acercándose paulatinamente a la zona objetivo de take-profit (+2.0% a +3.5%). Los mercados tradicionales (Wall Street) se encuentran cerrados, por lo que toda la atención se centra en sostener y gestionar estas posiciones activas sin forzar nuevas compras prematuras."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD muestra una ganancia actual del +0.76% con un RSI de 1H en 59.9. El impulso de rebote continúa su curso, por lo que se mantiene la posición buscando alcanzar el objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD registra un PnL positivo de +1.32% y un RSI de 1H estable en 51.1. La posición está madurando adecuadamente hacia la zona de toma de beneficios.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD mantiene un rendimiento positivo de +1.37% con un RSI de 1H en 49.0. Se retiene la posición a la espera de que el momentum alcista la impulse hacia el rango de take-profit estipulado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (BTC-USD, SOL-USD, ETH-USD) mientras continúan su avance. Monitorear de cerca el RSI de 1 hora y el avance de los precios: si alguna posición alcanza la zona de +2.0% a +3.5% de beneficio, proceder a vender para asegurar ganancias y rotar liquidez. Mantener el stop-loss estricto en -2.0%. No abrir nuevas posiciones en este ciclo para consolidar la recuperación del portafolio."
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
