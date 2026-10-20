# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 05:00:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.51 USD** | **$38.51 USD** | 🔴 **-3.73%** ($-1.49) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 18h 20m |
| `ETH-USD` | 0.004178 | $2393.62 | $2386.90 | $9.97 | 📉 -0.28% | 16h 9m |
| `SOL-USD` | 0.096034 | $104.13 | $104.28 | $10.01 | 📈 +0.14% | 12h 20m |
| `BTC-USD` | 0.000105 | $81767.70 | $81439.76 | $8.53 | 📉 -0.40% | 11h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se encuentra mayormente en un entorno lateral a bajista con los principales índices de Wall Street cerrados y precios congelados. Los activos criptográficos (ETH-USD, SOL-USD, BTC-USD), que operan 24/7, muestran una consolidación de corto plazo con ligeros retrocesos en las últimas 24 horas, pero manteniendo RSI diarios en niveles de sobreventa profunda que sugieren oportunidades latentes de rebote (mean reversion). No hay momentum agresivo inmediato en la última hora, por lo que la postura actual es defensiva a la espera de la apertura de los mercados tradicionales o de una confirmación de volumen en cripto."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 60%): La posición en SOL-USD se mantiene estable con una pequeña ganancia del 0.14% y un RSI diario extremadamente bajo (21.3). Esperamos que el rebote técnico se materialice hacia la zona de take-profit sin necesidad de realizar acciones precipitadas.
- **[HOLD] BTC-USD** (Confianza: 55%): BTC-USD registra una leve pérdida de -0.4%, manteniéndose dentro de los márgenes tolerables de riesgo antes del stop-loss estricto (-2.0%). Mantenemos la posición a la espera de un catalizador de volumen.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (QQQ, ETH-USD, SOL-USD, BTC-USD) ya que ninguna ha alcanzado el stop-loss estricto de -2.0% ni el take-profit de +2.0% a +3.5%. Dado que los mercados tradicionales están cerrados, la prioridad es monitorear el comportamiento de las criptomonedas abiertas 24/7. Si el RSI de 1 hora rompe al alza con volumen en SOL o BTC, mantendremos la posición buscando el objetivo de ganancia; de lo contrario, si el soporte falla, se procederá a recortar pérdidas para proteger el capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 23:00` | 🟢 BUY | `BTC-USD` | $4.00 | $81646.39 | BTC-USD presenta un RSI de 1 hora en 27.7, nivel de sobreventa profunda ideal para un rebo... |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |

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
