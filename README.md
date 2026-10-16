# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 17:10:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$19.98 USD** | **$38.27 USD** | 🔴 **-4.34%** ($-1.73) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $103.56 | $9.99 | 📉 -0.14% | 2h 9m |
| `ETH-USD` | 0.004144 | $2412.98 | $2411.02 | $9.99 | 📉 -0.08% | 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se encuentra operando 24/7 con una tendencia bajista generalizada pero mostrando señales iniciales de estabilización de corto plazo. SOL-USD y ETH-USD mantienen un comportamiento lateral con ligeros intentos de recuperación en su RSI de 1 hora, encontrándose cerca de zonas de sobreventa extrema en marcos diarios. Los mercados tradicionales permanecen cerrados, por lo que toda la atención táctica se concentra en la gestión de las posiciones actuales de criptoactivos."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD lleva poco tiempo abierta (-0.14% PnL) y muestra un intento de rebote en el RSI de 1h (29.5) con cambio positivo de 0.15% en la última hora. Mantendremos la posición en busca de la zona de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD se encuentra estable con una pérdida marginal de -0.08%, con un RSI diario profundamente deprimido en 30.2, lo que sugiere un potencial rebote técnico iminente que justifica retener la posición.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré las posiciones actuales de SOL-USD y ETH-USD supervisando de cerca los niveles de stop-loss estricto en -2.0% y buscando zonas de take-profit entre +2.0% y +3.5%. La liquidez actual se mantendrá en reserva a la espera de una ruptura de volumen más clara en BTC-USD o un impulso alcista consolidado en SOL-USD."
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
