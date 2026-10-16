# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 14:50:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.90 USD** | **$6.40 USD** | **$38.30 USD** | 🔴 **-4.25%** ($-1.70) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $527.28 | $6.40 | 📉 -1.47% | 1d 3h |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo bajista general con la mayoría de los activos operando bajo sus medias móviles diarias (SMA20). Sin embargo, el RSI de 1 hora en varios activos se encuentra en niveles cercanos o inferiores a 35, lo que sugiere oportunidades inminentes de rebote por reversión a la media (mean reversion). MSFT se mantiene en cartera mostrando un pequeño retroceso (-1.47%) tras un holding de 1 día y 3 horas, pero mantiene una tendencia diaria alcista sólida sobre la SMA20. Mantengo el capital disponible en efectivo para buscar entradas de alta convicción en cripto o tecnología si se confirma el giro de momentum."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 75%): MSFT se mantiene en cartera con una pérdida actual de -1.47%, la cual está lejos de activar el stop-loss estricto de -2.0%. Dado que su tendencia diaria es alcista (sobre la SMA20) y muestra un pequeño repunte en el cambio de 1h (+0.29%), mantengo la posición esperando el rebote hacia el objetivo de take-profit sin forzar ventas prematuras.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantengo la posición en MSFT vigilando el soporte y esperando una extensión del rebote hacia la zona de take-profit (+2%). Si MSFT rompe a la baja el stop-loss estricto de -2%, procederé a vender inmediatamente para cortar pérdidas. Con el efectivo disponible ($31.9 USD), mantendré la liquidez esperando activamente un cruce alcista en el RSI de 1 hora de activos como NVDA o BTC-USD para desplegar capital en el próximo ciclo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **62** | 🎯 **38.7%** (24W / 24L / 14BE) | 🔴 **$-1.49 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 14:30` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2399.90 | ETH-USD ha rebasado el umbral estricto de stop-loss (-2.12%), operando en tendencia bajist... |
| `2026-10-16 13:40` | 🔴 SELL (-0.02$) | `NVDA` | $7.98 | $216.80 | NVDA lleva más de 24 horas abierto operando bajo la SMA20 con un momentum débil, acumula u... |
| `2026-10-16 12:50` | 🔴 SELL (-0.06$) | `SOL-USD` | $2.94 | $104.34 | SOL-USD lleva varias horas abierto sin generar el rebote esperado, acumulando una pérdida ... |
| `2026-10-16 10:50` | 🔴 SELL (-0.04$) | `QQQ` | $9.95 | $721.83 | QQQ lleva más de 22 horas abierto operando bajo la SMA20 con un RSI de 1 hora en 30.2 y un... |
| `2026-10-16 05:10` | 🟢 BUY | `SOL-USD` | $3.00 | $106.33 | SOL-USD presenta un RSI diario en zona de sobreventa extrema (29.0) y un cambio positivo e... |

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
