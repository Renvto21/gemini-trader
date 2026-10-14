# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 05:20:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$12.06 USD** | **$39.59 USD** | 🔴 **-1.02%** ($-0.41) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83731.30 | $6.04 | 📈 +0.72% | 8h 19m |
| `SOL-USD` | 0.055840 | $107.45 | $107.82 | $6.02 | 📈 +0.34% | 6h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado y con precios congelados, por lo que toda la actividad se concentra en las criptomonedas (BTC-USD y SOL-USD), las cuales operan 24/7. Tanto BTC como SOL muestran un ligero sesgo alcista de corto plazo (cambio de 1h positivo) y se mantienen dentro de nuestras posiciones abiertas con pequeños beneficios, aunque sin alcanzar todavía la zona de take-profit óptima superior al 2.0%. ETH-USD muestra un momentum moderado, pero mantenemos la liquidez en efectivo vigilando cualquier oportunidad de rotación."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 70%): BTC-USD se mantiene estable con un PnL positivo del 0.72% y un RSI de 1H en 65.3 acercándose a la zona de atención, pero aún sin detonar la señal de venta por take-profit. Mantenemos la posición buscando extender el beneficio.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de BTC-USD y SOL-USD evaluando su cercanía a niveles de sobrecompra en 1H para asegurar beneficios si rozan el objetivo de +2.0% o más. Mantendremos la liquidez en reserva ante posibles cambios bruscos de momentum en el mercado cripto o aperturas futuras en activos tradicionales."
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
