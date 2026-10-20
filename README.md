# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 12:21:11`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.98 USD** | **$39.10 USD** | 🔴 **-2.24%** ($-0.90) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $340.33 | $9.99 | 📉 -0.09% | 19m |
| `GLD` | 0.026337 | $379.70 | $379.29 | $9.99 | 📉 -0.11% | 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra mayormente con un sesgo bajista de corto plazo en la última hora, aunque AAPL y GLD muestran condiciones de sobreventa intradía con RSI de 1 hora en 32.4 y 29.9 respectivamente, manteniendo intacta nuestra tesis de rebote técnico de media reversión. El efectivo disponible es de $19.12 USD y los mercados tradicionales permanecen abiertos."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 80%): AAPL mantiene una tendencia alcista diaria sólida con un RSI de 1 hora en 32.4 (cercano a sobreventa). El tiempo abierto es corto y seguimos esperando el rebote hacia nuestro objetivo de take-profit.
- **[HOLD] GLD** (Confianza: 80%): GLD presenta un RSI de 1 hora en 29.9, totalmente en zona de sobreventa intradía. Mantenemos la posición buscando la reversión a la media dentro del rango operativo establecido.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales en AAPL y GLD ya que el tiempo de retención sigue siendo bajo (19 minutos) y buscamos el rebote técnico hacia la zona de take-profit entre +2.5% y +3.5%. El stop-loss se mantiene estricto en -2.0%. Si alguna de las posiciones rompe soportes o se estanca sin momentum, realizaremos una venta para rotar capital hacia criptomonedas o activos con mayor dinamismo intradiario."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **81** | 🎯 **44.4%** (36W / 30L / 15BE) | 🔴 **$-0.74 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-20 12:01` | 🟢 BUY | `GLD` | $10.00 | $379.70 | GLD presenta un RSI de 1 hora en 31.4, acercándose a la zona ideal de sobreventa para acti... |
| `2026-10-20 12:01` | 🟢 BUY | `AAPL` | $10.00 | $340.64 | AAPL se encuentra en tendencia alcista diaria con un RSI de 1 hora en 33.1 (cercano a sobr... |
| `2026-10-20 11:10` | 🔴 SELL (+0.12$) | `BTC-USD` | $8.69 | $82949.93 | BTC-USD muestra un RSI de 1 hora en 72.2 (sobrecompra) y un rendimiento positivo de +1.45%... |
| `2026-10-20 11:10` | 🔴 SELL (+0.28$) | `SOL-USD` | $10.28 | $107.08 | SOL-USD registra un excelente rendimiento de +2.83% con un RSI de 1 hora en sobrecompra (7... |
| `2026-10-20 11:10` | 🔴 SELL (+0.23$) | `ETH-USD` | $10.23 | $2449.11 | ETH-USD ha alcanzado un PnL de +2.32% y su RSI de 1 hora ha tocado el nivel de sobrecompra... |

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
