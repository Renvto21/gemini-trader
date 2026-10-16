# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 16:00:53`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$21.90 USD** | **$16.31 USD** | **$38.21 USD** | 🔴 **-4.48%** ($-1.79) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $526.00 | $6.39 | 📉 -1.71% | 1d 5h |
| `SOL-USD` | 0.096423 | $103.71 | $102.90 | $9.92 | 📉 -0.78% | 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra bajo una presión bajista generalizada, con los principales índices y activos operando por debajo de sus medias móviles de 20 periodos (SMA20). Sin embargo, el RSI de 1 hora en varios activos se encuentra en niveles de sobreventa o cercanos a ella, lo que sugiere oportunidades inminentes de rebote técnico. Mantenemos una postura defensiva pero activa, revisando de cerca nuestras posiciones abiertas para cortar pérdidas rápidamente y liberar capital."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 60%): MSFT se mantiene con un holding de más de 1 día y un PnL de -1.71%. Aunque el momentum es débil, se encuentra sobre la SMA20 diaria (tendencia alcista macro). Monitorearemos de cerca el nivel de stop-loss de -2.0% para evitar mayores pérdidas.
- **[HOLD] SOL-USD** (Confianza: 65%): SOL-USD presenta un RSI de 1 hora en 26.5, reflejando condiciones de sobreventa. El PnL actual es de -0.78%. Esperaremos a que el precio rompa la inercia bajista para buscar un rebote hacia el objetivo de take-profit de +2.5%, vigilando estrictamente el stop-loss en -2.0%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "En MSFT, el holding supera un día con un PnL de -1.71%; si rompe el soporte o no muestra recuperación, procederé a vender para liberar capital. En SOL-USD, el RSI de 1 hora ha caído a 26.5 y el PnL está en -0.78%; mantendré la posición buscando el objetivo de take-profit en +2.5% o aplicaré un stop-loss estricto en -2.0% si continúa el deterioro. La liquidez en efectivo ($21.90 USD) se mantendrá vigilante para nuevas entradas tácticas en cripto o tech cuando se confirme un cambio de momentum."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **62** | 🎯 **38.7%** (24W / 24L / 14BE) | 🔴 **$-1.49 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 15:01` | 🟢 BUY | `SOL-USD` | $10.00 | $103.71 | SOL-USD presenta un RSI de 1 hora en 34.3 saliendo de la zona de sobreventa extrema, acomp... |
| `2026-10-16 14:30` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2399.90 | ETH-USD ha rebasado el umbral estricto de stop-loss (-2.12%), operando en tendencia bajist... |
| `2026-10-16 13:40` | 🔴 SELL (-0.02$) | `NVDA` | $7.98 | $216.80 | NVDA lleva más de 24 horas abierto operando bajo la SMA20 con un momentum débil, acumula u... |
| `2026-10-16 12:50` | 🔴 SELL (-0.06$) | `SOL-USD` | $2.94 | $104.34 | SOL-USD lleva varias horas abierto sin generar el rebote esperado, acumulando una pérdida ... |
| `2026-10-16 10:50` | 🔴 SELL (-0.04$) | `QQQ` | $9.95 | $721.83 | QQQ lleva más de 22 horas abierto operando bajo la SMA20 con un RSI de 1 hora en 30.2 y un... |

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
