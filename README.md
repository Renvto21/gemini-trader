# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 16:30:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.01 USD** | **$39.76 USD** | **$39.77 USD** | 🔴 **-0.57%** ($-0.23) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.279466 | $107.20 | $107.65 | $30.08 | 📈 +0.42% |
| `ETH-USD` | 0.003860 | $2507.92 | $2507.92 | $9.68 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra oportunidades claras de rebote técnico en activos de criptomonedas. SOL-USD se mantiene en cartera con una ligera ganancia tras un rebote incipiente, mientras ETH-USD muestra condiciones de sobreventa extrema (RSI de 35.8) con un rendimiento positivo en 24 horas (+2.6%), lo que indica un fuerte potencial de reversión a la media. En el sector tecnológico, MSFT ha entrado en zona de sobrecompra clara (RSI de 78.4). El capital actual está totalmente desplegado en SOL-USD y el efectivo es nulo, por lo que para capturar la nueva oportunidad en ETH-USD realizaremos una rotación parcial vendiendo una fracción de SOL-USD."*

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 85%): Realizamos una toma parcial de beneficios y rotación de capital liberando aproximadamente 9.68 USD de SOL-USD para financiar la entrada en ETH-USD, aprovechando que SOL se encuentra con una ganancia actual del 0.42% y manteniendo la mayor parte de la posición principal.
- **[BUY] ETH-USD** (Confianza: 88%): ETH-USD muestra un RSI de 35.8 en zona de fuerte sobreventa y un impulso alcista diario del 2.6%. Conforme a nuestra estrategia agresiva de mean reversion y captura de rebotes rápidos, asignamos este capital para aprovechar el momentum de recuperación técnica.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 16:30` | 🟢 BUY | `ETH-USD` | $9.68 | $2507.92 | ETH-USD muestra un RSI de 35.8 en zona de fuerte sobreventa y un impulso alcista diario de... |
| `2026-10-13 16:30` | 🔴 SELL | `SOL-USD` | $9.69 | $107.65 | Realizamos una toma parcial de beneficios y rotación de capital liberando aproximadamente ... |
| `2026-10-13 14:01` | 🟢 BUY | `SOL-USD` | $7.97 | $107.29 | SOL-USD presenta una condición de sobreventa extrema con un RSI de 27.9 y un desplome sema... |
| `2026-10-13 14:01` | 🔴 SELL | `ETH-USD` | $7.97 | $2508.01 | Liberamos la totalidad de la posición en ETH-USD para consolidar efectivo y rotar hacia un... |
| `2026-10-13 08:30` | 🟢 BUY | `ETH-USD` | $7.96 | $2505.44 | ETH-USD muestra un RSI de 35.6 en zona de sobreventa y un cambio positivo de 2.45% en 24 h... |

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
