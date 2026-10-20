# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 08:40:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.52 USD** | **$38.52 USD** | 🔴 **-3.71%** ($-1.48) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 21h 59m |
| `ETH-USD` | 0.004178 | $2393.62 | $2386.66 | $9.97 | 📉 -0.29% | 19h 49m |
| `SOL-USD` | 0.096034 | $104.13 | $104.26 | $10.01 | 📈 +0.12% | 15h 59m |
| `BTC-USD` | 0.000105 | $81767.70 | $81522.26 | $8.54 | 📉 -0.30% | 15h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional (QQQ, SPY, etc.) se encuentra cerrado y sin movimiento significativo. Las criptomonedas (SOL-USD, ETH-USD, BTC-USD) operan con un sesgo lateral a ligeramente bajista, manteniendo un comportamiento estable pero sin la fuerza de rebote esperada en el corto plazo tras casi 20 horas de tenencia. No se han alcanzado los límites de stop-loss estricto (-2.0%) ni de take-profit (+2.0%)."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 65%): La posición mantiene un rendimiento plano (+0.12%) tras cerca de 16 horas. El RSI de 1 hora está en 44.4 y el diario en 21.3, lo que sugiere acumulación en soporte. Mantenemos la posición a la espera de un impulso alcista hacia el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 60%): La posición registra una pérdida menor del -0.29%. El RSI diario en 24.2 muestra sobreventa profunda, por lo que se mantiene la posición para cazar el rebote técnico sin romper las reglas de riesgo.
- **[HOLD] BTC-USD** (Confianza: 60%): El precio se mantiene estable con una ligera pérdida del -0.3%. El RSI de 1 hora en 38.0 muestra compresión a la espera de un catalizador de volumen. Mantenemos la posición activa.
- **[HOLD] QQQ** (Confianza: 70%): El mercado tradicional está cerrado y la posición muestra estabilidad (-0.08%). Se mantiene en cartera a la espera de la apertura de Wall Street para evaluar su evolución y posible rotación si fuera necesario.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones abiertas actuales ya que ninguna ha tocado el stop-loss ni el take-profit. Dado que el efectivo es 0.0 USD, no se pueden realizar nuevas compras. Continuaremos monitoreando el comportamiento de las criptomonedas en busca de una aceleración en el RSI de 1 hora o la llegada a zonas de take-profit para asegurar ganancias y rotar capital en los siguientes ciclos."
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
