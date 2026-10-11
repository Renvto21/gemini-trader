# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 13:30:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$29.16 USD** | **$12.05 USD** | **$41.21 USD** | 🟢 **+3.03%** ($+1.21) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.004740 | $2531.44 | $2542.37 | $12.05 | 📈 +0.43% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo positivo general en los índices y tecnológicas, destacando el fuerte impulso de MSFT que ha entrado en sobrecompra con un RSI de 72.3. En criptomonedas, SOL-USD y ETH-USD muestran signos claros de sobreventa y agotamiento bajista (RSI de 28.3 y 34.4 respectivamente), habiendo iniciado un rebote técnico en las últimas 24 horas. Nuestra posición en SOL-USD se acerca al objetivo de take-profit con un rendimiento del 2.43%, mientras que ETH-USD se mantiene estable sin momentum significativo."*

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 90%): SOL-USD ha alcanzado un rendimiento cercano a nuestra meta de take-profit del 2.5% (+2.43%). Siguiendo la regla de rotación y toma rápida de ganancias, vendemos la posición completa para asegurar los beneficios y liberar liquidez con el fin de capturar nuevas oportunidades de momentum en el mercado.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 13:30` | 🔴 SELL | `SOL-USD` | $19.04 | $111.95 | SOL-USD ha alcanzado un rendimiento cercano a nuestra meta de take-profit del 2.5% (+2.43%... |
| `2026-10-11 13:20` | 🟢 BUY | `ETH-USD` | $12.00 | $2531.44 | ETH-USD se encuentra en zona de profunda sobreventa técnica con un RSI de 32.8 y una caída... |
| `2026-10-11 13:10` | 🔴 SELL | `ETH-USD` | $9.99 | $2530.10 | ETH-USD se encuentra estancado con un P&L cercano a 0% (-0.06%) y bajo tendencia bajista e... |
| `2026-10-11 13:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2531.65 | ETH-USD se encuentra en clara sobreventa técnica con un RSI de 32.8 y una fuerte caída sem... |
| `2026-10-11 13:00` | 🔴 SELL | `SOL-USD` | $19.02 | $111.81 | Tomamos beneficios de manera parcial en SOL-USD ya que la posición acumula una ganancia ce... |

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
