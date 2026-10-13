# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 08:50:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.31 USD** | **$39.31 USD** | 🔴 **-1.73%** ($-0.69) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $106.30 | $31.38 | 📉 -0.81% |
| `ETH-USD` | 0.003177 | $2505.44 | $2496.00 | $7.93 | 📉 -0.38% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa, destacando SOL-USD con un RSI de 25.1, lo que representa una oportunidad ideal de rebote técnico por reversión a la media. ETH-USD también se encuentra en zona de sobreventa con un RSI de 34.5. Mantendremos nuestras posiciones actuales ya que están cerca de puntos de inflexión alcista y no han tocado los límites de stop-loss estricto (-2.5%), operando con paciencia táctica para capturar el impulso de recuperación."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD presenta un RSI extremadamente bajo de 25.1 tras una caída semanal del -8.54%. Estamos ante un claro escenario de sobreventa profunda ideal para cazar un rebote técnico. Mantenemos la posición para capturar el movimiento alcista inminente.

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
