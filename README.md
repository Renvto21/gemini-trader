# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 20:00:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.10 USD** | **$38.39 USD** | 🔴 **-4.02%** ($-1.61) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.33 | $10.06 | 📈 +0.60% | 4h 59m |
| `ETH-USD` | 0.004144 | $2412.98 | $2423.06 | $10.04 | 📈 +0.42% | 3h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado y sin actividad, mientras que el sector cripto se mantiene abierto 24/7 con un comportamiento lateral a ligeramente bajista. Las posiciones abiertas en SOL-USD y ETH-USD muestran ganancias menores (+0.60% y +0.42% respectivamente) tras casi 4 a 5 horas en cartera, operando por debajo de la zona objetivo de take-profit (+2.0% a +3.5%) pero manteniéndose alejadas de los niveles de stop-loss. No hay suficiente impulso alcista en este preciso momento para justificar nuevas entradas agresivas, por lo que la postura táctica es mantener las posiciones actuales y conservar liquidez."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición mantiene un rendimiento positivo de +0.60% con un tiempo en cartera de cerca de 5 horas. El impulso de rebote continúa formándose lentamente y se mantiene lejos del límite de stop-loss, por lo que se decide mantener a la espera del objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD registra una ganancia del +0.42% tras poco más de 3 horas de mantener la posición. El contexto técnico muestra soporte en los niveles de sobreventa diaria previa, por lo que se mantiene en cartera para buscar el objetivo de take-profit estipulado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en SOL-USD y ETH-USD para permitir que alcancen la zona objetivo de take-profit entre +2.0% y +3.5%. Vigilar el RSI de 1 hora; si se acerca a sobrecompra (> 70) o se alcanza la rentabilidad esperada, asegurar beneficios. Ejecutar stop-loss inmediato si el rendimiento cae por debajo de -2.0%. Mantener la liquidez actual intacta hasta la apertura del mercado tradicional o hasta que aparezca una ruptura con alta convicción en cripto."
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
