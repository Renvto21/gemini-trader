# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 03:50:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.16 USD** | **$38.45 USD** | 🔴 **-3.88%** ($-1.55) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.70 | $10.10 | 📈 +0.95% | 12h 49m |
| `ETH-USD` | 0.004144 | $2412.98 | $2428.70 | $10.07 | 📈 +0.65% | 11h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene abierto y operando en un rango lateral con sesgo bajista general bajo la SMA20. Las posiciones actuales en SOL-USD y ETH-USD muestran ligeras ganancias (+0.95% y +0.65% respectivamente), pero aún no alcanzan el objetivo óptimo de take-profit del +2.0% al +3.5% ni presentan la sobrecompra requerida en el RSI de 1 hora. Los mercados bursátiles tradicionales están cerrados, por lo que toda la atención se centra en mantener la vigilancia sobre las criptomonedas abiertas."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición muestra una ganancia moderada de +0.95% con un holding time de casi 13 horas. El RSI de 1 hora se encuentra en 60.8, acercándose gradualmente a la zona de sobrecompra. Mantenemos la posición a la espera de que alcance el rango objetivo de take-profit del +2.0% al +3.5%.
- **[HOLD] ETH-USD** (Confianza: 75%): La posición acumula una ganancia de +0.65% tras más de 11 horas abierta. El RSI diario se mantiene en niveles atractivos de sobreventa anterior (31.0) y el RSI de 1 hora en 50.2. Esperamos que el impulso continúe para asegurar ganancias en el rango del +2.0% al +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones abiertas de SOL-USD y ETH-USD. Monitorear de cerca el RSI de 1 hora y el avance de los precios hacia el objetivo de take-profit (+2.0% a +3.5%). Si SOL-USD o ETH-USD se acercan a la zona de resistencia o alcanzan la ganancia objetivo, proceder a vender para tomar beneficios y asegurar liquidez. Mantener el stop-loss estricto en -2.0% ante cualquier reversión del mercado."
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
