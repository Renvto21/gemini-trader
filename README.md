# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 09:50:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.54 USD** | **$38.54 USD** | 🔴 **-3.65%** ($-1.46) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 23h 10m |
| `ETH-USD` | 0.004178 | $2393.62 | $2392.34 | $9.99 | 📉 -0.05% | 20h 59m |
| `SOL-USD` | 0.096034 | $104.13 | $104.33 | $10.02 | 📈 +0.19% | 17h 9m |
| `BTC-USD` | 0.000105 | $81767.70 | $81474.18 | $8.53 | 📉 -0.36% | 16h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene abierto con un sesgo lateral a ligeramente alcista en el corto plazo, donde activos como ETH-USD, SOL-USD y BTC-USD muestran ligeros rebotes en el cambio de 1 hora y RSI de 1 hora recuperándose desde zonas neutrales. Los mercados tradicionales (QQQ) se encuentran cerrados, por lo que la liquidez y la acción táctica se centran en las criptomonedas para buscar la toma de ganancias en el rango del +2.0% al +3.5% o rotación."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra un rendimiento positivo de +0.19% con un RSI de 1h en 39.0 y un RSI diario extremadamente bajo de 21.4. Mantenemos la posición esperando que continúe el momentum alcista hacia el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD registra un cambio de 1h positivo de +0.46% y un RSI de 1h en 42.4, mostrando signos de recuperación técnica en soporte diario.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca las posiciones en ETH-USD, SOL-USD y BTC-USD buscando que el RSI de 1 hora supere la zona de 50 para asegurar ganancias de +2.0% a +3.5%. Mantener QQQ en cartera debido a que el mercado tradicional está cerrado. Si alguna criptomoneda pierde el soporte de -2.0%, ejecutar stop-loss inmediato."
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
