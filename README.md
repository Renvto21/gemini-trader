# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 00:50:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.17 USD** | **$38.46 USD** | 🔴 **-3.85%** ($-1.54) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.96 | $10.12 | 📈 +1.21% | 9h 49m |
| `ETH-USD` | 0.004144 | $2412.98 | $2424.98 | $10.05 | 📈 +0.50% | 8h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra CERRADO, por lo que toda la atención operativa se desplaza hacia las criptomonedas (ABIERTO 24/7). Las criptos principales (SOL-USD y ETH-USD) muestran ligeras recuperaciones con un momentum de corto plazo positivo, acercándose progresivamente a los objetivos de take-profit establecidos entre +2.0% y +3.5%. El sentimiento general sigue siendo cauteloso debido a tendencias macro bajistas, pero los rebotes técnicos intradiarios ofrecen oportunidades tácticas."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD mantiene un rendimiento positivo de +1.21% con un RSI de 1 hora en 43.8 y un cambio de +0.46% en la última hora, lo que muestra que el rebote técnico sigue evolucionando favorablemente hacia el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD registra una ganancia del +0.50% y un cambio positivo de 1 hora del +0.26%, consolidando el rebote desde la sobreventa diaria. Se mantiene la posición a la espera de alcanzar el rango óptimo de salida.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales de SOL-USD y ETH-USD mientras continúan su avance hacia la zona de take-profit del +2.0% al +3.5%. Vigilar el indicador RSI de 1 hora en busca de niveles de sobrecompra (>70) para asegurar beneficios de manera inmediata. Si alguna posición pierde impulso o se acerca a la zona de stop-loss del -2.0%, proceder a cortar pérdidas para proteger el capital. No abrir nuevas posiciones hasta que se materialice la toma de ganancias y se libere liquidez."
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
