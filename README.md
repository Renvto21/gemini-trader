# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 13:30:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.37 USD** | **$19.83 USD** | **$38.20 USD** | 🔴 **-4.49%** ($-1.80) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.097172 | $102.91 | $101.83 | $9.90 | 📉 -1.05% | 2h 29m |
| `ETH-USD` | 0.004205 | $2377.97 | $2363.08 | $9.94 | 📉 -0.63% | 1h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que la liquidez activa se concentra en las criptomonedas. BTC, ETH y SOL muestran condiciones de sobreventa extrema en sus gráficos diarios, aunque en el corto plazo continúan experimentando una ligera presión vendedora. Mantendremos las posiciones actuales buscando el rebote técnico tan pronto como el momentum de 1 hora se vuelva positivo y el RSI cruce al alza."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD se mantiene cerca del precio de entrada con una ligera pérdida del -1.05%. El RSI diario en 15.8 indica una sobreventa extrema profunda. Mantendremos la posición esperando el rebote técnico hacia la zona de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones de SOL-USD y ETH-USD mientras no alcancen el stop-loss estricto de -2.0%. Estar atentos a un cambio en el RSI de 1 hora (superando 50) para preparar la toma de beneficios entre +2.0% y +3.5%. Proteger rigurosamente el capital y evitar rotaciones prematuras ya que los precios están en soportes macro diarios clave."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **70** | 🎯 **41.4%** (29W / 27L / 14BE) | 🔴 **$-1.49 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 12:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2377.97 | ETH-USD presenta un RSI diario extremadamente bajo en 22.0 y un RSI de 1 hora saliendo de ... |
| `2026-10-18 11:01` | 🟢 BUY | `SOL-USD` | $10.00 | $102.91 | SOL-USD muestra un RSI diario extremadamente bajo (16.4) en zona de sobreventa profunda y ... |
| `2026-10-18 08:00` | 🔴 SELL (+0.13$) | `ETH-USD` | $10.13 | $2415.11 | ETH-USD registra un RSI de 1H en 72.1 (sobrecompra) y una ganancia de +1.26%. Se procede a... |
| `2026-10-18 08:00` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $103.84 | SOL-USD presenta un RSI de 1H en 67.6 acercándose a zona de sobrecompra con una ganancia d... |
| `2026-10-18 08:00` | 🔴 SELL (+0.10$) | `BTC-USD` | $10.08 | $81974.15 | BTC-USD ha alcanzado un RSI de 1H en 78.8 (sobrecompra profunda) tras el rebote esperado, ... |

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
