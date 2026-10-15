# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 10:30:52`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$16.50 USD** | **$21.91 USD** | **$38.41 USD** | 🔴 **-3.98%** ($-1.59) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $347.11 | $10.03 | 📈 +0.28% | 23h 40m |
| `ETH-USD` | 0.002539 | $2362.71 | $2337.06 | $5.93 | 📉 -1.09% | 9h 20m |
| `SOL-USD` | 0.058789 | $102.06 | $101.17 | $5.95 | 📉 -0.87% | 7h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un tono bajista generalizado tanto en renta variable estadounidense como en criptoactivos principales, con la mayoría de los índices y criptomonedas cotizando por debajo de sus medias móviles de 20 periodos. Sin embargo, se observan niveles de sobreventa extremos en indicadores de 1 hora en varios activos tecnológicos y criptos, lo que abre oportunidades tácticas puntuales de rebote técnico (mean reversion) para la cartera."

**Operaciones del ciclo:**
- **[SELL] BTC-USD** (Confianza: 85%): La posición en BTC-USD se acerca al límite de tolerancia de pérdida (-1.91%) y el activo permanece bajo su media móvil con un impulso horario débil, por lo que se ejecuta la venta para cortar pérdidas y proteger el capital disponible.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener la vigilancia sobre BTC-USD, ETH-USD y SOL-USD para asegurar take-profits rápidos si experimentan un rebote hacia zonas de resistencia o cortar pérdidas estrictamente si BTC-USD profundiza su caída por debajo del soporte actual. Evaluar la rotación de AAPL para capitalizar caídas en activos con mayor sobreventa como MSFT o NVDA si el momentum técnico mejora."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **55** | 🎯 **40.0%** (22W / 19L / 14BE) | 🔴 **$-1.39 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 10:30` | 🔴 SELL (-0.10$) | `BTC-USD` | $4.88 | $80081.22 | La posición en BTC-USD se acerca al límite de tolerancia de pérdida (-1.91%) y el activo p... |
| `2026-10-15 03:20` | 🟢 BUY | `SOL-USD` | $6.00 | $102.06 | SOL-USD muestra un RSI de 1h en 33.3 saliendo de zonas de compresión bajista, acompañado d... |
| `2026-10-15 01:10` | 🟢 BUY | `ETH-USD` | $6.00 | $2362.71 | ETH-USD presenta un RSI de 1h extremadamente bajo en 23.5 saliendo de sobreventa y un camb... |
| `2026-10-14 23:30` | 🔴 SELL (-0.30$) | `SOL-USD` | $9.70 | $101.32 | La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin ... |
| `2026-10-14 23:30` | 🔴 SELL (-0.32$) | `ETH-USD` | $9.68 | $2340.86 | 🚨 STOP-LOSS AUTOMÁTICO (CIRCUIT BREAKER): Pérdida de -3.20% superó el límite de seguridad ... |

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
