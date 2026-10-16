# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 10:50:52`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.12 USD** | **$24.41 USD** | **$38.54 USD** | 🔴 **-3.66%** ($-1.46) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $537.02 | $6.52 | 📈 +0.35% | 1d 0h |
| `NVDA` | 0.036812 | $217.32 | $215.68 | $7.94 | 📉 -0.75% | 22h 0m |
| `ETH-USD` | 0.002855 | $2451.90 | $2446.65 | $6.99 | 📉 -0.21% | 6h 19m |
| `SOL-USD` | 0.028214 | $106.33 | $105.15 | $2.97 | 📉 -1.11% | 5h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo defensivo con la mayoría de los activos bajo la media móvil de 20 días y caídas en la última hora. QQQ y NVDA presentan caídas con RSI de 1 hora en niveles de sobreventa extrema (30.2 y 21.4 respectivamente), lo que incrementa el riesgo de un desplome o requiere una rotación rápida si el rebote falla. Dado que operamos bajo una táctica agresiva de gestión de riesgo estricta, debemos cortar posiciones estancadas o con pérdida cercana al umbral de protección antes de que el circuit breaker actúe."

**Operaciones del ciclo:**
- **[SELL] QQQ** (Confianza: 85%): QQQ lleva más de 22 horas abierto operando bajo la SMA20 con un RSI de 1 hora en 30.2 y un rendimiento negativo sostenido. Aplicamos nuestra regla de rotación activa y protección contra pérdidas prolongadas para asegurar el capital remanente y buscar mejores oportunidades.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones de MSFT, ETH-USD y SOL-USD por ahora, monitoreando de cerca su evolución. QQQ y NVDA muestran debilidad prolongada cerca de sus límites de pérdida; si la situación no mejora en el siguiente ciclo, procederemos a liquidar QQQ y NVDA para liberar capital. Mantendremos liquidez cercana al mínimo operativo de $4.00 USD y buscaremos reasignar a activos con momentum alcista confirmado."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **59** | 🎯 **40.7%** (24W / 21L / 14BE) | 🔴 **$-1.26 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 10:50` | 🔴 SELL (-0.04$) | `QQQ` | $9.95 | $721.83 | QQQ lleva más de 22 horas abierto operando bajo la SMA20 con un RSI de 1 hora en 30.2 y un... |
| `2026-10-16 05:10` | 🟢 BUY | `SOL-USD` | $3.00 | $106.33 | SOL-USD presenta un RSI diario en zona de sobreventa extrema (29.0) y un cambio positivo e... |
| `2026-10-16 04:30` | 🟢 BUY | `ETH-USD` | $7.00 | $2451.90 | Aprovechamos la liquidez disponible sobre la reserva mínima ($14.17 vs $4.00 requeridos) p... |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |

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
