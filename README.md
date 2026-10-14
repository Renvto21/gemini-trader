# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 01:00:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.54 USD** | **$17.05 USD** | **$39.59 USD** | 🔴 **-1.02%** ($-0.41) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2509.86 | $5.00 | 📈 +0.06% | 7h 50m |
| `BTC-USD` | 0.000072 | $83128.62 | $83621.63 | $6.04 | 📈 +0.59% | 3h 59m |
| `SOL-USD` | 0.055840 | $107.45 | $107.67 | $6.01 | 📈 +0.20% | 1h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto mantiene una actividad moderada con los principales activos (BTC, ETH, SOL) operando en terreno positivo en las últimas 24 horas, aunque mostrando consolidación de corto plazo en la última hora. Las bolsas tradicionales permanecen cerradas, por lo que toda la atención táctica se centra en los mercados abiertos 24/7. Las posiciones actuales muestran ligeras ganancias pero se mantienen por debajo del objetivo de take-profit del +2.0%, por lo que el plan es mantenerlas y esperar mayor momentum."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): La posición se mantiene estable con una ganancia marginal del +0.06%. El RSI de 1 hora se encuentra en 46.8 y no hay señales de sobrecompra ni pérdida de soporte crítico, por lo que se mantiene a la espera del objetivo de take-profit.
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD registra una ganancia del +0.59% con un RSI de 1 hora en 55.0. El precio se consolida favorablemente tras el rebote reciente, por lo que se mantiene la posición buscando alcanzar la banda del +2.0% para asegurar beneficios.
- **[HOLD] SOL-USD** (Confianza: 78%): SOL-USD muestra un rendimiento positivo del +0.20% y un RSI de 1 hora en 53.5. Mantiene el impulso alcista diario y no ha activado ninguna señal de salida o stop-loss, por lo que continúa en cartera.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en ETH-USD, BTC-USD y SOL-USD. Vigilar de cerca el comportamiento del precio para asegurar ganancias en cuanto alcancen la zona de take-profit del +2.0% al +3.5% o si el RSI de 1 hora supera los 70 puntos. El stop-loss estricto se mantiene en -2.0% y se preserva una sólida reserva de efectivo por encima de los $4.00 USD."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **48** | 🎯 **45.8%** (22W / 12L / 14BE) | 🔴 **$-0.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |

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
