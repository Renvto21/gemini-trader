# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 10:10:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.52 USD** | **$38.52 USD** | 🔴 **-3.69%** ($-1.48) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 23h 29m |
| `ETH-USD` | 0.004178 | $2393.62 | $2391.38 | $9.99 | 📉 -0.09% | 21h 19m |
| `SOL-USD` | 0.096034 | $104.13 | $104.31 | $10.02 | 📈 +0.17% | 17h 29m |
| `BTC-USD` | 0.000105 | $81767.70 | $81361.97 | $8.52 | 📉 -0.50% | 16h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se encuentra operando en formato 24/7 con un sesgo lateral a bajista de corto plazo, con ligeros retrocesos en la última hora y las últimas 24 horas. Los activos tradicionales (como QQQ) permanecen con mercado cerrado y precios congelados. Nuestras posiciones en cripto llevan más de 16 horas abiertas sin mostrar el impulso alcista o despegue del RSI por encima de 50 que esperábamos, manteniéndose con variaciones mínimas y ligeramente negativas en el agregado."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 60%): La posición muestra una ganancia marginal de 0.17% con un RSI de 1 hora en 40.1. Mantenemos la posición a la espera de un impulso de volumen que active la toma de beneficios.
- **[HOLD] ETH-USD** (Confianza: 60%): La posición se encuentra estable con una ligera pérdida de -0.09% y un RSI de 1 hora en 41.2. Esperamos la confirmación del rebote técnico.
- **[HOLD] BTC-USD** (Confianza: 60%): Registra una pérdida leve de -0.5% con un RSI de 1 hora en 37.0. Se mantiene en vigilancia estricta para evitar superar el umbral de stop-loss.
- **[HOLD] QQQ** (Confianza: 50%): El mercado de valores se encuentra cerrado. La posición está prácticamente plana (-0.08%) a la espera de la apertura para evaluar su continuidad.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Las posiciones actuales (QQQ, ETH-USD, SOL-USD, BTC-USD) llevan más de medio día abiertas sin consolidar el rebote esperado. Dado que el efectivo actual es 0.0 USD, mantendremos las posiciones actuales por un ciclo más esperando un catalizador de volumen en cripto que impulse el RSI de 1 hora por encima de 50 para asegurar tomas de ganancias entre +2.0% y +3.5%. Si las posiciones continúan estancadas y se acercan al límite de -2.0% de pérdida, procederemos a vender para cortar pérdidas y rotar capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 23:00` | 🟢 BUY | `BTC-USD` | $4.00 | $81646.39 | BTC-USD presenta un RSI de 1 hora en 27.7, nivel de sobreventa profunda ideal para un rebo... |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |

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
