# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 11:30:53`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.12 USD** | **$24.55 USD** | **$38.67 USD** | 🔴 **-3.32%** ($-1.33) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $534.79 | $6.50 | 📉 -0.07% | 1d 0h |
| `NVDA` | 0.036812 | $217.32 | $217.42 | $8.00 | 📈 +0.05% | 22h 40m |
| `ETH-USD` | 0.002855 | $2451.90 | $2472.36 | $7.06 | 📈 +0.83% | 6h 59m |
| `SOL-USD` | 0.028214 | $106.33 | $106.07 | $2.99 | 📉 -0.24% | 6h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario muestra un tono cauteloso con varios activos operando bajo la SMA20, mientras que el sector cripto se mantiene dinámico 24/7. ETH-USD muestra un excelente momentum de corto plazo con un RSI de 1h acercándose a la zona de sobrecompra (66.8) y un rendimiento positivo del 0.83% en nuestra posición, consolidando el rebote esperado. NVDA presenta un RSI de 1h extremadamente bajo (27.8), manteniéndose en vigilancia cercana."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD está respondiendo positivamente al plan táctico de rebote técnico, acumulando una ganancia cercana al +0.83% con un RSI de 1h en 66.8. Mantenemos la posición para capturar el take-profit completo al acercarse a la zona de sobrecompra.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos ETH-USD buscando maximizar el take-profit si el RSI de 1h cruza el nivel de 70. Monitorizaremos la posición de NVDA y MSFT; si no muestran recuperación de impulso en las próximas horas, rotaremos capital hacia activos con mayor inercia alcista. La liquidez actual se mantendrá prudente por encima del umbral mínimo requerido."
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
