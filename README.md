# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 23:30:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.54 USD** | **$17.00 USD** | **$39.54 USD** | 🔴 **-1.15%** ($-0.46) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2504.69 | $4.99 | 📉 -0.15% | 6h 20m |
| `BTC-USD` | 0.000072 | $83128.62 | $83287.93 | $6.01 | 📈 +0.19% | 2h 29m |
| `SOL-USD` | 0.055840 | $107.45 | $107.39 | $6.00 | 📉 -0.06% | 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto 24/7 con un comportamiento lateral a ligeramente alcista en el corto plazo, mientras que los mercados tradicionales permanecen cerrados. Las posiciones actuales en ETH-USD, BTC-USD y SOL-USD se mantienen estables con ligeras variaciones, operando dentro de los rangos de control sin alcanzar los niveles de take-profit ni activar los stop-loss."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD se encuentra estable con una pequeña ganancia del 0.19% y un holding time de poco más de 2 horas. El momentum intradiario es neutral, por lo que se mantiene la posición esperando alcanzar la zona de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en ETH-USD, BTC-USD y SOL-USD vigentes. Monitorear de cerca los indicadores intradiarios de 1 hora para asegurar beneficios rápidos si alcanzan la zona de take-profit entre +2.0% y +3.5%. Conservar la liquidez remanente para evaluar nuevas oportunidades ante un rompimiento de tendencia o sobreventa extrema."
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
