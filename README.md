# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 06:00:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.48 USD** | **$38.48 USD** | 🔴 **-3.79%** ($-1.52) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 19h 20m |
| `ETH-USD` | 0.004178 | $2393.62 | $2383.93 | $9.96 | 📉 -0.40% | 17h 9m |
| `SOL-USD` | 0.096034 | $104.13 | $104.09 | $10.00 | 📉 -0.04% | 13h 20m |
| `BTC-USD` | 0.000105 | $81767.70 | $81469.26 | $8.53 | 📉 -0.36% | 12h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la atención se centra en las criptomonedas (ETH-USD, SOL-USD, BTC-USD), las cuales operan con un momentum moderado y sin grandes volatilidades en la última hora. Las posiciones actuales muestran ligeras pérdidas acumuladas pero se mantienen estables dentro de rangos normales de consolidación, sin activar nuestros niveles de stop-loss ni take-profit. Mantenemos la disciplina táctica sin realizar cierres precipitados."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD mantiene un holding time de más de 17 horas con una pérdida menor de -0.4%. El RSI de 1 hora está en un nivel neutral de 44.2 y no ha alcanzado ni el take-profit ni el stop-loss. Mantenemos la posición esperando un impulso alcista mayor.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD muestra estabilidad con una variación mínima y un RSI de 1 hora en 53.1. Sin razones técnicas para vender aún, esperamos la expansión del movimiento alcista.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca el comportamiento de ETH-USD, SOL-USD y BTC-USD en los siguientes ciclos. Esperar a que el RSI de 1 hora se acerque a zonas de sobrecompra (> 70) o que alcancen el objetivo de take-profit del +2.5% para asegurar ganancias parciales o totales. Proteger rigurosamente el capital si alguna posición rompe a la baja hacia el umbral de -2.0%. Mantener la liquidez disponible según las reglas de rotación."
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
