# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 11:00:56`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$10.00 USD** | **$28.35 USD** | **$38.35 USD** | 🔴 **-4.12%** ($-1.65) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $345.06 | $9.97 | 📉 -0.31% | 1d 0h |
| `ETH-USD` | 0.002539 | $2362.71 | $2338.36 | $5.94 | 📉 -1.03% | 9h 50m |
| `SOL-USD` | 0.058789 | $102.06 | $101.29 | $5.95 | 📉 -0.75% | 7h 40m |
| `MSFT` | 0.012146 | $535.17 | $534.53 | $6.49 | 📉 -0.12% | 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo general bajista en los índices principales y criptomonedas, con caídas semanales acentuadas en QQQ y NVDA. Sin embargo, observamos oportunidades tácticas de sobreventa extrema en ciertos activos de alta calidad como MSFT, mientras que las criptomonedas ETH-USD y SOL-USD se mantienen cerca de zonas críticas pero estables. Mantendremos el enfoque en la captura de rebotes técnicos selectivos cumpliendo estrictamente con la gestión de riesgo y rotación."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 80%): MSFT fue adquirida recientemente aprovechando su sobreventa extrema en el RSI de 1h (11.7). La tendencia diaria sigue siendo alcista y el activo se mantiene estable. Mantenemos la posición para capturar el rebote técnico esperado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en AAPL, MSFT, ETH-USD y SOL-USD vigilando de cerca los niveles de soporte. Si ETH-USD o SOL-USD rompen a la baja el umbral de pérdida del -2%, procederemos a cortar pérdidas de inmediato. Estar atentos a la evolución del RSI de 1h en MSFT y AAPL para asegurar beneficios rápidos si alcanzan el objetivo de +2.5% o superior."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **55** | 🎯 **40.0%** (22W / 19L / 14BE) | 🔴 **$-1.39 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 10:50` | 🟢 BUY | `MSFT` | $6.50 | $535.17 | MSFT presenta un RSI de 1h ultra comprimido en sobreventa extrema (14.7) con un cambio pos... |
| `2026-10-15 10:30` | 🔴 SELL (-0.10$) | `BTC-USD` | $4.88 | $80081.22 | La posición en BTC-USD se acerca al límite de tolerancia de pérdida (-1.91%) y el activo p... |
| `2026-10-15 03:20` | 🟢 BUY | `SOL-USD` | $6.00 | $102.06 | SOL-USD muestra un RSI de 1h en 33.3 saliendo de zonas de compresión bajista, acompañado d... |
| `2026-10-15 01:10` | 🟢 BUY | `ETH-USD` | $6.00 | $2362.71 | ETH-USD presenta un RSI de 1h extremadamente bajo en 23.5 saliendo de sobreventa y un camb... |
| `2026-10-14 23:30` | 🔴 SELL (-0.30$) | `SOL-USD` | $9.70 | $101.32 | La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin ... |

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
