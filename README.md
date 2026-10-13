# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 21:20:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$34.69 USD** | **$38.69 USD** | 🔴 **-3.29%** ($-1.31) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.220744 | $106.59 | $104.04 | $22.97 | 📉 -2.40% |
| `ETH-USD` | 0.004838 | $2480.41 | $2423.07 | $11.72 | 📉 -2.31% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto se encuentra bajo una fuerte presión bajista a corto plazo, con SOL-USD y ETH-USD mostrando condiciones extremas de sobreventa técnica con RSI de 22.2 y 26.5 respectivamente, acercándose peligrosamente a nuestros límites de stop-loss (-2.4% y -2.31%). Sin embargo, la estrategia de reversión a la media nos indica que estas caídas pronunciadas sin fundamentos macroeconómicos adversos nuevos representan oportunidades clásicas de rebote técnico. Mantendremos las posiciones actuales para evitar realizar pérdidas prematuras y aprovecharemos el efectivo disponible de 4.0 USD para mantenernos en modo HOLD, vigilando el soporte crítico."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): El RSI de 22.2 indica una sobreventa extrema. Aunque estamos con una pérdida flotante de -2.4%, aún no se ha alcanzado el stop-loss estricto del -3.0%. Esperamos un rebote técnico inminente hacia la media.

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
