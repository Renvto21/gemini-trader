# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 13:20:53`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$17.07 USD** | **$21.39 USD** | **$38.46 USD** | 🔴 **-3.85%** ($-1.54) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $528.83 | $6.42 | 📉 -1.18% | 1d 2h |
| `NVDA` | 0.036812 | $217.32 | $217.54 | $8.01 | 📈 +0.10% | 1d 0h |
| `ETH-USD` | 0.002855 | $2451.90 | $2438.48 | $6.96 | 📉 -0.55% | 8h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un tono mayoritariamente bajista con la mayoría de los activos cotizando por debajo de su SMA20. Sin embargo, en el sector cripto y algunas acciones seleccionadas se observan intentos de estabilización y ligeros rebotes de corto plazo. Mantenemos una postura defensiva pero activa, vigilando de cerca los niveles de sobreventa diaria para rotar capital eficientemente."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 60%): MSFT se mantiene con una pérdida moderada de -1.18%, dentro del margen de tolerancia antes del stop-loss del -2.0%. Esperamos que la tendencia alcista de fondo permita un rebote.
- **[HOLD] NVDA** (Confianza: 60%): NVDA se encuentra prácticamente en equilibrio (0.1%). Su RSI de 1 hora está bajo pero mostrando un ligero impulso positivo (0.43% en la última hora). Mantenemos para evaluar su evolución.
- **[HOLD] ETH-USD** (Confianza: 60%): ETH-USD registra una leve pérdida de -0.55% con un RSI diario atractivo en zona de sobreventa (31.5). Damos margen a la posición buscando el rebote técnico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca las posiciones abiertas (MSFT, NVDA, ETH-USD). Ejecutar stop-loss preventivo si alguna posición supera el -2.0% de pérdida o si el momentum se deteriora. Mantener la liquidez disponible para aprovechar oportunidades de alta convicción en cripto o tech cuando los indicadores técnicos muestren rupturas claras al alza."
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
