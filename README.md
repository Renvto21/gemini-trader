# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 23:20:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$37.38 USD** | **$41.38 USD** | 🟢 **+3.45%** ($+1.38) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.289416 | $111.58 | $112.03 | $32.42 | 📈 +0.40% |
| `ETH-USD` | 0.001940 | $2541.27 | $2555.03 | $4.96 | 📈 +0.54% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo alcista moderado en índices y acciones tecnológicas de alto beta como MSFT, mientras que las criptomonedas y metales experimentan procesos de recuperación tras caídas recientes. SOL-USD se encuentra en zona extrema de sobreventa con un RSI de 28.6, lo que representa una clara oportunidad de rebote técnico (mean reversion) de acuerdo con la estrategia agresiva. ETH-USD muestra un RSI de 36.1 comenzando a rebotar, pero mantendremos la posición actual para dejar correr el beneficio al estar cerca de la zona neutral. Con $4.00 USD de efectivo disponible, no hay capacidad para nuevas compras sin rotar capital, por lo que mantendremos las posiciones actuales enfocadas en capturar el impulso de recuperación en cripto."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD presenta un RSI de 28.6 (sobreventa extrema) y muestra un inicio de recuperación del 1.81% en 24h. Mantenemos la posición para capturar el rebote técnico hacia la zona del objetivo del +4%.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD sube un 2.04% en las últimas 24 horas con un RSI saliendo de sobreventa (36.1). Mantenemos la posición para permitir que el impulso alcista continúe y alcance el umbral de toma de ganancias.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 23:10` | 🟢 BUY | `ETH-USD` | $4.93 | $2541.27 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 34.2 y una caída semanal ... |
| `2026-10-11 23:00` | 🔴 SELL | `ETH-USD` | $3.92 | $2541.25 | La posicion en ETH-USD esta estancada y representa un monto muy pequeno ($3.92) sin sufici... |
| `2026-10-11 22:00` | 🔴 SELL | `ETH-USD` | $5.00 | $2542.93 | Vendemos parcialmente la posición en ETH-USD para liberar efectivo y cumplir con la regla ... |
| `2026-10-11 21:50` | 🟢 BUY | `ETH-USD` | $8.92 | $2542.73 | ETH-USD está en condiciones de clara sobreventa técnica (RSI de 34.5) tras una caída seman... |
| `2026-10-11 21:50` | 🔴 SELL | `SOL-USD` | $8.93 | $111.63 | Liberamos una fracción de la posición en SOL-USD que se encuentra estancada con rendimient... |

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
