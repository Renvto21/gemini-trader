# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 09:20:53`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.51 USD** | **$38.51 USD** | 🔴 **-3.72%** ($-1.49) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 22h 40m |
| `ETH-USD` | 0.004178 | $2393.62 | $2388.43 | $9.98 | 📉 -0.22% | 20h 29m |
| `SOL-USD` | 0.096034 | $104.13 | $104.26 | $10.01 | 📈 +0.12% | 16h 40m |
| `BTC-USD` | 0.000105 | $81767.70 | $81432.64 | $8.53 | 📉 -0.41% | 16h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con un sesgo lateral a ligeramente bajista, pero mostrando signos incipientes de recuperación en el corto plazo con RSI de 1 hora saliendo de zonas de compresión y cambios horarios positivos en SOL y ETH. Los activos tradicionales como QQQ se encuentran cerrados, manteniendo sus precios congelados y sin cambios significativos desde el ciclo anterior. Las posiciones actuales muestran variaciones mínimas y se mantienen dentro de los rangos de tolerancia antes del stop-loss."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra un RSI diario extremadamente bajo (21.3) y un ligero repunte en el RSI de 1 hora (37.8) con cambio positivo, sugiriendo la formación de un piso para un rebote técnico. Mantenemos la posición para buscar el objetivo de ganancia.
- **[HOLD] ETH-USD** (Confianza: 72%): ETH-USD mantiene un comportamiento correlacionado con el sector con un cambio horario positivo del 0.3% y RSI de 1 hora en 39.2. Sostenemos la posición esperando confirmación de tendencia alcista de corto plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca las posiciones en criptomonedas (SOL, ETH, BTC) buscando un incremento en el volumen y momentum que impulse el RSI de 1 hora por encima de 50 para activar los take-profits entre +2.0% y +3.5%. Mantener QQQ en espera hasta la apertura del mercado tradicional. Si las criptomonedas pierden impulso o se acercan al límite de -2.0%, procederemos a cortar pérdidas de inmediato."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 23:00` | 🟢 BUY | `BTC-USD` | $4.00 | $81646.39 | BTC-USD presenta un RSI de 1 hora en 27.7, nivel de sobreventa profunda ideal para un rebo... |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |

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
