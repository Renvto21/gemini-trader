# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 15:20:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$21.90 USD** | **$16.39 USD** | **$38.29 USD** | 🔴 **-4.28%** ($-1.71) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $526.72 | $6.40 | 📉 -1.58% | 1d 4h |
| `SOL-USD` | 0.096423 | $103.71 | $103.64 | $9.99 | 📉 -0.07% | 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra mayoritariamente bajista bajo la SMA20, con una presión vendedora que ha afectado tanto a los índices tradicionales como a las criptomonedas principales. Sin embargo, observamos niveles de RSI de 1 hora comprimidos y cercanos o inferiores a 35 en varios activos clave, lo que abre oportunidades tácticas puntuales para buscar rebotes técnicos por sobreventa."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 60%): MSFT mantiene una tendencia alcista macro sobre la SMA20 y un RSI de 1 hora en 34.6 saliendo de niveles bajos. Aunque acumula una leve pérdida del -1.58%, se mantiene dentro del margen operativo antes del stop-loss del -2.0%, por lo que vale la pena sostenerla buscando el objetivo de take-profit.
- **[HOLD] SOL-USD** (Confianza: 65%): La posición en SOL-USD fue abierta recientemente y se encuentra estable con una pérdida marginal del -0.07%. El RSI de 1 hora en 33.4 indica que la presión vendedora se desacelera, manteniendo viva la expectativa del rebote táctico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantengo la posición en MSFT vigilando el soporte y buscando el take-profit en +2.0%, pero aplicaré un stop-loss estricto si rompe el -2.0%. En cuanto a SOL-USD, el rebote muestra un comportamiento lateral leve y mantendremos la vigilancia estricta con un stop-loss del -2.0% y take-profit del +2.5%. Mantendré la liquidez actual para evaluar entradas adicionales si el momentum se consolida o rotar capital si alguna posición se estanca."
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
