# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 16:10:35`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$37.02 USD** | **$41.02 USD** | 🟢 **+2.54%** ($+1.02) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.004740 | $2531.44 | $2531.63 | $12.00 | 📈 +0.01% |
| `SOL-USD` | 0.224836 | $111.90 | $111.27 | $25.02 | 📉 -0.57% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con sesgo alcista en índices tradicionales y activos tecnológicos principales como QQQ y MSFT, este último alcanzando niveles de sobrecompra técnica con un RSI de 72.3. En el sector cripto, SOL-USD y ETH-USD se encuentran en clara sobreventa con RSI de 26.2 y 32.8 respectivamente, tras caídas semanales significativas. Mantenemos nuestra estrategia de cazar rebotes en cripto mientras gestionamos estrechamente el riesgo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD presenta un RSI profundamente en sobreventa de 26.2, lo que indica un fuerte potencial de rebote por reversión a la media. Aunque tiene una ligera pérdida latente del -0.57%, el precio está consolidando y no ha tocado el stop-loss estricto de -2.5%, por lo que mantenemos la posición para capturar el movimiento alcista esperado.

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
