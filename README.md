# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 13:30:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$36.16 USD** | **$40.16 USD** | 🟢 **+0.41%** ($+0.16) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001175 | $2553.82 | $2527.38 | $2.97 | 📉 -1.04% |
| `SOL-USD` | 0.305055 | $109.55 | $108.81 | $33.19 | 📉 -0.68% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de clara sobreventa a corto plazo, destacando SOL-USD con un RSI de 27.0 y ETH-USD con RSI de 32.5, lo cual activa nuestra estrategia de reversión a la media (Mean Reversion) para cazar rebotes técnicos agresivos. Ambas posiciones actuales están ligeramente en rojo pero dentro de los límites del stop-loss, y dado que buscamos maximizar el potencial de rebote sin sobrepasar el efectivo disponible, mantendremos las posiciones actuales para permitirles cumplir su ciclo de recuperación."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL se encuentra en una zona de sobreventa extrema con un RSI de 27.0 tras una caída semanal del 9.92%. Mantenemos la posición para capturar el rebote técnico esperado hacia la resistencia inmediata sin activar el stop-loss, ya que la caída actual es de -0.68%.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH muestra un RSI de 32.5 aproximándose a la zona de sobreventa y una caída moderada del -1.04%. Esperamos una reacción compradora en este nivel de soporte técnico antes de considerar cualquier rotación de capital.

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
