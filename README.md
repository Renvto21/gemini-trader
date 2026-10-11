# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 09:40:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.31 USD** | **$40.31 USD** | 🟢 **+0.78%** ($+0.31) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.330438 | $109.27 | $109.45 | $36.17 | 📈 +0.16% |
| `ETH-USD` | 0.001656 | $2500.14 | $2502.73 | $4.14 | 📈 +0.10% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un panorama mixto con oportunidades claras de rebote técnico por sobreventa extrema en criptomonedas. SOL-USD presenta un RSI extremadamente bajo de 21.3 y una fuerte caída semanal del -9.36%, lo que activa una oportunidad perfecta de Mean Reversion para capturar un rebote rápido. ETH-USD también se encuentra en sobreventa con un RSI de 28.4. Dado que el portafolio está completamente invertido y no hay efectivo libre, mantenemos nuestras posiciones actuales para permitirles desarrollar el rebote esperado y no realizamos ventas en este momento ya que ninguna ha alcanzado el objetivo de take-profit ni ha roto el stop-loss."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 90%): La posición en SOL-USD se mantiene firme a pesar de la caída semanal. Su RSI de 21.3 indica una condición de sobreventa profunda, configurando el escenario ideal para el rebote técnico buscado por nuestra estrategia de Crecimiento Acelerado.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH-USD muestra un RSI de 28.4 en zona de sobreventa. Mantenemos la posición para capturar el impulso de recuperación inminente respaldado por la alta volatilidad del activo.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 08:40` | 🟢 BUY | `ETH-USD` | $4.14 | $2500.14 | ETH-USD se encuentra en clara sobreventa con un RSI de 28.2 y una caída de 7.78% en los úl... |
| `2026-10-11 08:00` | 🔴 SELL | `ETH-USD` | $4.14 | $2498.90 | Vendemos la posición completa de ETH-USD para liberar 4.14 USD en efectivo. Aunque está en... |
| `2026-10-11 05:00` | 🟢 BUY | `ETH-USD` | $4.14 | $2499.59 | ETH-USD presenta un RSI de 28.2, lo que indica una clara condición de sobreventa técnica t... |
| `2026-10-11 04:50` | 🟢 BUY | `SOL-USD` | $12.00 | $109.36 | Alta convicción en el rebote técnico de Solana tras una caída semanal del -9.43% y un RSI ... |
| `2026-10-11 04:50` | 🔴 SELL | `ETH-USD` | $16.12 | $2500.30 | Rotamos capital fuera de ETH-USD para asegurar una pequeña ganancia del +0.75% y liberar l... |

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
