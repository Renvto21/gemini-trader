# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 01:40:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.54 USD** | **$17.09 USD** | **$39.63 USD** | 🔴 **-0.92%** ($-0.37) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2514.71 | $5.01 | 📈 +0.25% | 8h 29m |
| `BTC-USD` | 0.000072 | $83128.62 | $83714.40 | $6.04 | 📈 +0.70% | 4h 39m |
| `SOL-USD` | 0.055840 | $107.45 | $108.10 | $6.04 | 📈 +0.60% | 2h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto mantiene un tono neutral a ligeramente alcista con los principales activos (BTC-USD, ETH-USD, SOL-USD) operando abiertos 24/7 y mostrando ganancias moderadas en las últimas 24 horas. Los mercados tradicionales de Wall Street se encuentran cerrados, por lo que toda la atención táctica se centra en la continuidad de los rebotes en criptomonedas. Nuestras posiciones actuales muestran ganancias pequeñas pero positivas, sin alcanzar aún el objetivo de take-profit del 2.0% al 3.5% o niveles extremos de sobrecompra en RSI de 1 hora."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): La posición en BTC-USD muestra un rendimiento positivo de +0.70% y un RSI de 1 hora en 57.1. Se mantiene dentro del plan para buscar el objetivo de take-profit entre +2.0% y +3.5% sin activar el stop-loss.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD se mantiene estable con una ganancia de +0.25% y un RSI de 1 hora neutral en 50.5. Esperamos mayor tracción alcista para asegurar beneficios.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD presenta un rendimiento positivo de +0.60% y un RSI de 1 hora en 58.8. Continuamos monitoreando el rebote técnico desde la sobreventa diaria.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, ETH-USD y SOL-USD vigilando de cerca el progreso de las ganancias hacia el rango de take-profit del 2.0% al 3.5% o hasta que el RSI de 1 hora supere 70. Mantener el stop-loss estricto en -2.0%. Dado que el efectivo disponible es de $22.54 y ya tenemos una excelente exposición a los tres principales activos cripto, mantendremos las posiciones abiertas y esperaremos una mayor aceleración del momentum o la apertura de los mercados tradicionales para buscar nuevas entradas tácticas."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **48** | 🎯 **45.8%** (22W / 12L / 14BE) | 🔴 **$-0.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |

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
