# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 14:40:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$37.39 USD** | **$41.39 USD** | 🟢 **+3.46%** ($+1.39) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.004740 | $2531.44 | $2547.24 | $12.07 | 📈 +0.62% |
| `SOL-USD` | 0.224836 | $111.90 | $112.58 | $25.31 | 📈 +0.60% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un comportamiento mixto con oportunidades claras de rebote en criptomonedas de alta beta como SOL y ETH, las cuales se encontraban en zonas de sobreventa técnica (RSI cercano o inferior a 35) y muestran un repunte en las últimas 24 horas. Por otro lado, acciones como MSFT han entrado en sobrecompra (RSI superior a 70), lo que sugiere cautela en renta variable tecnológica tradicional, mientras mantenemos nuestras posiciones actuales en cripto aprovechando el momentum de recuperación."*

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 80%): ETH muestra un RSI de 35.1 saliendo de zona de sobreventa con un incremento del 1.73% en 24h. Mantenemos la posición ya que el rebote técnico está en desarrollo y aún no alcanza el objetivo de take-profit del +2.5%.
- **[HOLD] SOL-USD** (Confianza: 85%): SOL presenta un RSI de 30.2 respaldando un fuerte rebote técnico tras caídas semanales, registrando un avance diario del 2.31%. Conservamos la posición para maximizar el rendimiento hacia la zona de take-profit.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 14:10` | 🟢 BUY | `SOL-USD` | $5.16 | $111.90 | SOL-USD presenta un RSI de 28.2 indicando sobreventa clara tras una caída semanal del 7.33... |
| `2026-10-11 14:00` | 🟢 BUY | `SOL-USD` | $10.00 | $112.02 | SOL-USD se encuentra en clara sobreventa tecnica con un RSI de 28.5 tras una caida semanal... |
| `2026-10-11 13:40` | 🟢 BUY | `SOL-USD` | $10.00 | $111.79 | SOL-USD presenta una excelente oportunidad de rebote técnico de alta convicción al encontr... |
| `2026-10-11 13:30` | 🔴 SELL | `SOL-USD` | $19.04 | $111.95 | SOL-USD ha alcanzado un rendimiento cercano a nuestra meta de take-profit del 2.5% (+2.43%... |
| `2026-10-11 13:20` | 🟢 BUY | `ETH-USD` | $12.00 | $2531.44 | ETH-USD se encuentra en zona de profunda sobreventa técnica con un RSI de 32.8 y una caída... |

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
