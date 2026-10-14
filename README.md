# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 16:10:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$29.23 USD** | **$9.90 USD** | **$39.13 USD** | 🔴 **-2.18%** ($-0.87) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.76 | $9.90 | 📉 -0.98% | 5h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se encuentra bajo presión con la mayoría de los activos tecnológicos y criptomonedas mostrando tendencias bajistas en gráficos diarios. Sin embargo, se observan niveles de sobreventa extrema en marcos de tiempo de 1 hora (RSI inferior a 25-30) en varios índices y criptos, lo que sugiere posibles oportunidades de rebote técnico de corto plazo si el momentum intradiario da la vuelta."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 70%): La posición en AAPL lleva más de 5 horas abierta con una pérdida menor (-0.98%), pero se mantiene sobre su SMA20 en tendencia alcista diaria y un RSI de 1h en 55.9. Mantendremos la posición buscando alcanzar el objetivo de take-profit sin alterar el capital innecesariamente.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantengo la posición en AAPL por su tendencia alcista diaria y un RSI de 1h saludable (55.9), vigilando de cerca el objetivo de take-profit entre +2.0% y +3.5% o el stop-loss si perfora soportes. Dado que los mercados tradicionales están abiertos pero con sesgo bajista y sin confirmación clara de giro, prefiero conservar la liquidez actual y no forzar entradas prematuras en cripto o tech hasta ver un cambio positivo en el change_1h_pct."
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
