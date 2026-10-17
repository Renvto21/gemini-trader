# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 23:00:53`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.06 USD** | **$38.35 USD** | 🔴 **-4.13%** ($-1.65) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.18 | $10.05 | 📈 +0.45% | 7h 59m |
| `ETH-USD` | 0.004144 | $2412.98 | $2416.49 | $10.01 | 📈 +0.15% | 6h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado y congelado, mientras que las criptomonedas operan 24/7 en una fase de consolidación y ligera presión bajista macro. SOL-USD y ETH-USD muestran un momentum estancado de corto plazo con RSI de 1 hora en niveles bajos (35.9 y 24.0 respectivamente), pero se mantienen dentro de la zona de control de riesgo sin activar los stop-loss. Mantenemos las posiciones vigentes a la espera de un repunte en volumen que impulse los precios hacia el rango objetivo de take-profit del +2.0% al +3.5%."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición mantiene un PnL positivo del 0.45% tras casi 8 horas abiertas. Aunque el momentum de corto plazo es lento, el activo sigue respetando la estructura de soporte y se encuentra lejos del stop-loss, por lo que se mantiene para buscar el take-profit.
- **[HOLD] ETH-USD** (Confianza: 65%): ETH-USD muestra un RSI de 1 hora muy deprimido en 24.0, pero se mantiene en terreno neutral de PnL (+0.15%). Esperaremos un ciclo más para evaluar si el rebote técnico desde la sobreventa diaria se materializa antes de tomar la decisión de rotar el capital.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca a SOL-USD y ETH-USD en las próximas horas. Si ETH-USD no logra recuperar el RSI de 1 hora por encima de 30 y continúa deprimido, consideraremos la rotación parcial del capital. Mantener la disciplina con el stop-loss estricto a -2.0% y buscar la toma de ganancias si se alcanza el objetivo de +2.0% a +3.5%."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **63** | 🎯 **38.1%** (24W / 25L / 14BE) | 🔴 **$-1.60 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 16:30` | 🟢 BUY | `ETH-USD` | $10.00 | $2412.98 | ETH-USD muestra un RSI diario en niveles de sobreventa extrema (30.3) y un cambio positivo... |
| `2026-10-16 16:30` | 🔴 SELL (-0.11$) | `MSFT` | $6.39 | $526.18 | MSFT lleva más de 1 día y 5 horas abierto mostrando debilidad persistente y un rendimiento... |
| `2026-10-16 15:01` | 🟢 BUY | `SOL-USD` | $10.00 | $103.71 | SOL-USD presenta un RSI de 1 hora en 34.3 saliendo de la zona de sobreventa extrema, acomp... |
| `2026-10-16 14:30` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2399.90 | ETH-USD ha rebasado el umbral estricto de stop-loss (-2.12%), operando en tendencia bajist... |
| `2026-10-16 13:40` | 🔴 SELL (-0.02$) | `NVDA` | $7.98 | $216.80 | NVDA lleva más de 24 horas abierto operando bajo la SMA20 con un momentum débil, acumula u... |

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
