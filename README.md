# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 03:30:59`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.86 USD** | **$38.48 USD** | 🔴 **-3.81%** ($-1.52) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 16h 40m |
| `BTC-USD` | 0.000061 | $81640.68 | $80881.58 | $4.95 | 📉 -0.93% | 6h 20m |
| `ETH-USD` | 0.002539 | $2362.71 | $2362.31 | $6.00 | 📉 -0.02% | 2h 20m |
| `SOL-USD` | 0.058789 | $102.06 | $102.13 | $6.00 | 📈 +0.07% | 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario tradicional (SPY, QQQ, AAPL, NVDA, MSFT) se encuentra cerrado, por lo que toda la actividad se concentra en el mercado de criptomonedas (24/7). Las criptomonedas muestran signos iniciales de recuperación en el corto plazo con cambios positivos de 1h (BTC-USD +0.49%, ETH-USD +0.67%, SOL-USD +0.78%), a pesar de venir de fuertes caídas en 24h. Mantenemos nuestras posiciones abiertas en cripto buscando consolidar el rebote técnico y AAPL en renta variable debido a su tendencia alcista de fondo."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 80%): El activo se encuentra en mercado cerrado. Mantiene una tendencia alcista diaria sobre la SMA20 y una pérdida flotante mínima de -0.92%, por lo que se mantiene a la espera de la apertura de Wall Street.
- **[HOLD] BTC-USD** (Confianza: 75%): Muestra un cambio positivo de 1h de +0.49% y un RSI de 1h subiendo a 36.1, indicando que el rebote técnico desde la zona de sobreventa sigue intacto.
- **[HOLD] ETH-USD** (Confianza: 80%): Recién comprado en la zona de sobreventa extrema. El RSI de 1h en 26.0 y el cambio positivo de 1h en +0.67% respaldan la tesis de reversión a la media en curso.
- **[HOLD] SOL-USD** (Confianza: 80%): Posición recién abierta con un cambio favorable de 1h de +0.78%. Se le otorga tiempo de ejecución para capturar el impulso alcista del rebote técnico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones actuales en AAPL, BTC-USD, ETH-USD y SOL-USD. El efectivo disponible actual es de $11.61 USD (por encima del mínimo de reserva de $4.00), pero dado que las posiciones están recién abiertas y con ligeras fluctuaciones, esperaremos confirmación de volumen alcista o la toma de ganancias si alcanzan el objetivo de +2.0% a +3.5%. Vigilar estrictamente el stop-loss en -2.0% para cortar pérdidas rápidamente si el mercado cripto revierte a la baja."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **54** | 🎯 **40.7%** (22W / 18L / 14BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 03:20` | 🟢 BUY | `SOL-USD` | $6.00 | $102.06 | SOL-USD muestra un RSI de 1h en 33.3 saliendo de zonas de compresión bajista, acompañado d... |
| `2026-10-15 01:10` | 🟢 BUY | `ETH-USD` | $6.00 | $2362.71 | ETH-USD presenta un RSI de 1h extremadamente bajo en 23.5 saliendo de sobreventa y un camb... |
| `2026-10-14 23:30` | 🔴 SELL (-0.30$) | `SOL-USD` | $9.70 | $101.32 | La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin ... |
| `2026-10-14 23:30` | 🔴 SELL (-0.32$) | `ETH-USD` | $9.68 | $2340.86 | 🚨 STOP-LOSS AUTOMÁTICO (CIRCUIT BREAKER): Pérdida de -3.20% superó el límite de seguridad ... |
| `2026-10-14 21:10` | 🟢 BUY | `BTC-USD` | $5.00 | $81640.68 | BTC-USD presenta un RSI de 1h en 24.9 (sobreventa extrema) y liquidez disponible suficient... |

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
