# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 08:00:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.17 USD** | **$40.28 USD** | 🟢 **+0.71%** ($+0.28) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.54 | $20.09 | 📈 +0.47% |
| `ETH-USD` | 0.006448 | $2481.58 | $2493.66 | $16.08 | 📈 +0.49% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto se encuentra en una fase de fuerte sobreventa técnica con los RSI de SOL-USD en 22.4 y ETH-USD en 26.2, lo que presenta condiciones ideales para un rebote de reversión a la media. Por otro lado, las acciones tecnológicas (MSFT) muestran sobrecompra con RSI superior a 70, mientras que el índice QQQ y NVDA se mantienen estables. Nuestras posiciones actuales en SOL-USD y ETH-USD están estancadas con ganancias mínimas (+0.47% y +0.49%) y aún no alcanzan el objetivo de take-profit del +2.5%. Dado que el efectivo disponible es de solo $4.11 USD (respetando la reserva mínima) y no hay señales de ruptura de stop-loss ni saturación de take-profit, la estrategia óptima en este momento es mantener (HOLD) las posiciones actuales mientras esperamos la activación del rebote técnico en criptomonedas."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD mantiene un RSI extremadamente bajo (22.4), lo que indica una clara sobreventa y un potencial inminente de rebote técnico. La posición actual de $20.09 USD tiene una ganancia leve de +0.47%, manteniéndose lejos del stop-loss de -2.5% y esperando el impulso alcista hacia el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD muestra un RSI de 26.2, reflejando condiciones de sobreventa similares a las de Solana. La posición actual está intacta con una ganancia de +0.49%, por lo que se mantiene para capturar el esperado rebote de corto plazo.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-09 19:00` | 🟢 BUY | `ETH-USD` | $5.00 | $2482.07 | ETH-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.0. Utilizando el c... |
| `2026-10-09 19:00` | 🔴 SELL | `NVDA` | $4.99 | $229.28 | Rotación activa de capital. NVDA se encuentra estancada con un rendimiento de -0.16% y un ... |
| `2026-10-09 18:50` | 🟢 BUY | `SOL-USD` | $5.00 | $108.91 | Oportunidad de alta convicción por sobreventa extrema. SOL-USD tiene un RSI de 20.2 tras u... |
| `2026-10-09 18:50` | 🔴 SELL | `QQQ` | $5.00 | $751.27 | Rotación de capital activo. QQQ se encuentra estancado con rendimiento plano (-0.06%) y si... |
| `2026-10-09 18:40` | 🟢 BUY | `SOL-USD` | $5.00 | $109.02 | SOL-USD está extremadamente sobrevendido con un RSI de 20.3. Ejecutamos una compra agresiv... |

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
