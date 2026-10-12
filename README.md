# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 15:20:36`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$35.78 USD** | **$39.78 USD** | 🔴 **-0.54%** ($-0.22) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001175 | $2553.82 | $2511.14 | $2.95 | 📉 -1.67% |
| `SOL-USD` | 0.305055 | $109.55 | $107.62 | $32.83 | 📉 -1.77% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema, con SOL-USD registrando un RSI de 25.6 y una caída semanal del 10.9%, mientras ETH-USD presenta un RSI de 31.4. Estas condiciones son ideales para activar nuestra estrategia agresiva de rebote técnico (mean reversion). Dado que nuestras posiciones actuales están ligeramente en negativo pero cerca de los niveles de stop-loss sin haber roto agresivamente a la baja, y considerando que ya estamos invertidos casi al 100% con solo $4.00 de efectivo, mantendremos la exposición actual para permitir que el rebote técnico se materialice."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en un claro estado de sobreventa técnica con un RSI de 25.6 y una caída del 10.9% en 7 días. Aunque estamos experimentando una pérdida flotante del -1.77%, no ha alcanzado nuestro stop-loss estricto del -3%. Las condiciones actuales son óptimas para un rebote inminente de corto plazo, por lo que decidimos mantener la posición para capturar la recuperación.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un RSI de 31.4, acercándose a la zona de sobreventa profunda. Mantenemos la posición actual para acompañar el movimiento de recuperación junto con el ecosistema cripto, esperando un rebote rápido que nos permita tomar ganancias o rotar capital.

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
