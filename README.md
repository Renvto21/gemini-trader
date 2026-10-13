# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 18:04:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.68 USD** | **$34.91 USD** | **$39.59 USD** | 🔴 **-1.02%** ($-0.41) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.279466 | $107.20 | $107.03 | $29.91 | 📉 -0.16% | 4h 3m |
| `ETH-USD` | 0.001993 | $2508.37 | $2507.56 | $5.00 | 📉 -0.03% | 53m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional se encuentra cerrado, por lo que toda la actividad se concentra en los criptoactivos 24/7. Tanto SOL-USD como ETH-USD muestran consolidación lateral tras los rebotes recientes, con un RSI de 1 hora estabilizado alrededor de 38 y cambios de 24 horas positivos pero sin una fuerte aceleración alcista en el último tramo. La liquidez en efectivo es mínima ($4.68 USD) cumpliendo con la regla de mantener solo lo necesario."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición lleva más de 4 horas abierta con un rendimiento plano (-0.16%). Se mantiene a la espera de un mayor impulso alcista que acerque el precio al objetivo de take-profit sin romper el stop-loss de -2.0%.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra estabilidad con un cambio positivo de 24h del 2.59% y un PnL casi neutro (-0.03%). Se retiene para permitir que el rebote técnico continúe madurando.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en SOL-USD y ETH-USD durante este ciclo ya que se encuentran con pérdidas mínimas y operando de manera estable. Monitorear de cerca los objetivos de take-profit entre +2.0% y +3.5% o cruce de RSI de 1 hora por encima de 70. Activar stop-loss estricto si alguna posición cae más de -2.0%. Si el momentum continúa lateral, rotar capital en el siguiente ciclo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **47** | 🎯 **46.8%** (22W / 11L / 14BE) | 🔴 **$-0.28 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |
| `2026-10-13 16:30` | 🟢 BUY | `ETH-USD` | $9.68 | $2507.92 | ETH-USD muestra un RSI de 35.8 en zona de fuerte sobreventa y un impulso alcista diario de... |
| `2026-10-13 16:30` | 🔴 SELL | `SOL-USD` | $9.69 | $107.65 | Realizamos una toma parcial de beneficios y rotación de capital liberando aproximadamente ... |
| `2026-10-13 14:01` | 🟢 BUY | `SOL-USD` | $7.97 | $107.29 | SOL-USD presenta una condición de sobreventa extrema con un RSI de 27.9 y un desplome sema... |

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
