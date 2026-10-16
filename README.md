# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 11:50:55`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.12 USD** | **$24.61 USD** | **$38.73 USD** | 🔴 **-3.18%** ($-1.27) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $536.84 | $6.52 | 📈 +0.31% | 1d 1h |
| `NVDA` | 0.036812 | $217.32 | $218.23 | $8.03 | 📈 +0.42% | 23h 0m |
| `ETH-USD` | 0.002855 | $2451.90 | $2470.82 | $7.05 | 📈 +0.77% | 7h 19m |
| `SOL-USD` | 0.028214 | $106.33 | $106.26 | $3.00 | 📉 -0.07% | 6h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un tono mixto con sesgo alcista en las últimas horas para varios activos, mientras que las criptomonedas continúan operando de forma activa manteniéndose como el foco principal al estar abiertos los fines de semana o fuera de horario bursátil. Los índices y acciones seleccionados en cartera muestran ganancias ligeras, acercándose a las zonas de take-profit moderado."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD se encuentra con un rendimiento positivo de +0.77% y un RSI de 1h en 66.2, aproximándose a la zona de sobrecompra (>70) donde ejecutaremos el take-profit para asegurar ganancias.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener la vigilancia sobre ETH-USD cuyo RSI de 1h se encuentra en 66.2, preparándonos para asegurar ganancias parciales o totales si supera el nivel de 70. Monitorear las posiciones de MSFT y NVDA gestionando el riesgo de cerca. Si la liquidez lo permite y surgen nuevos impulsos claros, buscaremos rotar capital manteniendo el colchón mínimo de efectivo."
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
