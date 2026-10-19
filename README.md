# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 17:20:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$34.63 USD** | **$38.63 USD** | 🔴 **-3.43%** ($-1.37) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 6h 39m |
| `ETH-USD` | 0.004178 | $2393.62 | $2399.72 | $10.03 | 📈 +0.25% | 4h 29m |
| `SOL-USD` | 0.096034 | $104.13 | $104.53 | $10.04 | 📈 +0.38% | 39m |
| `BTC-USD` | 0.000056 | $81874.05 | $81961.16 | $4.57 | 📈 +0.11% | 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la actividad se concentra en el mercado de criptomonedas (abierto 24/7). Los activos de cripto muestran ligeros intentos de recuperación y rebote técnico de corto plazo tras caídas previas, con RSI de 1 hora saliendo de niveles de sobreventa y variaciones horarias positivas. Mantenemos una postura de vigilancia estricta sobre las posiciones abiertas en ETH, SOL y BTC, esperando que alcancen los objetivos de take-profit antes de rotar capital."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un cambio de 1 hora positivo (0.33%) y un RSI de 1 hora recuperándose a 37.2, consolidando el rebote técnico buscado. Mantenemos la posición para capturar el objetivo de take-profit.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD presenta un excelente momentum de corto plazo con un cambio de 1 hora de 0.65% y RSI diario en sobreventa profunda (20.8), lo que valida mantener la posición activa en busca de mayores ganancias.
- **[HOLD] BTC-USD** (Confianza: 70%): BTC-USD muestra estabilidad con un ligero incremento horario (0.27%) y RSI de 1 hora saliendo de zona de compresión (33.8). Mantenemos bajo estrecha vigilancia con stop-loss del -2.0%.
- **[HOLD] QQQ** (Confianza: 60%): QQQ se encuentra en mercado cerrado, por lo que no es posible operar. Mantenemos la posición actual a la espera de la apertura del mercado tradicional.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear las posiciones de ETH-USD, SOL-USD y BTC-USD en busca de un objetivo de take-profit entre +2.0% y +3.5%. Proteger con stop-loss estricto del -2.0% si el impulso se desacelera. La posición en QQQ permanece inactiva por cierre de mercado. Mantener la liquidez en efectivo al mínimo y rotar capital únicamente si surge una fuerte señal direccional."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |
| `2026-10-19 01:50` | 🔴 SELL (+0.09$) | `ETH-USD` | $8.09 | $2428.97 | ETH-USD registra una ganancia acumulada y su RSI de 1 hora ha alcanzado 68.3, acercándose ... |

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
