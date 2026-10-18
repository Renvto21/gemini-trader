# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 15:10:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.37 USD** | **$19.90 USD** | **$38.27 USD** | 🔴 **-4.33%** ($-1.73) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.097172 | $102.91 | $102.27 | $9.94 | 📉 -0.62% | 4h 9m |
| `ETH-USD` | 0.004205 | $2377.97 | $2367.80 | $9.96 | 📉 -0.43% | 3h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado y los principales índices muestran un tono bajista. En el sector cripto, que opera 24/7, SOL-USD y ETH-USD mantienen un comportamiento lateral con ligeras pérdidas en las últimas 24 horas, encontrándose en zonas de sobreventa profunda tanto en el RSI diario como en el de 1 hora. El cambio de 1 hora muestra un leve repunte incipiente en SOL-USD, lo que sugiere que el impulso de rebote podría desarrollarse próximamente."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD se encuentra en una zona de sobreventa extrema (RSI diario en 16.1) con un leve cambio positivo en 1h (+0.25%). Aunque lleva unas horas lateralizando, el escenario de rebote técnico sigue intacto y no ha alcanzado el stop-loss del -2.0%.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD presenta un RSI diario muy deprimido en 21.7. A pesar de una ligera contracción temporal, el activo está consolidando en niveles de soporte profundo a la espera de un gatillo alcista que permita buscar la toma de ganancias objetivo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas de SOL-USD y ETH-USD durante este ciclo ya que el holding time aún es moderado (~4h) y se encuentran en zonas clave de soporte macro (RSI diario < 30). Monitorear de cerca el RSI de 1 hora; si cruza al alza con decisión y la ganancia alcanza el rango de +2.0% a +3.5%, procederemos a tomar beneficios de inmediato. El stop-loss estricto permanece en -2.0%. La liquidez actual de $18.37 USD se mantendrá a la espera de confirmaciones adicionales."
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
