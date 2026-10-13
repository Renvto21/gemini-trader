# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 14:31:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.59 USD** | **$39.59 USD** | 🔴 **-1.02%** ($-0.41) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.369466 | $107.20 | $107.16 | $39.59 | 📉 -0.03% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra señales mixtas con criptomonedas como ETH-USD y SOL-USD en zonas de sobreventa técnica profunda (RSI < 38), ideales para capturar rebotes agresivos por mean reversion. Nuestra posición actual en SOL-USD se mantiene estable (-0.03%), preservando el valor patrimonial mientras el activo comienza a mostrar una recuperación intradía del +1.52%. Por otro lado, ETH-USD muestra un RSI de 35.3 y una ganancia de 2.4% en 24 horas, indicando un excelente punto de entrada técnico. Mantenemos SOL-USD para permitir que complete su rebote técnico hacia la media y buscamos maximizar la rotación de capital."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra en sobreventa extrema (RSI de 27.5) con un intento de recuperación del +1.52% en 24h. Dado que nuestra pérdida no ha superado el stop-loss estricto y estamos buscando capturar un rebote del +2% al +6%, mantenemos la posición para dejarla madurar.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 14:01` | 🟢 BUY | `SOL-USD` | $7.97 | $107.29 | SOL-USD presenta una condición de sobreventa extrema con un RSI de 27.9 y un desplome sema... |
| `2026-10-13 14:01` | 🔴 SELL | `ETH-USD` | $7.97 | $2508.01 | Liberamos la totalidad de la posición en ETH-USD para consolidar efectivo y rotar hacia un... |
| `2026-10-13 08:30` | 🟢 BUY | `ETH-USD` | $7.96 | $2505.44 | ETH-USD muestra un RSI de 35.6 en zona de sobreventa y un cambio positivo de 2.45% en 24 h... |
| `2026-10-13 08:30` | 🔴 SELL | `NVDA` | $7.96 | $226.32 | Liberamos capital de NVDA que se encuentra lateral y bajo su SMA20 sin momentum claro, par... |
| `2026-10-13 08:10` | 🟢 BUY | `NVDA` | $7.96 | $226.32 | Aprovechamos la corrección reciente de NVDA (caída de 7 días del -3.26% con un RSI de 46.4... |

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
