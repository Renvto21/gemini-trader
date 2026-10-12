# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 21:30:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$41.04 USD** | **$41.04 USD** | 🟢 **+2.60%** ($+1.04) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.369416 | $111.58 | $111.09 | $41.04 | 📉 -0.44% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra oportunidades claras de sobreventa en el sector cripto. ETH-USD presenta un RSI de 33.6, lo cual lo sitúa en una zona óptima para buscar un rebote técnico (Mean Reversion) alineado con nuestra estrategia agresiva. SOL-USD se mantiene en cartera con una ligera pérdida del -0.44% y un RSI extremadamente bajo de 25.6, por lo que decidimos mantenerla a la espera de su rebote. No ejecutamos ventas en SOL ya que no ha alcanzado el stop-loss estricto de -2.5%, y aprovechamos para rotar liquidez o abrir nueva posición en ETH."*

**Operaciones del ciclo:**
- **[BUY] ETH-USD** (Confianza: 86%): ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 33.6 y una caída semanal del -6.42%, lo que representa una excelente oportunidad de entrada para cazar un rebote rápido de corto plazo hacia la resistencia inmediata, cumpliendo con la estrategia de alta convicción.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 21:20` | 🟢 BUY | `SOL-USD` | $4.24 | $111.11 | Aprovechamos el capital liberado para incrementar la exposición en SOL-USD. Se encuentra e... |
| `2026-10-11 21:20` | 🔴 SELL | `ETH-USD` | $4.24 | $2534.63 | Vendemos la totalidad de la posición en ETH-USD (valorada en aproximadamente 4.24 USD) par... |
| `2026-10-11 21:10` | 🟢 BUY | `SOL-USD` | $3.82 | $111.13 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 25.7 y una caída semanal de... |
| `2026-10-11 21:10` | 🔴 SELL | `MSFT` | $3.82 | $535.07 | MSFT ha alcanzado un RSI de 72.3 en zona de sobrecompra y acumula un avance sólido. Ejecut... |
| `2026-10-11 21:00` | 🟢 BUY | `MSFT` | $3.82 | $535.07 | MSFT muestra un fuerte momentum alcista con un incremento de 2.38% en 24 horas y un RSI en... |

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
