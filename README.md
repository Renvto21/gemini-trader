# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 23:11:19`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.54 USD** | **$17.00 USD** | **$39.54 USD** | 🔴 **-1.14%** ($-0.46) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2505.09 | $4.99 | 📉 -0.13% | 6h 0m |
| `BTC-USD` | 0.000072 | $83128.62 | $83277.57 | $6.01 | 📈 +0.18% | 2h 10m |
| `SOL-USD` | 0.055840 | $107.45 | $107.45 | $6.00 | 📈 +0.00% | 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional (Wall Street) se encuentra cerrado y sus precios congelados, por lo que el foco operativo se concentra exclusivamente en las criptomonedas (24/7). BTC-USD y ETH-USD muestran estabilidad con pequeños rebotes en el último cambio de hora, mientras que SOL-USD muestra un RSI diario muy deprimido (28.3) y un rebote horario interesante (rsi_1h 55.9, cambio positivo), lo que lo convierte en un excelente candidato para reincorporarlo a la cartera y cazar el rebote técnico."

**Operaciones del ciclo:**
- **[BUY] SOL-USD** (Confianza: 85%): SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido cambio positivo en 1 hora con un RSI de 55.9, indicando un rebote técnico activo tras la rotación previa. Se asignan $6.00 USD para aprovechar esta oportunidad de alta convicción.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en ETH-USD y BTC-USD mientras persistan dentro del rango de tolerancia y no alcancen el take-profit entre +2.0% y +3.5% o el stop-loss de -2.0%. Aprovechar la liquidez disponible para reentrar en SOL-USD capturando su sobreventa diaria y momentum horario actual. Monitorear de cerca los niveles de RSI de 1 hora para asegurar beneficios con rapidez si se acercan a la zona de sobrecompra."
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
