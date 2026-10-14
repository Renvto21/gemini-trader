# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 20:00:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$9.23 USD** | **$29.90 USD** | **$39.13 USD** | 🔴 **-2.19%** ($-0.87) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 9h 10m |
| `SOL-USD` | 0.095785 | $104.40 | $104.42 | $10.00 | 📈 +0.02% | 3h 29m |
| `ETH-USD` | 0.004135 | $2418.34 | $2415.45 | $9.99 | 📉 -0.12% | 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se encuentra operando en 24/7 con una tendencia general bajista bajo la SMA20, pero presentando condiciones extremas de sobreventa intradiaria en activos clave como ETH-USD (rsi_1h en 22.5) y SOL-USD (rsi_1h en 34.5). Los mercados tradicionales (Wall Street) permanecen cerrados, por lo que la liquidez activa debe centrarse en aprovechar los rebotes técnicos de corto plazo en criptomonedas. La posición en AAPL se mantiene temporalmente inactiva debido al cierre del mercado accionario."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD se mantiene estable con un RSI de 1h en 34.5 saliendo de zona de compresión y un PnL neutral. Mantenemos la posición para capturar el rebote técnico esperado hacia la zona de sobrecompra.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD presenta una sobreventa extrema en el RSI de 1h (22.5) pero se encuentra dentro del rango aceptable de riesgo sin romper el stop-loss de -2.0%. Esperamos confirmación de giro en el momentum de corto plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en SOL-USD y ETH-USD mientras respeten los niveles de soporte crítico y busquen la recuperación del momentum intradiario. Vigilar de cerca el RSI de 1 hora para asegurar beneficios parciales si supera el nivel de 70, o activar el stop-loss estricto en caso de que alguna posición rompa el -2.0% de pérdida. Monitorear la apertura del mercado accionario para evaluar la rotación en AAPL si es necesario."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **52** | 🎯 **42.3%** (22W / 16L / 14BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 19:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2418.34 | ETH-USD presenta un RSI de 1h en 22.0 (sobreventa extrema) y un cambio de 1h que comienza ... |
| `2026-10-14 16:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.40 | SOL-USD presenta un RSI de 1h en 30.9 saliendo de la zona de compresión y un cambio positi... |
| `2026-10-14 15:20` | 🔴 SELL (-0.08$) | `SOL-USD` | $9.92 | $103.86 | SOL-USD lleva varias horas sin mostrar el rebote esperado, su RSI de 1h ha caído hasta 25.... |
| `2026-10-14 12:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.70 | SOL-USD presenta un RSI de 1h en 29.2 saliendo de sobreventa extrema y un cambio de 1h pos... |
| `2026-10-14 11:20` | 🔴 SELL (-0.09$) | `BTC-USD` | $5.89 | $81874.95 | BTC-USD lleva más de 14 horas abierto con un PnL negativo persistente (-1.51%) y un RSI de... |

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
