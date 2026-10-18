# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 08:00:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$38.37 USD** | **$0.00 USD** | **$38.37 USD** | 🔴 **-4.07%** ($-1.63) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *(Ninguna posición abierta - 100% en efectivo)* | - | - | - | - | - | - |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto muestra un comportamiento lateral a ligeramente alcista en las últimas 24 horas, con nuestros activos en cartera (BTC-USD, SOL-USD y ETH-USD) mostrando rebotes positivos moderados que sitúan el RSI de 1 hora en zona de sobrecompra (>70 para BTC y ETH, y casi 68 para SOL). Los mercados tradicionales (Wall Street) se encuentran cerrados, por lo que la liquidez y operativa se concentran en las criptomonedas abiertas 24/7."

**Operaciones del ciclo:**
- **[SELL] BTC-USD** (Confianza: 90%): BTC-USD ha alcanzado un RSI de 1H en 78.8 (sobrecompra profunda) tras el rebote esperado, con una ganancia actual de +0.99%. Es momento de tomar beneficios y asegurar liquidez.
- **[SELL] SOL-USD** (Confianza: 90%): SOL-USD presenta un RSI de 1H en 67.6 acercándose a zona de sobrecompra con una ganancia de +1.16%. Se ejecuta la venta para realizar ganancias y rotar capital.
- **[SELL] ETH-USD** (Confianza: 90%): ETH-USD registra un RSI de 1H en 72.1 (sobrecompra) y una ganancia de +1.26%. Se procede a cerrar la posición para asegurar el take-profit y maximizar la liquidez disponible.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Las posiciones en BTC-USD, SOL-USD y ETH-USD han alcanzado niveles de sobrecompra en el RSI de 1H (BTC en 78.8, ETH en 72.1, SOL en 67.6) cumpliendo con la estrategia de toma rápida de ganancias por rebote técnico. Procederé a vender la totalidad de las tres posiciones para asegurar los beneficios acumulados y acumular efectivo, preparándome para buscar nuevas entradas en cuanto se presenten correcciones o nuevos catalizadores de impulso."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **70** | 🎯 **41.4%** (29W / 27L / 14BE) | 🔴 **$-1.49 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 08:00` | 🔴 SELL (+0.13$) | `ETH-USD` | $10.13 | $2415.11 | ETH-USD registra un RSI de 1H en 72.1 (sobrecompra) y una ganancia de +1.26%. Se procede a... |
| `2026-10-18 08:00` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $103.84 | SOL-USD presenta un RSI de 1H en 67.6 acercándose a zona de sobrecompra con una ganancia d... |
| `2026-10-18 08:00` | 🔴 SELL (+0.10$) | `BTC-USD` | $10.08 | $81974.15 | BTC-USD ha alcanzado un RSI de 1H en 78.8 (sobrecompra profunda) tras el rebote esperado, ... |
| `2026-10-17 19:10` | 🟢 BUY | `ETH-USD` | $10.00 | $2385.05 | ETH-USD muestra un RSI de 1H en 29.0 (sobreventa profunda) combinado con un cambio de 1h p... |
| `2026-10-17 19:10` | 🟢 BUY | `SOL-USD` | $10.00 | $102.65 | SOL-USD presenta un RSI de 1H en 31.5 saliendo de zona de sobreventa estricta y un cambio ... |

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
