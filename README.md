# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 16:50:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.97 USD** | **$38.44 USD** | 🔴 **-3.89%** ($-1.56) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.95 | $10.00 | 📈 +0.01% | 6h 30m |
| `ETH-USD` | 0.004126 | $2423.75 | $2415.67 | $9.97 | 📉 -0.33% | 5h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la atención se centra exclusivamente en el ecosistema cripto que opera 24/7. Las posiciones actuales en SOL-USD y ETH-USD se mantienen estables pero con un impulso lateral leve tras varias horas de retención, con ETH registrando una ligera pérdida (-0.33%) y SOL prácticamente plana. Los indicadores diarios continúan mostrando niveles de sobreventa profunda en las altcoins principales, ofreciendo un entorno propicio para mantener las posiciones actuales a la espera de un rebote técnico inminente."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD se mantiene en rango de acumulación tras 6.5 horas de retención. El RSI diario se mantiene en sobreventa extrema (22.6) y el cambio horario es positivo (+0.18%), por lo que mantenemos la posición buscando el objetivo de take-profit sin violar el stop-loss.
- **[HOLD] ETH-USD** (Confianza: 72%): ETH-USD presenta una mínima pérdida de -0.33% tras 5 horas abierta. Con un RSI diario de 28.3 y soporte en zona de sobreventa, mantenemos la posición esperando la confirmación del rebote técnico hacia la zona objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones abiertas de SOL-USD y ETH-USD durante las próximas horas para permitir que el momentum alcista intradiario active el take-profit fijado entre +2.0% y +3.5%. El stop-loss estricto permanece vigilado en -2.0% por posición. Si transcurren más ciclos sin movimiento o las criptomonedas perforan soportes críticos, procederemos a vender para asegurar liquidez."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **65** | 🎯 **40.0%** (26W / 25L / 14BE) | 🔴 **$-1.41 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 11:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2423.75 | ETH-USD presenta un RSI diario en niveles de sobreventa profunda (28.9) y un cambio positi... |
| `2026-10-17 10:20` | 🟢 BUY | `SOL-USD` | $10.00 | $103.94 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (22.5) y un cambio positiv... |
| `2026-10-17 04:30` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $104.94 | SOL-USD ha alcanzado un RSI de 1 hora de 70.4, entrando en zona de sobrecompra, y acumula ... |
| `2026-10-17 04:00` | 🔴 SELL (+0.07$) | `ETH-USD` | $10.07 | $2429.64 | ETH-USD ha alcanzado un RSI de 1 hora de 73.3, entrando en zona de sobrecompra. Siguiendo ... |
| `2026-10-16 16:30` | 🟢 BUY | `ETH-USD` | $10.00 | $2412.98 | ETH-USD muestra un RSI diario en niveles de sobreventa extrema (30.3) y un cambio positivo... |

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
