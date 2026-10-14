# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 10:40:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$33.41 USD** | **$5.98 USD** | **$39.39 USD** | 🔴 **-1.52%** ($-0.61) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $82826.20 | $5.98 | 📉 -0.36% | 13h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se encuentra operando en un rango lateral con sesgo bajista en temporalidades diarias, aunque con leves intentos de recuperación intradiaria. Los mercados tradicionales de EE.UU. están abiertos, destacando AAPL con un sólido impulso alcista (cambio 1h del 1.49% y RSI diario de 60.9) y QQQ mostrando debilidad de corto plazo con un RSI de 1h en 32.6, abriendo posibles ventanas de rebote técnico. BTC-USD mantiene una postura estable pero estancada tras casi 14 horas."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 60%): La posición en BTC-USD lleva más de 13 horas abierta con una pérdida marginal de -0.36%. El precio respeta el soporte actual y no ha activado el stop-loss, por lo que se mantiene para permitir que desarrolle el rebote esperado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré la posición actual en BTC-USD monitoreando que no rompa el soporte crítico ni supere el stop-loss del -2.0%. Dado que AAPL muestra un fuerte momentum alcista en mercado abierto con un RSI saludable, evaluaré tomar una posición en el próximo ciclo si mantiene el empuje, mientras mantengo el resto del efectivo en reserva táctica."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **50** | 🎯 **44.0%** (22W / 14L / 14BE) | 🔴 **$-0.50 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 10:10` | 🔴 SELL (-0.11$) | `SOL-USD` | $5.89 | $105.41 | La posición en SOL-USD acumula una pérdida cercana al -1.9%, rozando nuestro stop-loss est... |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |

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
