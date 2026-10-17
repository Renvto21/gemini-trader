# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 00:20:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.10 USD** | **$38.39 USD** | 🔴 **-4.03%** ($-1.61) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.44 | $10.07 | 📈 +0.70% | 9h 19m |
| `ETH-USD` | 0.004144 | $2412.98 | $2419.76 | $10.03 | 📈 +0.28% | 7h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas continúa operando en un sesgo bajista general pero con señales mixtas de sobreventa en gráficos diarios y de 1 hora. Los mercados tradicionales permanecen cerrados. Las posiciones actuales de SOL-USD y ETH-USD muestran ligeras ganancias pero se mantienen estancadas sin el volumen alcista necesario para alcanzar los objetivos de take-profit en este ciclo."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 60%): SOL-USD se mantiene en terreno positivo con una ganancia de +0.7% tras 9 horas abierto. Aunque el impulso es lento, el RSI de 1 hora se encuentra en 38.3 y la posición está lejos del stop-loss del -2.0%. Esperamos continuación alcista.
- **[HOLD] ETH-USD** (Confianza: 60%): ETH-USD registra una ganancia del +0.28% tras casi 8 horas abierto. Mantiene condiciones técnicas estables con un RSI diario de sobreventa y no ha roto ningún soporte crítico, por lo que se mantiene para buscar el objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de SOL-USD y ETH-USD por debajo del umbral de stop-loss del -2.0% y buscaremos un take-profit entre +2.0% y +3.5%. Si el RSI de 1 hora vuelve a caer o se debilita el impulso, rotaremos el capital hacia liquidez o BTC-USD en el próximo ciclo."
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
