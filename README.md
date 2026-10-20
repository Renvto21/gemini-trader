# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 00:50:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.75 USD** | **$38.75 USD** | 🔴 **-3.12%** ($-1.25) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 14h 10m |
| `ETH-USD` | 0.004178 | $2393.62 | $2410.63 | $10.07 | 📈 +0.71% | 11h 59m |
| `SOL-USD` | 0.096034 | $104.13 | $105.19 | $10.10 | 📈 +1.02% | 8h 9m |
| `BTC-USD` | 0.000105 | $81767.70 | $81986.45 | $8.59 | 📈 +0.27% | 7h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se encuentra abierto 24/7 mostrando un comportamiento lateral con sesgo positivo moderado en las últimas horas, mientras que los mercados tradicionales están cerrados. Nuestras posiciones en criptomonedas (SOL-USD, ETH-USD y BTC-USD) muestran ganancias iniciales pero aún no han alcanzado el objetivo completo de take-profit del rango +2.0% a +3.5%. QQQ se mantiene operando lateralmente en mercado cerrado con ligeras pérdidas latentes pero bajo control técnico."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD mantiene un rendimiento positivo de +1.02% y un RSI de 1h en 63.3, apuntando hacia la zona de sobrecompra donde se ejecutará el take-profit. Se mantiene la posición para maximizar el rebote.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones activas en cripto y QQQ. Monitorear de cerca SOL-USD ya que se acerca a zonas clave de resistencia y su RSI de 1 hora se aproxima a la zona de sobrecompra (>70), punto en el cual se ejecutará la toma de beneficios para asegurar liquidez. Si alguna posición reduce su impulso de manera drástica, se procederá a rotar el capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 23:00` | 🟢 BUY | `BTC-USD` | $4.00 | $81646.39 | BTC-USD presenta un RSI de 1 hora en 27.7, nivel de sobreventa profunda ideal para un rebo... |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |

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
