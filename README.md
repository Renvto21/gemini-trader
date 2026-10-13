# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 00:20:33`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$7.43 USD** | **$32.00 USD** | **$39.43 USD** | 🔴 **-1.43%** ($-0.57) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.206603 | $106.48 | $106.42 | $21.99 | 📉 -0.06% |
| `ETH-USD` | 0.004032 | $2480.01 | $2484.00 | $10.02 | 📈 +0.16% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa con SOL-USD (RSI 24.3) y ETH-USD (RSI 29.7) tocando niveles atractivos para un rebote técnico inminente bajo la estrategia de reversión a la media. Mantenemos nuestras posiciones actuales esperando el rebote y conservamos $3.43 en efectivo libre, cerca de nuestra reserva mínima de $4.00, manteniendo todo el capital disponible trabajando activamente en alta volatilidad."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en clara sobreventa técnica con un RSI de 24.3 y una caída semanal del -11.89%. Estamos listos para cazar el rebote técnico agresivo en busca de un retorno rápido del +3% al +5%.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD registra un RSI de 29.7, también en zona de sobreventa. La posición se mantiene estable con una ganancia marginal del +0.16%, esperando el impulso alcista del mercado cripto para tomar beneficios parciales.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 00:10` | 🟢 BUY | `SOL-USD` | $10.00 | $106.61 | SOL-USD se encuentra en una clara condición de sobreventa con un RSI de 24.5 y una caída d... |
| `2026-10-12 23:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2480.01 | Ethereum se encuentra en clara sobreventa con un RSI de 29.5 y una caída semanal del 8.06%... |
| `2026-10-12 23:40` | 🟢 BUY | `SOL-USD` | $12.00 | $106.38 | SOL-USD presenta una clara condición de sobreventa técnica extrema con RSI de 24.3 tras un... |
| `2026-10-12 23:40` | 🔴 SELL | `GLD` | $12.00 | $382.15 | Posición estancada con rendimiento de 0% sin momentum alcista. Vendo la totalidad para lib... |
| `2026-10-12 23:30` | 🟢 BUY | `GLD` | $12.00 | $382.15 | Aprovechamos la liquidez liberada y el efectivo disponible para cazar un rebote técnico en... |

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
