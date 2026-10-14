# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 08:00:53`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$11.99 USD** | **$39.51 USD** | 🔴 **-1.22%** ($-0.49) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83332.43 | $6.01 | 📈 +0.25% | 11h 0m |
| `SOL-USD` | 0.055840 | $107.45 | $106.95 | $5.97 | 📉 -0.47% | 8h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 pero con baja volatilidad y ligeros retrocesos en la última hora, mientras que los mercados tradicionales (SPY, QQQ, AAPL, MSFT, NVDA) se encuentran cerrados. BTC-USD y SOL-USD muestran un comportamiento plano con ganancias y pérdidas marginales, respectivamente, sin alcanzar aún los objetivos de take-profit (+2% a +3.5%) ni activar los stop-loss. Mantenemos el efectivo libre para buscar entradas en rupturas cuando las condiciones mejoren."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 60%): BTC-USD se mantiene estable con un PnL positivo menor (+0.25%) tras 11 horas de holding. El RSI de 1H está en 47.1 y el precio no ha alcanzado el objetivo de take-profit (+2.0% a +3.5%) ni ha roto el stop-loss. Continuamos esperando el impulso alcista.
- **[HOLD] SOL-USD** (Confianza: 60%): SOL-USD registra un PnL de -0.47% con un tiempo de holding cercano a 9 horas. El RSI diario se mantiene en sobreventa extrema (28.1), lo que respalda la tesis de rebote a medio plazo, por lo que mantenemos la posición mientras no rompa el soporte crítico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener BTC-USD y SOL-USD bajo supervisión estricta mientras respeten el stop-loss de -2.0%. Si BTC-USD o SOL-USD alcanzan la zona de +2.0% a +3.5%, procederemos a asegurar beneficios de inmediato. Mantener los $27.53 USD de liquidez en efectivo listos para desplegar en oportunidades de alta convicción en criptomonedas o cuando abra el mercado tradicional si se presentan setups técnicos claros."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **49** | 🎯 **44.9%** (22W / 13L / 14BE) | 🔴 **$-0.39 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |

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
