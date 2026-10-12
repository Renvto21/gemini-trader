# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 09:31:07`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$37.03 USD** | **$41.03 USD** | 🟢 **+2.58%** ($+1.03) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.307862 | $111.77 | $110.59 | $34.05 | 📉 -1.06% |
| `ETH-USD` | 0.001175 | $2553.82 | $2537.70 | $2.98 | 📉 -0.63% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado tradicional muestra fortaleza con índices como QQQ y SPY sobre sus medias móviles y sectores como MSFT en sobrecompra (RSI 72.3), mientras el sector cripto atraviesa una fase de capitulación y sobreventa técnica severa (SOL RSI 29.4, ETH RSI 33.5). Esta divergencia configura un escenario clásico de reversión a la media (Mean Reversion). Dado que el efectivo disponible está en el piso mínimo de reserva de $4.00 USD y nuestras posiciones no han tocado niveles de stop-loss (-2.5%), se mantiene la exposición esperando el impulso alcista de rebote sin forzar rotaciones precipitadas."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD cotiza con sobreventa pronunciada (RSI 29.4) tras una caída de 8.44% en 7 días. La posición apenas retrocede un -1.06%, muy lejos del stop-loss de -2.5%. Vender ahora destruiría la tesis de cazar el rebote de alta volatilidad.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD se encuentra en zona de sobreventa con RSI 33.5 y una pérdida latente insignificante de -0.63% (-$0.02). Liquidar esta posición de $2.98 no generaría capital suficiente para una nueva entrada de $5-$8 USD respetando la reserva mínima de $4.00 USD.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 07:40` | 🟢 BUY | `ETH-USD` | $3.00 | $2553.82 | ETH-USD presenta un RSI de 35.7 indicando condiciones cercanas a la sobreventa, lo que act... |
| `2026-10-12 07:30` | 🔴 SELL | `ETH-USD` | $7.00 | $2553.60 | ETH-USD se encuentra estancado con un PnL cercano a 0% sin momentum inmediato. Vendemos la... |
| `2026-10-12 07:00` | 🟢 BUY | `SOL-USD` | $4.00 | $111.65 | SOL-USD está en zona de sobreventa profunda con un RSI de 31.8 y una caída semanal de -7.5... |
| `2026-10-12 06:10` | 🟢 BUY | `ETH-USD` | $2.00 | $2552.03 | ETH-USD presenta un RSI de 35.5 en clara zona de sobreventa tras caídas semanales del -5.3... |
| `2026-10-12 05:50` | 🟢 BUY | `ETH-USD` | $5.00 | $2553.65 | ETH-USD presenta un RSI de 35.7 en clara zona de sobreventa técnica tras una caída semanal... |

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
