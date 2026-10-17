# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 12:50:36`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.90 USD** | **$38.38 USD** | 🔴 **-4.06%** ($-1.62) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.58 | $9.97 | 📉 -0.35% | 2h 30m |
| `ETH-USD` | 0.004126 | $2423.75 | $2408.46 | $9.94 | 📉 -0.63% | 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional (Wall Street) se encuentra cerrado, por lo que toda la actividad se concentra en las criptomonedas, que operan 24/7. Tanto SOL-USD como ETH-USD muestran ligeros retrocesos en la última hora y los indicadores RSI de 1 hora se mantienen neutrales (alrededor de 41-43), sin alcanzar aún el objetivo de take-profit (+2.0% a +3.5%) ni activar el stop-loss estricto de -2.0%. El portafolio se mantiene estable mientras esperamos una confirmación del impulso alcista de corto plazo."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición muestra una pérdida marginal de -0.35%, manteniéndose muy por encima del stop-loss del -2.0%. Esperamos que el momentum de corto plazo recupere terreno para buscar la zona de take-profit.
- **[HOLD] ETH-USD** (Confianza: 70%): La posición se mantiene estable con una pequeña variación negativa de -0.63%, operando de manera saludable dentro del rango de tolerancia antes de activar medidas de protección o toma de beneficios.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en SOL-USD y ETH-USD durante este ciclo ya que se encuentran dentro de rangos normales de fluctuación y no han roto los límites de stop-loss ni alcanzado los niveles de take-profit. Para el próximo ciclo, vigilar si el RSI de 1 hora supera 70 para asegurar ganancias, o si se deterioran por debajo de -2.0% para cortar pérdidas de inmediato."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **65** | 🎯 **40.0%** (26W / 25L / 14BE) | 🔴 **$-1.41 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 11:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2423.75 | ETH-USD presenta un RSI diario en niveles de sobreventa profunda (28.9) y un cambio positi... |
| `2026-10-17 10:20` | 🟢 BUY | `SOL-USD` | $10.00 | $103.94 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (22.5) y un cambio positiv... |
| `2026-10-17 04:30` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $104.94 | SOL-USD ha alcanzado un RSI de 1 hora de 70.4, entrando en zona de sobrecompra, y acumula ... |
| `2026-10-17 04:00` | 🔴 SELL (+0.07$) | `ETH-USD` | $10.07 | $2429.64 | ETH-USD ha alcanzado un RSI de 1 hora de 73.3, entrando en zona de sobrecompra. Siguiendo ... |
| `2026-10-16 16:30` | 🟢 BUY | `ETH-USD` | $10.00 | $2412.98 | ETH-USD muestra un RSI diario en niveles de sobreventa extrema (30.3) y un cambio positivo... |

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
