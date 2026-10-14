# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 09:50:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$11.88 USD** | **$39.41 USD** | 🔴 **-1.48%** ($-0.59) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $82812.37 | $5.98 | 📉 -0.38% | 12h 49m |
| `SOL-USD` | 0.055840 | $107.45 | $105.74 | $5.90 | 📉 -1.59% | 10h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto muestra un sesgo bajista moderado en el corto plazo con los principales activos (BTC-USD, SOL-USD y ETH-USD) cotizando por debajo de sus medias móviles de 20 periodos. Los mercados tradicionales se encuentran cerrados, por lo que toda la atención táctica se centra en la gestión de las posiciones actuales de criptomonedas y la protección del capital disponible."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 60%): BTC-USD registra una pérdida menor del -0.38% tras casi 13 horas de holding. Aunque el RSI de 1H se sitúa en 38.1 y la tendencia es bajista, aún no se alcanza el umbral de stop-loss estricto del -2.0%, por lo que se mantiene la posición esperando un rebote técnico.
- **[HOLD] SOL-USD** (Confianza: 60%): SOL-USD presenta una pérdida de -1.59% con un RSI diario en sobreventa extrema (26.4). Nos encontramos cerca del límite de protección de -2.0%, pero el contexto diario sugiere que podría consolidar un suelo próximamente. Mantendremos la vigilancia estricta.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones abiertas de BTC-USD y SOL-USD vigilando de cerca el nivel de stop-loss del -2.0%. El holding time ya supera las 10 horas y el momentum es débil, por lo que si las pérdidas se acercan al límite crítico o el RSI de 1H cae por debajo de 35 sin signos de reacción, procederemos a liquidar de inmediato para preservar efectivo y buscar nuevas oportunidades de rotación."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **49** | 🎯 **44.9%** (22W / 13L / 14BE) | 🔴 **$-0.39 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |

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
