# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 21:40:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.08 USD** | **$38.37 USD** | 🔴 **-4.07%** ($-1.63) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.28 | $10.05 | 📈 +0.55% | 6h 39m |
| `ETH-USD` | 0.004144 | $2412.98 | $2419.97 | $10.03 | 📈 +0.29% | 5h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado bursátil tradicional se encuentra cerrado, por lo que toda la actividad se concentra exclusivamente en las criptomonedas (ABIERTO 24/7). Las criptos principales como SOL-USD y ETH-USD muestran un momentum débil y lateralizado en el corto plazo, con RSI de 1 hora volviendo a presionar la zona baja (29.4 y 30.1 respectivamente) tras haber tenido un avance leve. El portafolio mantiene ambas posiciones con ligeras ganancias (+0.55% y +0.29%), aún lejos del objetivo de take-profit (+2.0% a +3.5%) y sin alcanzar los umbrales de stop-loss. Mantenemos la liquidez en efectivo para buscar oportunidades si se presenta un repunte de volumen."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición en SOL-USD acumula una ganancia moderada de +0.55% tras más de 6 horas abierta. Aunque el RSI de 1h ha descendido a 29.4, el precio se mantiene estable y no ha tocado nuestro stop-loss del -2.0% ni el objetivo de take-profit. Esperamos mayor claridad de impulso para decidir una toma de ganancias o rotación.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD muestra un comportamiento similar, con una ganancia actual del +0.29% y un holding time de más de 5 horas. El RSI de 1h en 30.1 y el RSI diario en 30.6 sugieren soporte macro cercano. Mantenemos la posición para buscar el objetivo de take-profit entre +2.0% y +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en SOL-USD y ETH-USD supervisando de cerca la evolución del RSI de 1 hora para asegurar ganancias si se roza el rango de +2.0% a +3.5%, o recortar si rompen soportes a la baja (-2.0%). Conservar la liquidez actual de 18.29 USD para entradas rápidas en cuanto el mercado cripto presente un catalizador de aceleración alcista más claro."
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
