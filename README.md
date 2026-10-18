# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 18:00:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$29.98 USD** | **$8.02 USD** | **$38.01 USD** | 🔴 **-4.98%** ($-1.99) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.079341 | $100.83 | $101.13 | $8.02 | 📈 +0.30% | 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado por fin de semana, por lo que toda la liquidez y atención se concentran exclusivamente en las criptomonedas (24/7). Las principales criptos como SOL, ETH y BTC muestran una tendencia bajista de fondo bajo la SMA20, pero con indicadores de RSI diario extremadamente deprimidos, lo que sugiere oportunidades potenciales de rebote por reversión a la media. SOL-USD muestra un avance muy ligero pero su RSI de 1 hora se mantiene bajo, por lo que mantendremos la posición actual buscando el take-profit, mientras evaluamos la entrada en ETH-USD para aprovechar su sobreventa."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD lleva poco tiempo abierta (~59 minutos) y presenta una ganancia marginal del +0.3%. El RSI diario está extremadamente deprimido (15.5) y mantenemos la expectativa de un rebote técnico hacia la zona del take-profit sin necesidad de rotar el capital todavía.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos la posición abierta en SOL-USD vigilando que el precio alcance nuestro objetivo de take-profit entre +2.0% y +3.5% (aprox. $103.00 - $104.00) y aplicando un stop-loss estricto en -2.0% (~$98.80) si el impulso decae. Para el próximo ciclo, evaluaremos abrir una posición de compra en ETH-USD si su RSI de 1 hora cruza al alza y el cambio horario se torna positivo, utilizando parte de los $29.98 USD de efectivo disponible."
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
