# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 11:40:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.12 USD** | **$24.60 USD** | **$38.72 USD** | 🔴 **-3.20%** ($-1.28) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $535.73 | $6.51 | 📈 +0.10% | 1d 0h |
| `NVDA` | 0.036812 | $217.32 | $218.36 | $8.04 | 📈 +0.48% | 22h 50m |
| `ETH-USD` | 0.002855 | $2451.90 | $2471.80 | $7.06 | 📈 +0.81% | 7h 9m |
| `SOL-USD` | 0.028214 | $106.33 | $106.18 | $3.00 | 📉 -0.14% | 6h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento mixto con sesgo a la recuperación en criptomonedas y selectividad en acciones. ETH-USD se acerca rápidamente a la zona de sobrecompra en 1h (RSI 66.4) con un incremento constante en su precio, aproximándose al objetivo de take-profit. NVDA y MSFT se mantienen estables pero sin el momentum explosivo deseado, mientras que la liquidez se encuentra en $14.12 USD, superando ligeramente el umbral de reserva mínima de $4.00 USD."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un excelente rendimiento con un RSI de 1h en 66.4 y tendencia alcista de corto plazo. Esperaremos a que cruce el umbral de sobrecompra (>70) para ejecutar un take-profit parcial o total y asegurar la ganancia.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos ETH-USD y monitorizaremos su RSI de 1h buscando el nivel de 70 para asegurar ganancias de forma óptima. Las posiciones en MSFT, NVDA y SOL-USD se mantendrán temporalmente mientras sigan protegiendo el capital, pero rotaremos hacia activos con mayor inercia si el impulso lateral persiste. Operaremos con cautela manteniendo la liquidez por encima del mínimo requerido."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **59** | 🎯 **40.7%** (24W / 21L / 14BE) | 🔴 **$-1.26 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 10:50` | 🔴 SELL (-0.04$) | `QQQ` | $9.95 | $721.83 | QQQ lleva más de 22 horas abierto operando bajo la SMA20 con un RSI de 1 hora en 30.2 y un... |
| `2026-10-16 05:10` | 🟢 BUY | `SOL-USD` | $3.00 | $106.33 | SOL-USD presenta un RSI diario en zona de sobreventa extrema (29.0) y un cambio positivo e... |
| `2026-10-16 04:30` | 🟢 BUY | `ETH-USD` | $7.00 | $2451.90 | Aprovechamos la liquidez disponible sobre la reserva mínima ($14.17 vs $4.00 requeridos) p... |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |

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
