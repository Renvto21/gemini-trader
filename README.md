# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 14:10:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.37 USD** | **$19.91 USD** | **$38.28 USD** | 🔴 **-4.30%** ($-1.72) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.097172 | $102.91 | $102.26 | $9.94 | 📉 -0.63% | 3h 9m |
| `ETH-USD` | 0.004205 | $2377.97 | $2371.46 | $9.97 | 📉 -0.27% | 2h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado por fin de semana, por lo que toda la atención se centra en el mercado de criptomonedas abierto 24/7. Tanto SOL-USD como ETH-USD muestran sobreventa profunda en gráficos diarios, pero en el corto plazo (1 hora) sus RSI se mantienen deprimidos (<30) y sin una ruptura clara al alza, aunque registran ligeros repuntes en change_1h_pct (+0.29% y +0.34% respectivamente). Mantendremos las posiciones actuales para darles tiempo a desarrollar el rebote técnico esperado, respetando los stop-loss en -2.0%."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD lleva poco tiempo abierta (3h 9m). Aunque el RSI diario es extremadamente bajo (16.1), el activo muestra un tímido momentum positivo de corto plazo (+0.29% en 1h). Mantenemos la posición a la espera del rebote técnico hacia el objetivo de take-profit, respetando el stop-loss.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD presenta una pérdida marginal (-0.27%) tras 2h 9m de holding. El RSI de 1 hora se mantiene en 25.6 con un cambio de 1h positivo (+0.34%). Daremos margen para que el rebote técnico se consolide sin apresurar la venta, monitoreando el soporte.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones de SOL-USD y ETH-USD vigentes. Monitorear de cerca los indicadores de 1 hora; si el RSI de 1h supera los 40 y el change_1h_pct se mantiene firmemente positivo, buscar la toma de beneficios (take-profit) entre +2.0% y +3.5%. En caso de perforar el stop-loss del -2.0%, cortar pérdidas inmediatamente y liberar liquidez."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **70** | 🎯 **41.4%** (29W / 27L / 14BE) | 🔴 **$-1.49 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 12:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2377.97 | ETH-USD presenta un RSI diario extremadamente bajo en 22.0 y un RSI de 1 hora saliendo de ... |
| `2026-10-18 11:01` | 🟢 BUY | `SOL-USD` | $10.00 | $102.91 | SOL-USD muestra un RSI diario extremadamente bajo (16.4) en zona de sobreventa profunda y ... |
| `2026-10-18 08:00` | 🔴 SELL (+0.13$) | `ETH-USD` | $10.13 | $2415.11 | ETH-USD registra un RSI de 1H en 72.1 (sobrecompra) y una ganancia de +1.26%. Se procede a... |
| `2026-10-18 08:00` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $103.84 | SOL-USD presenta un RSI de 1H en 67.6 acercándose a zona de sobrecompra con una ganancia d... |
| `2026-10-18 08:00` | 🔴 SELL (+0.10$) | `BTC-USD` | $10.08 | $81974.15 | BTC-USD ha alcanzado un RSI de 1H en 78.8 (sobrecompra profunda) tras el rebote esperado, ... |

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
