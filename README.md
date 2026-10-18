# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 05:20:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.20 USD** | **$38.24 USD** | 🔴 **-4.39%** ($-1.76) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81590.97 | $10.05 | 📈 +0.52% | 10h 19m |
| `SOL-USD` | 0.097418 | $102.65 | $103.17 | $10.05 | 📈 +0.51% | 10h 9m |
| `ETH-USD` | 0.004193 | $2385.05 | $2407.31 | $10.09 | 📈 +0.93% | 10h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que la liquidez opera al 100% en criptomonedas (BTC-USD, ETH-USD y SOL-USD). Las posiciones abiertas muestran ganancias moderadas (+0.52% a +0.93%), acercándose a la zona de take-profit objetivo (+2.0% a +3.5%), pero aún sin alcanzarla. El RSI de 1 hora se ha estabilizado en niveles neutrales tras el rebote inicial, manteniendo un sesgo constructivo en cripto mientras los índices globales permanecen estancados."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición muestra un rendimiento positivo de +0.52%. El precio se mantiene estable tras el rebote y no ha alcanzado ni el objetivo de take-profit ni el stop-loss, por lo que mantenemos la exposición.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD lidera las ganancias actuales con un +0.93%. Mantiene una estructura favorable en el corto plazo y continuamos buscando el objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] SOL-USD** (Confianza: 80%): La posición en SOL-USD registra una ganancia de +0.51%. El impulso técnico inicial se sostiene y no hay señales de debilidad que justifiquen una salida anticipada.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones vigentes en BTC, SOL y ETH en este ciclo ya que se encuentran en terreno positivo y sin activar ningún stop-loss. Seguiremos monitoreando de cerca la acción del precio para asegurar beneficios parciales o totales tan pronto como alcancen el rango de take-profit entre +2.0% y +3.5%. La reserva de efectivo se mantiene en niveles operativos mínimos."
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
