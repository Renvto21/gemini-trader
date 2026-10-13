# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 07:50:35`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.33 USD** | **$39.33 USD** | 🔴 **-1.69%** ($-0.67) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $106.27 | $31.37 | 📉 -0.84% |
| `ETH-USD` | 0.003192 | $2506.03 | $2492.04 | $7.96 | 📉 -0.56% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones claras de sobreventa en activos clave como SOL-USD (RSI de 25.0) y ETH-USD (RSI de 34.1), lo cual activa nuestra estrategia de Mean Reversion para buscar rebotes técnicos agresivos. El portafolio actual se encuentra completamente invertido con pérdidas no realizadas menores al 1% en ambos criptoactivos, respetando los límites de stop-loss pero manteniendo el enfoque en la captura de momentum alcista de corto plazo. Mantendremos las posiciones actuales para permitirles rebotar tras el descuento reciente de los últimos 7 días."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL se encuentra en una situación extrema de sobreventa con un RSI de 25.0 y una caída de -8.56% en los últimos 7 días. Está perfectamente alineado con nuestra estrategia de cazar rebotes técnicos, y la pérdida actual (-0.84%) está muy lejos de activar nuestro stop-loss, por lo que debemos mantener la posición para capturar el rebote inminente.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH muestra un RSI de 34.1, entrando en zona de sobreventa con un intento de recuperación del 1.95% en las últimas 24 horas. La pérdida actual es marginal (-0.56%) y el activo tiene el momentum necesario para buscar un movimiento hacia la resistencia a corto plazo.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 02:30` | 🟢 BUY | `SOL-USD` | $4.00 | $108.19 | SOL-USD presenta un RSI extremadamente bajo de 26.3, lo que indica sobreventa técnica seve... |
| `2026-10-13 01:30` | 🟢 BUY | `SOL-USD` | $6.23 | $107.75 | SOL-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.8 tras una caída s... |
| `2026-10-13 01:10` | 🟢 BUY | `ETH-USD` | $8.00 | $2506.03 | ETH-USD se encuentra en clara sobreventa técnica con un RSI de 31.1 tras una caída semanal... |
| `2026-10-13 01:10` | 🔴 SELL | `SOL-USD` | $16.14 | $107.57 | Vendemos parcialmente SOL-USD para liberar liquidez y poder financiar la entrada en ETH-US... |
| `2026-10-13 01:00` | 🟢 BUY | `SOL-USD` | $12.00 | $107.31 | Aprovechamos la sobreventa extrema de SOL-USD (RSI 25.3 y caída semanal de -11.16%) para i... |

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
