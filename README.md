# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 17:40:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.68 USD** | **$34.97 USD** | **$39.65 USD** | 🔴 **-0.87%** ($-0.35) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.279466 | $107.20 | $107.24 | $29.97 | 📈 +0.04% |
| `ETH-USD` | 0.001993 | $2508.37 | $2509.45 | $5.00 | 📈 +0.04% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones claras de sobreventa técnica con SOL-USD en un RSI de 27.7 y ETH-USD en un RSI de 36.0, lo cual presenta una oportunidad ideal para capturar rebotes agresivos de mean reversion. Las posiciones actuales se encuentran estancadas cerca del 0% de PnL y el efectivo disponible es bajo, por lo que mantendremos la exposición actual en SOL-USD y ETH-USD para aprovechar el potencial rebote alcista a corto plazo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en un nivel de sobreventa extrema con un RSI de 27.7, cumpliendo perfectamente con la estrategia de cazar rebotes en cripto. Mantenemos la posición para capturar el movimiento alcista hacia el objetivo de ganancia del +3%.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |
| `2026-10-13 16:30` | 🟢 BUY | `ETH-USD` | $9.68 | $2507.92 | ETH-USD muestra un RSI de 35.8 en zona de fuerte sobreventa y un impulso alcista diario de... |
| `2026-10-13 16:30` | 🔴 SELL | `SOL-USD` | $9.69 | $107.65 | Realizamos una toma parcial de beneficios y rotación de capital liberando aproximadamente ... |
| `2026-10-13 14:01` | 🟢 BUY | `SOL-USD` | $7.97 | $107.29 | SOL-USD presenta una condición de sobreventa extrema con un RSI de 27.9 y un desplome sema... |

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
