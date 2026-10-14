# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 17:50:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.23 USD** | **$19.86 USD** | **$39.08 USD** | 🔴 **-2.29%** ($-0.92) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 7h 0m |
| `SOL-USD` | 0.095785 | $104.40 | $103.86 | $9.95 | 📉 -0.52% | 1h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra cerrado, por lo que toda la actividad debe centrarse en los activos cripto abiertos 24/7. Las criptomonedas principales como SOL-USD, ETH-USD y BTC-USD muestran condiciones de sobreventa severa en el RSI de 1h, pero SOL-USD y ETH-USD están experimentando una ligera presión bajista adicional o estancamiento de corto plazo que pone a prueba la paciencia del portafolio. AAPL permanece cerrada con una pérdida leve."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 60%): SOL-USD registra una pequeña pérdida (-0.52%) y un RSI de 1h en 27.7. Aunque el impulso se ha retrasado ligeramente, aún no cruza el stop-loss estricto de -2.0%, por lo que mantendremos la posición para darle una oportunidad final de rebote antes de rotar capital.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos AAPL ya que el mercado está cerrado. Para SOL-USD, el RSI de 1h se encuentra en 27.7 y el cambio de 1h es ligeramente negativo (-0.22%), rozando nuestro límite de stop-loss estricto de -2.0% general o vigilando de cerca que no extienda sus pérdidas. Si SOL-USD rompe a la baja con mayor fuerza o continúa estancado sin mostrar el rebote esperado, procederemos a vender en el próximo ciclo para proteger el capital. Estaremos atentos a ETH-USD por si muestra una clara señal de giro en su RSI de 1h (actualmente en 22.2) para una posible rotación de capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **52** | 🎯 **42.3%** (22W / 16L / 14BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 16:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.40 | SOL-USD presenta un RSI de 1h en 30.9 saliendo de la zona de compresión y un cambio positi... |
| `2026-10-14 15:20` | 🔴 SELL (-0.08$) | `SOL-USD` | $9.92 | $103.86 | SOL-USD lleva varias horas sin mostrar el rebote esperado, su RSI de 1h ha caído hasta 25.... |
| `2026-10-14 12:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.70 | SOL-USD presenta un RSI de 1h en 29.2 saliendo de sobreventa extrema y un cambio de 1h pos... |
| `2026-10-14 11:20` | 🔴 SELL (-0.09$) | `BTC-USD` | $5.89 | $81874.95 | BTC-USD lleva más de 14 horas abierto con un PnL negativo persistente (-1.51%) y un RSI de... |
| `2026-10-14 10:50` | 🟢 BUY | `AAPL` | $10.00 | $346.15 | AAPL se encuentra con un excelente momentum alcista intradiario, un incremento de 1.4% en ... |

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
