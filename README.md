# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 14:01:00`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.05 USD** | **$13.34 USD** | **$38.39 USD** | 🔴 **-4.03%** ($-1.61) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $527.79 | $6.41 | 📉 -1.38% | 1d 3h |
| `ETH-USD` | 0.002855 | $2451.90 | $2428.44 | $6.93 | 📉 -0.96% | 9h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo bajista generalizado con la mayoría de los activos cotizando por debajo de su SMA20. Las criptomonedas continúan operando 24/7 con una presión de venta moderada, mientras que los índices y acciones tecnológicas en Wall Street muestran debilidad de corto plazo pero manteniendo algunos soportes críticos diarios."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 70%): MSFT se mantiene con una pérdida controlada de -1.38% dentro del tiempo de retención aceptable, operando sobre su tendencia alcista diaria. Mantengo la posición esperando el rebote.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD muestra un RSI diario de 31.0 indicando sobreventa profunda y un soporte potencial de mediano plazo. La pérdida actual es de -0.96% y el activo sigue abierto 24/7.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré las posiciones abiertas de MSFT y ETH-USD supervisando de cerca el soporte del stop-loss en -2.0%. Si MSFT o ETH-USD rompen sus niveles clave a la baja, ejecutaré ventas inmediatas para proteger capital. Mantendré el efectivo disponible esperando señales claras de rebote con RSI de 1 hora saliendo de sobreventa para realizar nuevas entradas tácticas."
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
