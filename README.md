# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 07:10:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.17 USD** | **$34.54 USD** | **$38.71 USD** | 🔴 **-3.22%** ($-1.29) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 20h 20m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 18h 50m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 18h 20m |
| `ETH-USD` | 0.002855 | $2451.90 | $2442.42 | $6.97 | 📉 -0.39% | 2h 39m |
| `SOL-USD` | 0.028214 | $106.33 | $105.71 | $2.98 | 📉 -0.58% | 1h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario de Wall Street se encuentra CERRADO, por lo que toda la actividad se concentra en las criptomonedas, que operan 24/7. Las posiciones actuales en acciones (MSFT, QQQ, NVDA) muestran variaciones menores y se mantienen estables a la espera de la apertura. En cripto, ETH-USD y SOL-USD registran ligeros retrocesos en la última hora, pero mantienen su tesis de rebote por sobreventa en gráficos diarios, con niveles de efectivo ajustados cerca del mínimo requerido ($4.17 USD)."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD se mantiene operando dentro del rango esperado tras su reciente compra, con un RSI diario en zona de sobreventa profunda (31.8). Mantenemos la posición para capturar el rebote técnico y esperamos una confirmación de impulso alcista en el corto plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en cripto (ETH-USD y SOL-USD) monitoreando de cerca el soporte para evitar activar el stop-loss del -2.0%. Esperar la apertura de Wall Street para evaluar la rotación de capital de las acciones si alguna se estanca o buscar oportunidades en take-profit si alcanzan la zona de +2.0% a +3.5%."
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
