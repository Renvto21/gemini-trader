# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 10:50:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$28.57 USD** | **$10.01 USD** | **$38.58 USD** | 🔴 **-3.56%** ($-1.42) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $719.66 | $10.01 | 📈 +0.10% | 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo mixto con oportunidades de rebote técnico en activos tecnológicos e índices que intentan recuperar terreno tras caídas semanales. QQQ mantiene un buen comportamiento intradiario con un incremento del 1.38% en la última hora y un RSI de 1 hora estable en 49.6, reflejando continuidad en el impulso alcista reciente. Por otro lado, las criptomonedas como ETH-USD y SOL-USD se mantienen operativas 24/7 con RSI diarios muy deprimidos (24.6 y 21.2 respectivamente), lo cual sigue abriendo la puerta a futuras entradas tácticas de reversión a la media cuando se confirme el gatillo de corto plazo."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 80%): La posición en QQQ lleva pocos minutos abierta y muestra un comportamiento estable con una ligera ganancia del 0.1%. Esperaremos a que se acerque a nuestros objetivos de take-profit o que el momentum intradiario nos permita maximizar el rendimiento antes de realizar cualquier cambio.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantenemos la posición abierta en QQQ tras su reciente entrada, vigilando de cerca que mantenga su estructura alcista intradiaria con un objetivo de take-profit entre +2.5% y +3.5% (aproximadamente entre $737.00 y $744.00) y un stop-loss estricto a -2.0% para proteger capital. La liquidez disponible en efectivo es de $28.57 USD, por lo que evaluaremos oportunidades adicionales en cripto si ETH-USD o SOL-USD muestran una ruptura clara de su RSI de 1 hora por encima de 60."
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
