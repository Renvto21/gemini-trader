# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 20:10:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$35.36 USD** | **$39.35 USD** | 🔴 **-1.61%** ($-0.65) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.220744 | $106.59 | $106.20 | $23.44 | 📉 -0.37% |
| `ETH-USD` | 0.004838 | $2480.41 | $2462.87 | $11.92 | 📉 -0.71% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema con ETH-USD (RSI 28.5) y SOL-USD (RSI 24.1) cotizando a la baja pero acercándose a zonas ideales de rebote técnico (Mean Reversion). Dado que nuestras posiciones actuales en SOL-USD y ETH-USD se encuentran ligeramente en negativo pero dentro del rango de tolerancia y sin romper el stop-loss estricto del -2.5% a -3.0%, mantenemos la calma y aprovechamos la liquidez disponible de $9.53 USD para incrementar exposición en SOL-USD, aprovechando su RSI profundamente deprimido para cazar un rebote rápido a corto plazo."*

**Operaciones del ciclo:**
- **[BUY] SOL-USD** (Confianza: 88%): SOL-USD presenta una condición de sobreventa extrema con un RSI de 24.1 y una caída de 7 días del -12.08%. Esto representa una oportunidad clásica de rebote técnico (Mean Reversion) bajo nuestra estrategia agresiva. Asignamos $5.53 USD para capitalizar este movimiento alcista inminente, manteniendo el efectivo operativo al límite mínimo requerido.

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
