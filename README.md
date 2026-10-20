# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 01:00:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.77 USD** | **$38.77 USD** | 🔴 **-3.08%** ($-1.23) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 14h 20m |
| `ETH-USD` | 0.004178 | $2393.62 | $2412.18 | $10.08 | 📈 +0.78% | 12h 9m |
| `SOL-USD` | 0.096034 | $104.13 | $105.21 | $10.10 | 📈 +1.04% | 8h 20m |
| `BTC-USD` | 0.000105 | $81767.70 | $82041.26 | $8.59 | 📈 +0.33% | 7h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional (QQQ, SPY, NVDA) se encuentra cerrado, por lo que toda la actividad se concentra en criptomonedas (24/7). Las criptomonedas principales (SOL-USD, ETH-USD, BTC-USD) muestran ligeras recuperaciones con RSI de 1 hora neutrales y RSI diario en zonas de sobreventa profunda, manteniendo el sesgo de rebote técnico. Ninguna de nuestras posiciones ha alcanzado aún el objetivo de take-profit (+2% a +3.5%) ni ha roto los stop-loss, por lo que se prioriza la retención de activos abiertos y la paciencia."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD mantiene un rendimiento positivo (+1.04%) y un RSI diario bajo (22.7) con potencial alcista. El RSI de 1 hora (59.1) aún no alcanza la zona de sobrecompra (>70) necesaria para ejecutar la toma de beneficios, por lo que se mantiene la posición.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones activas en SOL-USD, ETH-USD, BTC-USD y QQQ. Estar alerta al comportamiento de SOL-USD y ETH-USD para asegurar ganancias parciales o totales si el RSI de 1 hora se acerca o supera la zona de 70. Vigilar la apertura de los mercados tradicionales para evaluar la rotación o toma de beneficios en QQQ si se presenta una oportunidad de mayor impulso."
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
