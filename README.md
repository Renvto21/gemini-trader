# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 03:40:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.02 USD** | **$40.30 USD** | **$40.33 USD** | 🟢 **+0.82%** ($+0.33) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.220708 | $109.23 | $109.51 | $24.17 | 📈 +0.26% |
| `ETH-USD` | 0.006448 | $2481.58 | $2502.33 | $16.13 | 📈 +0.84% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo mixto con los principales índices como SPY y QQQ manteniendo una tendencia alcista moderada, mientras que el sector cripto (SOL-USD y ETH-USD) se encuentra profundamente en zona de sobreventa técnica (RSI de 22.3 y 27.7 respectivamente) tras caídas semanales significativas. Sin embargo, nuestro efectivo disponible es prácticamente cero ($0.02 USD), lo que limita nuestra capacidad de realizar compras adicionales sin liquidar posiciones existentes. Dado que nuestras posiciones actuales (SOL-USD y ETH-USD) se encuentran con ganancias muy ligeras (0.26% y 0.84%) y lejos de la zona de take-profit (>2.5%) o stop-loss, y considerando que ETH muestra condiciones técnicas extremas de rebote inminente, la mejor decisión táctica bajo nuestra estrategia agresiva de rotación y gestión de capital es mantener (HOLD) ambas posiciones para permitirles desarrollar el rebote técnico esperado hacia la zona de sobrecompra."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra en condición de extrema sobreventa con un RSI de 22.3 tras una caída semanal del 9.89%. Aunque la tendencia es bajista a corto plazo, el potencial de un rebote técnico de reversión a la media es muy alto. Mantenemos la posición para capturar el movimiento alcista sin alterar la asignación actual al carecer de efectivo libre.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD presenta un RSI de 27.7, situándose también en zona de sobreventa profunda con una ganancia actual del 0.84%. Mantenemos la posición para buscar el objetivo de take-profit del +2.5% o superior, aprovechando la alta probabilidad de un rebote impulsado por la sobreventa técnica.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 03:20` | 🟢 BUY | `SOL-USD` | $12.00 | $109.35 | SOL-USD se encuentra en una situación de sobreventa técnica masiva con un RSI de 14 en 21.... |
| `2026-10-11 03:20` | 🔴 SELL | `MSFT` | $12.00 | $535.07 | MSFT ha entrado en zona de sobrecompra técnica con un RSI de 72.3. Aplicando la regla táct... |
| `2026-10-11 03:10` | 🟢 BUY | `MSFT` | $12.00 | $535.07 | Aprovechando la fuerte subida de MSFT (2.38% en 24h y RSI de 72.3 en zona de aceleración d... |
| `2026-10-11 03:10` | 🔴 SELL | `SOL-USD` | $12.02 | $109.29 | Liberando parcialmente capital de SOL-USD para aprovechar una rotación táctica hacia activ... |
| `2026-10-11 02:20` | 🟢 BUY | `SOL-USD` | $4.11 | $109.54 | SOL-USD se encuentra en extrema sobreventa técnica con un RSI de 22.4 y una caída semanal ... |

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
