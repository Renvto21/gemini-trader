# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 13:50:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.85 USD** | **$38.32 USD** | 🔴 **-4.19%** ($-1.68) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.24 | $9.93 | 📉 -0.67% | 3h 30m |
| `ETH-USD` | 0.004126 | $2423.75 | $2403.39 | $9.92 | 📉 -0.84% | 2h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se encuentra operando en fin de semana con un sesgo lateral a ligeramente bajista, mientras que los mercados tradicionales permanecen cerrados. Las posiciones actuales en SOL-USD y ETH-USD muestran ligeras pérdidas no realizadas (-0.67% y -0.84% respectivamente), pero se mantienen dentro de un rango de tolerancia aceptable lejos del stop-loss estricto del -2.0%. Los indicadores de 1 hora muestran un impulso pausado sin señales inmediatas de ruptura alcista o sobrecompra."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición se mantiene abierta con una pérdida menor de -0.67% tras 3 horas y media. El RSI de 1 hora en 33.4 sugiere que la presión vendedora se está desacelerando, por lo que es prudente mantener y esperar el rebote técnico esperado.
- **[HOLD] ETH-USD** (Confianza: 70%): La posición acumula una pérdida temporal de -0.84% con un holding time de 2 horas. El contexto diario muestra sobreventa profunda (RSI diario 27.7), por lo que se mantiene la posición a la espera de la reacción alcista.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en SOL-USD y ETH-USD durante este ciclo a la espera de un repunte en el momentum intradiario. Vigilar de cerca el nivel de soporte actual y estar preparados para asegurar beneficios parciales si el RSI de 1 hora rebota hacia la zona de 70, o ejecutar un stop-loss estricto si las pérdidas superan el -2.0% en cualquiera de los dos activos."
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
