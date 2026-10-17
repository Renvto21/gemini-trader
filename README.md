# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 21:50:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.04 USD** | **$38.33 USD** | 🔴 **-4.19%** ($-1.67) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.01 | $10.03 | 📈 +0.29% | 6h 49m |
| `ETH-USD` | 0.004144 | $2412.98 | $2414.91 | $10.01 | 📈 +0.08% | 5h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto mantiene una tendencia bajista de corto plazo pero muestra condiciones de sobreventa extrema tanto en gráficos horarios como diarios (RSI 1H y diario por debajo de 30 para SOL y ETH). Los mercados tradicionales (Wall Street) se encuentran cerrados, por lo que toda la actividad operativa debe concentrarse exclusivamente en las criptomonedas abiertas 24/7."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD se mantiene en rango con una pequeña ganancia del 0.29% tras casi 7 horas. El RSI de 1 hora se encuentra en 28.1 y el diario en 25.3, lo que indica sobreventa extrema y un potencial rebote técnico inminente que justifica mantener la posición.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un comportamiento similar con una ganancia marginal del 0.08% tras 5 horas. Su RSI de 1 hora está en 28.6 y el diario en 30.4, por lo que se mantiene la postura de aguardar el rebote hacia el objetivo de +2.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en SOL-USD y ETH-USD supervisando de cerca la evolución del RSI de 1 hora para asegurar ganancias si se roza el rango de +2.0% a +3.5%, o recortar si rompen soportes a la baja (-2.0%). Conservar la liquidez actual de 18.29 USD para entradas rápidas en cuanto el mercado cripto presente un catalizador de aceleración alcista más claro."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **63** | 🎯 **38.1%** (24W / 25L / 14BE) | 🔴 **$-1.60 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 16:30` | 🟢 BUY | `ETH-USD` | $10.00 | $2412.98 | ETH-USD muestra un RSI diario en niveles de sobreventa extrema (30.3) y un cambio positivo... |
| `2026-10-16 16:30` | 🔴 SELL (-0.11$) | `MSFT` | $6.39 | $526.18 | MSFT lleva más de 1 día y 5 horas abierto mostrando debilidad persistente y un rendimiento... |
| `2026-10-16 15:01` | 🟢 BUY | `SOL-USD` | $10.00 | $103.71 | SOL-USD presenta un RSI de 1 hora en 34.3 saliendo de la zona de sobreventa extrema, acomp... |
| `2026-10-16 14:30` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2399.90 | ETH-USD ha rebasado el umbral estricto de stop-loss (-2.12%), operando en tendencia bajist... |
| `2026-10-16 13:40` | 🔴 SELL (-0.02$) | `NVDA` | $7.98 | $216.80 | NVDA lleva más de 24 horas abierto operando bajo la SMA20 con un momentum débil, acumula u... |

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
