# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 10:10:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$33.41 USD** | **$5.97 USD** | **$39.38 USD** | 🔴 **-1.56%** ($-0.62) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $82648.73 | $5.97 | 📉 -0.58% | 13h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se encuentra operando en fin de semana con un sesgo lateral a ligeramente bajista. BTC y SOL muestran debilidad temporal bajo sus medias móviles, acercándose de manera peligrosa a los límites de stop-loss estipulados. Los mercados tradicionales (Wall Street) se encuentran cerrados, por lo que toda la acción y enfoque táctico se mantiene exclusivamente en los pares de criptomonedas abiertos 24/7."

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 90%): La posición en SOL-USD acumula una pérdida cercana al -1.9%, rozando nuestro stop-loss estricto del -2.0%. Tras casi 11 horas de holding sin la recuperación esperada, ejecutamos la venta para cortar pérdidas, proteger el capital restante y mantener liquidez para futuras oportunidades.
- **[HOLD] BTC-USD** (Confianza: 60%): BTC-USD mantiene una pérdida moderada de -0.58% con un holding time de más de 13 horas. Aunque el momentum es débil, el RSI de 1H se sitúa en 41 y aún no rompe el stop-loss estricto. Esperaremos confirmación de volumen o un rebote técnico antes de tomar una decisión de salida.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos por el momento BTC-USD vigilando de cerca su soporte, pero se ha decidido liquidar SOL-USD tras rozar el límite de stop-loss del -2.0% y mostrar un holding time de casi 11 horas sin un rebote consistente. Rotaremos el capital hacia liquidez o buscaremos un punto de entrada más sólido cuando el RSI de 1H muestre una recuperación superior a 45 con volumen comprador."
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
