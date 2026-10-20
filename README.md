# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 13:51:03`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.95 USD** | **$39.08 USD** | 🔴 **-2.30%** ($-0.92) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $340.77 | $10.00 | 📈 +0.04% | 1h 49m |
| `ETH-USD` | 0.004058 | $2452.17 | $2452.17 | $9.95 | 📈 +0.00% | 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento mixto con sesgo lateral en activos tradicionales, mientras que las criptomonedas continúan operando 24/7 con un ligero sesgo alcista y mejor momento en el corto plazo. GLD ha profundizado su caída y su rsi_1h ha bajado a 29.8, acercándose a un nivel crítico, mientras que AAPL se mantiene plano sin la velocidad de rebote esperada. ETH-USD y SOL-USD muestran mejor momentum intradiario."

**Operaciones del ciclo:**
- **[SELL] GLD** (Confianza: 80%): GLD se encuentra estancado con un rendimiento ligeramente negativo (-0.47%) y un rsi_1h de 29.8 que no ha logrado generar el rebote técnico esperado. Rotamos el capital hacia activos con mayor dinamismo.
- **[BUY] ETH-USD** (Confianza: 85%): ETH-USD muestra un excelente impulso de corto plazo con change_1h_pct positivo (+0.55%) y rsi_1h en 64.6, operando en mercado abierto 24/7 y cumpliendo con nuestra estrategia de cazar momentum.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos AAPL por un ciclo más para observar si el rsi_1h rompe al alza con decisión. Venderemos GLD debido a que su momentum se ha debilitado y su rsi_1h tocó sobreventa sin rebotar adecuadamente, liberando liquidez. Reasignaremos esa liquidez hacia ETH-USD para aprovechar su momento alcista intradiario y cumplir con la regla de rotación de capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **82** | 🎯 **43.9%** (36W / 31L / 15BE) | 🔴 **$-0.79 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-20 13:51` | 🟢 BUY | `ETH-USD` | $9.95 | $2452.17 | ETH-USD muestra un excelente impulso de corto plazo con change_1h_pct positivo (+0.55%) y ... |
| `2026-10-20 13:51` | 🔴 SELL (-0.05$) | `GLD` | $9.95 | $377.90 | GLD se encuentra estancado con un rendimiento ligeramente negativo (-0.47%) y un rsi_1h de... |
| `2026-10-20 12:01` | 🟢 BUY | `GLD` | $10.00 | $379.70 | GLD presenta un RSI de 1 hora en 31.4, acercándose a la zona ideal de sobreventa para acti... |
| `2026-10-20 12:01` | 🟢 BUY | `AAPL` | $10.00 | $340.64 | AAPL se encuentra en tendencia alcista diaria con un RSI de 1 hora en 33.1 (cercano a sobr... |
| `2026-10-20 11:10` | 🔴 SELL (+0.12$) | `BTC-USD` | $8.69 | $82949.93 | BTC-USD muestra un RSI de 1 hora en 72.2 (sobrecompra) y un rendimiento positivo de +1.45%... |

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
