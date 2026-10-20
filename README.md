# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 06:10:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.43 USD** | **$38.43 USD** | 🔴 **-3.93%** ($-1.57) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 19h 30m |
| `ETH-USD` | 0.004178 | $2393.62 | $2379.34 | $9.94 | 📉 -0.60% | 17h 19m |
| `SOL-USD` | 0.096034 | $104.13 | $103.88 | $9.98 | 📉 -0.24% | 13h 30m |
| `BTC-USD` | 0.000105 | $81767.70 | $81330.31 | $8.52 | 📉 -0.53% | 13h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene operando 24/7 con un sesgo ligeramente bajista y consolidando tras las caídas recientes, mientras que los mercados tradicionales permanecen cerrados. Las posiciones actuales en cripto (ETH-USD, SOL-USD, BTC-USD) y el ETF QQQ registran ligeras pérdidas no realizadas inferiores al 1%, manteniéndose estables dentro de un rango operativo normal sin activar los stops de emergencia. El RSI de 1 hora se sitúa en niveles neutrales para la mayoría de los activos, por lo que la prioridad es mantener las posiciones actuales a la espera de un catalizador de volumen que impulse el rebote técnico hacia la zona de take-profit."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición se mantiene abierta con una pérdida marginal de -0.24%. A pesar de un holding time de más de 13 horas, el RSI diario se mantiene en zona de sobrecompra profunda (21.0), lo que sugiere que el potencial alcista de reversión sigue intacto a la espera de un impulso en el mercado cripto.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear la evolución de las posiciones abiertas (ETH-USD, SOL-USD, BTC-USD y QQQ). Mantener la disciplina operativa permitiendo que los activos desarrollen su rebote técnico hacia el objetivo de +2.5% o salida por take-profit al alcanzar RSI de 1 hora > 70. Vigilar estrictamente que ninguna posición cruce el límite de pérdida de -2.0%. Dado que el efectivo disponible es de $0.00, no se realizarán nuevas compras hasta asegurar ganancias o realizar rotación de capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 23:00` | 🟢 BUY | `BTC-USD` | $4.00 | $81646.39 | BTC-USD presenta un RSI de 1 hora en 27.7, nivel de sobreventa profunda ideal para un rebo... |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |

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
