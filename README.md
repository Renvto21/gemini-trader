# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 14:20:55`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.93 USD** | **$39.06 USD** | 🔴 **-2.35%** ($-0.94) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $340.67 | $10.00 | 📈 +0.01% | 2h 19m |
| `ETH-USD` | 0.004058 | $2452.17 | $2447.98 | $9.93 | 📉 -0.17% | 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento mixto con sesgo lateral en la última hora. Las criptomonedas continúan mostrando un desempeño superior diario liderado por ETH y BTC, mientras que los índices y acciones estadounidenses se mantienen estables pero en rangos estrechos. Los activos actuales en cartera (AAPL y ETH-USD) se mantienen relativamente estables sin mostrar señales claras de sobrecompra o pérdidas críticas que activen los stop-loss."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 70%): AAPL se mantiene estable con un P&L neutral y un RSI de 1 hora en 39.1, respetando la zona de soporte técnico. No hay motivos para vender ni para ampliar exposición por el momento.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un rendimiento diario positivo (+1.79%) y un RSI de 1 hora en 60.6, lo cual indica estabilidad y potencial alcista continuo dentro del mercado cripto abierto 24/7.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos AAPL y ETH-USD durante este ciclo. AAPL muestra un rsi_1h de 39.1 con soporte cercano y ETH-USD se mantiene sólido con rsi_1h en 60.6. Seguiremos vigilando de cerca el take-profit en +2.5% o el stop-loss en -2.0%. Si no hay expansión de volumen o volatilidad alcista en el próximo ciclo, rotaremos capital hacia activos con mayor momentum."
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
