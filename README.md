# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 03:40:35`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.18 USD** | **$38.46 USD** | 🔴 **-3.84%** ($-1.54) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.79 | $10.10 | 📈 +1.04% | 12h 39m |
| `ETH-USD` | 0.004144 | $2412.98 | $2430.18 | $10.07 | 📈 +0.71% | 11h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, manteniendo los precios congelados y obligando a enfocar la operativa 100% en criptomonedas. SOL-USD y ETH-USD muestran un comportamiento estable con ganancias moderadas pero sin alcanzar todavía la zona de take-profit objetivo (+2.0% a +3.5%). El RSI de 1 hora de SOL-USD ha subido a 62.4, acercándose a la zona de resistencia o sobrecompra a corto plazo, mientras que ETH-USD mantiene una estructura lateral alcista leve. Mantendremos las posiciones abiertas esperando el impulso final para asegurar ganancias."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición acumula una ganancia de +1.04% y un RSI de 1h en 62.4 acercándose a la zona de take-profit. Se mantiene activa para buscar el objetivo completo de ganancia sin forzar una salida prematura.
- **[HOLD] ETH-USD** (Confianza: 75%): La posición muestra un rendimiento positivo de +0.71% con un RSI de 1h equilibrado en 51.3. Se conserva a la espera de que el impulso alcista la acerque a la banda de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas de SOL-USD y ETH-USD. Vigilar de cerca el RSI de 1 hora de SOL-USD (actualmente en 62.4): si alcanza la zona de sobrecompra (>70) o llega al rango de take-profit del +2.0% al +3.5%, proceder a vender para tomar beneficios y liberar efectivo. Mantener el stop-loss estricto en -2.0% para proteger el capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **63** | 🎯 **38.1%** (24W / 25L / 14BE) | 🔴 **$-1.60 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 16:30` | 🟢 BUY | `ETH-USD` | $10.00 | $2412.98 | ETH-USD muestra un RSI diario en niveles de sobreventa extrema (30.3) y un cambio positivo... |
| `2026-10-16 16:30` | 🔴 SELL (-0.11$) | `MSFT` | $6.39 | $526.18 | MSFT lleva más de 1 día y 5 horas abierto mostrando debilidad persistente y un rendimiento... |
| `2026-10-16 15:01` | 🟢 BUY | `SOL-USD` | $10.00 | $103.71 | SOL-USD presenta un RSI de 1 hora en 34.3 saliendo de la zona de sobreventa extrema, acomp... |
| `2026-10-16 14:30` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2399.90 | ETH-USD ha rebasado el umbral estricto de stop-loss (-2.12%), operando en tendencia bajist... |
| `2026-10-16 13:40` | 🔴 SELL (-0.02$) | `NVDA` | $7.98 | $216.80 | NVDA lleva más de 24 horas abierto operando bajo la SMA20 con un momentum débil, acumula u... |

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
