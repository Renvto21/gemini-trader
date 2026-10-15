# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 16:20:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.17 USD** | **$24.65 USD** | **$38.81 USD** | 🔴 **-2.97%** ($-1.19) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $540.77 | $6.57 | 📈 +1.05% | 5h 29m |
| `QQQ` | 0.013791 | $725.09 | $728.68 | $10.05 | 📈 +0.50% | 3h 59m |
| `NVDA` | 0.036812 | $217.32 | $218.09 | $8.03 | 📈 +0.35% | 3h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra señales mixtas con una tendencia general de rebote en los índices y tecnológicas clave tras recientes caídas. MSFT presenta un rendimiento positivo del +1.05% acercándose al objetivo de toma de beneficios, mientras que AAPL se mantiene estancada con un pequeño retroceso. QQQ y NVDA están consolidando sus rebotes tras haber estado en sobreventa. La liquidez se mantiene ajustada en el portafolio."

**Operaciones del ciclo:**
- **[SELL] AAPL** (Confianza: 80%): AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar el objetivo de ganancia, manteniéndose con un PnL negativo de -0.95%. Se ejecuta la venta para liberar capital y rotar hacia oportunidades de mayor dinamismo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca el rendimiento de MSFT para asegurar beneficios si alcanza el rango de +2.0% a +3.5%. Evaluar la evolución de AAPL; si no muestra impulso alcista en el próximo ciclo, proceder a rotar el capital hacia oportunidades con mayor momentum en cripto o tecnología. Mantener la liquidez en niveles mínimos."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **58** | 🎯 **41.4%** (24W / 20L / 14BE) | 🔴 **$-1.22 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |
| `2026-10-15 12:10` | 🔴 SELL (+0.14$) | `ETH-USD` | $6.14 | $2417.73 | ETH-USD ha alcanzado un rendimiento del +2.33%, cumpliendo con el rango establecido para l... |
| `2026-10-15 11:50` | 🔴 SELL (+0.13$) | `SOL-USD` | $6.13 | $104.21 | SOL-USD ha alcanzado un rendimiento de +2.11%, cumpliendo con la regla de toma rápida de g... |

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
