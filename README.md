# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 08:00:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.14 USD** | **$36.10 USD** | **$40.24 USD** | 🟢 **+0.60%** ($+0.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.330438 | $109.27 | $109.24 | $36.10 | 📉 -0.03% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con sesgo alcista moderado en los índices principales (SPY y QQQ con tendencias alcistas saludables y RSI en zona neutral alta). Sin embargo, el sector cripto se encuentra castigado con caídas semanales importantes y niveles de sobreventa extremos, especialmente en SOL-USD (RSI de 21.1) y ETH-USD (RSI de 28.1). Esto representa una oportunidad clásica de rebote técnico por reversión a la media (mean reversion). Dado que nuestras posiciones actuales en SOL y ETH están estancadas con un rendimiento cercano a cero y sin momentum inmediato, y teniendo en cuenta que el efectivo actual es 0, optaremos por mantener la posición principal en SOL-USD debido a su altísimo potencial de rebote inminente por sobreventa extrema, y realizaremos una pequeña venta parcial en ETH-USD para liberar liquidez y rotar hacia una oportunidad de mayor impulso en el sector tecnológico o mantenernos ágiles."*

**Operaciones del ciclo:**
- **[SELL] ETH-USD** (Confianza: 82%): Vendemos la posición completa de ETH-USD para liberar 4.14 USD en efectivo. Aunque está en sobreventa, SOL-USD ofrece un perfil de beta más alto y mayor potencial de rebote rápido, permitiéndonos rotar este capital hacia oportunidades más dinámicas o cumplir con la estrategia de agilidad de cartera.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 08:00` | 🔴 SELL | `ETH-USD` | $4.14 | $2498.90 | Vendemos la posición completa de ETH-USD para liberar 4.14 USD en efectivo. Aunque está en... |
| `2026-10-11 05:00` | 🟢 BUY | `ETH-USD` | $4.14 | $2499.59 | ETH-USD presenta un RSI de 28.2, lo que indica una clara condición de sobreventa técnica t... |
| `2026-10-11 04:50` | 🟢 BUY | `SOL-USD` | $12.00 | $109.36 | Alta convicción en el rebote técnico de Solana tras una caída semanal del -9.43% y un RSI ... |
| `2026-10-11 04:50` | 🔴 SELL | `ETH-USD` | $16.12 | $2500.30 | Rotamos capital fuera de ETH-USD para asegurar una pequeña ganancia del +0.75% y liberar l... |
| `2026-10-11 03:20` | 🟢 BUY | `SOL-USD` | $12.00 | $109.35 | SOL-USD se encuentra en una situación de sobreventa técnica masiva con un RSI de 14 en 21.... |

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
