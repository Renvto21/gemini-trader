# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 06:20:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$12.00 USD** | **$39.52 USD** | 🔴 **-1.19%** ($-0.48) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83370.74 | $6.02 | 📈 +0.29% | 9h 19m |
| `SOL-USD` | 0.055840 | $107.45 | $107.08 | $5.98 | 📉 -0.34% | 7h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que la operativa actual se concentra en el segmento cripto (24/7). BTC-USD y SOL-USD se mantienen en rangos estables con ligeras variaciones positivas en el corto plazo, pero sin alcanzar los niveles de take-profit definidos (+2.0% a +3.5%) ni activar los stop-loss. El sentimiento general es de consolidación a la espera de mayor momentum."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 70%): BTC-USD se mantiene estable con un PnL positivo moderado (+0.29%) y un RSI de 1H en 54.2. No hay señales de sobrecompra ni motivos para cerrar la posición prematuramente; esperamos que alcance el objetivo de take-profit.
- **[HOLD] SOL-USD** (Confianza: 65%): SOL-USD registra un PnL ligeramente negativo (-0.34%) pero con un RSI diario en niveles de sobreventa extrema que respalda la tesis de rebote. Damos tiempo adicional para que el activo desarrolle su inercia alcista antes de considerar una rotación.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales de BTC-USD y SOL-USD vigilando de cerca los niveles de take-profit entre +2.0% y +3.5% o cruces de RSI de 1H superiores a 70. Si SOL-USD no muestra un repunte más decidido y prolonga su estancia sin momentum, evaluaremos rotar capital en los siguientes ciclos. Mantener la reserva mínima de efectivo intacta."
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
