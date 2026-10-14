# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 23:50:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.54 USD** | **$17.02 USD** | **$39.56 USD** | 🔴 **-1.09%** ($-0.44) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2506.34 | $5.00 | 📉 -0.08% | 6h 40m |
| `BTC-USD` | 0.000072 | $83128.62 | $83431.73 | $6.02 | 📈 +0.36% | 2h 49m |
| `SOL-USD` | 0.055840 | $107.45 | $107.56 | $6.01 | 📈 +0.10% | 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se encuentra operando de forma activa con un sesgo ligeramente positivo en el corto plazo (cambios de 1h positivos en BTC, ETH y SOL), aunque mantenidos bajo sus medias móviles de 20 periodos en el gráfico diario. Los mercados tradicionales permanecen cerrados. Las posiciones actuales muestran estabilidad con ligeras ganancias o pérdidas contenidas, por lo que se prioriza mantener la exposición y vigilar de cerca los niveles objetivo de take-profit sin apresurarse a cerrar posiciones prematuramente."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD se encuentra con un rendimiento positivo del 0.36% y un RSI de 1h equilibrado en 54.2. El holding time es de aproximadamente 2 horas y 49 minutos, por lo que el rebote sigue su curso esperado sin señales de agotamiento.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra estabilidad con una pérdida marginal de -0.08% y un RSI de 1h en 52.9. Se mantiene en cartera para permitir que alcance su objetivo de rebote técnico.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD presenta un PnL positivo del 0.10% tras un tiempo de holding reciente de 39 minutos. Su RSI diario está en sobreventa extrema (28.6) y muestra un cambio positivo de 24h del 1.9%, por lo que tiene potencial alcista adicional.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, ETH-USD y SOL-USD. Vigilar que el RSI de 1 hora se mantenga estable y buscar la toma de beneficios (take-profit) si se alcanza el rango del +2.0% al +3.5%. Conservar la liquidez actual como reserva y estar atentos a cualquier ruptura de soporte en los activos cripto para cortar pérdidas a tiempo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **48** | 🎯 **45.8%** (22W / 12L / 14BE) | 🔴 **$-0.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |

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
