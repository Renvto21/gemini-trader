# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 06:10:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.17 USD** | **$34.60 USD** | **$38.76 USD** | 🔴 **-3.09%** ($-1.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 19h 20m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 17h 50m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 17h 20m |
| `ETH-USD` | 0.002855 | $2451.90 | $2451.80 | $7.00 | 📈 -0.00% | 1h 39m |
| `SOL-USD` | 0.028214 | $106.33 | $106.58 | $3.01 | 📈 +0.24% | 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de renta variable (Wall Street) se encuentra actualmente CERRADO, manteniendo los precios congelados y limitando la operativa de corto plazo en acciones y ETFs. Las criptomonedas operan con normalidad 24/7, pero muestran un impulso lateral a levemente bajista en este ciclo, sin rupturas de alta convicción que justifiquen el despliegue inmediato de nuevo capital. Mantenemos la liquidez en $4.17 USD, cumpliendo estrictamente con la reserva mínima establecida de $4.00 USD, mientras las posiciones actuales en cartera (MSFT, QQQ, NVDA, ETH-USD y SOL-USD) se encuentran estables con oscilaciones mínimas y sin activar los umbrales de stop-loss ni take-profit."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 60%): La posición se encuentra operando dentro de un rango lateral estables sin señales de alerta. Esperamos el desarrollo del impulso alcista para asegurar ganancias conforme al plan táctico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales y monitorear de cerca el comportamiento de ETH-USD y SOL-USD en busca de un incremento de volumen y momentum que impulse sus precios hacia el rango de take-profit (+2.0% a +3.5%) o un RSI de 1H superior a 70. Permanecer atentos a la apertura de Wall Street para evaluar posibles rotaciones de capital en renta variable si alguna posición estancada pierde fuerza o si surge una oportunidad clara de rebote técnico."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **58** | 🎯 **41.4%** (24W / 20L / 14BE) | 🔴 **$-1.22 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 05:10` | 🟢 BUY | `SOL-USD` | $3.00 | $106.33 | SOL-USD presenta un RSI diario en zona de sobreventa extrema (29.0) y un cambio positivo e... |
| `2026-10-16 04:30` | 🟢 BUY | `ETH-USD` | $7.00 | $2451.90 | Aprovechamos la liquidez disponible sobre la reserva mínima ($14.17 vs $4.00 requeridos) p... |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |

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
