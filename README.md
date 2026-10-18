# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 12:40:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.37 USD** | **$19.85 USD** | **$38.22 USD** | 🔴 **-4.44%** ($-1.78) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.097172 | $102.91 | $101.72 | $9.88 | 📉 -1.16% | 1h 39m |
| `ETH-USD` | 0.004205 | $2377.97 | $2370.46 | $9.97 | 📉 -0.32% | 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario tradicional se encuentra cerrado y congelado durante el fin de semana, por lo que el foco absoluto está en el mercado cripto (24/7). Las criptomonedas principales como ETH-USD y SOL-USD se mantienen en niveles de sobreventa diaria profunda (RSI diario en 21.8 y 15.8 respectivamente), consolidando tras las recientes compras. El holding time de nuestras posiciones abiertas sigue siendo bajo (menos de 2 horas), y aunque muestran ligeras pérdidas no estructurales (-1.16% y -0.32%), el contexto de soporte macro invita a mantener la paciencia a la espera del rebote técnico."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD tiene un tiempo abierto de menos de 2 horas. Su RSI diario se encuentra en 15.8 (sobreventa profunda) y el RSI de 1h está en 34.0. No se ha alcanzado el stop-loss de -2.0% (-1.16% actual), por lo que se mantiene la posición buscando el rebote técnico esperado.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD lleva menos de 1 hora abierta. Presenta un RSI diario en 21.8 y una pérdida marginal de -0.32%, manteniéndose dentro de los parámetros esperados de acumulación en zona de soporte para capturar el próximo impulso alcista de corto plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas de SOL-USD y ETH-USD ya que el tiempo en cartera es bajo y los indicadores diarios se mantienen en sobreventa extrema. Monitorear de cerca el RSI de 1 hora y el cambio porcentual: si el RSI de 1 hora supera los 55-60 y las posiciones logran una ganancia de +2.0% a +3.5%, ejecutar la toma de beneficios para rotar capital. Activar el stop-loss estricto en -2.0% de manera individual para proteger el capital si la presión bajista rompe los soportes actuales."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **70** | 🎯 **41.4%** (29W / 27L / 14BE) | 🔴 **$-1.49 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 12:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2377.97 | ETH-USD presenta un RSI diario extremadamente bajo en 22.0 y un RSI de 1 hora saliendo de ... |
| `2026-10-18 11:01` | 🟢 BUY | `SOL-USD` | $10.00 | $102.91 | SOL-USD muestra un RSI diario extremadamente bajo (16.4) en zona de sobreventa profunda y ... |
| `2026-10-18 08:00` | 🔴 SELL (+0.13$) | `ETH-USD` | $10.13 | $2415.11 | ETH-USD registra un RSI de 1H en 72.1 (sobrecompra) y una ganancia de +1.26%. Se procede a... |
| `2026-10-18 08:00` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $103.84 | SOL-USD presenta un RSI de 1H en 67.6 acercándose a zona de sobrecompra con una ganancia d... |
| `2026-10-18 08:00` | 🔴 SELL (+0.10$) | `BTC-USD` | $10.08 | $81974.15 | BTC-USD ha alcanzado un RSI de 1H en 78.8 (sobrecompra profunda) tras el rebote esperado, ... |

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
