# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 12:40:51`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.12 USD** | **$24.39 USD** | **$38.51 USD** | 🔴 **-3.73%** ($-1.49) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $531.03 | $6.45 | 📉 -0.77% | 1d 1h |
| `NVDA` | 0.036812 | $217.32 | $217.90 | $8.02 | 📈 +0.27% | 23h 50m |
| `ETH-USD` | 0.002855 | $2451.90 | $2440.42 | $6.97 | 📉 -0.47% | 8h 9m |
| `SOL-USD` | 0.028214 | $106.33 | $104.55 | $2.95 | 📉 -1.67% | 7h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un tono de cautela con la mayoría de los activos bajo sus medias móviles de 20 periodos. Los índices y grandes tecnológicas intentan estabilizarse, mientras que las criptomonedas exhiben una alta volatilidad de corto plazo. Mantenemos una postura defensiva pero listos para rotar capital hacia oportunidades con mejor momentum."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 60%): La posición se mantiene estable con una pérdida marginal del -0.77% y un RSI de 1 hora en recuperación (37.8). Esperamos la evolución de la sesión para decidir si se mantiene o se rota.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorearemos de cerca las posiciones abiertas en MSFT, NVDA, ETH-USD y SOL-USD. Si SOL-USD o ETH-USD rompen soportes adicionales o se estancan, procederemos a recortar las posiciones para liberar liquidez. Buscaremos puntos de entrada con mayor fuerza direccional en activos que presenten RSI de 1 hora saliendo de sobreventa extrema."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **59** | 🎯 **40.7%** (24W / 21L / 14BE) | 🔴 **$-1.26 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 10:50` | 🔴 SELL (-0.04$) | `QQQ` | $9.95 | $721.83 | QQQ lleva más de 22 horas abierto operando bajo la SMA20 con un RSI de 1 hora en 30.2 y un... |
| `2026-10-16 05:10` | 🟢 BUY | `SOL-USD` | $3.00 | $106.33 | SOL-USD presenta un RSI diario en zona de sobreventa extrema (29.0) y un cambio positivo e... |
| `2026-10-16 04:30` | 🟢 BUY | `ETH-USD` | $7.00 | $2451.90 | Aprovechamos la liquidez disponible sobre la reserva mínima ($14.17 vs $4.00 requeridos) p... |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |

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
