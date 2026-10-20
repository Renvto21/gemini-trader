# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 01:40:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.74 USD** | **$38.74 USD** | 🔴 **-3.15%** ($-1.26) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 14h 59m |
| `ETH-USD` | 0.004178 | $2393.62 | $2409.38 | $10.07 | 📈 +0.66% | 12h 49m |
| `SOL-USD` | 0.096034 | $104.13 | $105.10 | $10.09 | 📈 +0.93% | 8h 59m |
| `BTC-USD` | 0.000105 | $81767.70 | $81975.98 | $8.59 | 📈 +0.25% | 8h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra cerrado, manteniendo congelados los precios de los activos tradicionales como QQQ. Por otro lado, el mercado cripto opera de manera continua (24/7), mostrando ligeras ganancias estables en ETH-USD (+0.66%) y SOL-USD (+0.93%), mientras que BTC-USD se mantiene cerca del precio de entrada. Ninguno de los activos ha alcanzado aún el objetivo de take-profit de +2.0% a +3.5%, ni han activado los stop-loss."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición en SOL-USD presenta una ganancia del 0.93% y un RSI de 1 hora en 57.3. Aunque hay buen impulso, aún no alcanza el objetivo óptimo de take-profit (+2.0% a +3.5%), por lo que se mantiene para maximizar la ganancia.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD mantiene una ligera ganancia del 0.66% con un RSI de 1 hora neutral en 50.5. No hay razones para vender ni recortar pérdidas dado que el soporte se mantiene intacto.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en Cripto (ETH-USD, SOL-USD, BTC-USD) aprovechando que operan 24/7 y muestran resiliencia en sus rebotes. Monitorear de cerca a SOL-USD y ETH-USD para asegurar beneficios parciales si se acercan al rango de take-profit del 2.0% al 3.5% o si el RSI de 1 hora entra en sobrecompra (>70). QQQ se mantiene inalterado por estar cerrado el mercado bursátil."
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
