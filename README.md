# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 03:50:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$11.99 USD** | **$39.52 USD** | 🔴 **-1.20%** ($-0.48) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83351.20 | $6.02 | 📈 +0.27% | 6h 49m |
| `SOL-USD` | 0.055840 | $107.45 | $107.03 | $5.98 | 📉 -0.39% | 4h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario tradicional se encuentra cerrado, por lo que toda la atención y liquidez operativa se centra en los criptoactivos (BTC-USD, SOL-USD y ETH-USD). El sentimiento general en cripto muestra un impulso moderado tras las recientes recuperaciones de 24 horas, aunque el momentum de muy corto plazo (1 hora) se ha enfriado ligeramente con variaciones planas. Mantenemos una postura de vigilancia estricta sobre nuestras posiciones abiertas para asegurar ganancias si rozan el objetivo o recortar si pierden soporte."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 65%): BTC-USD muestra una ligera ganancia (+0.27%) tras casi 7 horas de holding. El RSI de 1H está en 51.4 y el de 24h es positivo (+1.94%). Mantenemos la posición a la espera de que el precio acelere hacia la zona de take-profit.
- **[HOLD] SOL-USD** (Confianza: 60%): SOL-USD registra una pequeña pérdida (-0.39%) en un rango de consolidación tras 4.5 horas. El RSI diario se mantiene bajo (27.1), sugiriendo potencial de rebote a mediano plazo. Mantenemos el stop-loss estricto sin sobrepasar los límites de riesgo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Las posiciones en BTC-USD y SOL-USD se mantienen activas tras varias horas de holding con un rendimiento moderadamente estable. Mantendremos el objetivo de take-profit entre +2.0% y +3.5% y un stop-loss estricto en -2.0%. Si en los próximos ciclos el momentum de 1h sigue sin despegar, consideraremos rotar parte del capital para buscar mayores oportunidades en otros activos o reentrar con mayor fuerza si se confirma una ruptura alcista."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **49** | 🎯 **44.9%** (22W / 13L / 14BE) | 🔴 **$-0.39 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |

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
