# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 20:30:51`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$34.54 USD** | **$4.98 USD** | **$39.52 USD** | 🔴 **-1.21%** ($-0.48) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2496.13 | $4.98 | 📉 -0.49% | 3h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado y sus precios están congelados, por lo que toda la atención táctica se centra en los activos de criptomonedas (24/7). ETH-USD muestra un comportamiento lateral con un leve descenso en la última hora (-0.51%), manteniendo una pérdida flotante mínima (-0.49%) tras más de 3 horas de retención. BTC-USD y SOL-USD operan bajo su SMA20 pero muestran resiliencia en su cambio de 24 horas. La liquidez debe mantenerse parcialmente o asignarse selectivamente si se detecta un momentum claro."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): La posición actual en ETH-USD registra una pérdida leve de -0.49% con un tiempo de tenencia de poco más de 3 horas. No ha alcanzado el stop-loss estricto de -2.0% ni el objetivo de take-profit, y el RSI de 1H se mantiene en un nivel neutral (40.6). Se prefiere mantener la posición a la espera de un impulso alcista que active la toma de beneficios.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos la posición actual en ETH-USD vigilando que no rompa el soporte crítico. El stop-loss se mantiene estricto en -2.0% y buscaremos la toma de beneficios si alcanza el rango de +2.0% a +3.5% o si el RSI de 1H supera los 70 puntos. Si la posición continúa estancada sin volumen o rebote en las próximas horas, rotaremos el capital hacia liquidez o hacia otra oportunidad en cripto."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **48** | 🎯 **45.8%** (22W / 12L / 14BE) | 🔴 **$-0.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |
| `2026-10-13 16:30` | 🟢 BUY | `ETH-USD` | $9.68 | $2507.92 | ETH-USD muestra un RSI de 35.8 en zona de fuerte sobreventa y un impulso alcista diario de... |
| `2026-10-13 16:30` | 🔴 SELL | `SOL-USD` | $9.69 | $107.65 | Realizamos una toma parcial de beneficios y rotación de capital liberando aproximadamente ... |

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
