# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 16:20:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.71 USD** | **$39.72 USD** | 🔴 **-0.71%** ($-0.28) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001175 | $2553.82 | $2508.28 | $2.95 | 📉 -1.78% |
| `SOL-USD` | 0.342237 | $109.34 | $107.43 | $36.77 | 📉 -1.75% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra una corrección moderada en criptomonedas y tecnología de alto beta. SOL-USD y ETH-USD se encuentran en niveles extremos de sobreventa técnica (RSI de 25.4 y 31.2 respectivamente), lo cual activa nuestra estrategia de cazar rebotes por mean reversion. El capital actual está totalmente desplegado en cripto con pérdidas no realizadas menores al 2%, manteniéndose lejos de nuestro stop-loss estricto (-2.5% a -3.0%). Dado que no hay efectivo disponible y las criptomonedas están listas para un rebote técnico inminente, optamos por mantener nuestras posiciones actuales para capturar la recuperación de corto plazo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD presenta un RSI extremadamente bajo de 25.4, lo que indica sobreventa profunda. Aunque acumula una pérdida temporal de -1.75%, no ha tocado el stop-loss estricto de -2.5% y las condiciones favorecen un rebote técnico inminente hacia la media.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD se encuentra con un RSI de 31.2 en zona de sobreventa. Mantenemos la posición ya que se alinea con la estrategia de capturar rebotes rápidos en criptoactivos de alta volatilidad sin incurrir en pérdidas innecesarias por ventas prematuras.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 15:40` | 🟢 BUY | `SOL-USD` | $4.00 | $107.58 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 25.6 y una caída acumulada ... |
| `2026-10-12 12:20` | 🟢 BUY | `SOL-USD` | $3.42 | $108.91 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 27.1 y una caída acumulada ... |
| `2026-10-12 12:10` | 🟢 BUY | `SOL-USD` | $10.00 | $108.93 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 27.2 y una... |
| `2026-10-12 12:01` | 🟢 BUY | `SOL-USD` | $10.00 | $109.96 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 28.5 y una caída semanal de... |
| `2026-10-12 11:50` | 🟢 BUY | `SOL-USD` | $10.00 | $110.00 | SOL-USD presenta un RSI de 28.6 indicando sobreventa extrema y una caída acumulada semanal... |

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
