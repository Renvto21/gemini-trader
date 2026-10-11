# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 20:30:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.02 USD** | **$41.03 USD** | **$41.06 USD** | 🟢 **+2.64%** ($+1.06) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.296859 | $111.70 | $111.14 | $32.99 | 📉 -0.50% |
| `ETH-USD` | 0.003174 | $2520.20 | $2533.12 | $8.04 | 📈 +0.51% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema, especialmente en SOL-USD (RSI de 25.7) tras caídas semanales del -7.96%, lo que representa una oportunidad ideal para cazar un rebote técnico por reversión a la media. ETH-USD se mantiene estable con un ligero incremento diario pero aún con RSI bajo (33.1). Por otro lado, en el sector tecnológico, MSFT ha entrado en zona de sobrecompra (RSI 72.3), pero dado que nuestro portafolio está enfocado en cripto y el efectivo disponible es casi nulo, mantendremos las posiciones actuales para permitir el desarrollo del rebote de Solana y Ethereum."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD se encuentra en clara sobreventa técnica con un RSI de 25.7, cumpliendo perfectamente con la estrategia de cazar rebotes en cripto. Aunque registra una pequeña pérdida del -0.5%, mantenemos la posición con alta convicción a la espera del impulso alcista hacia la media.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un rendimiento positivo de +0.51% y un RSI de 33.1, cerca de la zona de oportunidad. No ha alcanzado el objetivo de take-profit del +2.5% pero se mantiene con buen tono técnico dentro del rebote general del mercado cripto.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 20:00` | 🟢 BUY | `SOL-USD` | $4.00 | $110.96 | SOL-USD se encuentra en una clara condicion de sobreventa tecnica profunda con un RSI de 2... |
| `2026-10-11 18:20` | 🟢 BUY | `ETH-USD` | $8.00 | $2520.20 | ETH-USD presenta un RSI de 31.1 y una caída acumulada del 7.04% en los últimos 7 días, sit... |
| `2026-10-11 17:50` | 🔴 SELL | `ETH-USD` | $12.02 | $2536.22 | ETH-USD se encuentra estancado con una ganancia mínima de +0.19% y bajo una tendencia baji... |
| `2026-10-11 17:40` | 🟢 BUY | `SOL-USD` | $4.00 | $111.14 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 25.7 y una... |
| `2026-10-11 14:10` | 🟢 BUY | `SOL-USD` | $5.16 | $111.90 | SOL-USD presenta un RSI de 28.2 indicando sobreventa clara tras una caída semanal del 7.33... |

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
