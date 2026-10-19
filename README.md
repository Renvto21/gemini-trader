# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 11:00:58`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$28.57 USD** | **$9.98 USD** | **$38.55 USD** | 🔴 **-3.64%** ($-1.45) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $717.50 | $9.98 | 📉 -0.20% | 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo mixto con varios activos intentando recuperarse de caídas recientes de 7 días. Los índices y grandes tecnológicas como QQQ, NVDA y SPY muestran un leve impulso en la última hora, aunque la mayoría de los activos siguen operando por debajo de sus medias móviles de 20 periodos en el gráfico diario. Las criptomonedas muestran consolidación con un sesgo ligeramente bajista en la última hora sin señales claras de sobreventa o ruptura inminente."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 80%): La posición en QQQ lleva pocos minutos abierta con una pérdida marginal de -0.2%. Mantiene un cambio positivo en la última hora (+1.08%) y cumple con la tesis de rebote técnico. Mantendremos la posición para permitir que alcance el objetivo de take-profit sin apresurar salidas.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantenemos la posición abierta en QQQ tras su reciente entrada de hace 20 minutos; actualmente registra un PnL de -0.2%. Monitorearemos de cerca que mantenga el soporte y busque la zona de take-profit entre +2.0% y +3.5% (aprox. $733.30 a $744.00), mientras que mantendremos un stop-loss estricto a -2.0% (aprox. $704.54). Dado que la liquidez en efectivo es de $28.57 USD (por encima de la reserva mínima) y no hay señales claras de ruptura en cripto con RSI de 1 hora saliendo de sobreventa extrema, decidimos mantener la posición actual y conservar liquidez en espera de una confirmación más sólida en el próximo ciclo."
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
