# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 04:00:51`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.85 USD** | **$38.47 USD** | 🔴 **-3.84%** ($-1.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 17h 10m |
| `BTC-USD` | 0.000061 | $81640.68 | $80873.68 | $4.95 | 📉 -0.94% | 6h 50m |
| `ETH-USD` | 0.002539 | $2362.71 | $2356.56 | $5.98 | 📉 -0.26% | 2h 50m |
| `SOL-USD` | 0.058789 | $102.06 | $102.20 | $6.01 | 📈 +0.14% | 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general de renta variable se encuentra cerrado, por lo que la liquidez activa se concentra exclusivamente en el ecosistema cripto. Las criptomonedas muestran signos de consolidación tras caídas recientes de 24 horas, con SOL-USD manteniendo un leve sesgo positivo de recuperación mientras ETH-USD y BTC-USD operan con cautela en zonas de soporte técnico."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra operando en positivo (+0.14%) con un RSI de 1h en recuperación (36.8). Mantendremos la posición activa para buscar la toma de ganancias en el rango objetivo de +2.0% a +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales en AAPL, BTC-USD, ETH-USD y SOL-USD. La posición en SOL-USD muestra un inicio positivo y se vigilará para asegurar beneficios si alcanza el objetivo de +2.0% a +3.5%. ETH-USD y BTC-USD se mantendrán monitoreando sus niveles de RSI de 1 hora para confirmar rebotes o aplicar un stop-loss estricto si rompen soportes clave a la baja."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **54** | 🎯 **40.7%** (22W / 18L / 14BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 03:20` | 🟢 BUY | `SOL-USD` | $6.00 | $102.06 | SOL-USD muestra un RSI de 1h en 33.3 saliendo de zonas de compresión bajista, acompañado d... |
| `2026-10-15 01:10` | 🟢 BUY | `ETH-USD` | $6.00 | $2362.71 | ETH-USD presenta un RSI de 1h extremadamente bajo en 23.5 saliendo de sobreventa y un camb... |
| `2026-10-14 23:30` | 🔴 SELL (-0.30$) | `SOL-USD` | $9.70 | $101.32 | La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin ... |
| `2026-10-14 23:30` | 🔴 SELL (-0.32$) | `ETH-USD` | $9.68 | $2340.86 | 🚨 STOP-LOSS AUTOMÁTICO (CIRCUIT BREAKER): Pérdida de -3.20% superó el límite de seguridad ... |
| `2026-10-14 21:10` | 🟢 BUY | `BTC-USD` | $5.00 | $81640.68 | BTC-USD presenta un RSI de 1h en 24.9 (sobreventa extrema) y liquidez disponible suficient... |

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
