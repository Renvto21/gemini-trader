# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 22:10:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.31 USD** | **$16.16 USD** | **$38.47 USD** | 🔴 **-3.82%** ($-1.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.077662 | $103.01 | $104.46 | $8.11 | 📈 +1.41% | 2h 40m |
| `ETH-USD` | 0.003330 | $2402.76 | $2417.02 | $8.05 | 📈 +0.59% | 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas permanece activo y muestra un sesgo de recuperación gradual tras caídas previas. SOL-USD y ETH-USD se encuentran en zonas de sobreventa diaria pero consolidando rebotes de corto plazo en gráficos de 1 hora, con RSI en torno a 50-54 y variaciones positivas recientes. Los mercados tradicionales (Wall Street) se encuentran cerrados, por lo que toda la atención operativa se concentra en mantener y gestionar el riesgo de las posiciones abiertas en crypto."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD presenta una ganancia actual de +1.41%, acercándose al rango objetivo de take-profit (+2.0% a +3.5%). El RSI de 1h se encuentra en 53.9 con un cambio positivo del 0.29%, lo que indica continuidad en el rebote técnico sin señales de agotamiento.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un rendimiento positivo de +0.59% tras haber abierto la posición recientemente. Mantiene un RSI de 1h en 50.3 y un cambio horario positivo, por lo que se mantiene en cartera para permitir que desarrolle todo su potencial de rebote hacia el objetivo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones de SOL-USD y ETH-USD mientras sigan mostrando un momentum positivo y no alcancen los niveles objetivo de take-profit (+2.0% a +3.5%) o sobrecompra en 1h (> 70). El stop-loss se mantiene estricto en -2.0% para proteger el capital. No abrimos nuevas posiciones para conservar la liquidez mínima requerida y permitir que las operaciones actuales maduren."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **74** | 🎯 **41.9%** (31W / 29L / 14BE) | 🔴 **$-1.55 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 21:20` | 🟢 BUY | `ETH-USD` | $8.00 | $2402.76 | ETH-USD muestra un RSI diario fuertemente sobrevendido en 23.2 y un cambio positivo en la ... |
| `2026-10-18 21:00` | 🔴 SELL (+0.16$) | `ETH-USD` | $8.16 | $2409.06 | ETH-USD ha alcanzado una ganancia del +2.03%, cumpliendo con la regla de toma rápida de ga... |
| `2026-10-18 19:30` | 🟢 BUY | `SOL-USD` | $8.00 | $103.01 | SOL-USD presenta un RSI diario extremadamente bajo (16.5) y un RSI de 1h recuperándose has... |
| `2026-10-18 19:10` | 🔴 SELL (+0.17$) | `SOL-USD` | $8.17 | $102.92 | SOL-USD ha alcanzado un rendimiento de +2.07% cumpliendo con nuestra regla de toma rápida ... |
| `2026-10-18 18:40` | 🟢 BUY | `ETH-USD` | $8.00 | $2361.22 | ETH-USD muestra un RSI diario deprimido en 21.5 y un RSI de 1 hora que se recupera a 34.3 ... |

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
