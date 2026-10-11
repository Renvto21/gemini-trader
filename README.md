# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 02:20:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.35 USD** | **$40.35 USD** | 🟢 **+0.88%** ($+0.35) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.220969 | $109.11 | $109.54 | $24.20 | 📈 +0.39% |
| `ETH-USD` | 0.006448 | $2481.58 | $2504.54 | $16.15 | 📈 +0.93% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un tono mixto con recuperación en los índices principales y soporte en activos tecnológicos, mientras que criptomonedas clave como ETH-USD y SOL-USD se mantienen en niveles de sobreventa técnica extrema con RSI de 28.0 y 22.4 respectivamente. Esto representa una excelente oportunidad de mean reversion para capturar rebotes a corto plazo. Mantenemos una postura agresiva rotando nuestro capital disponible hacia estas zonas de alta sobreventa."*

**Operaciones del ciclo:**
- **[BUY] SOL-USD** (Confianza: 90%): SOL-USD se encuentra en extrema sobreventa técnica con un RSI de 22.4 y una caída semanal del -9.86%. Aprovechamos todo el efectivo disponible restante ($4.11) para maximizar la posición en este activo de alta beta buscando un rebote técnico inminente.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 02:20` | 🟢 BUY | `SOL-USD` | $4.11 | $109.54 | SOL-USD se encuentra en extrema sobreventa técnica con un RSI de 22.4 y una caída semanal ... |
| `2026-10-10 12:10` | 🔴 SELL | `MSFT` | $4.11 | $535.07 | MSFT ha alcanzado un RSI de 72.3 (sobrecompra) cumpliendo con la regla táctica de toma de ... |
| `2026-10-10 12:00` | 🟢 BUY | `MSFT` | $4.11 | $535.07 | Aprovechamos el capital liberado de GLD para entrar en MSFT, que muestra un fuerte momentu... |
| `2026-10-10 12:00` | 🔴 SELL | `GLD` | $4.11 | $384.58 | Liberamos la totalidad de la posición en GLD ya que se encuentra estancada con 0% de PnL y... |
| `2026-10-10 11:50` | 🟢 BUY | `GLD` | $4.11 | $384.58 | Aprovechamos el efectivo disponible para cazar un rebote por sobreventa en GLD, cuyo RSI s... |

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
