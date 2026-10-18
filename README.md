# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 19:40:34`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.15 USD** | **$16.11 USD** | **$38.26 USD** | 🔴 **-4.36%** ($-1.74) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.003388 | $2361.22 | $2387.00 | $8.09 | 📈 +1.09% | 59m |
| `SOL-USD` | 0.077662 | $103.01 | $103.25 | $8.02 | 📈 +0.23% | 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene abierto y con un tono ligeramente positivo en el muy corto plazo, destacando leves rebotes en ETH-USD y SOL-USD tras tocar niveles de sobreventa diaria extremos. Los activos tradicionales se encuentran cerrados, por lo que el enfoque táctico se concentra plenamente en maximizar las oportunidades en criptomonedas."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un rendimiento positivo de +1.09%, acercándose progresivamente a nuestra zona objetivo de take-profit (+2.0% a +3.5%). Mantenemos la posición para dejar que el impulso continúe.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD se mantiene estable con una ganancia de +0.23% tras su reciente apertura, con un RSI de 1 hora recuperándose a 51.2. Mantenemos la posición a la espera de mayores ganancias que permitan cumplir el take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en ETH-USD y SOL-USD mientras continúen su recuperación técnica. Vigilar de cerca el objetivo de take-profit entre +2.0% y +3.5% o la entrada en sobrecompra del RSI de 1 hora (>70) para asegurar ganancias rápidas. Proteger estrictamente con stop-loss a -2.0% y mantener una reserva mínima de efectivo de $4.00 USD."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **73** | 🎯 **41.1%** (30W / 29L / 14BE) | 🔴 **$-1.71 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 19:30` | 🟢 BUY | `SOL-USD` | $8.00 | $103.01 | SOL-USD presenta un RSI diario extremadamente bajo (16.5) y un RSI de 1h recuperándose has... |
| `2026-10-18 19:10` | 🔴 SELL (+0.17$) | `SOL-USD` | $8.17 | $102.92 | SOL-USD ha alcanzado un rendimiento de +2.07% cumpliendo con nuestra regla de toma rápida ... |
| `2026-10-18 18:40` | 🟢 BUY | `ETH-USD` | $8.00 | $2361.22 | ETH-USD muestra un RSI diario deprimido en 21.5 y un RSI de 1 hora que se recupera a 34.3 ... |
| `2026-10-18 17:00` | 🟢 BUY | `SOL-USD` | $8.00 | $100.83 | SOL-USD muestra un RSI diario extremadamente deprimido en 15.3 y un RSI de 1 hora en 23.4 ... |
| `2026-10-18 16:40` | 🔴 SELL (-0.19$) | `ETH-USD` | $9.81 | $2332.39 | ETH-USD registra una pérdida del -1.92% con un RSI de 1 hora en 18.5 que refleja debilidad... |

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
