# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 07:20:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$11.96 USD** | **$39.49 USD** | 🔴 **-1.27%** ($-0.51) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83274.97 | $6.01 | 📈 +0.18% | 10h 19m |
| `SOL-USD` | 0.055840 | $107.45 | $106.63 | $5.95 | 📉 -0.76% | 8h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando de forma lateral con ligeros sesgos positivos de corto plazo, mientras que los mercados tradicionales permanecen cerrados. Las posiciones actuales en BTC y SOL muestran un comportamiento estancado sin alcanzar aún los objetivos de take-profit ni los stop-loss, operando con un PnL cercano al plano tras más de 8 a 10 horas de retención."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 65%): BTC-USD mantiene un rendimiento plano (+0.18%) tras más de 10 horas de holding. El RSI de 1 hora se sitúa en 48.2 y el diario en 49.0. No ha activado el stop-loss ni ha alcanzado el take-profit, por lo que se mantiene la posición esperando mayor momentum.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos BTC-USD y SOL-USD en este ciclo ya que se mantienen por encima de los límites estrictos de stop-loss del -2.0%. Si BTC-USD se acerca al objetivo de take-profit (+2%) o si SOL-USD rompe a la baja el soporte diario con un RSI debilitado, procederemos a rotar el capital hacia liquidez o nuevas oportunidades. La liquidez actual se mantendrá en reserva estricta para evitar sobreexposición en un mercado lateral."
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
