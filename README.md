# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 13:30:51`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.31 USD** | **$19.90 USD** | **$39.21 USD** | 🔴 **-1.98%** ($-0.79) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $345.11 | $9.97 | 📉 -0.30% | 2h 40m |
| `SOL-USD` | 0.095511 | $104.70 | $103.97 | $9.93 | 📉 -0.70% | 1h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento predominantemente bajista en el corto plazo con varios índices y criptomonedas bajo sus medias móviles de 20 periodos y RSI de 1 hora en niveles de sobreventa extrema, lo que incrementa las probabilidades de rebotes técnicos inminentes. AAPL se mantiene fuerte con una tendencia alcista macro y un RSI de 1h cercano a la sobrecompra (66.0), mientras que SOL-USD muestra un ligero cambio positivo de 1h (0.24%) a pesar de su sobreventa."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 80%): AAPL mantiene una tendencia alcista saludable sobre la SMA20 con un PnL estable (-0.3%) y un RSI de 1h en 66.0, aproximándose a la zona de toma de ganancias.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra signos incipientes de giro con un cambio de 1h positivo del 0.24% tras haber entrado en sobreventa, por lo que se le dará un ciclo más para confirmar el rebote.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos AAPL vigilando de cerca su RSI de 1h para asegurar ganancias si supera 70, y mantendremos SOL-USD mientras su rebote intradiario se consolide. La liquidez en efectivo se mantiene por encima del umbral mínimo de seguridad ($4.00) a la espera de confirmaciones adicionales en cripto si ETH o BTC muestran rupturas de volumen con RSI alcista."
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
