# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 07:30:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$7.00 USD** | **$34.32 USD** | **$41.32 USD** | 🟢 **+3.30%** ($+1.32) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.307862 | $111.77 | $111.47 | $34.32 | 📉 -0.27% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones claras de sobreventa en activos clave como SOL-USD (RSI de 31.2) y ETH-USD (RSI de 35.7), lo que activa nuestra estrategia de Mean Reversion y búsqueda de rebotes tácticos rápidos. Por otro lado, en el sector tecnológico, MSFT ha entrado en territorio de sobrecompra (RSI 72.3), mientras que QQQ y SPY muestran fortaleza alcista moderada. Nuestro portafolio se encuentra completamente invertido con liquidez en cero, por lo que realizaremos una rotación parcial vendiendo la posición lateral de ETH-USD para liberar capital y reasignarlo a una nueva oportunidad de alta convicción."*

**Operaciones del ciclo:**
- **[SELL] ETH-USD** (Confianza: 85%): ETH-USD se encuentra estancado con un PnL cercano a 0% sin momentum inmediato. Vendemos la posición completa para liberar los 7.00 USD de efectivo y rotar el capital hacia oportunidades con mayor potencial de rebote y alta volatilidad.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 07:30` | 🔴 SELL | `ETH-USD` | $7.00 | $2553.60 | ETH-USD se encuentra estancado con un PnL cercano a 0% sin momentum inmediato. Vendemos la... |
| `2026-10-12 07:00` | 🟢 BUY | `SOL-USD` | $4.00 | $111.65 | SOL-USD está en zona de sobreventa profunda con un RSI de 31.8 y una caída semanal de -7.5... |
| `2026-10-12 06:10` | 🟢 BUY | `ETH-USD` | $2.00 | $2552.03 | ETH-USD presenta un RSI de 35.5 en clara zona de sobreventa tras caídas semanales del -5.3... |
| `2026-10-12 05:50` | 🟢 BUY | `ETH-USD` | $5.00 | $2553.65 | ETH-USD presenta un RSI de 35.7 en clara zona de sobreventa técnica tras una caída semanal... |
| `2026-10-12 05:50` | 🔴 SELL | `SOL-USD` | $5.00 | $111.85 | Liberamos una pequeña porción de SOL-USD para rescatar liquidez y financiar una entrada tá... |

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
