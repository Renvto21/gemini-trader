# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 23:30:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$37.34 USD** | **$41.34 USD** | 🟢 **+3.36%** ($+1.34) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.289416 | $111.58 | $111.93 | $32.39 | 📈 +0.31% |
| `ETH-USD` | 0.001940 | $2541.27 | $2550.24 | $4.95 | 📈 +0.35% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones claras de sobreventa en activos de alta beta como SOL-USD (RSI de 28.3) y ETH-USD (RSI de 35.5), ofreciendo una excelente oportunidad de rebote técnico (Mean Reversion). Por otro lado, en el sector tecnológico tradicional, MSFT ha entrado en territorio de sobrecompra con un RSI de 72.3 y un fuerte incremento de 2.38% en 24 horas, lo que activa la regla de toma rápida de ganancias en caso de tener exposición o nos muestra que el impulso alcista madura. Nuestro efectivo está en el límite mínimo de $4.00 USD, por lo que mantendremos nuestras posiciones actuales en cripto que están comenzando a recuperar terreno y nos prepararemos para rotar capital si alguna de ellas alcanza el objetivo de ganancia."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD se encuentra en clara sobreventa técnica con un RSI de 28.3, lo que favorece un rebote inminente hacia la media. Mantenemos la posición para capturar la recuperación de +2% a +6% esperada bajo nuestra estrategia de alta volatilidad.

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
