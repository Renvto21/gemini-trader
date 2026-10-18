# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 07:10:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.37 USD** | **$38.42 USD** | 🔴 **-3.95%** ($-1.58) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $82054.24 | $10.11 | 📈 +1.09% | 12h 9m |
| `SOL-USD` | 0.097418 | $102.65 | $103.87 | $10.12 | 📈 +1.19% | 11h 59m |
| `ETH-USD` | 0.004193 | $2385.05 | $2419.97 | $10.15 | 📈 +1.46% | 11h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con un tono de recuperación moderada, mientras que los mercados tradicionales permanecen cerrados. Nuestras posiciones en criptomonedas (BTC-USD, SOL-USD y ETH-USD) se encuentran en zona de ganancias moderadas (entre +1.09% y +1.46%), aproximándose progresivamente a nuestra zona de objetivo de take-profit sin alcanzar aún el umbral estricto del +2.0% o un RSI de 1H superior a 70. La liquidez actual se encuentra en $8.05 USD, lo cual cubre adecuadamente los mínimos requeridos."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición muestra una ganancia actual de +1.09% con un RSI de 1H en 62.6. Aunque avanza positivamente, todavía no alcanza el rango objetivo de take-profit (+2.0% a +3.5%) ni cruza el umbral de sobrecompra de 70. Se mantiene operando para dejar correr el beneficio.
- **[HOLD] SOL-USD** (Confianza: 80%): La posición registra un rendimiento positivo de +1.19% y un RSI de 1H en 48.7. El rebote técnico sigue su curso de manera saludable, por lo que mantenemos la posición esperando mayor aceleración hacia el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH-USD lidera las ganancias actuales con un +1.46% y un RSI de 1H en 50.6. Está cerca de la zona de toma parcial de beneficios, por lo que se prefiere mantener la exposición activa para capturar el impulso alcista antes de ejecutar una venta.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD mientras sigan consolidando su rebote técnico y no toquen la zona de take-profit (+2.0% a +3.5%) o se acerquen al stop-loss (-2.0%). Monitorear de cerca los indicadores de RSI de 1H para asegurar beneficios en cuanto crucen el umbral de sobrecompra o alcancen la rentabilidad deseada. Conservar la liquidez disponible para futuras oportunidades."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **67** | 🎯 **38.8%** (26W / 27L / 14BE) | 🔴 **$-1.84 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 19:10` | 🟢 BUY | `ETH-USD` | $10.00 | $2385.05 | ETH-USD muestra un RSI de 1H en 29.0 (sobreventa profunda) combinado con un cambio de 1h p... |
| `2026-10-17 19:10` | 🟢 BUY | `SOL-USD` | $10.00 | $102.65 | SOL-USD presenta un RSI de 1H en 31.5 saliendo de zona de sobreventa estricta y un cambio ... |
| `2026-10-17 19:00` | 🟢 BUY | `BTC-USD` | $10.00 | $81170.65 | BTC-USD muestra un RSI de 1H saliendo de niveles bajos (37.5) con un cambio positivo de 0.... |
| `2026-10-17 18:40` | 🔴 SELL (-0.22$) | `ETH-USD` | $9.78 | $2370.09 | La posición acumula una pérdida de -2.21%, excediendo el umbral de stop-loss del -2.0%. El... |
| `2026-10-17 18:40` | 🔴 SELL (-0.21$) | `SOL-USD` | $9.79 | $101.78 | La posición ha alcanzado una pérdida de -2.08%, rompiendo el límite de stop-loss estricto ... |

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
