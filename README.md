# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 23:40:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.43 USD** | **$12.00 USD** | **$39.43 USD** | 🔴 **-1.44%** ($-0.57) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.112803 | $106.38 | $106.38 | $12.00 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa con Solana (SOL-USD) registrando un RSI de 24.3 y Ethereum (ETH-USD) en 29.5, lo que representa una oportunidad ideal de rebote por reversión a la media (Mean Reversion). GLD se encuentra estancado sin momentum, por lo que rotaremos ese capital para cazar el rebote de alta convicción en SOL."*

**Operaciones del ciclo:**
- **[SELL] GLD** (Confianza: 90%): Posición estancada con rendimiento de 0% sin momentum alcista. Vendo la totalidad para liberar capital y financiar oportunidades de alto potencial en cripto.
- **[BUY] SOL-USD** (Confianza: 90%): SOL-USD presenta una clara condición de sobreventa técnica extrema con RSI de 24.3 tras una caída de doble dígito en 7 días. Es una oportunidad ideal de rebote rápido buscando un objetivo de +4% a +6% cumpliendo nuestra estrategia agresiva.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 23:40` | 🟢 BUY | `SOL-USD` | $12.00 | $106.38 | SOL-USD presenta una clara condición de sobreventa técnica extrema con RSI de 24.3 tras un... |
| `2026-10-12 23:40` | 🔴 SELL | `GLD` | $12.00 | $382.15 | Posición estancada con rendimiento de 0% sin momentum alcista. Vendo la totalidad para lib... |
| `2026-10-12 23:30` | 🟢 BUY | `GLD` | $12.00 | $382.15 | Aprovechamos la liquidez liberada y el efectivo disponible para cazar un rebote técnico en... |
| `2026-10-12 23:30` | 🔴 SELL | `ETH-USD` | $10.26 | $2479.99 | La posición registra un beneficio del +2.57%, alcanzando el objetivo de toma rápida de gan... |
| `2026-10-12 23:30` | 🔴 SELL | `SOL-USD` | $20.56 | $106.33 | La posición ha alcanzado una ganancia del +2.78%, cumpliendo con la regla de Take-Profit (... |

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
