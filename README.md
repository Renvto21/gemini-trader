# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 01:10:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.75 USD** | **$38.75 USD** | 🔴 **-3.11%** ($-1.25) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 14h 29m |
| `ETH-USD` | 0.004178 | $2393.62 | $2410.35 | $10.07 | 📈 +0.70% | 12h 19m |
| `SOL-USD` | 0.096034 | $104.13 | $105.17 | $10.10 | 📈 +1.00% | 8h 29m |
| `BTC-USD` | 0.000105 | $81767.70 | $82028.74 | $8.59 | 📈 +0.32% | 7h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la atención se centra en los criptoactivos (abiertos 24/7). SOL-USD muestra un rendimiento positivo con una ganancia del 1.0% y un RSI de 1 hora en 58.4, acercándose a zonas de interés para asegurar ganancias parciales o totales si supera el umbral de sobrecompra. ETH-USD y BTC-USD registran ganancias modestas, manteniendo un comportamiento lateral en el corto plazo. Dado que la liquidez en efectivo es de 0.0 USD y las posiciones actuales no han alcanzado el objetivo take-profit de +2.0% a +3.5% ni han roto los niveles de stop-loss, la estrategia óptima es mantener las posiciones actuales y esperar a que el momentum alcista active las tomas de beneficios para rotar capital."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición muestra un rendimiento positivo de +1.0% y un RSI de 1h en 58.4. Aunque se acerca a la zona de take-profit, aún no llega al objetivo óptimo de +2.0% a +3.5%, por lo que es prudente mantener y esperar mayor momentum alcista.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en QQQ, ETH-USD, SOL-USD y BTC-USD. Estar preparado para vender SOL-USD si su RSI de 1 hora supera 70 o si alcanza la zona de take-profit entre +2.0% y +3.5%. Vigilar el comportamiento de ETH-USD y BTC-USD para capturar ganancias rápidas. No realizar nuevas compras hasta liberar liquidez mediante ventas."
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
