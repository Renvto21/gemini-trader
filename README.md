# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 05:30:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.23 USD** | **$40.24 USD** | 🟢 **+0.59%** ($+0.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.330438 | $109.27 | $109.24 | $36.10 | 📉 -0.03% |
| `ETH-USD` | 0.001656 | $2499.59 | $2497.75 | $4.14 | 📉 -0.07% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa con SOL-USD en un RSI de 21.1 y ETH-USD en 28.1, tras una corrección semanal importante (-9.53% y -7.87%). Estas lecturas extremas cumplen perfectamente con nuestra estrategia de mean reversion y búsqueda de rebotes rápidos. Por otro lado, las posiciones actuales están estancadas con rendimiento cercano al 0% y sin momentum a corto plazo. Mantener SOL y ETH es óptimo en este momento debido al potencial inminente de rebote técnico alcista desde estos niveles de sobreventa profunda, por lo que decidimos mantener ambas posiciones a la espera del impulso alcista."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD se encuentra en sobreventa extrema con un RSI de 21.1 tras una fuerte caída semanal. La estrategia exige cazar rebotes en cripto bajo estas condiciones, por lo que mantener la posición actual maximiza la exposición al inevitable rebote técnico de reversión a la media.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH-USD muestra un RSI de 28.1, situándose también en territorio de sobreventa profunda. Mantenemos la posición para capturar el rebote alcista esperado en el corto plazo sin incurrir en costos de transacción innecesarios.

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
