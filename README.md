# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 21:10:35`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.07 USD** | **$38.36 USD** | 🔴 **-4.10%** ($-1.64) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.22 | $10.05 | 📈 +0.49% | 6h 9m |
| `ETH-USD` | 0.004144 | $2412.98 | $2418.16 | $10.02 | 📈 +0.21% | 4h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado y los índices muestran una tendencia bajista de corto plazo. En el mercado de criptomonedas, que opera 24/7, los activos principales como SOL-USD y ETH-USD presentan una ligera compresión en el RSI de 1 hora (por debajo de 30), consolidando tras los intentos previos de rebote. Mantenemos las posiciones actuales buscando una ruptura al alza cuando el impulso intradiario recupere fuerza."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 65%): La posición mantiene una ganancia leve de +0.49% tras 6 horas de holding. Aunque el RSI de 1h se ha comprimido a 29.1, aún no alcanza el objetivo de take-profit de +2.0% ni el stop-loss, por lo que se mantiene para permitir que el rebote técnico evolucione.
- **[HOLD] ETH-USD** (Confianza: 65%): ETH-USD registra una ganancia marginal de +0.21% con un RSI diario en sobreventa extrema (30.5). Se mantiene la posición en busca del objetivo de take-profit establecido sin infringir los límites de riesgo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear estrictamente las posiciones abiertas en SOL-USD y ETH-USD para asegurar ganancias si se alcanza el rango de +2.0% a +3.5%, o activar el stop-loss en caso de que caigan por debajo del -2.0%. Mantener la liquidez remanente lista para desplegar en cuanto se detecte una mejora clara en el momentum intradiario."
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
