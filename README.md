# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 03:10:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.15 USD** | **$38.44 USD** | 🔴 **-3.90%** ($-1.56) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.72 | $10.10 | 📈 +0.97% | 12h 9m |
| `ETH-USD` | 0.004144 | $2412.98 | $2426.44 | $10.06 | 📈 +0.56% | 10h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con un tono lateral a ligeramente bajista, mientras que los mercados tradicionales permanecen cerrados. Las posiciones actuales en SOL-USD y ETH-USD muestran ganancias moderadas (+0.97% y +0.56% respectivamente) pero aún no alcanzan la zona objetivo de take-profit de +2.0% a +3.5% ni presentan señales de sobrecompra urgente en el RSI de 1 hora."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición mantiene una ganancia del 0.97% tras más de 12 horas. El RSI de 1 hora está en 61.2, acercándose a la zona de atención, pero aún no llega a la sobrecompra de +2.0% a +3.5% o RSI > 70 para ejecutar el take-profit. Mantenemos la posición para dejar correr el rebote.
- **[HOLD] ETH-USD** (Confianza: 70%): La posición acumula una ganancia de 0.56% con un RSI de 1 hora en 48.5. No hay señales de debilidad ni de sobrecompra que justifiquen una venta anticipada, por lo que se mantiene buscando el objetivo de beneficio establecido.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas de SOL-USD y ETH-USD supervisando su avance hacia el objetivo de ganancia de +2.0% a +3.5% o hasta que el RSI de 1 hora supere los 70. Conservar la liquidez actual como reserva y preparar el capital para rotar o buscar oportunidades en activos tradicionales o cripto en cuanto se intensifique el momentum o reabran los mercados."
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
