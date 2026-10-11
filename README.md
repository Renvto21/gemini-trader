# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 12:20:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.38 USD** | **$40.38 USD** | 🟢 **+0.95%** ($+0.38) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.340197 | $109.29 | $109.65 | $37.30 | 📈 +0.33% |
| `ETH-USD` | 0.001228 | $2504.75 | $2505.50 | $3.08 | 📈 +0.03% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo mixto con los índices tradicionales y tecnológicas fuertes (SPY y QQQ con tendencias alcistas), mientras que las criptomonedas se encuentran profundamente en zona de sobreventa técnica (SOL-USD con RSI de 21.5 y ETH-USD con RSI de 28.7) tras caídas semanales significativas. Mantenemos nuestras posiciones en cripto esperando el rebote por reversión a la media, pero dado que el efectivo es de $0.0 y no hemos alcanzado el take-profit del +2.5% en nuestras posiciones actuales, decidimos mantener la estructura actual sin realizar nuevas compras ni ventas en este ciclo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD presenta una condición extrema de sobreventa con un RSI de 21.5 y una caída semanal del -9.19%. Mantenemos la posición actual para cazar el rebote técnico inminente sin realizar nuevas compras al carecer de liquidez en efectivo.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 12:10` | 🟢 BUY | `ETH-USD` | $3.08 | $2504.75 | ETH-USD se encuentra en un estado de sobreventa extrema con un RSI de 28.6 y una caída sem... |
| `2026-10-11 11:00` | 🟢 BUY | `SOL-USD` | $12.00 | $109.33 | Aprovechamos la altísima sobreventa en SOL-USD (RSI de 21.2 y -9.46% en 7 días) para incre... |
| `2026-10-11 11:00` | 🔴 SELL | `ETH-USD` | $10.00 | $2499.66 | ETH-USD está estancado con un PnL cercano a 0% (-0.03%). Vendemos la posición completa par... |
| `2026-10-11 10:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2500.42 | ETH-USD presenta un RSI de 28.2 en profunda sobreventa y una caída semanal del 7.77%, cump... |
| `2026-10-11 10:50` | 🔴 SELL | `SOL-USD` | $10.93 | $109.32 | Liberamos liquidez de SOL-USD que se encuentra estancada para aprovechar la oportunidad de... |

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
