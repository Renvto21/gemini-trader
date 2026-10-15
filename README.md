# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 16:10:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.26 USD** | **$34.50 USD** | **$38.77 USD** | 🔴 **-3.08%** ($-1.23) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.48 | $9.89 | 📉 -1.06% | 1d 5h |
| `MSFT` | 0.012146 | $535.17 | $540.66 | $6.57 | 📈 +1.03% | 5h 19m |
| `QQQ` | 0.013791 | $725.09 | $726.99 | $10.03 | 📈 +0.26% | 3h 49m |
| `NVDA` | 0.036812 | $217.32 | $217.80 | $8.02 | 📈 +0.22% | 3h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un comportamiento mixto con recuperación técnica en algunos activos tecnológicos y criptomonedas, aunque persiste la cautela general con varios índices por debajo de su SMA20. MSFT registra una ganancia moderada cercana al objetivo, mientras que QQQ y NVDA operan con RSI de 1h deprimido pero mostrando leves intentos de estabilización."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 75%): MSFT se encuentra en tendencia alcista con un rendimiento positivo del 1.03%, acercándose al objetivo de toma de beneficios (+2.0% a +3.5%). Mantengo la posición a la espera de que madure el movimiento.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca el rendimiento de MSFT para asegurar beneficios si alcanza el rango de +2.0% a +3.5%. Mantener la vigilancia en QQQ y NVDA evaluando su momentum de corto plazo; si no logran consolidar el rebote en los siguientes ciclos, considerar la rotación de capital hacia activos con mayor dinamismo. La liquidez se mantendrá en niveles mínimos."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **57** | 🎯 **42.1%** (24W / 19L / 14BE) | 🔴 **$-1.12 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |
| `2026-10-15 12:10` | 🔴 SELL (+0.14$) | `ETH-USD` | $6.14 | $2417.73 | ETH-USD ha alcanzado un rendimiento del +2.33%, cumpliendo con el rango establecido para l... |
| `2026-10-15 11:50` | 🔴 SELL (+0.13$) | `SOL-USD` | $6.13 | $104.21 | SOL-USD ha alcanzado un rendimiento de +2.11%, cumpliendo con la regla de toma rápida de g... |
| `2026-10-15 10:50` | 🟢 BUY | `MSFT` | $6.50 | $535.17 | MSFT presenta un RSI de 1h ultra comprimido en sobreventa extrema (14.7) con un cambio pos... |

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
