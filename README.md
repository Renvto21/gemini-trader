# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 15:30:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.37 USD** | **$19.84 USD** | **$38.21 USD** | 🔴 **-4.48%** ($-1.79) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.097172 | $102.91 | $102.01 | $9.91 | 📉 -0.87% | 4h 29m |
| `ETH-USD` | 0.004205 | $2377.97 | $2359.66 | $9.92 | 📉 -0.77% | 3h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado por fin de semana, por lo que toda la actividad se concentra en las criptomonedas, que operan 24/7. Las principales criptomonedas (SOL, ETH y BTC) muestran tendencias bajistas de corto plazo bajo la SMA20, con RSI diarios deprimidos en zona de sobreventa profunda, lo que sugiere potenciales rebotes de reversión a la media (mean reversion) pero exigiendo un monitoreo cercano del stop-loss."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición en SOL-USD tiene un holding time de poco más de 4 horas y una pérdida moderada de -0.87%, manteniéndose muy por encima del stop-loss estricto de -2.0%. El RSI diario en sobreventa profunda (15.9) respalda mantener la posición a la espera del rebote.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD muestra un comportamiento similar, con una pérdida actual de -0.77% y un holding time menor a 4 horas. Dado que el mercado cripto está abierto y el RSI diario se ubica en 21.4, se le dará tiempo al precio para desarrollar el impulso de recuperación esperado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones de SOL-USD y ETH-USD por ahora, ya que el holding time es inferior a 5 horas y las caídas se mantienen dentro del margen de tolerancia antes de activar el stop-loss estricto de -2.0%. Estaremos atentos a que el RSI de 1 hora supere los niveles de 50-70 o que la rentabilidad alcance el rango de +2.0% a +3.5% para tomar beneficios. Si el precio rompe a la baja superando el -2.0%, ejecutaremos la venta inmediata para proteger el capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **70** | 🎯 **41.4%** (29W / 27L / 14BE) | 🔴 **$-1.49 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 12:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2377.97 | ETH-USD presenta un RSI diario extremadamente bajo en 22.0 y un RSI de 1 hora saliendo de ... |
| `2026-10-18 11:01` | 🟢 BUY | `SOL-USD` | $10.00 | $102.91 | SOL-USD muestra un RSI diario extremadamente bajo (16.4) en zona de sobreventa profunda y ... |
| `2026-10-18 08:00` | 🔴 SELL (+0.13$) | `ETH-USD` | $10.13 | $2415.11 | ETH-USD registra un RSI de 1H en 72.1 (sobrecompra) y una ganancia de +1.26%. Se procede a... |
| `2026-10-18 08:00` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $103.84 | SOL-USD presenta un RSI de 1H en 67.6 acercándose a zona de sobrecompra con una ganancia d... |
| `2026-10-18 08:00` | 🔴 SELL (+0.10$) | `BTC-USD` | $10.08 | $81974.15 | BTC-USD ha alcanzado un RSI de 1H en 78.8 (sobrecompra profunda) tras el rebote esperado, ... |

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
