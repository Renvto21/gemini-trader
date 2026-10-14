# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 19:50:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$9.23 USD** | **$29.91 USD** | **$39.14 USD** | 🔴 **-2.15%** ($-0.86) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 9h 0m |
| `SOL-USD` | 0.095785 | $104.40 | $104.50 | $10.01 | 📈 +0.10% | 3h 19m |
| `ETH-USD` | 0.004135 | $2418.34 | $2417.50 | $10.00 | 📉 -0.03% | 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado bursátil de Wall Street se encuentra CERRADO, por lo que toda la atención operativa se desplaza hacia los mercados de criptomonedas (abiertos 24/7). Los principales activos digitales como SOL-USD y ETH-USD muestran niveles de sobreventa extrema en RSI de 1 hora, consolidándose tras caídas previas. Mantenemos posiciones abiertas en AAPL (cerrado), SOL-USD y ETH-USD, vigilando de cerca los niveles de soporte y preparándonos para capitalizar cualquier rebote técnico."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD se mantiene estable con un RSI de 1h en 32.8. No muestra señales de ruptura a la baja ni el impulso alcista necesario para asegurar ganancias, por lo que mantenemos la posición a la espera de un rebote más fuerte.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en SOL-USD y ETH-USD mientras estén operando en zonas de sobreventa y respeten los niveles de soporte crítico. La posición en AAPL está inactiva debido al cierre del mercado accionario. Si ETH-USD o SOL-USD muestran pérdida de soporte o caen por debajo del stop-loss del -2.0%, procederemos a vender inmediatamente para proteger el capital. Monitorear el cambio en el momentum de 1 hora para buscar oportunidades de toma de beneficios si el RSI supera 70."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **52** | 🎯 **42.3%** (22W / 16L / 14BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 19:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2418.34 | ETH-USD presenta un RSI de 1h en 22.0 (sobreventa extrema) y un cambio de 1h que comienza ... |
| `2026-10-14 16:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.40 | SOL-USD presenta un RSI de 1h en 30.9 saliendo de la zona de compresión y un cambio positi... |
| `2026-10-14 15:20` | 🔴 SELL (-0.08$) | `SOL-USD` | $9.92 | $103.86 | SOL-USD lleva varias horas sin mostrar el rebote esperado, su RSI de 1h ha caído hasta 25.... |
| `2026-10-14 12:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.70 | SOL-USD presenta un RSI de 1h en 29.2 saliendo de sobreventa extrema y un cambio de 1h pos... |
| `2026-10-14 11:20` | 🔴 SELL (-0.09$) | `BTC-USD` | $5.89 | $81874.95 | BTC-USD lleva más de 14 horas abierto con un PnL negativo persistente (-1.51%) y un RSI de... |

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
