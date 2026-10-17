# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 02:50:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.13 USD** | **$38.42 USD** | 🔴 **-3.94%** ($-1.58) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.63 | $10.09 | 📈 +0.89% | 11h 49m |
| `ETH-USD` | 0.004144 | $2412.98 | $2423.87 | $10.05 | 📈 +0.45% | 10h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con un sesgo lateral a bajista en el corto plazo, mientras que los mercados tradicionales permanecen cerrados. Nuestras posiciones actuales en SOL-USD y ETH-USD muestran ligeras ganancias (+0.89% y +0.45% respectivamente), acercándose a los niveles de vigilancia para asegurar beneficios si el momentum de corto plazo empuja los precios al alza. El RSI de 1 hora de SOL-USD ha subido a 63.5, lo que sugiere estar atentos a una posible zona de toma de ganancias si se acerca al rango objetivo de +2.0% a +3.5%."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD se mantiene en terreno positivo con una ganancia del 0.89% y un RSI de 1h en 63.5. Aunque se acerca a la zona de take-profit, el precio aún no ha alcanzado el objetivo óptimo de +2.0% a +3.5%, por lo que mantenemos la posición para maximizar el rebote técnico.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD registra un beneficio modesto del 0.45% tras su apertura reciente. El precio se mantiene estable y el stop-loss está protegido; esperamos mayor tracción o la aproximación a sobrecompra intradía para asegurar ganancias.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca SOL-USD para ejecutar toma de beneficios (SELL) si el RSI de 1 hora supera los 70 o la ganancia alcanza el objetivo de +2.0% a +3.5%. Mantener ETH-USD vigilando el stop-loss en -2.0% y preparado para asegurar ganancias parciales ante cualquier aceleración del rebote. Mantener liquidez activa y esperar aperturas de mercados tradicionales para nuevas oportunidades de rotación."
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
