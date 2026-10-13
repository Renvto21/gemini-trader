# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 21:00:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$35.18 USD** | **$39.18 USD** | 🔴 **-2.06%** ($-0.82) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.220744 | $106.59 | $105.73 | $23.34 | 📉 -0.81% |
| `ETH-USD` | 0.004838 | $2480.41 | $2447.61 | $11.84 | 📉 -1.32% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto presenta condiciones de sobreventa extrema, con SOL-USD registrando un RSI de 23.7 y ETH-USD un RSI de 27.7, lo cual representa una oportunidad ideal de Mean Reversion para cazar rebotes técnicos rápidos. Por otro lado, las posiciones actuales muestran minusvalías controladas que aún no alcanzan el límite estricto de stop-loss, y el efectivo disponible es de apenas $4.00 USD. Dado que buscamos maximizar el rendimiento y capturar rebotes inminentes, mantendremos las posiciones actuales para permitirles rebotar desde estos niveles de sobreventa."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL se encuentra en niveles de sobreventa extrema (RSI 23.7) tras una fuerte caída semanal. Aunque la tendencia es bajista, el potencial de un rebote técnico a corto plazo es muy alto. Mantenemos la posición para capturar la recuperación sin gastar liquidez adicional.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 20:10` | 🟢 BUY | `SOL-USD` | $5.53 | $106.20 | SOL-USD presenta una condición de sobreventa extrema con un RSI de 24.1 y una caída de 7 d... |
| `2026-10-12 20:00` | 🟢 BUY | `SOL-USD` | $8.00 | $106.40 | SOL-USD se encuentra en clara sobreventa con un RSI de 24.3 y una caída de -11.91% en 7 dí... |
| `2026-10-12 19:40` | 🟢 BUY | `ETH-USD` | $12.00 | $2480.41 | ETH-USD se encuentra en una clara condición de sobreventa con un RSI de 14 de 29.5 y una c... |
| `2026-10-12 19:30` | 🟢 BUY | `SOL-USD` | $10.00 | $106.97 | SOL-USD se encuentra en clara condición de sobreventa profunda con un RSI de 24.9 y una ca... |
| `2026-10-12 19:20` | 🔴 SELL | `SOL-USD` | $39.52 | $106.94 | La posición actual en SOL-USD acumula un PnL de -2.11% acercándose peligrosamente al stop-... |

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
