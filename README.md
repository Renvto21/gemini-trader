# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 11:52:20`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$39.12 USD** | **$0.00 USD** | **$39.12 USD** | 🔴 **-2.19%** ($-0.88) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *(Ninguna posición abierta - 100% en efectivo)* | - | - | - | - | - | - |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto mantiene un sesgo alcista de muy corto plazo con el RSI de 1 hora de SOL, BTC y ETH en niveles de sobrecompra (>70). Los mercados tradicionales se encuentran en rangos estables. Dado que la regla de oro indica buscar puntos de entrada óptimos tras un enfriamiento, actualmente nos encontramos en liquidez total ($39.12 USD) esperando retrocesos en cripto o oportunidades de valor en activos tradicionales con RSI atractivo como GLD."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): Esperando el enfriamiento del RSI de 1h desde la zona de sobrecompra (71.9) hacia niveles más saludables antes de reingresar en busca de un nuevo impulso.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantenemos $39.12 USD en efectivo. Las criptomonedas siguen en sobrecompra de 1 hora, por lo que esperamos un retroceso del RSI hacia la zona de 45-50 para desplegar hasta $35 USD en posiciones de alta convicción. Monitorearemos GLD ya que su RSI de 1 hora se encuentra en 30.8, acercándose a una posible zona de sobreventa para un rebote táctico."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **81** | 🎯 **44.4%** (36W / 30L / 15BE) | 🔴 **$-0.74 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-20 11:10` | 🔴 SELL (+0.12$) | `BTC-USD` | $8.69 | $82949.93 | BTC-USD muestra un RSI de 1 hora en 72.2 (sobrecompra) y un rendimiento positivo de +1.45%... |
| `2026-10-20 11:10` | 🔴 SELL (+0.28$) | `SOL-USD` | $10.28 | $107.08 | SOL-USD registra un excelente rendimiento de +2.83% con un RSI de 1 hora en sobrecompra (7... |
| `2026-10-20 11:10` | 🔴 SELL (+0.23$) | `ETH-USD` | $10.23 | $2449.11 | ETH-USD ha alcanzado un PnL de +2.32% y su RSI de 1 hora ha tocado el nivel de sobrecompra... |
| `2026-10-20 10:50` | 🔴 SELL (-0.08$) | `QQQ` | $9.92 | $713.02 | QQQ lleva más de 24 horas abierto sin momentum alcista, con un rendimiento de -0.82% y baj... |
| `2026-10-19 23:00` | 🟢 BUY | `BTC-USD` | $4.00 | $81646.39 | BTC-USD presenta un RSI de 1 hora en 27.7, nivel de sobreventa profunda ideal para un rebo... |

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
