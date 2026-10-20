# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 00:40:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.73 USD** | **$38.73 USD** | 🔴 **-3.17%** ($-1.27) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 14h 0m |
| `ETH-USD` | 0.004178 | $2393.62 | $2408.66 | $10.06 | 📈 +0.63% | 11h 49m |
| `SOL-USD` | 0.096034 | $104.13 | $105.13 | $10.10 | 📈 +0.96% | 8h 0m |
| `BTC-USD` | 0.000105 | $81767.70 | $81928.38 | $8.58 | 📈 +0.20% | 7h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto 24/7 mostrando ligeros signos de recuperación gradual, con SOL-USD registrando un rendimiento positivo cercano al +0.96% y ETH-USD en +0.63%, acercándose a nuestra zona de objetivos intermedios. Los activos tradicionales como QQQ y SPY se encuentran cerrados, por lo que la liquidez y la atención táctica se concentran en optimizar las posiciones cripto abiertas sin forzar nuevas entradas hasta alcanzar niveles clave de take-profit o sobrecompra en el RSI de 1 hora."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra un rendimiento positivo constante (+0.96%) pero aún no alcanza la zona objetivo de take-profit entre +2.0% y +3.5% ni presenta un RSI de 1 hora en sobrecompra extrema (>70). Mantenemos la posición para dejar correr las ganancias.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en criptomonedas (SOL-USD, ETH-USD, BTC-USD) y QQQ. Monitorear de cerca a SOL-USD y ETH-USD para asegurar ganancias parciales o totales si alcanzan el rango de take-profit de +2.0% a +3.5% o si el RSI de 1 hora supera los 70 puntos. Si alguna posición estanca su impulso o retrocede, se procederá a recortar para asegurar capital de cara a la apertura de los mercados tradicionales."
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
