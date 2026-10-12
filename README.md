# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 11:20:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.77 USD** | **$40.77 USD** | 🟢 **+1.93%** ($+0.77) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.344173 | $111.60 | $109.81 | $37.79 | 📉 -1.61% |
| `ETH-USD` | 0.001175 | $2553.82 | $2532.62 | $2.98 | 📉 -0.83% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema lideradas por SOL-USD con un RSI de 28.3 y caídas semanales acumuladas del -9.09%, lo que activa nuestra estrategia táctica de mean reversion para cazar un rebote técnico rápido. Nuestras posiciones actuales en SOL-USD y ETH-USD presentan pérdidas menores pero controladas, operando aún dentro de rangos tolerables cercanos a nuestra regla de stop-loss, pero priorizamos mantener la exposición para aprovechar el rebote inminente sin realizar ventas prematuras en mínimos."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en clara sobreventa con un RSI de 28.3. Mantenemos la posición actual de 0.344173 acciones para capturar el rebote técnico esperado hacia la zona de resistencia inmediata, aprovechando la alta volatilidad a nuestro favor.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 11:10` | 🟢 BUY | `SOL-USD` | $4.00 | $110.16 | SOL-USD presenta un RSI extremadamente bajo de 28.8 y una caída acumulada del 8.8% en 7 dí... |
| `2026-10-12 07:40` | 🟢 BUY | `ETH-USD` | $3.00 | $2553.82 | ETH-USD presenta un RSI de 35.7 indicando condiciones cercanas a la sobreventa, lo que act... |
| `2026-10-12 07:30` | 🔴 SELL | `ETH-USD` | $7.00 | $2553.60 | ETH-USD se encuentra estancado con un PnL cercano a 0% sin momentum inmediato. Vendemos la... |
| `2026-10-12 07:00` | 🟢 BUY | `SOL-USD` | $4.00 | $111.65 | SOL-USD está en zona de sobreventa profunda con un RSI de 31.8 y una caída semanal de -7.5... |
| `2026-10-12 06:10` | 🟢 BUY | `ETH-USD` | $2.00 | $2552.03 | ETH-USD presenta un RSI de 35.5 en clara zona de sobreventa tras caídas semanales del -5.3... |

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
