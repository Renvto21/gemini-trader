# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 09:10:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$37.13 USD** | **$41.14 USD** | 🟢 **+2.84%** ($+1.14) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.307862 | $111.77 | $110.92 | $34.15 | 📉 -0.76% |
| `ETH-USD` | 0.001175 | $2553.82 | $2541.72 | $2.99 | 📉 -0.47% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con sesgo alcista en indices tradicionales como SPY y QQQ, mientras que el sector cripto (SOL-USD y ETH-USD) se encuentra bajo presion bajista pero con claras señales de sobreventa extrema (RSI de 29.9 para SOL y 34.1 para ETH), lo cual activa nuestra estrategia de captura de rebotes tecnicos (Mean Reversion). Dado que mantenemos una reserva minima de efectivo y buscamos dinamismo, evaluamos el estado de nuestras posiciones actuales y priorizamos la rotacion tactica si es necesario."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD presenta un RSI de 29.9 en profunda sobreventa, alineado con nuestra estrategia de cazar rebotes tecnicos. Aunque muestra una ligera perdida de -0.76%, la alta volatilidad y la caida acumulada de 7 dias de -8.17% ofrecen un escenario ideal para un rebote inminente hacia el objetivo del +3%.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD se encuentra en una condicion similar con un RSI de 34.1 y cotizando cerca de zona de soporte. Mantenemos la posicion abierta para capturar el rebote tecnico de corto plazo sin incurrir en perdidas mayores, respetando el stop-loss estricto.

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
