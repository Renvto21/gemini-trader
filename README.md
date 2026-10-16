# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 13:31:00`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$17.07 USD** | **$21.39 USD** | **$38.46 USD** | 🔴 **-3.85%** ($-1.54) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $529.01 | $6.43 | 📉 -1.15% | 1d 2h |
| `NVDA` | 0.036812 | $217.32 | $217.42 | $8.00 | 📈 +0.05% | 1d 0h |
| `ETH-USD` | 0.002855 | $2451.90 | $2439.89 | $6.97 | 📉 -0.49% | 9h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo bajista general con la mayoría de los activos operando bajo sus medias móviles de 20 períodos, aunque Wall Street se encuentra abierto permitiendo la gestión de acciones y criptoactivos 24/7. Las posiciones actuales se mantienen en rangos estables con ligeras pérdidas pero sin alcanzar los umbrales de stop-loss estricto, mientras que el efectivo se preserva adecuadamente."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 70%): MSFT se mantiene con una pérdida moderada de -1.15% dentro de un canal alcista a nivel diario. No ha roto el stop-loss estricto del -2.0% y su RSI de 1 hora está en 35.8, por lo que es prudente mantener y esperar un rebote.
- **[HOLD] NVDA** (Confianza: 70%): NVDA se encuentra prácticamente en equilibrio (0.05%) tras un día de tenencia. Aunque su tendencia es bajista a corto plazo, el RSI de 1 hora en 34.9 sugiere estabilización. Mantendremos la posición vigilando posibles take-profits o recortes.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un cambio de 1 hora positivo (+0.48%) y un RSI diario en zona de soporte (31.6). La pérdida actual es marginal (-0.49%) y se espera que continúe el intento de rebote técnico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas actuales (MSFT, NVDA, ETH-USD) vigilando de cerca sus soportes. Si MSFT o NVDA profundizan pérdidas acercándose al -2.0% o si ETH-USD pierde fuerza en su rebote, ejecutaré ventas para proteger el capital. Monitorearé el comportamiento de cripto y tech en busca de rupturas con alto volumen para desplegar la liquidez disponible."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **60** | 🎯 **40.0%** (24W / 22L / 14BE) | 🔴 **$-1.32 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 12:50` | 🔴 SELL (-0.06$) | `SOL-USD` | $2.94 | $104.34 | SOL-USD lleva varias horas abierto sin generar el rebote esperado, acumulando una pérdida ... |
| `2026-10-16 10:50` | 🔴 SELL (-0.04$) | `QQQ` | $9.95 | $721.83 | QQQ lleva más de 22 horas abierto operando bajo la SMA20 con un RSI de 1 hora en 30.2 y un... |
| `2026-10-16 05:10` | 🟢 BUY | `SOL-USD` | $3.00 | $106.33 | SOL-USD presenta un RSI diario en zona de sobreventa extrema (29.0) y un cambio positivo e... |
| `2026-10-16 04:30` | 🟢 BUY | `ETH-USD` | $7.00 | $2451.90 | Aprovechamos la liquidez disponible sobre la reserva mínima ($14.17 vs $4.00 requeridos) p... |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |

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
