# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 12:50:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.31 USD** | **$19.93 USD** | **$39.23 USD** | 🔴 **-1.91%** ($-0.77) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $345.19 | $9.97 | 📉 -0.28% | 2h 0m |
| `SOL-USD` | 0.095511 | $104.70 | $104.22 | $9.95 | 📉 -0.46% | 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento predominantemente bajista en el corto plazo con la mayoría de los activos cotizando bajo sus medias móviles de 20 periodos y experimentando descensos en las últimas 24 horas. Sin embargo, los RSI de 1 hora se encuentran en niveles muy deprimidos (zona de sobreventa extrema), lo que abre la puerta a posibles rebotes técnicos por reversión a la media. Mantendremos la cautela pero listos para capturar movimientos rápidos."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 75%): AAPL mantiene una tendencia alcista macro sobre su SMA20 y un RSI de 1h cercano a sobrecompra (64.3). Nos mantenemos firmes esperando alcanzar el objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD tiene un PnL de -0.46% y un holding time corto. Aunque su tendencia es bajista, el RSI de 1h en 24.0 sugiere que está consolidando cerca de suelos de corto plazo, por lo que le daremos más tiempo antes de considerar una rotación.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos nuestras posiciones abiertas actuales (AAPL y SOL-USD) mientras evaluamos si logran sostener sus niveles técnicos. AAPL se acerca a la zona de sobrecompra en RSI 1h (64.3), por lo que vigilaremos de cerca el objetivo de take-profit entre +2.0% y +3.5%. SOL-USD muestra un RSI diario muy bajo y un RSI de 1h en 24.0, mantendremos la posición con un stop-loss estricto a -2.0%. Conservaremos el efectivo disponible ($19.31) esperando una señal de confirmación más clara antes de arriesgar capital adicional."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **51** | 🎯 **43.1%** (22W / 15L / 14BE) | 🔴 **$-0.59 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 12:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.70 | SOL-USD presenta un RSI de 1h en 29.2 saliendo de sobreventa extrema y un cambio de 1h pos... |
| `2026-10-14 11:20` | 🔴 SELL (-0.09$) | `BTC-USD` | $5.89 | $81874.95 | BTC-USD lleva más de 14 horas abierto con un PnL negativo persistente (-1.51%) y un RSI de... |
| `2026-10-14 10:50` | 🟢 BUY | `AAPL` | $10.00 | $346.15 | AAPL se encuentra con un excelente momentum alcista intradiario, un incremento de 1.4% en ... |
| `2026-10-14 10:10` | 🔴 SELL (-0.11$) | `SOL-USD` | $5.89 | $105.41 | La posición en SOL-USD acumula una pérdida cercana al -1.9%, rozando nuestro stop-loss est... |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |

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
