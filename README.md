# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 14:20:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.57 USD** | **$20.02 USD** | **$38.59 USD** | 🔴 **-3.53%** ($-1.41) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $719.44 | $10.01 | 📈 +0.07% | 3h 40m |
| `ETH-USD` | 0.004178 | $2393.62 | $2396.87 | $10.01 | 📈 +0.14% | 1h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general muestra un comportamiento mixto con ligero sesgo bajista en el corto plazo, donde los índices principales como QQQ y SPY operan bajo sus medias móviles de 20 periodos. Los activos criptográficos (ETH-USD, BTC-USD, SOL-USD) se encuentran consolidando en rangos estrechos tras recientes correcciones, manteniendo RSI de 1 hora moderados sin mostrar todavía el impulso alcista decisivo para un rebote fuerte."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 75%): La posición en QQQ se mantiene dentro del rango de tolerancia operativo con una ganancia marginal del +0.07% tras 3 horas y media abierta. No ha alcanzado el objetivo de take-profit ni ha roto el stop-loss, por lo que se mantiene en cartera esperando mayor momentum intradiario.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD registra una pequeña ganancia del +0.14% y un RSI de 1 hora en 37.7. Aunque el rebote aún es lento, se mantiene operando dentro de los parámetros esperados de gestión de riesgo, por lo que conservamos la posición para buscar la zona de salida objetivo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de QQQ y ETH-USD ya que se encuentran estables con ligeras ganancias (+0.07% y +0.14%) y lejos de los límites de stop-loss del -2.0%. Mantendremos una reserva de efectivo prudente de $18.57 USD y esperaremos a que el RSI de 1 hora en criptomonedas supere 50 con volumen alcista confirmado o que nuestras posiciones alcancen la zona de take-profit del +2.0% al +3.5% para asegurar ganancias."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |
| `2026-10-19 01:50` | 🔴 SELL (+0.09$) | `ETH-USD` | $8.09 | $2428.97 | ETH-USD registra una ganancia acumulada y su RSI de 1 hora ha alcanzado 68.3, acercándose ... |
| `2026-10-19 01:00` | 🔴 SELL (-0.00$) | `SOL-USD` | $8.00 | $105.08 | SOL-USD ha entrado en sobrecompra con un RSI de 1 hora en 72.7, cumpliendo estrictamente c... |
| `2026-10-18 23:20` | 🟢 BUY | `SOL-USD` | $8.00 | $105.11 | SOL-USD presenta un RSI diario en 21.8 (sobreventa extrema) y un momentum de 24 horas alci... |

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
