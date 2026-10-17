# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 01:00:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.15 USD** | **$38.44 USD** | 🔴 **-3.90%** ($-1.56) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.81 | $10.11 | 📈 +1.06% | 9h 59m |
| `ETH-USD` | 0.004144 | $2412.98 | $2424.00 | $10.05 | 📈 +0.46% | 8h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado bursátil tradicional se encuentra cerrado y operando con precios congelados, por lo que el enfoque está totalmente volcado en las criptomonedas, que operan 24/7. Las posiciones actuales en SOL-USD y ETH-USD muestran ligeras ganancias (+1.06% y +0.46% respectivamente), manteniéndose por debajo de la zona objetivo de take-profit del +2.0% al +3.5%. Los indicadores de 1 hora se mantienen moderados sin sobrecompra inmediata, por lo que mantendremos el plan a la espera de que alcancen los objetivos de ganancia."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD registra una ganancia del 1.06% con un holding time de casi 10 horas. Aunque el impulso de corto plazo se ha moderado, se mantiene en territorio positivo y lejos de la zona de stop-loss, por lo que es prudente mantener la posición hasta alcanzar el objetivo de take-profit del +2.0% o más.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un avance del 0.46% tras poco más de 8 horas abierto. Se mantiene operando dentro del rango esperado tras su reciente entrada por sobreventa diaria, por lo que se continuará el ciclo a la espera de una extensión del movimiento alcista hacia el take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas de SOL-USD y ETH-USD. Monitorear de cerca el RSI de 1 hora para buscar niveles de sobrecompra superior a 70 que permitan asegurar ganancias parciales o totales entre el +2.0% y +3.5%. Vigilar el soporte para evitar activar el stop-loss en -2.0%. Preservar el efectivo restante hasta que las criptomonedas alcancen sus objetivos de salida o surja una nueva oportunidad clara de rebote."
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
