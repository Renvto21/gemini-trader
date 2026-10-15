# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 22:20:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.23 USD** | **$34.89 USD** | **$39.11 USD** | 🔴 **-2.21%** ($-0.89) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 11h 29m |
| `SOL-USD` | 0.095785 | $104.40 | $104.25 | $9.99 | 📉 -0.14% | 5h 49m |
| `ETH-USD` | 0.004135 | $2418.34 | $2416.45 | $9.99 | 📉 -0.08% | 3h 19m |
| `BTC-USD` | 0.000061 | $81640.68 | $81661.87 | $5.00 | 📈 +0.03% | 1h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra CERRADO, por lo que toda la atención operativa se concentra en el mercado de criptomonedas (abierto 24/7). Los principales activos cripto (BTC-USD, ETH-USD y SOL-USD) muestran condiciones de sobreventa extrema en RSI de 1h con leves intentos de estabilización en el cambio porcentual de la última hora. Mantenemos las posiciones activas buscando el rebote de reversión a la media, mientras que la posición en AAPL permanece bloqueada hasta la apertura del mercado bursátil."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD mantiene un RSI de 1h en 28.0 y un cambio positivo de 0.13%, mostrando indicios iniciales de formación de suelo tras la caída de 24h. Mantenemos posición buscando el rebote técnico.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD presenta un RSI de 1h de 22.9 en zona de sobreventa profunda. El precio está consolidando y esperamos que reaccione al alza en las próximas horas hacia el objetivo de take-profit.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra un RSI de 1h recuperando terreno levemente a 32.3. Se mantiene dentro de la tesis de rebote por reversión a la media, sin alcanzar aún los niveles de take-profit ni de stop-loss.
- **[HOLD] AAPL** (Confianza: 70%): AAPL se encuentra en mercado CERRADO. La posición se mantiene estable con una ligera pérdida menor al -1%, muy por encima del stop-loss y esperando la apertura bursátil.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en BTC-USD, ETH-USD y SOL-USD para capturar el rebote técnico hacia la zona de take-profit (+2.0% a +3.5%). Vigilar estrictamente que ninguna posición rompa el stop-loss del -2.0%. Mantener la liquidez disponible actual de $4.23 y estar preparados para rotar capital o tomar beneficios en cuanto los indicadores muestren sobrecompra en 1h (> 70)."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **52** | 🎯 **42.3%** (22W / 16L / 14BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 21:10` | 🟢 BUY | `BTC-USD` | $5.00 | $81640.68 | BTC-USD presenta un RSI de 1h en 24.9 (sobreventa extrema) y liquidez disponible suficient... |
| `2026-10-14 19:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2418.34 | ETH-USD presenta un RSI de 1h en 22.0 (sobreventa extrema) y un cambio de 1h que comienza ... |
| `2026-10-14 16:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.40 | SOL-USD presenta un RSI de 1h en 30.9 saliendo de la zona de compresión y un cambio positi... |
| `2026-10-14 15:20` | 🔴 SELL (-0.08$) | `SOL-USD` | $9.92 | $103.86 | SOL-USD lleva varias horas sin mostrar el rebote esperado, su RSI de 1h ha caído hasta 25.... |
| `2026-10-14 12:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.70 | SOL-USD presenta un RSI de 1h en 29.2 saliendo de sobreventa extrema y un cambio de 1h pos... |

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
