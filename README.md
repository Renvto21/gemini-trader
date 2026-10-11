# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 19:30:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.02 USD** | **$36.99 USD** | **$41.01 USD** | 🟢 **+2.53%** ($+1.01) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.260810 | $111.80 | $111.02 | $28.96 | 📉 -0.70% |
| `ETH-USD` | 0.003174 | $2520.20 | $2531.08 | $8.03 | 📈 +0.43% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con ligera recuperación en criptomonedas y fortaleza en el sector tecnológico. SOL-USD y ETH-USD se encuentran en zonas de marcada sobreventa técnica con RSI en 25.3 y 32.8 respectivamente, lo cual presenta una oportunidad ideal para acumular en base a nuestra estrategia de captura de rebotes. Mantenemos una postura agresiva y dinámica, con el efectivo cercano a la reserva mínima establecida."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD muestra un RSI profundamente en sobreventa de 25.3 y una caída semanal del -8.06%. Mantenemos la posición actual para cazar el rebote técnico inminente sin sobrepasar la exposición.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 18:20` | 🟢 BUY | `ETH-USD` | $8.00 | $2520.20 | ETH-USD presenta un RSI de 31.1 y una caída acumulada del 7.04% en los últimos 7 días, sit... |
| `2026-10-11 17:50` | 🔴 SELL | `ETH-USD` | $12.02 | $2536.22 | ETH-USD se encuentra estancado con una ganancia mínima de +0.19% y bajo una tendencia baji... |
| `2026-10-11 17:40` | 🟢 BUY | `SOL-USD` | $4.00 | $111.14 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 25.7 y una... |
| `2026-10-11 14:10` | 🟢 BUY | `SOL-USD` | $5.16 | $111.90 | SOL-USD presenta un RSI de 28.2 indicando sobreventa clara tras una caída semanal del 7.33... |
| `2026-10-11 14:00` | 🟢 BUY | `SOL-USD` | $10.00 | $112.02 | SOL-USD se encuentra en clara sobreventa tecnica con un RSI de 28.5 tras una caida semanal... |

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
