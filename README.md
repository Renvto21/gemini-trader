# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 22:10:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.07 USD** | **$38.36 USD** | 🔴 **-4.10%** ($-1.64) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.24 | $10.05 | 📈 +0.51% | 7h 9m |
| `ETH-USD` | 0.004144 | $2412.98 | $2418.28 | $10.02 | 📈 +0.22% | 5h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional se encuentra cerrado, por lo que toda la actividad se concentra en el sector cripto. Las criptomonedas principales (BTC-USD, ETH-USD y SOL-USD) muestran un sesgo bajista y RSI de 1 hora deprimidos, aunque estables cerca de soportes. Nuestras posiciones actuales en SOL-USD y ETH-USD se mantienen con ligeras ganancias pero sin el momentum alcista rápido esperado, por lo que decidimos mantenerlas vigilando de cerca los niveles de soporte."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición en SOL-USD se mantiene en terreno ligeramente positivo (+0.51%). El RSI de 1 hora está en 30.3 y aunque el momentum es lento, se mantiene firme por encima del precio de entrada. Esperaremos la consolidación del rebote para buscar la salida con beneficio.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD muestra un pequeño beneficio (+0.22%) con un RSI diario de 30.5 en zona de soporte clave. Mantenemos la posición para capturar el rebote técnico hacia la zona del objetivo de ganancia preestablecida.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones en SOL-USD y ETH-USD esperando un impulso alcista que nos permita alcanzar el objetivo de take-profit entre +2.0% y +3.5%. Conservar los 18.29 USD de efectivo para desplegarlos si BTC-USD o ETH-USD rompen con fuerza al alza o si se presenta una oportunidad clara de rebote. Si las posiciones actuales rompen soporte a la baja o caen por debajo de -1.5%, recortaremos para proteger capital."
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
