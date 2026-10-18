# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 16:40:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$37.98 USD** | **$0.00 USD** | **$37.98 USD** | 🔴 **-5.04%** ($-2.02) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *(Ninguna posición abierta - 100% en efectivo)* | - | - | - | - | - | - |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene en una tendencia bajista de corto plazo con los precios de SOL-USD y ETH-USD presionados a la baja y RSI de 1 hora profundamente deprimidos (18.5 y 25.1 respectivamente). Los mercados tradicionales permanecen cerrados. Las posiciones actuales se encuentran rozando el límite de pérdida del -2.0%, y al llevar casi 6 horas abiertas sin mostrar el rebote esperado, es momento de activar el protocolo de rotación de capital para cortar pérdidas y proteger la cuenta."

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 90%): La posición en SOL-USD lleva casi 6 horas abierta con una pérdida del -1.95% y un RSI de 1 hora decayendo a 25.1 sin señales de rebote. Cumpliendo la regla de gestión de tiempo y stop-loss, cerramos la posición para proteger el capital remanente.
- **[SELL] ETH-USD** (Confianza: 90%): ETH-USD registra una pérdida del -1.92% con un RSI de 1 hora en 18.5 que refleja debilidad persistente. Ante la falta de impulso alcista tras varias horas, ejecutamos la venta para asegurar la liquidez y evitar mayores caídas.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Las posiciones en SOL-USD y ETH-USD han superado el tiempo prudencial de espera sin materializar el rebote técnico y se acercan peligrosamente al stop-loss táctico del -2.0%. Procedemos a vender ambas posiciones para liberar efectivo, aceptar la pequeña pérdida y esperar nuevas condiciones de sobreventa extrema con confirmación de volumen o giro alcista antes de reingresar al mercado cripto."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **72** | 🎯 **40.3%** (29W / 29L / 14BE) | 🔴 **$-1.88 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 16:40` | 🔴 SELL (-0.19$) | `ETH-USD` | $9.81 | $2332.39 | ETH-USD registra una pérdida del -1.92% con un RSI de 1 hora en 18.5 que refleja debilidad... |
| `2026-10-18 16:40` | 🔴 SELL (-0.20$) | `SOL-USD` | $9.80 | $100.90 | La posición en SOL-USD lleva casi 6 horas abierta con una pérdida del -1.95% y un RSI de 1... |
| `2026-10-18 12:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2377.97 | ETH-USD presenta un RSI diario extremadamente bajo en 22.0 y un RSI de 1 hora saliendo de ... |
| `2026-10-18 11:01` | 🟢 BUY | `SOL-USD` | $10.00 | $102.91 | SOL-USD muestra un RSI diario extremadamente bajo (16.4) en zona de sobreventa profunda y ... |
| `2026-10-18 08:00` | 🔴 SELL (+0.13$) | `ETH-USD` | $10.13 | $2415.11 | ETH-USD registra un RSI de 1H en 72.1 (sobrecompra) y una ganancia de +1.26%. Se procede a... |

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
