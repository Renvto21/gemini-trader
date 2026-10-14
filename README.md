# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 02:31:02`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.54 USD** | **$17.02 USD** | **$39.56 USD** | 🔴 **-1.10%** ($-0.44) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2506.14 | $5.00 | 📉 -0.09% | 9h 20m |
| `BTC-USD` | 0.000072 | $83128.62 | $83533.15 | $6.03 | 📈 +0.49% | 5h 30m |
| `SOL-USD` | 0.055840 | $107.45 | $107.37 | $6.00 | 📉 -0.07% | 3h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "Los mercados tradicionales se encuentran cerrados, por lo que toda la actividad se concentra en el mercado de criptomonedas (24/7). Las criptomonedas principales (BTC, ETH, SOL) muestran consolidación tras leves repuntes de 24 horas, con BTC manteniendo un rendimiento positivo leve (+0.49%) mientras que ETH y SOL se encuentran planos o ligeramente negativos (-0.09% y -0.07% respectivamente). El impulso alcista de corto plazo se ha ralentizado, pero mantenemos una postura disciplinada esperando señales de sobrecompra para tomar beneficios o rotación si el momentum decae."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 70%): BTC-USD mantiene un leve rendimiento positivo (+0.49%) y un RSI de 1H en 54.8. No ha alcanzado el objetivo de take-profit (+2.0% a +3.5%) ni muestra signos de sobrecompra extrema, por lo que mantenemos la posición para dejar correr el beneficio.
- **[HOLD] ETH-USD** (Confianza: 60%): ETH-USD se encuentra plano (-0.09%) operando con un holding time de más de 9 horas. Aunque el momentum es débil, no ha tocado el stop-loss del -2.0%, por lo que se mantiene a la espera de un rebote o catalizador antes de decidir su rotación.
- **[HOLD] SOL-USD** (Confianza: 60%): SOL-USD registra una variación mínima de -0.07% con un RSI diario en sobreventa extrema (28.1). El rebote técnico aún no se materializa con fuerza, pero mantenemos la posición respaldada por la expectativa de reversión a la media en el mediano plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca las posiciones abiertas en BTC-USD, ETH-USD y SOL-USD. BTC muestra una ganancia marginal pero estable; ETH y SOL llevan varias horas sin generar momentum fuerte. El objetivo sigue siendo capturar un take-profit entre +2.0% y +3.5%, o salida táctica si el RSI 1H supera 70. Mantener la disciplina en el stop-loss en -2.0% y conservar la reserva de efectivo mínima de $4.00 USD."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **48** | 🎯 **45.8%** (22W / 12L / 14BE) | 🔴 **$-0.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |

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
