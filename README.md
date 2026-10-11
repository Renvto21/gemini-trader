# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 06:00:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.29 USD** | **$40.29 USD** | 🟢 **+0.73%** ($+0.29) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.330438 | $109.27 | $109.40 | $36.15 | 📈 +0.12% |
| `ETH-USD` | 0.001656 | $2499.59 | $2498.46 | $4.14 | 📉 -0.05% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa con SOL-USD (RSI en 21.3) y ETH-USD (RSI en 28.1), lo cual representa una excelente oportunidad de rebote técnico (Mean Reversion) a corto plazo. Mantenemos nuestras posiciones actuales en criptomonedas debido a que se encuentran operando cerca de sus zonas de soporte y no han roto los stop-loss estrictos del -2.5% a -3.0%. Por otro lado, en el sector tecnológico, MSFT ha entrado en sobrecompra (RSI en 72.3), pero dado que no lo tenemos en cartera y nuestro efectivo actual es cero, la estrategia se centra en mantener la paciencia y sostener las posiciones de criptomonedas actuales esperando el impulso alcista que permita asegurar beneficios rápidos."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en una situación de extrema sobreventa con un RSI de 21.3 y una caída semanal del 9.4%. No ha activado el stop-loss y está listo para un rebote técnico inminente hacia la zona de take-profit.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un RSI de 28.1 en zona de sobreventa clara. Mantenemos la posición para capturar el rebote de reversión a la media sin asumir pérdidas prematuras.

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
