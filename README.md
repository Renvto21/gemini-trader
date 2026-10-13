# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 09:41:12`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.33 USD** | **$39.34 USD** | 🔴 **-1.66%** ($-0.66) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $106.35 | $31.39 | 📉 -0.77% |
| `ETH-USD` | 0.003177 | $2505.44 | $2499.37 | $7.94 | 📉 -0.24% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto presenta condiciones extremas de sobreventa con SOL-USD mostrando un RSI profundamente deprimido en 25.2 tras una caída semanal del 8.49%, lo cual representa una oportunidad ideal de rebote por reversión a la media (Mean Reversion). ETH-USD también muestra debilidad en las últimas sesiones con un RSI de 34.9, pero mantenemos nuestra posición actual operando sin exceder el riesgo ya que estamos casi fully invested. En el sector tecnológico, MSFT se encuentra en clara sobrecompra con un RSI de 77.9. Dado que nuestro capital está completamente desplegado y el efectivo actual es 0.0 USD, no realizaremos nuevas compras hasta asegurar liquidez, manteniendo nuestras posiciones actuales en cripto a la espera del rebote técnico."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD está en condiciones de extrema sobreventa (RSI 25.2), lo que aumenta considerablemente la probabilidad de un rebote técnico rápido del 2% al 6%. Mantenemos la posición para capturar el movimiento alcista sin vender en el suelo.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 08:30` | 🟢 BUY | `ETH-USD` | $7.96 | $2505.44 | ETH-USD muestra un RSI de 35.6 en zona de sobreventa y un cambio positivo de 2.45% en 24 h... |
| `2026-10-13 08:30` | 🔴 SELL | `NVDA` | $7.96 | $226.32 | Liberamos capital de NVDA que se encuentra lateral y bajo su SMA20 sin momentum claro, par... |
| `2026-10-13 08:10` | 🟢 BUY | `NVDA` | $7.96 | $226.32 | Aprovechamos la corrección reciente de NVDA (caída de 7 días del -3.26% con un RSI de 46.4... |
| `2026-10-13 08:10` | 🔴 SELL | `ETH-USD` | $7.96 | $2494.07 | Ejecutamos rotación activa de capital vendiendo la posición completa de ETH-USD para liber... |
| `2026-10-13 02:30` | 🟢 BUY | `SOL-USD` | $4.00 | $108.19 | SOL-USD presenta un RSI extremadamente bajo de 26.3, lo que indica sobreventa técnica seve... |

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
