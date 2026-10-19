# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 12:01:24`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$28.57 USD** | **$10.03 USD** | **$38.60 USD** | 🔴 **-3.51%** ($-1.40) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $721.16 | $10.03 | 📈 +0.31% | 1h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra mayormente estable pero con una ligera atonía en el corto plazo tras los rebotes recientes. Los índices principales y las criptomonedas muestran un movimiento lateral en la última hora, con RSI de 1 hora neutrales rondando la zona de 40 a 50, sin mostrar señales claras de sobreventa o sobrecompra extrema en este preciso instante."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 75%): La posición en QQQ muestra un rendimiento positivo del +0.31% tras poco tiempo de haber sido abierta. Mantiene una estructura técnica aceptable y no ha activado ninguna señal de salida por take-profit o stop-loss, por lo que es óptimo mantenerla para dejar correr el pequeño impulso.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos la posición en QQQ ya que registra una ganancia moderada del +0.31% y aún no alcanza nuestro objetivo de take-profit (+2.0% a +3.5%) ni ha tocado el stop-loss estricto de -2.0%. El efectivo disponible es de $28.57 USD y esperamos mejores oportunidades de entrada en cripto o renta variable cuando el RSI de 1 hora descienda por debajo de 35 para capturar rebotes con alta convicción."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |
| `2026-10-19 01:50` | 🔴 SELL (+0.09$) | `ETH-USD` | $8.09 | $2428.97 | ETH-USD registra una ganancia acumulada y su RSI de 1 hora ha alcanzado 68.3, acercándose ... |
| `2026-10-19 01:00` | 🔴 SELL (-0.00$) | `SOL-USD` | $8.00 | $105.08 | SOL-USD ha entrado en sobrecompra con un RSI de 1 hora en 72.7, cumpliendo estrictamente c... |
| `2026-10-18 23:20` | 🟢 BUY | `SOL-USD` | $8.00 | $105.11 | SOL-USD presenta un RSI diario en 21.8 (sobreventa extrema) y un momentum de 24 horas alci... |
| `2026-10-18 23:10` | 🔴 SELL (+0.17$) | `SOL-USD` | $8.17 | $105.19 | SOL-USD acumula una ganancia del +2.12%, cumpliendo con la regla de toma rápida de gananci... |

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
