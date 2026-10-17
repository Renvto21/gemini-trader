# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 22:40:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.06 USD** | **$38.35 USD** | 🔴 **-4.12%** ($-1.65) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.24 | $10.05 | 📈 +0.51% | 7h 39m |
| `ETH-USD` | 0.004144 | $2412.98 | $2415.71 | $10.01 | 📈 +0.11% | 6h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene en una tendencia bajista de corto plazo bajo la SMA20, con activos clave como ETH-USD y SOL-USD mostrando condiciones de sobreventa extrema en el RSI de 1 hora (20.2 y 30.3 respectivamente). Los mercados tradicionales permanecen cerrados, por lo que la liquidez activa debe centrarse en los activos 24/7. Las posiciones actuales muestran un rendimiento plano (+0.51% en SOL y +0.11% en ETH) tras varias horas sin lograr el impulso alcista esperado, lo que requiere paciencia o rotación si el momentum falla."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD muestra un rendimiento positivo marginal de +0.51% tras 7 horas de holding. El RSI de 1 hora está en 30.3, consolidando bases para un posible rebote desde la zona de sobreventa. Mantendremos la posición vigilando estrictamente el stop-loss del -2.0%.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD se mantiene estable con un PnL de +0.11%. A pesar de que el RSI de 1 hora cayó a 20.2, el RSI diario en 30.4 actúa como un soporte clave de mean reversion. Esperaremos a que se active el momentum alcista para buscar la toma de ganancias.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas de SOL-USD y ETH-USD durante este ciclo a pesar de la lentitud, ya que sus indicadores de sobreventa sugieren un posible rebote técnico inminente. Monitorear de cerca que el PnL no supere el límite de stop-loss de -2.0% y esperar un aumento de volumen y cruce del RSI de 1 hora por encima de 40 para asegurar ganancias en el rango objetivo de +2.0% a +3.5%. Conservar el efectivo actual como reserva."
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
