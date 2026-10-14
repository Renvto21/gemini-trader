# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 09:30:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$11.91 USD** | **$39.44 USD** | 🔴 **-1.41%** ($-0.56) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83009.13 | $5.99 | 📉 -0.14% | 12h 29m |
| `SOL-USD` | 0.055840 | $107.45 | $106.01 | $5.92 | 📉 -1.34% | 10h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se encuentra operando en un rango lateral bajista de corto plazo, con BTC-USD y SOL-USD mostrando ligeras correcciones en la última hora y cotizando por debajo de su SMA20. Los activos de Wall Street están cerrados, por lo que toda la atención se concentra en mantener la disciplina táctica en los activos abiertos 24/7. Las posiciones actuales se mantienen estables pero sin el momentum alcista inmediato esperado."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 65%): BTC-USD muestra una pequeña pérdida no realizada de -0.14% tras 12 horas y media de holding. El RSI de 1H está en 41.1 y el precio se mantiene relativamente estable. No hay razones para cortar la posición prematuramente ya que aún está lejos del stop-loss del -2.0% y el mercado cripto está abierto buscando un reimpulso.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones abiertas de BTC-USD y SOL-USD por unas horas más para evaluar si logran consolidar un rebote técnico desde los niveles de soporte diario, ya que el RSI diario de SOL se mantiene en sobreventa extrema (26.7). Si el holding time supera las 20 horas sin momentum o si las pérdidas se acercan al límite del -2.0%, procederemos a cortar las posiciones para proteger capital. Monitorearemos la evolución del RSI de 1H en busca de señales de giro alcista superior a 50 para asegurar ganancias parciales."
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
