# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 20:10:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.15 USD** | **$16.14 USD** | **$38.29 USD** | 🔴 **-4.28%** ($-1.71) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.003388 | $2361.22 | $2388.95 | $8.09 | 📈 +1.17% | 1h 29m |
| `SOL-USD` | 0.077662 | $103.01 | $103.60 | $8.05 | 📈 +0.57% | 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 mientras los mercados tradicionales están cerrados. ETH-USD y SOL-USD se encuentran en posiciones abiertas con ganancias modestas pero aún lejos de nuestro objetivo de take-profit de +2.0% a +3.5%. Los indicadores de RSI de 1 hora se mantienen neutrales (39.8 y 48.1 respectivamente) y el RSI diario continúa profundamente deprimido, sugiriendo que debemos mantener la paciencia y dejar correr las posiciones actuales mientras esperamos la confirmación de momentum alcista para asegurar ganancias."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): La posición en ETH-USD muestra una ganancia actual de +1.17%, acercándose gradualmente a nuestra meta de take-profit. El RSI de 1 hora está en 39.8 y el holding time es corto, por lo que mantenemos la posición esperando el impulso alcista necesario para cerrar con beneficio.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD registra un PnL positivo de +0.57% con un RSI de 1h en 48.1. Mantiene el potencial de rebote por su sobreventa diaria extrema, por lo que decidimos sostener la posición a la espera de la zona objetivo de toma de ganancias.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en ETH-USD y SOL-USD. Monitorear de cerca el rendimiento de ambas para asegurar ganancias en cuanto alcancen el rango de +2.0% a +3.5% o si el RSI de 1 hora supera 70. Mantener la reserva de efectivo requerida y no abrir nuevas operaciones hasta que se concrete la toma de ganancias y se libere capital."
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
