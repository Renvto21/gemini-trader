# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 10:20:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.15 USD** | **$36.16 USD** | **$40.30 USD** | 🟢 **+0.76%** ($+0.30) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.330438 | $109.27 | $109.42 | $36.16 | 📈 +0.13% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra divergencias interesantes. Las criptomonedas SOL-USD y ETH-USD se encuentran en niveles extremos de sobreventa técnica con un RSI de 21.3 y 28.5 respectivamente, tras caídas semanales significativas. Esto presenta una oportunidad clásica de rebote técnico (Mean Reversion). Por otro lado, activos tecnológicos y el mercado general muestran resiliencia, con MSFT alcanzando un RSI de sobrecompra (>70). Nuestro portafolio actual está totalmente invertido sin efectivo disponible, por lo que realizaremos una rotación parcial para liberar liquidez y comprar un activo con mayor impulso o aprovechar el rebote."*

**Operaciones del ciclo:**
- **[SELL] ETH-USD** (Confianza: 85%): Vendemos la posición completa en ETH-USD para liberar liquidez. Aunque tiene sobreventa, concentraremos nuestro capital limitado en SOL-USD que muestra una caída semanal más profunda y mayor potencial de rebote agresivo por alta volatilidad.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 10:20` | 🔴 SELL | `ETH-USD` | $4.15 | $2504.04 | Vendemos la posición completa en ETH-USD para liberar liquidez. Aunque tiene sobreventa, c... |
| `2026-10-11 08:40` | 🟢 BUY | `ETH-USD` | $4.14 | $2500.14 | ETH-USD se encuentra en clara sobreventa con un RSI de 28.2 y una caída de 7.78% en los úl... |
| `2026-10-11 08:00` | 🔴 SELL | `ETH-USD` | $4.14 | $2498.90 | Vendemos la posición completa de ETH-USD para liberar 4.14 USD en efectivo. Aunque está en... |
| `2026-10-11 05:00` | 🟢 BUY | `ETH-USD` | $4.14 | $2499.59 | ETH-USD presenta un RSI de 28.2, lo que indica una clara condición de sobreventa técnica t... |
| `2026-10-11 04:50` | 🟢 BUY | `SOL-USD` | $12.00 | $109.36 | Alta convicción en el rebote técnico de Solana tras una caída semanal del -9.43% y un RSI ... |

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
