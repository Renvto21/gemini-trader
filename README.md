# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 07:30:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.29 USD** | **$40.29 USD** | 🟢 **+0.72%** ($+0.29) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.330438 | $109.27 | $109.39 | $36.15 | 📈 +0.11% |
| `ETH-USD` | 0.001656 | $2499.59 | $2499.12 | $4.14 | 📉 -0.02% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra divergencias interesantes. Las criptomonedas se encuentran profundamente en territorio de sobreventa técnica con SOL-USD registrando un RSI de 21.3 y ETH-USD en 28.2, lo cual activa nuestra estrategia de cazar rebotes por mean reversion. Por otro lado, activos tecnológicos como MSFT han entrado en sobrecompra con un RSI de 72.3 tras fuertes subidas. Mantenemos una postura agresiva manteniendo nuestras posiciones en cripto mientras consolidamos capital para posibles rotaciones rápidas si se activan stops o tomas de ganancias."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD está en condición de extrema sobreventa con un RSI de 21.3 y una fuerte caída semanal del -9.41%. Aunque está bajo la SMA20, esperamos un rebote técnico inminente hacia la resistencia cercana para capturar un movimiento del +3% al +5%.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD presenta un RSI de 28.2, mostrando clara sobreventa técnica y preparándose para acompañar el rebote de la cripto principal. La pérdida actual es insignificante y mantenemos la posición para capturar el impulso alcista.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 05:00` | 🟢 BUY | `ETH-USD` | $4.14 | $2499.59 | ETH-USD presenta un RSI de 28.2, lo que indica una clara condición de sobreventa técnica t... |
| `2026-10-11 04:50` | 🟢 BUY | `SOL-USD` | $12.00 | $109.36 | Alta convicción en el rebote técnico de Solana tras una caída semanal del -9.43% y un RSI ... |
| `2026-10-11 04:50` | 🔴 SELL | `ETH-USD` | $16.12 | $2500.30 | Rotamos capital fuera de ETH-USD para asegurar una pequeña ganancia del +0.75% y liberar l... |
| `2026-10-11 03:20` | 🟢 BUY | `SOL-USD` | $12.00 | $109.35 | SOL-USD se encuentra en una situación de sobreventa técnica masiva con un RSI de 14 en 21.... |
| `2026-10-11 03:20` | 🔴 SELL | `MSFT` | $12.00 | $535.07 | MSFT ha entrado en zona de sobrecompra técnica con un RSI de 72.3. Aplicando la regla táct... |

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
