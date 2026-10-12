# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 03:20:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$37.47 USD** | **$41.46 USD** | 🟢 **+3.66%** ($+1.46) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.245354 | $111.72 | $112.10 | $27.50 | 📈 +0.34% |
| `ETH-USD` | 0.003904 | $2561.78 | $2552.57 | $9.96 | 📉 -0.36% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un rebote técnico interesante en activos cripto que se encontraban bajo fuerte presión bajista la última semana. SOL-USD presenta un RSI muy atractivo de 28.8 en clara zona de sobreventa, mientras ETH-USD registra un RSI de 35.8. Mantenemos nuestras posiciones actuales y desplegamos el remanente de efectivo para aprovechar la sobreventa en SOL-USD y buscar el rebote de corto plazo."*

**Operaciones del ciclo:**
- **[BUY] SOL-USD** (Confianza: 86%): Aprovechamos la reserva de efectivo por encima del mínimo requerido ($4.00) para incrementar nuestra posición en SOL-USD. Su RSI de 28.8 indica una clara sobreventa técnica y un punto ideal para cazar un rebote rápido, cumpliendo con nuestra estrategia agresiva de mean reversion.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 03:20` | 🟢 BUY | `SOL-USD` | $2.92 | $112.10 | Aprovechamos la reserva de efectivo por encima del mínimo requerido ($4.00) para increment... |
| `2026-10-12 03:01` | 🟢 BUY | `ETH-USD` | $10.00 | $2561.78 | ETH-USD se encuentra en clara sobreventa técnica (RSI de 37) y muestra un repunte del 2.31... |
| `2026-10-12 03:01` | 🔴 SELL | `SOL-USD` | $16.91 | $112.74 | Vendemos parcialmente SOL-USD para capitalizar una pequeña ganancia y liberar efectivo, pe... |
| `2026-10-12 02:30` | 🟢 BUY | `SOL-USD` | $4.95 | $112.41 | SOL-USD mantiene un RSI en zona crítica de sobreventa (29.7) y un cambio positivo de 2.16%... |
| `2026-10-12 02:30` | 🔴 SELL | `ETH-USD` | $4.95 | $2553.65 | Tomamos beneficios totales en ETH-USD ya que se encuentra mostrando un rebote positivo per... |

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
