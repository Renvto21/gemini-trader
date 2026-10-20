# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 05:40:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.50 USD** | **$38.50 USD** | 🔴 **-3.74%** ($-1.50) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 18h 59m |
| `ETH-USD` | 0.004178 | $2393.62 | $2387.72 | $9.98 | 📉 -0.25% | 16h 49m |
| `SOL-USD` | 0.096034 | $104.13 | $104.18 | $10.00 | 📈 +0.05% | 12h 59m |
| `BTC-USD` | 0.000105 | $81767.70 | $81448.09 | $8.53 | 📉 -0.39% | 12h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento mixto a defensivo. Los activos tradicionales como QQQ, SPY, GLD y NVDA se encuentran en mercados cerrados con precios congelados y tendencias bajistas de corto plazo. En el ecosistema cripto, que permanece abierto 24/7, los precios muestran una ligera consolidación lateral con cambios de 1 hora cercanos a cero (BTC-USD, ETH-USD, SOL-USD), manteniendo sus niveles de soporte macro pero sin el impulso alcista inmediato necesario para disparar rebotes rápidos. La liquidez en efectivo es actualmente cero y ninguna posición ha alcanzado los umbrales estrictos de stop-loss (-2.0%) o take-profit (+2.0%)."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición se mantiene estable con un PnL de +0.05% tras 12 horas. No ha alcanzado el take-profit ni el stop-loss, por lo que se mantiene en cartera esperando un incremento de momentum en cripto.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos todas las posiciones actuales (QQQ, ETH-USD, SOL-USD, BTC-USD) ya que se encuentran estables dentro de los rangos de tolerancia y operando sin liquidez libre. Para los siguientes ciclos, el plan táctico consiste en vigilar de cerca el comportamiento de SOL-USD y ETH-USD: si el RSI de 1 hora supera los 60 con volumen incremental o se acerca al objetivo de take-profit del +2.5%, realizaremos tomas parciales o totales de beneficios para liberar efectivo. Si alguna posición perfora el soporte y se acerca al stop-loss del -2.0%, procederemos a vender inmediatamente para proteger el capital y rotar hacia nuevas oportunidades."
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
