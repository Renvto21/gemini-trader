# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 23:50:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$17.43 USD** | **$22.00 USD** | **$39.42 USD** | 🔴 **-1.44%** ($-0.58) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.112803 | $106.38 | $106.35 | $12.00 | 📉 -0.03% |
| `ETH-USD` | 0.004032 | $2480.01 | $2480.01 | $10.00 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra una corrección generalizada en criptomonedas, situando a varios activos en zonas de sobreventa extrema muy atractivas para estrategia de rebote por reversión a la media. SOL-USD mantiene un RSI de 24.3 y ETH-USD se encuentra en 29.5, lo cual activa nuestras reglas tácticas agresivas para cazar un rebote a corto plazo. Mantendremos SOL-USD por su potencial y aprovecharemos la liquidez disponible para sumar ETH-USD."*

**Operaciones del ciclo:**
- **[BUY] ETH-USD** (Confianza: 88%): Ethereum se encuentra en clara sobreventa con un RSI de 29.5 y una caída semanal del 8.06%. Aplicando la regla de alta convicción para cazar rebotes en cripto, asignamos $10 USD para capturar un movimiento alcista rápido del 2% al 6%.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 23:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2480.01 | Ethereum se encuentra en clara sobreventa con un RSI de 29.5 y una caída semanal del 8.06%... |
| `2026-10-12 23:40` | 🟢 BUY | `SOL-USD` | $12.00 | $106.38 | SOL-USD presenta una clara condición de sobreventa técnica extrema con RSI de 24.3 tras un... |
| `2026-10-12 23:40` | 🔴 SELL | `GLD` | $12.00 | $382.15 | Posición estancada con rendimiento de 0% sin momentum alcista. Vendo la totalidad para lib... |
| `2026-10-12 23:30` | 🟢 BUY | `GLD` | $12.00 | $382.15 | Aprovechamos la liquidez liberada y el efectivo disponible para cazar un rebote técnico en... |
| `2026-10-12 23:30` | 🔴 SELL | `ETH-USD` | $10.26 | $2479.99 | La posición registra un beneficio del +2.57%, alcanzando el objetivo de toma rápida de gan... |

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
