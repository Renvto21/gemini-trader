# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 23:40:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.54 USD** | **$17.01 USD** | **$39.55 USD** | 🔴 **-1.14%** ($-0.45) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2504.72 | $4.99 | 📉 -0.15% | 6h 30m |
| `BTC-USD` | 0.000072 | $83128.62 | $83314.20 | $6.01 | 📈 +0.22% | 2h 39m |
| `SOL-USD` | 0.055840 | $107.45 | $107.44 | $6.00 | 📉 -0.01% | 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la actividad se concentra en el sector de criptomonedas (abierto 24/7). Los activos principales de nuestra cartera (BTC-USD, ETH-USD y SOL-USD) muestran estabilidad y ligeros repuntes de 24 horas tras haber entrado en zonas de sobreventa diaria, aunque operan bajo sus medias móviles de 20 periodos. Mantenemos una postura de vigilancia estricta para asegurar beneficios rápidos si alcanzan la zona de take-profit o para cortar pérdidas si se invalidan los soportes."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD muestra un comportamiento estable con un PnL positivo del 0.22% tras su reciente compra. El RSI de 1H se sitúa en 51.4 y el cambio de 24h es positivo (+1.9%), por lo que mantenemos la posición a la espera de que se acerque al objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD registra una ligera pérdida de -0.15%, manteniendo una alta estabilidad tras más de 6 horas en cartera. El RSI de 1H en 51.8 y el repunte del 2.47% en 24h respaldan mantener la posición buscando un rebote mayor.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD se encuentra prácticamente plano (-0.01%) tras su reciente apertura, respaldado por un RSI diario en sobreventa extrema (28.3). Mantenemos la posición para capturar el esperado rebote técnico de reversión a la media.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, ETH-USD y SOL-USD. Vigilar de cerca el RSI de 1 hora y el porcentaje de cambio para asegurar ganancias si se alcanza el rango objetivo de +2.0% a +3.5%. Mantener la reserva mínima de efectivo y estar preparados para rotar capital si alguna posición se estanca o rompe a la baja."
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
