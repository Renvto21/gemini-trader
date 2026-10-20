# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 02:10:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.73 USD** | **$38.73 USD** | 🔴 **-3.18%** ($-1.27) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 15h 30m |
| `ETH-USD` | 0.004178 | $2393.62 | $2408.15 | $10.06 | 📈 +0.61% | 13h 19m |
| `SOL-USD` | 0.096034 | $104.13 | $105.05 | $10.09 | 📈 +0.88% | 9h 29m |
| `BTC-USD` | 0.000105 | $81767.70 | $81961.16 | $8.59 | 📈 +0.24% | 8h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado bursátil de Wall Street se encuentra cerrado y sus precios están congelados, por lo que toda la atención táctica se centra en los mercados de criptomonedas que operan 24/7. Las posiciones actuales en cripto (ETH-USD, SOL-USD y BTC-USD) muestran ligeras ganancias pero se acercan a zonas de resistencia técnica de corto plazo. Específicamente, SOL-USD muestra un RSI de 1 hora en 67.0 y ETH-USD en 63.5, aproximándose al objetivo de toma de beneficios. Mantendremos la disciplina esperando que alcancen la zona de sobrecompra superior a 70 para asegurar capital."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD muestra una ganancia del +0.88% y un RSI de 1 hora en 67.0. Aunque se acerca a la zona objetivo de take-profit (>70), el impulso actual sugiere esperar un ciclo más para asegurar la ganancia óptima sin anticipar la salida.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en cripto y QQQ (este último cerrado). Monitorear de cerca a SOL-USD y ETH-USD para ejecutar una toma parcial de beneficios tan pronto como su RSI de 1 hora supere 70 o acumulen un rendimiento del +2%. Si se concretan las ventas, liberar liquidez para buscar nuevas oportunidades de rebote en activos con mayor ímpetu."
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
