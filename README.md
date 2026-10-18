# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 11:01:02`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$28.37 USD** | **$10.00 USD** | **$38.37 USD** | 🔴 **-4.07%** ($-1.63) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.097172 | $102.91 | $102.91 | $10.00 | 📈 +0.00% | 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "Los mercados tradicionales (Wall Street) se encuentran cerrados, por lo que toda la operativa activa se concentra en las criptomonedas. BTC-USD, ETH-USD y SOL-USD muestran una fase de consolidación neutral con RSI de 1H en rangos medios (44-50) y leves variaciones positivas de corto plazo. Tras la reciente toma de ganancias, cuento con una sólida liquidez de $38.37 USD para cazar oportunidades de rebote técnico."

**Operaciones del ciclo:**
- **[BUY] SOL-USD** (Confianza: 85%): SOL-USD muestra un RSI diario extremadamente bajo (16.4) en zona de sobreventa profunda y un RSI de 1H recuperándose a 45.9 con un cambio de 1h positivo (+0.1%). Esto indica un excelente escenario para cazar un rebote de reversión a la media (mean reversion) buscando una ganancia rápida del 2% al 3.5%. Asigno $10.00 USD dada la alta convicción en la sobreventa macro.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantengo $38.37 USD en efectivo tras rotar capital exitosamente. Los criptoactivos están estables pero con RSI diario bajo en el caso de SOL y ETH, lo que sugiere un potencial rebote de sobreventa si se intensifica el volumen. Monitorearé de cerca a SOL-USD y ETH-USD para desplegar $8.00 a $10.00 USD en cuanto el RSI de 1H supere 55 con un cambio de 1h positivo claro, buscando un take-profit rápido del 2% al 3.5% y manteniendo un stop-loss estricto a -2.0%."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **70** | 🎯 **41.4%** (29W / 27L / 14BE) | 🔴 **$-1.49 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 11:01` | 🟢 BUY | `SOL-USD` | $10.00 | $102.91 | SOL-USD muestra un RSI diario extremadamente bajo (16.4) en zona de sobreventa profunda y ... |
| `2026-10-18 08:00` | 🔴 SELL (+0.13$) | `ETH-USD` | $10.13 | $2415.11 | ETH-USD registra un RSI de 1H en 72.1 (sobrecompra) y una ganancia de +1.26%. Se procede a... |
| `2026-10-18 08:00` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $103.84 | SOL-USD presenta un RSI de 1H en 67.6 acercándose a zona de sobrecompra con una ganancia d... |
| `2026-10-18 08:00` | 🔴 SELL (+0.10$) | `BTC-USD` | $10.08 | $81974.15 | BTC-USD ha alcanzado un RSI de 1H en 78.8 (sobrecompra profunda) tras el rebote esperado, ... |
| `2026-10-17 19:10` | 🟢 BUY | `ETH-USD` | $10.00 | $2385.05 | ETH-USD muestra un RSI de 1H en 29.0 (sobreventa profunda) combinado con un cambio de 1h p... |

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
