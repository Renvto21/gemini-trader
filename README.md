# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 08:50:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$11.99 USD** | **$39.52 USD** | 🔴 **-1.20%** ($-0.48) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83357.03 | $6.02 | 📈 +0.27% | 11h 49m |
| `SOL-USD` | 0.055840 | $107.45 | $107.04 | $5.98 | 📉 -0.38% | 9h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la actividad se concentra en los activos cripto 24/7 (BTC-USD y SOL-USD). Ambos activos muestran un comportamiento lateral a ligeramente negativo en el corto plazo, con un RSI de 1H normalizado alrededor de 47-50, sin mostrar el impulso alcista necesario para asegurar ganancias rápidas, pero tampoco han activado los stop-loss de -2.0%. Mantendremos la paciencia y las posiciones actuales hasta observar una ruptura clara del RSI de 1H."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 70%): La posición en BTC-USD muestra un PnL plano de +0.27% tras casi 12 horas. El RSI de 1H se encuentra en 47.6 sin señales de sobrecompra ni de ruptura del stop-loss, por lo que se mantiene en cartera esperando mayor momentum.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD registra un PnL de -0.38% con un holding time de casi 10 horas. Aunque el RSI diario sigue en zona de sobreventa (28.3), el RSI de 1H está en 50.4. No amerita venta anticipada ya que está lejos del stop-loss de -2.0% y mantenemos la expectativa de rebote.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones de BTC-USD y SOL-USD activas. Monitorearemos de cerca si el holding time supera las 15-20 horas sin movimiento relevante, lo cual nos obligará a rotar el capital. Esperaremos un RSI de 1H superando los 60 puntos o cayendo hacia soportes extremos para ajustar posiciones o tomar beneficios."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **49** | 🎯 **44.9%** (22W / 13L / 14BE) | 🔴 **$-0.39 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |

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
