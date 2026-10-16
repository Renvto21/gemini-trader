# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 12:50:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$17.07 USD** | **$21.41 USD** | **$38.48 USD** | 🔴 **-3.80%** ($-1.52) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $530.76 | $6.45 | 📉 -0.82% | 1d 2h |
| `NVDA` | 0.036812 | $217.32 | $217.83 | $8.02 | 📈 +0.23% | 1d 0h |
| `ETH-USD` | 0.002855 | $2451.90 | $2433.65 | $6.95 | 📉 -0.74% | 8h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un tono de cautela y debilidad general con la mayoría de los activos operando bajo sus medias móviles de 20 días. Las criptomonedas continúan con presión bajista a nivel diario, y SOL-USD se acerca al límite de tolerancia de pérdida (-1.87%), mostrando debilidad continuada tras varias horas de tenencia. Mantenemos una postura defensiva pero listos para rotar capital hacia activos con mayor ímpetu."

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 85%): SOL-USD lleva varias horas abierto sin generar el rebote esperado, acumulando una pérdida de -1.87% y mostrando un cambio negativo de 1h (-1.13%). De acuerdo con nuestras reglas de gestión de riesgo y rotación de capital ante momentum fallido, cerramos la posición para proteger el capital y evitar mayores pérdidas.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorearemos de cerca la posición en SOL-USD debido a su pérdida cercana al límite del -2.0% y la falta de rebote en su RSI de 1 hora. Si SOL-USD profundiza su caída o continúa estancada, procederemos a venderla para cortar pérdidas y liberar liquidez. Mantendremos NVDA, MSFT y ETH-USD vigilando de cerca los niveles de take-profit entre +2.0% y +3.5%."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **60** | 🎯 **40.0%** (24W / 22L / 14BE) | 🔴 **$-1.32 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 12:50` | 🔴 SELL (-0.06$) | `SOL-USD` | $2.94 | $104.34 | SOL-USD lleva varias horas abierto sin generar el rebote esperado, acumulando una pérdida ... |
| `2026-10-16 10:50` | 🔴 SELL (-0.04$) | `QQQ` | $9.95 | $721.83 | QQQ lleva más de 22 horas abierto operando bajo la SMA20 con un RSI de 1 hora en 30.2 y un... |
| `2026-10-16 05:10` | 🟢 BUY | `SOL-USD` | $3.00 | $106.33 | SOL-USD presenta un RSI diario en zona de sobreventa extrema (29.0) y un cambio positivo e... |
| `2026-10-16 04:30` | 🟢 BUY | `ETH-USD` | $7.00 | $2451.90 | Aprovechamos la liquidez disponible sobre la reserva mínima ($14.17 vs $4.00 requeridos) p... |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |

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
