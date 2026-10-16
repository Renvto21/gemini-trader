# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 13:50:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.05 USD** | **$13.35 USD** | **$38.40 USD** | 🔴 **-4.01%** ($-1.60) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $528.17 | $6.41 | 📉 -1.31% | 1d 3h |
| `ETH-USD` | 0.002855 | $2451.90 | $2429.21 | $6.94 | 📉 -0.93% | 9h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo bajista generalizado con la mayoría de los activos operando bajo sus respectivas SMA20 y con caídas moderadas en el corto plazo. Los índices y grandes tecnológicas como QQQ, SPY y NVDA continúan presionados, mientras que el sector cripto (BTC, ETH, SOL) muestra signos de consolidación tras recientes descensos, ofreciendo posibles zonas de sobreventa y oportunidades tácticas de rebote para mean reversion."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 65%): MSFT se mantiene sobre su SMA20 con tendencia alcista diaria. A pesar de una ligera caída horaria, el holding time indica paciencia; mantendré la posición buscando un rebote hacia objetivos de take-profit cercanos al +2%.
- **[HOLD] ETH-USD** (Confianza: 60%): ETH-USD opera en un entorno cripto 24/7 con un RSI diario de 31.0 en zona de potencial reversión. La pérdida actual es menor al -1% y mantendré la posición esperando el impulso alcista del sector.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré abiertas las posiciones actuales de MSFT y ETH-USD supervisando de cerca sus soportes; MSFT opera sobre su SMA20 diaria, mientras ETH-USD muestra un RSI diario bajo (31.0) sugiriendo un posible suelo de corto plazo. Ejecutaré ventas inmediatas si alguna posición rompe el stop-loss del -2.0% para proteger capital. El efectivo se mantendrá vigilante para buscar una oportunidad de alta convicción en activos con sobreventa extrema."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **61** | 🎯 **39.3%** (24W / 23L / 14BE) | 🔴 **$-1.34 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 13:40` | 🔴 SELL (-0.02$) | `NVDA` | $7.98 | $216.80 | NVDA lleva más de 24 horas abierto operando bajo la SMA20 con un momentum débil, acumula u... |
| `2026-10-16 12:50` | 🔴 SELL (-0.06$) | `SOL-USD` | $2.94 | $104.34 | SOL-USD lleva varias horas abierto sin generar el rebote esperado, acumulando una pérdida ... |
| `2026-10-16 10:50` | 🔴 SELL (-0.04$) | `QQQ` | $9.95 | $721.83 | QQQ lleva más de 22 horas abierto operando bajo la SMA20 con un RSI de 1 hora en 30.2 y un... |
| `2026-10-16 05:10` | 🟢 BUY | `SOL-USD` | $3.00 | $106.33 | SOL-USD presenta un RSI diario en zona de sobreventa extrema (29.0) y un cambio positivo e... |
| `2026-10-16 04:30` | 🟢 BUY | `ETH-USD` | $7.00 | $2451.90 | Aprovechamos la liquidez disponible sobre la reserva mínima ($14.17 vs $4.00 requeridos) p... |

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
