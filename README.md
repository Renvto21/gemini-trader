# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 01:10:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.54 USD** | **$17.05 USD** | **$39.59 USD** | 🔴 **-1.01%** ($-0.41) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2510.33 | $5.00 | 📈 +0.08% | 8h 0m |
| `BTC-USD` | 0.000072 | $83128.62 | $83660.78 | $6.04 | 📈 +0.64% | 4h 9m |
| `SOL-USD` | 0.055840 | $107.45 | $107.67 | $6.01 | 📈 +0.20% | 1h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto operando en un rango estable con ligeras recuperaciones de 24 horas (BTC +2.32%, ETH +2.70%, SOL +2.0%), aunque la tendencia principal sigue bajo la SMA20 y los indicadores de 1 hora muestran una pausa en el impulso alcista. Los activos tradicionales (Wall Street) se encuentran cerrados. El portafolio mantiene una pequeña ganancia acumulada en las posiciones de BTC y SOL, pero aún no alcanzan la zona de take-profit objetivo del +2.0% al +3.5%."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD muestra una ganancia actual de +0.64% con un RSI de 1h en 55.9. Mantenemos la posición a la espera de que el impulso continúe hacia nuestra zona de take-profit objetivo (+2.0% a +3.5%).
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD se encuentra estable con una ganancia marginal del +0.08% y un holding time de 8 horas. Mantenemos la posición vigilando de cerca su soporte técnico y esperando una expansión de volatilidad alcista.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD presenta un PnL de +0.20% respaldado por un RSI diario en sobreventa extrema (28.9). Mantenemos la posición para capturar el rebote técnico anticipado hacia la resistencia de corto plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en ETH-USD, BTC-USD y SOL-USD mientras monitoreamos el comportamiento del RSI de 1 hora y el cambio porcentual. Esperar a que alguna posición alcance el rango de take-profit (+2.0% a +3.5%) o un RSI de 1H superior a 70 para asegurar ganancias y rotar capital. Mantener estricto el stop-loss en -2.0% y conservar la liquidez actual por encima de los $4.00 USD."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **48** | 🎯 **45.8%** (22W / 12L / 14BE) | 🔴 **$-0.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |

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
