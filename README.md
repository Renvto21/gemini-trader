# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 16:40:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.01 USD** | **$39.92 USD** | **$39.92 USD** | 🔴 **-0.19%** ($-0.08) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.369549 | $109.24 | $108.01 | $39.92 | 📉 -1.13% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones claras de sobreventa técnica, destacando SOL-USD con un RSI de 26.1 y ETH-USD con un RSI de 31.7, lo que activa nuestra estrategia de Mean Reversion y búsqueda agresiva de rebotes alcistas. El portafolio actual se encuentra completamente invertido y con ligeras minusvalías que aún no alcanzan el stop-loss estricto, pero la oportunidad de acumular más Solana en su fuerte descuento actual justifica realizar una rotación táctica."*

**Operaciones del ciclo:**
- **[SELL] ETH-USD** (Confianza: 82%): Vendemos la posición completa en ETH-USD para liberar liquidez y concentrar el capital disponible en SOL-USD, que presenta una sobreventa mucho más agresiva y un potencial de rebote técnico más inmediato.
- **[BUY] SOL-USD** (Confianza: 90%): Aprovechamos el capital liberado de Ethereum para incrementar la exposición en SOL-USD. Su RSI en 26.1 indica una clara condición de sobreventa extrema, ideal para capturar un rebote rápido del 2% al 6% según la estrategia de crecimiento acelerado.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 16:40` | 🟢 BUY | `SOL-USD` | $2.95 | $108.01 | Aprovechamos el capital liberado de Ethereum para incrementar la exposición en SOL-USD. Su... |
| `2026-10-12 16:40` | 🔴 SELL | `ETH-USD` | $2.95 | $2515.02 | Vendemos la posición completa en ETH-USD para liberar liquidez y concentrar el capital dis... |
| `2026-10-12 15:40` | 🟢 BUY | `SOL-USD` | $4.00 | $107.58 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 25.6 y una caída acumulada ... |
| `2026-10-12 12:20` | 🟢 BUY | `SOL-USD` | $3.42 | $108.91 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 27.1 y una caída acumulada ... |
| `2026-10-12 12:10` | 🟢 BUY | `SOL-USD` | $10.00 | $108.93 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 27.2 y una... |

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
