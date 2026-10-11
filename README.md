# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 14:30:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$37.28 USD** | **$41.28 USD** | 🟢 **+3.19%** ($+1.28) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.004740 | $2531.44 | $2543.28 | $12.06 | 📈 +0.47% |
| `SOL-USD` | 0.224836 | $111.90 | $112.18 | $25.22 | 📈 +0.25% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento general alcista en los índices tradicionales (SPY, QQQ) y en tecnológicas de alto beta, mientras que las criptomonedas (ETH-USD y SOL-USD) se encuentran en zonas de sobreventa técnica (RSI de 34.5 y 29.0 respectivamente) tras caídas semanales, lo que representa una clara oportunidad de rebote por reversión a la media (Mean Reversion). Dado nuestro mandato de gestión cuantitativa agresiva, mantenemos y protegemos nuestras posiciones actuales en cripto mientras el efectivo disponible se encuentra en el límite mínimo establecido de $4.00 USD, priorizando la consolidación de las ganancias actuales antes de realizar nuevas rotaciones de capital."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD presenta un RSI de 29.0, indicando una fuerte sobreventa técnica ideal para nuestra estrategia de caza de rebotes. Aunque muestra una tendencia bajista de corto plazo, el cambio de 24 horas es positivo (+1.95%) y estamos posicionados muy cerca del precio de entrada con una pequeña ganancia. Mantenemos la posición para capturar el rebote hacia la media.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un RSI de 34.5, también en zona de interés para rebotes técnicos tras caídas recientes de la semana. La posición está con un ligero beneficio del 0.47% y preferimos retenerla para aprovechar la recuperación del mercado cripto junto con SOL-USD.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 14:10` | 🟢 BUY | `SOL-USD` | $5.16 | $111.90 | SOL-USD presenta un RSI de 28.2 indicando sobreventa clara tras una caída semanal del 7.33... |
| `2026-10-11 14:00` | 🟢 BUY | `SOL-USD` | $10.00 | $112.02 | SOL-USD se encuentra en clara sobreventa tecnica con un RSI de 28.5 tras una caida semanal... |
| `2026-10-11 13:40` | 🟢 BUY | `SOL-USD` | $10.00 | $111.79 | SOL-USD presenta una excelente oportunidad de rebote técnico de alta convicción al encontr... |
| `2026-10-11 13:30` | 🔴 SELL | `SOL-USD` | $19.04 | $111.95 | SOL-USD ha alcanzado un rendimiento cercano a nuestra meta de take-profit del 2.5% (+2.43%... |
| `2026-10-11 13:20` | 🟢 BUY | `ETH-USD` | $12.00 | $2531.44 | ETH-USD se encuentra en zona de profunda sobreventa técnica con un RSI de 32.8 y una caída... |

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
