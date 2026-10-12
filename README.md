# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 20:20:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$35.37 USD** | **$39.36 USD** | 🔴 **-1.59%** ($-0.64) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.220744 | $106.59 | $106.24 | $23.45 | 📉 -0.33% |
| `ETH-USD` | 0.004838 | $2480.41 | $2463.13 | $11.92 | 📉 -0.70% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto y tecnológico muestra un comportamiento bajista a corto plazo con caídas marcadas en SOL-USD y ETH-USD, lo que ha llevado a ambos activos a condiciones extremas de sobreventa técnica con valores de RSI de 24.2 y 28.5 respectivamente. Nuestra reserva de efectivo se encuentra en el límite mínimo ($4.00), y las posiciones actuales están experimentando un retroceso menor pero se mantienen operando dentro de márgenes aceptables de stop-loss, sin alcanzar aún la necesidad de una venta forzosa por pérdida profunda. Dado que no hay liquidez libre adicional para abrir nuevas posiciones de rebote y las posiciones actuales están estancadas cerca de 0% de PnL sin momentum positivo inmediato, optamos por mantener nuestra exposición actual esperando la recuperación técnica en los niveles de sobreventa actuales."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): A pesar de la caída del 4.5% en 24 horas y el RSI en sobreventa extrema (24.2), la posición se encuentra dentro del rango operativo sin romper el stop-loss estricto del -3%. Mantenemos para buscar el rebote técnico esperado por mean reversion.

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
