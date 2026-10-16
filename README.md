# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 11:10:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.12 USD** | **$24.45 USD** | **$38.57 USD** | 🔴 **-3.57%** ($-1.43) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $536.10 | $6.51 | 📈 +0.17% | 1d 0h |
| `NVDA` | 0.036812 | $217.32 | $216.24 | $7.96 | 📉 -0.50% | 22h 20m |
| `ETH-USD` | 0.002855 | $2451.90 | $2453.61 | $7.00 | 📈 +0.07% | 6h 39m |
| `SOL-USD` | 0.028214 | $106.33 | $105.45 | $2.98 | 📉 -0.83% | 5h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un tono mayormente defensivo con varios índices y activos principales cotizando por debajo de su SMA20. Los mercados de Wall Street se encuentran abiertos y operando con ligera debilidad, mientras que las criptomonedas muestran estabilidad con sesgo lateral tras los recientes intentos de rebote en marcos diarios de sobreventa. Mantenemos una postura estricta de gestión de riesgo sobre activos que no muestran el momentum esperado."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 60%): MSFT mantiene una tendencia alcista sobre la SMA20 con un PnL positivo de +0.17%. Mantendremos la posición operativa a la espera de un mayor impulso hacia la zona de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorearemos de cerca el comportamiento de MSFT y ETH-USD para asegurar ganancias si alcanzan los objetivos de take-profit entre +2.0% y +3.5%. NVDA se mantiene bajo vigilancia por su debilidad prolongada, pero dado que el mercado accionario está abierto, evaluaremos su desempeño inmediato en este ciclo antes de proceder a una liquidación total si el RSI de 1 hora no logra romper al alza. Mantendremos la liquidez cercana al mínimo operativo."
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
