# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 14:00:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$35.83 USD** | **$39.83 USD** | 🔴 **-0.42%** ($-0.17) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001175 | $2553.82 | $2510.94 | $2.95 | 📉 -1.68% |
| `SOL-USD` | 0.305055 | $109.55 | $107.78 | $32.88 | 📉 -1.62% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto se encuentra en condiciones de sobreventa extrema, destacando SOL-USD con un RSI de 25.8 y ETH-USD con un RSI de 31.4, lo que activa nuestra estrategia de Mean Reversion para buscar un rebote técnico rápido. Mantenemos una posición pesada en SOL-USD que sufre una ligera pérdida, pero dentro de parámetros de control. Con un efectivo muy ajustado, la prioridad es mantener las posiciones actuales en cripto aprovechando los niveles de sobreventa o rotar si es necesario, pero dado que estamos cerca de soportes clave y cumplimos la regla de mantener baja liquidez, optamos por mantener nuestras posiciones actuales para capturar el rebote inminente."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD presenta un RSI extremadamente bajo de 25.8 en zona de profunda sobreventa. Aunque registra una caída del -1.62%, la estrategia agresiva de mean reversion nos dicta mantener y acumular potencial de rebote rápido del +2% al +6% sin vender en el suelo.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 12:20` | 🟢 BUY | `SOL-USD` | $3.42 | $108.91 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 27.1 y una caída acumulada ... |
| `2026-10-12 12:10` | 🟢 BUY | `SOL-USD` | $10.00 | $108.93 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 27.2 y una... |
| `2026-10-12 12:01` | 🟢 BUY | `SOL-USD` | $10.00 | $109.96 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 28.5 y una caída semanal de... |
| `2026-10-12 11:50` | 🟢 BUY | `SOL-USD` | $10.00 | $110.00 | SOL-USD presenta un RSI de 28.6 indicando sobreventa extrema y una caída acumulada semanal... |
| `2026-10-12 11:40` | 🔴 SELL | `SOL-USD` | $37.42 | $108.72 | Activación del stop-loss estricto debido a que la posición ha caído un -2.58%, rompiendo e... |

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
