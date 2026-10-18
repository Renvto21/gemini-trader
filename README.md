# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 19:50:36`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.15 USD** | **$16.15 USD** | **$38.30 USD** | 🔴 **-4.24%** ($-1.70) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.003388 | $2361.22 | $2392.74 | $8.11 | 📈 +1.33% | 1h 9m |
| `SOL-USD` | 0.077662 | $103.01 | $103.63 | $8.05 | 📈 +0.60% | 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas continúa operando con un sesgo alcista de corto plazo en los activos abiertos, destacando la recuperación de ETH-USD y SOL-USD. Los mercados tradicionales se encuentran cerrados, por lo que toda la atención táctica se concentra en las criptomonedas para capitalizar rebotes por sobreventa diaria. ETH-USD muestra un rendimiento positivo de +1.33% y SOL-USD de +0.60%, ambos acercándose gradualmente a la zona objetivo de take-profit entre +2.0% y +3.5%."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un rendimiento actual de +1.33% con un RSI de 1h en 45.5 y un cambio positivo de 1h de 1.05%. El rebote técnico sigue en marcha y nos estamos acercando a nuestra meta de take-profit entre +2.0% y +3.5%.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD registra un PnL de +0.60% con un RSI de 1h en 53.7 y fuerte impulso de corto plazo (change_1h_pct +1.61%). Mantenemos la posición para capturar el objetivo de take-profit sin alterar la estructura.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en ETH-USD y SOL-USD mientras continúen su ascenso técnico. Vigilar el RSI de 1 hora y el porcentaje de ganancia para ejecutar la venta (take-profit) tan pronto como alcancen el rango de +2.0% a +3.5% o si el RSI supera 70. Mantener la reserva de efectivo requerida y no abrir nuevas posiciones hasta asegurar capital."
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
