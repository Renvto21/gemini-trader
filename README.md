# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 00:00:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.09 USD** | **$38.38 USD** | 🔴 **-4.06%** ($-1.62) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.39 | $10.07 | 📈 +0.66% | 8h 59m |
| `ETH-USD` | 0.004144 | $2412.98 | $2418.38 | $10.02 | 📈 +0.22% | 7h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado durante el fin de semana, por lo que toda la actividad se concentra en las criptomonedas, que operan 24/7. Las criptomonedas principales (SOL-USD, ETH-USD, BTC-USD) muestran un comportamiento lateral con sesgo bajista de corto plazo, con RSI de 1 hora moderados y RSI diarios en zonas de sobreventa o cercanos a soportes clave. Nuestras posiciones abiertas en SOL y ETH se mantienen estables con ligeras ganancias (+0.66% y +0.22%), aún por debajo de la meta de take-profit de +2.0%, pero sin activar el stop-loss de -2.0%. Mantendremos las posiciones vigentes esperando un catalizador de volumen que impulse el rebote."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición acumula una ganancia moderada de +0.66% tras 8 horas de holding. El RSI de 1 hora se encuentra en 38.0 y el activo sigue en rango de consolidación sin amenazar el stop-loss. Esperamos que alcance el objetivo de take-profit entre +2.0% y +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de SOL-USD y ETH-USD activas buscando el take-profit en el rango de +2.0% a +3.5%. El stop-loss se mantiene rigurosamente en -2.0% para proteger el capital. Con una liquidez de 18.29 USD, conservaremos efectivo por encima de la reserva mínima de 4.00 USD y esperaremos una confirmación de aceleración alcista en el RSI de 1 hora por encima de 45 antes de desplegar nuevo capital en BTC o incrementar exposición."
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
