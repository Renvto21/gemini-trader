# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 09:40:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$11.88 USD** | **$39.41 USD** | 🔴 **-1.49%** ($-0.59) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $82665.74 | $5.97 | 📉 -0.56% | 12h 39m |
| `SOL-USD` | 0.055840 | $107.45 | $105.88 | $5.91 | 📉 -1.46% | 10h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado y con precios congelados. En el segmento de criptomonedas, que opera 24/7, observamos una ligera presión bajista a corto plazo con BTC-USD y SOL-USD experimentando descensos en la última hora y cotizando por debajo de su SMA20. A pesar de esto, mantenemos la vigilancia sobre los soportes diarios y el comportamiento del RSI para evaluar si las posiciones actuales logran estabilizarse o si requerirán una salida anticipada para proteger el capital."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 65%): BTC-USD se mantiene abierto y dentro de la zona de vigilancia. Aunque muestra un pequeño retroceso en la última hora, el precio no ha roto los niveles críticos de soporte ni alcanzado el stop-loss estricto de -2.0%. Mantendremos la posición esperando el rebote técnico desde los niveles actuales.
- **[HOLD] SOL-USD** (Confianza: 60%): SOL-USD presenta un RSI diario en sobreventa extrema (26.5), lo que respalda la tesis de mean reversion. A pesar del leve descenso reciente de 1H, el holding time aún permite evaluar la consolidación del soporte antes de tomar una decisión de corte de pérdidas.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de BTC-USD y SOL-USD por unas horas adicionales, monitoreando de cerca el límite de pérdida del -2.0% y esperando señales claras de rebote con un RSI de 1H superando los 50 puntos. Si las pérdidas se aproximan al umbral crítico o si el holding time supera las 20 horas sin momentum positivo, procederemos a liquidar para proteger el efectivo y buscar nuevas oportunidades de rotación."
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
