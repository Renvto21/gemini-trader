# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 16:20:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$29.23 USD** | **$9.91 USD** | **$39.14 USD** | 🔴 **-2.15%** ($-0.86) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $343.16 | $9.91 | 📉 -0.86% | 5h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general muestra un sesgo bajista en el corto plazo con varios activos probando condiciones de sobreventa en gráficos de 1 hora (RSI bajo 30). Sin embargo, AAPL se mantiene resistente con tendencia alcista y un RSI de 1h saludable en 56.9, consolidándose por encima de su SMA20. Los mercados tradicionales están abiertos y las criptomonedas muestran una ligera recuperación en el cambio de 1h, pero sin la fuerza direccional necesaria para forzar nuevas entradas inmediatas."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 75%): AAPL mantiene una tendencia alcista diaria sólida y un RSI de 1h en 56.9. Aunque registra una leve pérdida temporal (-0.86%), el activo se encuentra dentro del rango esperado sin romper soportes críticos, por lo que mantengo la posición buscando el objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré la posición abierta en AAPL ya que lleva más de 5 horas operando de manera estable con tendencia alcista y sin romper soporte. Establezco mi objetivo de take-profit entre +2.0% y +3.5% (aproximadamente $350.00) y un stop-loss estricto si perfora la zona de los $336.00. Para los siguientes ciclos, vigilaré posibles oportunidades de rebote en Cripto (como BTC-USD o SOL-USD) solo si el RSI de 1h confirma una salida clara de sobreventa con un change_1h_pct más robusto."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **52** | 🎯 **42.3%** (22W / 16L / 14BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 15:20` | 🔴 SELL (-0.08$) | `SOL-USD` | $9.92 | $103.86 | SOL-USD lleva varias horas sin mostrar el rebote esperado, su RSI de 1h ha caído hasta 25.... |
| `2026-10-14 12:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.70 | SOL-USD presenta un RSI de 1h en 29.2 saliendo de sobreventa extrema y un cambio de 1h pos... |
| `2026-10-14 11:20` | 🔴 SELL (-0.09$) | `BTC-USD` | $5.89 | $81874.95 | BTC-USD lleva más de 14 horas abierto con un PnL negativo persistente (-1.51%) y un RSI de... |
| `2026-10-14 10:50` | 🟢 BUY | `AAPL` | $10.00 | $346.15 | AAPL se encuentra con un excelente momentum alcista intradiario, un incremento de 1.4% en ... |
| `2026-10-14 10:10` | 🔴 SELL (-0.11$) | `SOL-USD` | $5.89 | $105.41 | La posición en SOL-USD acumula una pérdida cercana al -1.9%, rozando nuestro stop-loss est... |

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
