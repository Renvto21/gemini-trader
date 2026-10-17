# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 23:20:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.09 USD** | **$38.38 USD** | 🔴 **-4.06%** ($-1.62) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.37 | $10.06 | 📈 +0.64% | 8h 19m |
| `ETH-USD` | 0.004144 | $2412.98 | $2419.10 | $10.03 | 📈 +0.25% | 6h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado y sin actividad. En el sector cripto, que opera 24/7, mantenemos posiciones en SOL-USD y ETH-USD con ligeras ganancias (+0.64% y +0.25% respectivamente). El impulso alcista es moderado y el RSI de 1 hora se mantiene estable, por lo que el plan táctico se centra en conservar las posiciones actuales mientras no rompan soportes y esperar a que alcancen el objetivo de take-profit entre +2.0% y +3.5%."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición mantiene un rendimiento positivo de +0.64% tras un holding de más de 8 horas. El RSI de 1 hora está en 38.4 y no muestra signos de debilidad inminente, por lo que es óptimo mantener para buscar la zona de take-profit del +2.0% al +3.5%.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD se mantiene en terreno positivo con +0.25% y un RSI diario en niveles de sobreventa. Continuamos dentro del plan táctico esperando un rebote más fuerte hacia el rango de ganancias establecido.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en SOL-USD y ETH-USD supervisando de cerca el stop-loss estricto a -2.0% y buscando tomar beneficios si alcanzan el rango objetivo de +2.0% a +3.5%. La liquidez actual se mantendrá en $18.29 USD a la espera de nuevas señales de volumen alcista en cripto para rotar o incrementar exposición."
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
