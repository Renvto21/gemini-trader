# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 07:00:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$11.95 USD** | **$39.48 USD** | 🔴 **-1.31%** ($-0.52) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83158.16 | $6.00 | 📈 +0.04% | 9h 59m |
| `SOL-USD` | 0.055840 | $107.45 | $106.49 | $5.95 | 📉 -0.89% | 7h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene operando 24/7 con un comportamiento lateral y de bajo momentum en el corto plazo. BTC-USD y SOL-USD muestran variaciones mínimas en la última hora, con RSI de 1H en niveles neutrales (alrededor de 40-45), mientras que los mercados tradicionales están cerrados. No hay señales claras de un rebote explosivo inminente, pero las posiciones actuales se mantienen estables dentro de los márgenes de riesgo."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD se encuentra con un PnL plano (0.04%) tras casi 10 horas de holding. El RSI de 1H está en 45.1 sin mostrar signos de sobrecompra para tomar ganancias ni de debilidad extrema para activar un stop-loss, por lo que se mantiene la posición.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD registra una pequeña pérdida latente de -0.89% tras casi 8 horas, pero su RSI diario se mantiene en niveles de sobreventa extrema (27.2), lo que sugiere que el soporte macro sigue intacto y vale la pena darle espacio para un posible rebote técnico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener BTC-USD y SOL-USD por el momento mientras no rompan soportes críticos. Monitorearemos la evolución de su RSI de 1H y la acción de precio. Si BTC-USD se acerca al take-profit (+2.0%) o SOL-USD muestra un incremento de volumen con recuperación del RSI hacia zona neutral-alta, realizaremos ganancias o evaluaremos mantener. El efectivo disponible se mantendrá reservado para capitalizar oportunidades con mayor dinamismo en futuros ciclos."
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
