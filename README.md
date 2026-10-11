# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 20:20:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.02 USD** | **$40.99 USD** | **$41.01 USD** | 🟢 **+2.53%** ($+1.01) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.296859 | $111.70 | $111.00 | $32.95 | 📉 -0.62% |
| `ETH-USD` | 0.003174 | $2520.20 | $2531.89 | $8.04 | 📈 +0.46% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con sesgo alcista en índices y tecnológicas, pero con oportunidades claras de sobreventa (mean reversion) en criptomonedas clave como SOL-USD y ETH-USD, cuyos RSI se encuentran en niveles muy deprimidos (25.3 y 32.9 respectivamente), ideales para cazar rebotes agresivos de corto plazo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): A pesar de estar ligeramente en negativo (-0.62%), SOL-USD muestra un RSI de 25.3 en profunda sobreventa, cumpliendo exactamente con la estrategia de buscar rebotes en cripto. Mantenemos la posición para capturar el esperado rebote técnico hacia la resistencia inmediata.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD se encuentra con un RSI de 32.9 en zona de posible reversión alcista y con una ligera ganancia actual. Mantenemos la posición ya que el efectivo disponible es casi nulo y el activo mantiene buen potencial de rebote técnico.

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
