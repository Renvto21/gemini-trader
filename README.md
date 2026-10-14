# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 22:51:30`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$28.54 USD** | **$11.01 USD** | **$39.55 USD** | 🔴 **-1.12%** ($-0.45) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2506.90 | $5.00 | 📉 -0.06% | 5h 40m |
| `BTC-USD` | 0.000072 | $83128.62 | $83316.85 | $6.01 | 📈 +0.23% | 1h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado y con precios congelados. En el segmento de criptomonedas, que opera 24/7, mantenemos posiciones abiertas en ETH-USD y BTC-USD. ETH-USD muestra un RSI de 1 hora recuperándose a 56.4 y BTC-USD se mantiene estable con un RSI de 51.8. SOL-USD muestra un RSI de 1 hora elevado en 65.3 pero tendencia diaria bajista, por lo que priorizamos conservar liquidez y mantener nuestras posiciones actuales mientras evaluamos su evolución hacia el objetivo de take-profit."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): La posición lleva casi 6 horas abierta con un rendimiento plano (-0.06%), pero su RSI de 1 hora se encuentra en un nivel saludable de 56.4 y el mercado cripto sigue abierto. Mantenemos la posición a la espera del objetivo de take-profit.
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD muestra una ganancia leve de 0.23% con un RSI de 1 hora en 51.8. El precio se mantiene estable y operando con normalidad, por lo que conservamos la posición para buscar mayor impulso alcista.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales en ETH-USD y BTC-USD vigilando que alcancen el objetivo de take-profit entre +2.0% y +3.5%, o recortando inmediatamente si el RSI de 1 hora vuelve a caer por debajo de 35 o el PnL toca el stop-loss de -2.0%. La liquidez en efectivo se mantiene en $28.54 USD listos para futuras oportunidades."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **48** | 🎯 **45.8%** (22W / 12L / 14BE) | 🔴 **$-0.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |
| `2026-10-13 16:30` | 🟢 BUY | `ETH-USD` | $9.68 | $2507.92 | ETH-USD muestra un RSI de 35.8 en zona de fuerte sobreventa y un impulso alcista diario de... |

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
