# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 03:50:57`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$41.54 USD** | **$41.54 USD** | 🟢 **+3.85%** ($+1.54) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.280926 | $111.80 | $112.26 | $31.54 | 📈 +0.41% |
| `ETH-USD` | 0.003904 | $2561.78 | $2562.67 | $10.00 | 📈 +0.03% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con señales claras de sobreventa en criptoactivos principales como SOL-USD, cuyo RSI se encuentra en un nivel de 29.3, indicando una clara oportunidad de rebote técnico por mean reversion. Ethereum también muestra un RSI bajo en 37.2. Por otro lado, acciones tecnológicas y índices como QQQ y SPY se mantienen estables o con sesgo alcista, pero la estrategia agresiva actual dicta priorizar la rotación hacia las mayores caídas en cripto para capturar el rebote rápido."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD presenta un RSI profundamente sobrevendido de 29.3 y un cambio de 7 días de -7.03%. Aunque está en tendencia bajista a corto plazo, el setup técnico es ideal para buscar un rebote rápido del 2% al 6% manteniendo la posición actual intacta.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un RSI de 37.2 en zona de posible sobreventa y un intento de recuperación en 24h (+2.34%). Mantenemos la posición para capturar el momentum alcista de corto plazo alineado con la estrategia de rebotes.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 03:40` | 🟢 BUY | `SOL-USD` | $4.00 | $112.34 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 29.5 y una caída semanal de... |
| `2026-10-12 03:20` | 🟢 BUY | `SOL-USD` | $2.92 | $112.10 | Aprovechamos la reserva de efectivo por encima del mínimo requerido ($4.00) para increment... |
| `2026-10-12 03:01` | 🟢 BUY | `ETH-USD` | $10.00 | $2561.78 | ETH-USD se encuentra en clara sobreventa técnica (RSI de 37) y muestra un repunte del 2.31... |
| `2026-10-12 03:01` | 🔴 SELL | `SOL-USD` | $16.91 | $112.74 | Vendemos parcialmente SOL-USD para capitalizar una pequeña ganancia y liberar efectivo, pe... |
| `2026-10-12 02:30` | 🟢 BUY | `SOL-USD` | $4.95 | $112.41 | SOL-USD mantiene un RSI en zona crítica de sobreventa (29.7) y un cambio positivo de 2.16%... |

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
