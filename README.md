# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 04:30:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$12.02 USD** | **$39.54 USD** | 🔴 **-1.14%** ($-0.46) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83386.98 | $6.02 | 📈 +0.31% | 7h 30m |
| `SOL-USD` | 0.055840 | $107.45 | $107.40 | $6.00 | 📉 -0.05% | 5h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la actividad se concentra en los criptoactivos (BTC-USD y SOL-USD) que operan 24/7. Tanto Bitcoin como Solana muestran estabilidad con ligeros sesgos alcistas tras los rebotes recientes, manteniendo un RSI de 1 hora moderado y consolidando posiciones dentro de rangos aceptables sin alcanzar aún los objetivos estrictos de take-profit ni los stop-loss."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición en BTC-USD muestra un PnL positivo de 0.31% y un RSI de 1H saludable en 60.0. Continuamos esperando el objetivo de take-profit entre +2.0% y +3.5% sin activar ninguna señal de salida anticipada.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se mantiene estable con un PnL plano de -0.05% y un RSI de 1H en 54.5. Mantenemos la posición para permitir que el rebote desde el soporte diario continúe desarrollándose.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de BTC-USD y SOL-USD vigilando de cerca que el RSI de 1H no sobrepase el umbral de 70 para asegurar beneficios parciales de acuerdo con nuestra estrategia de take-profit. La liquidez en efectivo se mantiene preservada esperando un catalizador mayor o una oportunidad en activos abiertos si se intensifica el momentum."
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
