# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 13:40:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.85 USD** | **$38.32 USD** | 🔴 **-4.19%** ($-1.68) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.22 | $9.93 | 📉 -0.69% | 3h 20m |
| `ETH-USD` | 0.004126 | $2423.75 | $2403.35 | $9.92 | 📉 -0.84% | 1h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene en una fase de consolidación bajista de corto plazo, con un sentimiento general débil pero con los precios sostenidos cerca de zonas de sobreventa diaria profunda. Los activos de Wall Street se encuentran cerrados, por lo que toda la operativa se concentra exclusivamente en criptoactivos (24/7). Las posiciones abiertas en SOL-USD y ETH-USD muestran ligeras pérdidas no realizadas (-0.69% y -0.84% respectivamente), pero aún se encuentran lejos del stop-loss estricto del -2.0% y sus indicadores de 1 hora muestran estabilidad tras el retroceso inicial."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición en SOL-USD registra una leve pérdida del -0.69%, manteniéndose estable y sin alcanzar los límites de stop-loss ni de take-profit. El RSI diario se encuentra en niveles de sobreventa extrema (22.0), por lo que se prefiere mantener la posición a la espera del rebote técnico.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD muestra un comportamiento similar, con una pérdida actual de -0.84% y un RSI diario en 27.7. El activo sigue dentro de los parámetros operativos permitidos, por lo que se mantiene en cartera esperando la recuperación del impulso.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear las posiciones abiertas en SOL-USD y ETH-USD. Esperar a que el RSI de 1 hora supere la zona de 70 para asegurar beneficios o que se acerquen al stop-loss estricto de -2.0%. Mantener la liquidez actual intacta hasta ver un repunte claro en el momentum de las criptomonedas."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **65** | 🎯 **40.0%** (26W / 25L / 14BE) | 🔴 **$-1.41 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 11:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2423.75 | ETH-USD presenta un RSI diario en niveles de sobreventa profunda (28.9) y un cambio positi... |
| `2026-10-17 10:20` | 🟢 BUY | `SOL-USD` | $10.00 | $103.94 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (22.5) y un cambio positiv... |
| `2026-10-17 04:30` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $104.94 | SOL-USD ha alcanzado un RSI de 1 hora de 70.4, entrando en zona de sobrecompra, y acumula ... |
| `2026-10-17 04:00` | 🔴 SELL (+0.07$) | `ETH-USD` | $10.07 | $2429.64 | ETH-USD ha alcanzado un RSI de 1 hora de 73.3, entrando en zona de sobrecompra. Siguiendo ... |
| `2026-10-16 16:30` | 🟢 BUY | `ETH-USD` | $10.00 | $2412.98 | ETH-USD muestra un RSI diario en niveles de sobreventa extrema (30.3) y un cambio positivo... |

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
