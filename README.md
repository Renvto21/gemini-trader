# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 16:40:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.17 USD** | **$24.62 USD** | **$38.79 USD** | 🔴 **-3.04%** ($-1.21) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $540.37 | $6.56 | 📈 +0.97% | 5h 50m |
| `QQQ` | 0.013791 | $725.09 | $728.58 | $10.05 | 📈 +0.48% | 4h 20m |
| `NVDA` | 0.036812 | $217.32 | $217.53 | $8.01 | 📈 +0.10% | 3h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un comportamiento mixto con un sesgo cauteloso en activos tecnológicos tradicionales, mientras que las criptomonedas y algunos índices registran una ligera estabilización. Las posiciones actuales en cartera (MSFT, QQQ, NVDA) se mantienen estables pero con un momentum de corto plazo muy débil o plano. MSFT muestra un rendimiento positivo cercano al +0.97%, mientras que QQQ y NVDA operan con ganancias mínimas. No se alcanzan aún los objetivos de take-profit óptimos (+2.0% a +3.5%), pero es necesario vigilar de cerca la falta de aceleración en NVDA, cuyo RSI de 1h se mantiene profundamente deprimido en 18.1, indicando fatiga."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 70%): La posición en MSFT muestra una ganancia moderada de +0.97% dentro del horario operativo y se mantiene sobre la media móvil. Mantendremos la posición esperando acercarnos al rango de take-profit de +2.0% a +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener MSFT y QQQ buscando que alcancen el rango objetivo de take-profit (+2.0% a +3.5%). Monitorear de cerca a NVDA: si en el próximo ciclo no muestra un rebote contundente tras su fuerte sobreventa, procederé a venderla para rotar el capital hacia oportunidades con mayor dinamismo en cripto o activos con mejor tendencia alcista. Proteger estrictamente el capital manteniendo la reserva de liquidez operativa."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **58** | 🎯 **41.4%** (24W / 20L / 14BE) | 🔴 **$-1.22 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |
| `2026-10-15 12:10` | 🔴 SELL (+0.14$) | `ETH-USD` | $6.14 | $2417.73 | ETH-USD ha alcanzado un rendimiento del +2.33%, cumpliendo con el rango establecido para l... |
| `2026-10-15 11:50` | 🔴 SELL (+0.13$) | `SOL-USD` | $6.13 | $104.21 | SOL-USD ha alcanzado un rendimiento de +2.11%, cumpliendo con la regla de toma rápida de g... |

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
