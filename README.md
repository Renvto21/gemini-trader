# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 19:00:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$34.66 USD** | **$38.66 USD** | 🔴 **-3.36%** ($-1.34) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 8h 20m |
| `ETH-USD` | 0.004178 | $2393.62 | $2401.98 | $10.03 | 📈 +0.35% | 6h 9m |
| `SOL-USD` | 0.096034 | $104.13 | $104.73 | $10.06 | 📈 +0.58% | 2h 20m |
| `BTC-USD` | 0.000056 | $81874.05 | $81995.18 | $4.58 | 📈 +0.15% | 1h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional (QQQ y acciones) se encuentra cerrado, manteniendo los precios congelados y operando bajo una ligera presión bajista macro. En contraste, los mercados de criptomonedas (ETH-USD, SOL-USD, BTC-USD) están abiertos 24/7 y muestran ligeros repuntes de corto plazo con cambios de 1 hora positivos y recuperación gradual en los indicadores RSI de 1 hora, alineándose con las condiciones de rebote técnico (mean reversion) buscadas."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): La posición en ETH-USD muestra un pequeño rendimiento positivo (+0.35%) con un RSI de 1 hora recuperándose a 35.4 y cambio de 1 hora positivo. Se mantiene la posición a la espera de alcanzar el objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD presenta el mejor rendimiento actual de la cartera (+0.58%) con un RSI de 1 hora en 41.8 y cambio positivo. Mantenemos la posición para capturar una mayor expansión del rebote técnico antes de tomar beneficios.
- **[HOLD] BTC-USD** (Confianza: 70%): BTC-USD se mantiene estable con un ligero beneficio (+0.15%) y RSI de 1 hora en 33.9. Continuamos operando la tesis de rebote sin activar salidas prematuras.
- **[HOLD] QQQ** (Confianza: 70%): El mercado tradicional se encuentra CERRADO, por lo que QQQ mantiene su precio congelado. Se mantiene la posición intacta hasta la reapertura de Wall Street.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas actuales (QQQ, ETH-USD, SOL-USD, BTC-USD) ya que se encuentran en zona de recuperación y aún no alcanzan los objetivos de take-profit entre +2.0% y +3.5%. QQQ permanece inalterado hasta la apertura del mercado tradicional. Seguir monitoreando el RSI de 1 hora en cripto; si ETH o SOL superan los objetivos de ganancia o alcanzan sobrecompra en RSI de 1 hora (>70), proceder a la venta parcial para asegurar liquidez. No se requiere realizar compras adicionales en este ciclo debido a que la liquidez se mantiene en el límite mínimo ($4.00 USD)."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |
| `2026-10-19 01:50` | 🔴 SELL (+0.09$) | `ETH-USD` | $8.09 | $2428.97 | ETH-USD registra una ganancia acumulada y su RSI de 1 hora ha alcanzado 68.3, acercándose ... |

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
