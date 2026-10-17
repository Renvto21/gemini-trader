# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 02:40:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.15 USD** | **$38.44 USD** | 🔴 **-3.90%** ($-1.56) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.76 | $10.10 | 📈 +1.01% | 11h 39m |
| `ETH-USD` | 0.004144 | $2412.98 | $2424.80 | $10.05 | 📈 +0.49% | 10h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de acciones tradicionales se encuentra cerrado, por lo que toda la atención y liquidez operativa debe concentrarse exclusivamente en los activos cripto abiertos 24/7. Las posiciones actuales en SOL-USD y ETH-USD muestran ligeras ganancias (+1.01% y +0.49% respectivamente), manteniéndose estables pero sin alcanzar todavía el umbral óptimo de take-profit (+2.0% a +3.5%) o sobrecompra en 1h. Mantenemos la disciplina táctica sin forzar nuevas entradas mientras esperamos que las posiciones actuales maduren o alcancen sus objetivos de salida."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición muestra un rendimiento positivo de +1.01% tras casi 12 horas abiertas. El RSI de 1 hora está en 64.8, acercándose a la zona de sobrecompra donde buscaremos asegurar beneficios parciales o totales al llegar al rango de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): La posición se mantiene en terreno positivo (+0.49%) tras poco más de 10 horas. El contexto diario muestra un RSI en sobrecompra previa que justifica mantener el rebote técnico en curso sin disparar el stop-loss.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear SOL-USD para asegurar ganancias si su RSI de 1 hora se acerca a 70 o si el precio alcanza la zona objetivo de take-profit (+2.0% a +3.5%). Vigilar ETH-USD de cerca manteniendo el stop-loss en -2.0% y preparado para rotar capital o tomar beneficios parciales si el impulso de corto plazo se intensifica."
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
