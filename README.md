# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 15:30:53`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$21.90 USD** | **$16.40 USD** | **$38.30 USD** | 🔴 **-4.26%** ($-1.70) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $526.49 | $6.39 | 📉 -1.62% | 1d 4h |
| `SOL-USD` | 0.096423 | $103.71 | $103.74 | $10.00 | 📈 +0.03% | 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se encuentra bajo presión bajista con la mayoría de los activos cotizando por debajo de la SMA20. Sin embargo, en el segmento cripto observamos indicios tempranos de estabilización y rebotes técnicos en marcos de 1 hora, destacando SOL-USD que mantiene una estructura de acumulación reciente. En cuanto a las acciones tradicionales como MSFT, el activo muestra una pérdida leve acumulada pero mantiene su tendencia alcista macro en gráfico diario, por lo que mantendremos la vigilancia sobre sus soportes operativos."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD fue adquirido recientemente basándose en un RSI de 1 hora saliendo de sobreventa y mantiene un comportamiento lateral estable con un PnL neutral. Continuamos esperando el desarrollo del rebote técnico esperado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré la posición abierta en SOL-USD buscando consolidar el rebote técnico hacia la zona de take-profit (+2.5%), operando con un stop-loss estricto de -2.0%. En MSFT, supervisaré el comportamiento del holding actual de 1d 4h para asegurar la toma de ganancias si se acerca al +2.0% o aplicar corte de pérdidas si rompe el soporte del -2.0%. Mantendré liquidez disponible para futuras entradas en criptomonedas o tecnología si el impulso mejora."
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
