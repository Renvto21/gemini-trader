# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 21:10:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$34.71 USD** | **$38.71 USD** | 🔴 **-3.23%** ($-1.29) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.220744 | $106.59 | $104.13 | $22.99 | 📉 -2.31% |
| `ETH-USD` | 0.004838 | $2480.41 | $2423.40 | $11.72 | 📉 -2.30% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto presenta una fuerte sobreventa técnica con SOL-USD en un RSI de 22.2 y ETH-USD en 26.5, acercándose peligrosamente a nuestros límites de stop-loss pero ofreciendo una clara oportunidad de rebote por mean reversion. Por otro lado, MSFT muestra un RSI de 72.3 en zona de sobrecompra. Mantendremos nuestras posiciones actuales en cripto aprovechando la alta sobreventa y la liquidez actual para buscar un rebote técnico rápido."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): A pesar de la caída del 2.31%, el RSI extremadamente bajo de 22.2 indica una sobreventa profunda. Mantenemos la posición para capturar el rebote técnico inminente sin activar el stop-loss prematuramente.
- **[HOLD] ETH-USD** (Confianza: 78%): Con un RSI de 26.5 y una pérdida no realizada del 2.3%, ETH-USD se encuentra en niveles ideales de soporte para un rebote de reversión a la media. Conservamos la posición.

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
