# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 18:10:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$29.98 USD** | **$8.01 USD** | **$37.99 USD** | 🔴 **-5.02%** ($-2.01) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.079341 | $100.83 | $100.95 | $8.01 | 📈 +0.12% | 1h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se encuentra abierto 24/7 con una tendencia general bajista pero mostrando condiciones extremas de sobreventa en gráficos diarios y de 1 hora, ideales para estrategias de mean reversion. Los mercados tradicionales están cerrados, por lo que toda la liquidez debe enfocarse exclusivamente en activos digitales."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición en SOL-USD lleva poco más de una hora abierta, registra una pequeña ganancia del +0.12% y mantiene un RSI de 1 hora de 28.4 junto con un RSI diario extremadamente deprimido en 15.4. Continuamos buscando el rebote técnico hacia el objetivo de take-profit establecido.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos la posición actual en SOL-USD vigilando que alcance nuestro objetivo de take-profit entre +2.0% y +3.5% (aprox. $103.00 - $104.50) y aplicando un stop-loss estricto en -2.0% (~$98.80). Asimismo, mantendremos una reserva mínima de efectivo de $4.00 USD y evaluaremos el comportamiento del precio de SOL en el próximo ciclo para asegurar ganancias o cortar pérdidas rápidamente."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **72** | 🎯 **40.3%** (29W / 29L / 14BE) | 🔴 **$-1.88 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 17:00` | 🟢 BUY | `SOL-USD` | $8.00 | $100.83 | SOL-USD muestra un RSI diario extremadamente deprimido en 15.3 y un RSI de 1 hora en 23.4 ... |
| `2026-10-18 16:40` | 🔴 SELL (-0.19$) | `ETH-USD` | $9.81 | $2332.39 | ETH-USD registra una pérdida del -1.92% con un RSI de 1 hora en 18.5 que refleja debilidad... |
| `2026-10-18 16:40` | 🔴 SELL (-0.20$) | `SOL-USD` | $9.80 | $100.90 | La posición en SOL-USD lleva casi 6 horas abierta con una pérdida del -1.95% y un RSI de 1... |
| `2026-10-18 12:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2377.97 | ETH-USD presenta un RSI diario extremadamente bajo en 22.0 y un RSI de 1 hora saliendo de ... |
| `2026-10-18 11:01` | 🟢 BUY | `SOL-USD` | $10.00 | $102.91 | SOL-USD muestra un RSI diario extremadamente bajo (16.4) en zona de sobreventa profunda y ... |

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
