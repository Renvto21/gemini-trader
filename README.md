# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 23:30:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.43 USD** | **$12.00 USD** | **$39.43 USD** | 🔴 **-1.44%** ($-0.57) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `GLD` | 0.031401 | $382.15 | $382.15 | $12.00 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con debilidad y correcciones recientes en criptomonedas y tecnología de alto beta. Las posiciones actuales de SOL-USD y ETH-USD han alcanzado ganancias del +2.78% y +2.57% respectivamente, cumpliendo estrictamente con la regla táctica de toma rápida de ganancias (Take-Profit) al superar el umbral del +2.5%. Además, GLD presenta un RSI de sobreventa extrema en 34.6, lo que representa una excelente oportunidad de rebote técnico (Mean Reversion)."*

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 90%): La posición ha alcanzado una ganancia del +2.78%, cumpliendo con la regla de Take-Profit (+2.5%). Vendemos el total para asegurar ganancias en efectivo y rotar el capital hacia nuevas oportunidades.
- **[SELL] ETH-USD** (Confianza: 90%): La posición registra un beneficio del +2.57%, alcanzando el objetivo de toma rápida de ganancias. Ejecutamos la venta total para liberar liquidez y maximizar la rotación del portafolio.
- **[BUY] GLD** (Confianza: 85%): Aprovechamos la liquidez liberada y el efectivo disponible para cazar un rebote técnico en GLD, el cual se encuentra en clara sobreventa con un RSI de 34.6. Asignamos una entrada de alta convicción para capturar el movimiento de reversión alcista.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 23:30` | 🟢 BUY | `GLD` | $12.00 | $382.15 | Aprovechamos la liquidez liberada y el efectivo disponible para cazar un rebote técnico en... |
| `2026-10-12 23:30` | 🔴 SELL | `ETH-USD` | $10.26 | $2479.99 | La posición registra un beneficio del +2.57%, alcanzando el objetivo de toma rápida de gan... |
| `2026-10-12 23:30` | 🔴 SELL | `SOL-USD` | $20.56 | $106.33 | La posición ha alcanzado una ganancia del +2.78%, cumpliendo con la regla de Take-Profit (... |
| `2026-10-12 22:00` | 🟢 BUY | `SOL-USD` | $10.00 | $103.02 | SOL-USD presenta un RSI extremadamente bajo de 21.3 tras una caída del -7.39% en 24 horas.... |
| `2026-10-12 21:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2417.81 | ETH-USD se encuentra en una profunda corrección con una caída de -4.61% en 24h y un RSI de... |

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
