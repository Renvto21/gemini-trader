# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 10:20:57`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.55 USD** | **$38.55 USD** | 🔴 **-3.63%** ($-1.45) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 23h 40m |
| `ETH-USD` | 0.004178 | $2393.62 | $2393.55 | $10.00 | 📈 -0.00% | 21h 29m |
| `SOL-USD` | 0.096034 | $104.13 | $104.42 | $10.03 | 📈 +0.28% | 17h 40m |
| `BTC-USD` | 0.000105 | $81767.70 | $81407.33 | $8.53 | 📉 -0.44% | 17h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento general bajista con la mayoría de los activos tradicionales (QQQ, SPY, NVDA) cerrados y con precios congelados bajo su media móvil de 20 periodos. Los activos cripto (ETH-USD, SOL-USD, BTC-USD) se encuentran abiertos pero muestran un momentum estancado y lateral, con RSI de 1 hora oscilando entre 38 y 42 sin lograr romper al alza de forma decisiva. No hay suficiente presión de compra en el corto plazo para activar los take-profits objetivo, pero las posiciones se mantienen estables sin alcanzar el stop-loss estricto de -2.0%."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 60%): SOL-USD se mantiene con una pequeña ganancia del 0.28% tras 17 horas abierto. Aunque el momentum es lento, se encuentra por encima del precio de entrada y no justifica una venta anticipada ni la rotación de capital en este preciso instante. Esperaremos un aumento de volumen.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Las posiciones abiertas (QQQ, ETH-USD, SOL-USD, BTC-USD) llevan más de medio día sin consolidar el rebote esperado. Mantendremos las posiciones vigentes por un ciclo más esperando un catalizador de volumen en cripto que impulse el RSI de 1 hora por encima de 50 para asegurar tomas de ganancias entre +2.0% y +3.5%. Si el mercado cripto continúa lateralizado y las posiciones se acercan al límite de -2.0% de pérdida, procederemos a vender para cortar pérdidas y rotar capital hacia nuevas oportunidades de momentum."
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
