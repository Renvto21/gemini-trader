# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 15:41:05`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$21.90 USD** | **$16.40 USD** | **$38.30 USD** | 🔴 **-4.25%** ($-1.70) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $526.48 | $6.39 | 📉 -1.62% | 1d 4h |
| `SOL-USD` | 0.096423 | $103.71 | $103.81 | $10.01 | 📈 +0.10% | 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo defensivo y bajista generalizado en la mayoría de los activos (bajo sus respectivas SMA20), con indicadores RSI de 1 hora en niveles bajos o de rebote potencial. MSFT se mantiene cerca de su soporte con un RSI de 1 hora en 34, mientras que los criptoactivos como SOL-USD muestran ligeros intentos de recuperación en el corto plazo tras caídas previas."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra abierto 24/7 con un RSI de 1h en 35.4 y un ligero cambio positivo de 0.24% en la última hora, cumpliendo la tesis de rebote técnico desde niveles de sobreventa recientes. Mantengo la posición buscando el take-profit.
- **[HOLD] MSFT** (Confianza: 70%): MSFT está operando abierto con un RSI de 1h en 34.0, manteniendo una tendencia macro alcista sobre la SMA20 a pesar de la corrección de 24 horas. Aunque lleva más de 24 horas en cartera, el PnL de -1.62% aún respeta el margen de stop-loss antes de un posible rebote.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré abierta la posición en SOL-USD evaluando su consolidación y buscando el objetivo de take-profit en +2.5%, con un stop-loss estricto en -2.0%. En MSFT, monitorearé la duración del holding (> 1 día) y su PnL cercano a -1.62%; si no logra romper al alza y se acerca al límite de pérdida, ejecutaré la venta para rotar el capital. Mantendré la reserva de liquidez y vigilaré posibles entradas en activos con mayor momentum."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **62** | 🎯 **38.7%** (24W / 24L / 14BE) | 🔴 **$-1.49 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 15:01` | 🟢 BUY | `SOL-USD` | $10.00 | $103.71 | SOL-USD presenta un RSI de 1 hora en 34.3 saliendo de la zona de sobreventa extrema, acomp... |
| `2026-10-16 14:30` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2399.90 | ETH-USD ha rebasado el umbral estricto de stop-loss (-2.12%), operando en tendencia bajist... |
| `2026-10-16 13:40` | 🔴 SELL (-0.02$) | `NVDA` | $7.98 | $216.80 | NVDA lleva más de 24 horas abierto operando bajo la SMA20 con un momentum débil, acumula u... |
| `2026-10-16 12:50` | 🔴 SELL (-0.06$) | `SOL-USD` | $2.94 | $104.34 | SOL-USD lleva varias horas abierto sin generar el rebote esperado, acumulando una pérdida ... |
| `2026-10-16 10:50` | 🔴 SELL (-0.04$) | `QQQ` | $9.95 | $721.83 | QQQ lleva más de 22 horas abierto operando bajo la SMA20 con un RSI de 1 hora en 30.2 y un... |

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
