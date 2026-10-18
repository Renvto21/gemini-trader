# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 14:50:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.37 USD** | **$19.85 USD** | **$38.22 USD** | 🔴 **-4.46%** ($-1.78) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.097172 | $102.91 | $101.85 | $9.90 | 📉 -1.03% | 3h 49m |
| `ETH-USD` | 0.004205 | $2377.97 | $2365.96 | $9.95 | 📉 -0.51% | 2h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se mantiene bajo presión bajista, con los principales índices de Wall Street cerrados. Las criptomonedas operan 24/7 y muestran lecturas extremas de sobreventa en gráficos diarios y de 1 hora. SOL-USD y ETH-USD se encuentran en posiciones abiertas con ligeras pérdidas (-1.03% y -0.51% respectivamente), manteniendo un comportamiento lateral sin un rebote decisivo aún."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD registra un RSI diario extremadamente bajo (15.8) y una pérdida actual contenida de -1.03%. Mantenemos la posición a la espera de que el momentum intradiario rompa al alza para capturar el rebote.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un RSI diario en 21.6 y una pérdida menor de -0.51%. El precio se mantiene estable y esperamos confirmación de volumen y un giro positivo en el RSI de 1 hora para buscar la toma de ganancias.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones de SOL-USD y ETH-USD durante este ciclo para permitir que madure el rebote técnico desde niveles extremos de sobreventa. Monitorearemos de cerca que el RSI de 1 hora cruce al alza y el cambio de 1h se mantenga positivo para asegurar beneficios entre +2.0% y +3.5%. Stop-loss estricto en -2.0% para ambas posiciones. No realizaremos nuevas entradas por ahora para proteger el remanente de liquidez de $18.37 USD."
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
