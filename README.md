# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 03:30:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.22 USD** | **$38.27 USD** | 🔴 **-4.33%** ($-1.73) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81586.38 | $10.05 | 📈 +0.51% | 8h 29m |
| `SOL-USD` | 0.097418 | $102.65 | $103.40 | $10.07 | 📈 +0.73% | 8h 20m |
| `ETH-USD` | 0.004193 | $2385.05 | $2408.13 | $10.10 | 📈 +0.97% | 8h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene abierto 24/7 con los activos en cartera mostrando ligeras ganancias dentro del rango objetivo de rebote técnico. Las posiciones en BTC-USD, SOL-USD y ETH-USD registran retornos positivos de entre +0.51% y +0.97%, manteniendo un RSI de 1 hora moderado y saludable (cerca de 52-61), aunque aún sin alcanzar el umbral estricto de take-profit (+2.0% a +3.5%) o sobrecompra extrema (>70). Los mercados tradicionales permanecen cerrados. La liquidez actual se encuentra en $8.05 USD, cumpliendo parcialmente con la reserva mínima."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD muestra una ganancia actual de +0.51% con un RSI de 1H en 61.3. Se mantiene dentro de la tesis de rebote técnico a la espera de alcanzar el objetivo de take-profit (+2.0% a +3.5%).

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD durante este ciclo. Continuar monitoreando el RSI de 1 hora de cerca: si cualquiera de los activos alcanza el rango objetivo de ganancia de +2.0% a +3.5% o cruza a sobrecompra (>70), ejecutaré la venta inmediata para asegurar beneficios y rotar liquidez. Vigilar el stop-loss estricto a -2.0% para proteger el capital ante cualquier giro bajista repentino."
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
