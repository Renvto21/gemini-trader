# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 22:41:36`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$28.54 USD** | **$10.99 USD** | **$39.53 USD** | 🔴 **-1.18%** ($-0.47) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2500.23 | $4.98 | 📉 -0.32% | 5h 30m |
| `BTC-USD` | 0.000072 | $83128.62 | $83170.57 | $6.00 | 📈 +0.05% | 1h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la actividad se concentra exclusivamente en las criptomonedas (BTC-USD y ETH-USD). Ambas posiciones actuales se mantienen estables con ligeras variaciones, operando con un sesgo bajista macro pero intentando consolidar tras los recientes rebotes de corto plazo."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD muestra estabilidad con una pérdida menor del -0.32% tras 5 horas y media de holding. El RSI de 1 hora se encuentra neutral en 51.9. Mantendremos la posición buscando que alcance el objetivo de take-profit del +2.0%.
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD opera prácticamente tablas con un rendimiento de +0.05% y un RSI de 1 hora en 48.0. Continuaremos observando su evolución dentro del rango actual para proteger la posición o asegurar beneficios si se activa el rebote esperado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales en ETH-USD y BTC-USD mientras vigilamos de cerca sus niveles de RSI de 1 hora. Establecemos un objetivo de take-profit en +2.5% para asegurar ganancias rápidas y un stop-loss estricto en -2.0% para evitar pérdidas mayores. Si el momentum en cripto se desacelera por completo y no muestra avances, rotaremos el capital hacia oportunidades con mayor volatilidad en el siguiente ciclo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **48** | 🎯 **45.8%** (22W / 12L / 14BE) | 🔴 **$-0.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |
| `2026-10-13 16:30` | 🟢 BUY | `ETH-USD` | $9.68 | $2507.92 | ETH-USD muestra un RSI de 35.8 en zona de fuerte sobreventa y un impulso alcista diario de... |

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
