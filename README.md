# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 21:20:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.07 USD** | **$38.36 USD** | 🔴 **-4.10%** ($-1.64) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.22 | $10.05 | 📈 +0.49% | 6h 19m |
| `ETH-USD` | 0.004144 | $2412.98 | $2417.98 | $10.02 | 📈 +0.21% | 4h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado bursátil tradicional se encuentra cerrado, por lo que toda la actividad se concentra en el mercado de criptomonedas (24/7). Las posiciones abiertas en SOL-USD y ETH-USD muestran ligeras ganancias positivas (+0.49% y +0.21% respectivamente) tras el rebote inicial, pero el momentum se mantiene moderado en un contexto general bajista. Mantendremos las posiciones actuales esperando que alcancen la zona objetivo de take-profit (+2.0% a +3.5%) o un incremento en el volumen intradiario."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición mantiene un rendimiento positivo de +0.49% con un holding time de poco más de 6 horas. El precio está reaccionando adecuadamente desde el soporte diario, por lo que se mantiene para buscar el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): La posición en ETH-USD muestra un rendimiento positivo de +0.21%. El RSI diario está en sobreventa extrema y el activo muestra un cambio de 1 hora positivo, por lo que el rebote sigue vigente.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear las posiciones SOL-USD y ETH-USD para asegurar ganancias si alcanzan la zona de +2.0% a +3.5% o activar el stop-loss en -2.0%. Mantener la liquidez remanente de 18.29 USD lista para desplegar en cuanto aparezca una oportunidad de alta convicción en cripto con un RSI de 1 hora saliendo de sobreventa y cambio positivo."
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
