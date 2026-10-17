# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 02:20:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.15 USD** | **$38.44 USD** | 🔴 **-3.90%** ($-1.56) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.77 | $10.10 | 📈 +1.02% | 11h 19m |
| `ETH-USD` | 0.004144 | $2412.98 | $2424.67 | $10.05 | 📈 +0.48% | 9h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario se encuentra cerrado, por lo que toda la actividad se concentra en el mercado cripto 24/7. SOL-USD muestra un rendimiento positivo con un PnL de +1.02% y un RSI de 1 hora en 64.8, acercándose a la zona objetivo de take-profit. ETH-USD registra un avance moderado con +0.48% de PnL y un RSI diario en niveles de soporte, manteniendo su tendencia de recuperación. El efectivo disponible se mantiene en $18.29 USD."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD acumula una ganancia de +1.02% tras casi 11.5 horas abierta. Su RSI de 1 hora se sitúa en 64.8, acercándose a la zona de sobrecompra. Se mantiene la posición a la espera de alcanzar el objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD presenta una ganancia modesta de +0.48% con un RSI diario de 30.8 en zona de soporte. El precio mantiene el impulso inicial de rebote y continúa abierto para consolidar su recuperación.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca SOL-USD para ejecutar un Take-Profit total o parcial si alcanza el rango de +2.0% a +3.5% o si su RSI de 1 hora supera 70. Mantener ETH-USD para permitir que su rebote diario madure, estableciendo un stop-loss estricto en -2.0% para ambas posiciones. Mantener la reserva de efectivo requerida y buscar nuevas entradas si se genera sobreventa extrema en otros activos abiertos."
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
