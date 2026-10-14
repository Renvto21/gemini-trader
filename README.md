# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 10:30:53`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$33.41 USD** | **$5.96 USD** | **$39.37 USD** | 🔴 **-1.57%** ($-0.63) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $82575.17 | $5.96 | 📉 -0.67% | 13h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general muestra un sesgo bajista de corto plazo en los principales índices y criptomonedas, con la mayoría de activos operando por debajo de sus medias móviles de 20 períodos. Sin embargo, en el ecosistema cripto disponible 24/7, los precios se mantienen relativamente estables con ligeras variaciones de 1 hora. BTC-USD mantiene un rendimiento cercano al punto de entrada con un PnL de -0.67% tras 13.5 horas de holding, manteniéndose seguro por encima del umbral de stop-loss estricto del -2.0%."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 65%): La posición en BTC-USD lleva 13 horas abierta con una pérdida leve de -0.67%, manteniéndose holgadamente dentro de nuestros límites de riesgo y lejos del stop-loss de -2.0%. Esperamos que el RSI de 1H recupere niveles superiores a 45 para buscar un rebote hacia la toma de ganancias.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos la posición abierta de BTC-USD mientras el precio respete el soporte y no alcance el stop-loss del -2.0%. Dado que el mercado de valores sigue cerrado y el impulso en criptomonedas permanece moderado sin señales claras de ruptura de RSI por encima de 45, mantendremos el efectivo restante inactivo a la espera de una confirmación más fuerte de volumen o un rebote técnico más agresivo antes de desplegar nuevo capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **50** | 🎯 **44.0%** (22W / 14L / 14BE) | 🔴 **$-0.50 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 10:10` | 🔴 SELL (-0.11$) | `SOL-USD` | $5.89 | $105.41 | La posición en SOL-USD acumula una pérdida cercana al -1.9%, rozando nuestro stop-loss est... |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |

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
