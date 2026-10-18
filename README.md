# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 17:50:35`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$29.98 USD** | **$8.01 USD** | **$37.99 USD** | 🔴 **-5.01%** ($-2.01) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.079341 | $100.83 | $100.97 | $8.01 | 📈 +0.14% | 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado bursátil tradicional se encuentra cerrado por lo que la liquidez activa se concentra en criptomonedas. SOL-USD muestra un ligero repunte de corto plazo con un cambio positivo de 1h del 0.26% aunque su RSI diario permanece en niveles extremadamente deprimidos de 15.4, sugiriendo potencial de rebote por sobreventa extrema (mean reversion). ETH-USD también presenta un cambio positivo de 1h del 0.34% con RSI diario en 20.9."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD lleva poco tiempo abierta (49 minutos) y se mantiene en terreno ligeramente positivo (0.14%). El RSI diario está extremadamente bajo (15.4) y el cambio de 1h es positivo (0.26%), lo cual respalda mantener la tesis de rebote técnico sin necesidad de forzar ventas prematuras.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos la posición actual en SOL-USD monitoreando que el impulso alcista de 1 hora se consolide. Establecemos un objetivo de take-profit entre +2.0% y +3.5% (aproximadamente $103.35) y un stop-loss estricto a -2.0% ($98.81) para proteger el capital. Evaluaremos una entrada adicional en ETH-USD si su RSI de 1 hora rompe con mayor fuerza al alza y el cambio positivo se mantiene. El efectivo disponible se mantendrá a la espera de confirmación de momentum."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **72** | 🎯 **40.3%** (29W / 29L / 14BE) | 🔴 **$-1.88 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 17:00` | 🟢 BUY | `SOL-USD` | $8.00 | $100.83 | SOL-USD muestra un RSI diario extremadamente deprimido en 15.3 y un RSI de 1 hora en 23.4 ... |
| `2026-10-18 16:40` | 🔴 SELL (-0.19$) | `ETH-USD` | $9.81 | $2332.39 | ETH-USD registra una pérdida del -1.92% con un RSI de 1 hora en 18.5 que refleja debilidad... |
| `2026-10-18 16:40` | 🔴 SELL (-0.20$) | `SOL-USD` | $9.80 | $100.90 | La posición en SOL-USD lleva casi 6 horas abierta con una pérdida del -1.95% y un RSI de 1... |
| `2026-10-18 12:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2377.97 | ETH-USD presenta un RSI diario extremadamente bajo en 22.0 y un RSI de 1 hora saliendo de ... |
| `2026-10-18 11:01` | 🟢 BUY | `SOL-USD` | $10.00 | $102.91 | SOL-USD muestra un RSI diario extremadamente bajo (16.4) en zona de sobreventa profunda y ... |

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
