# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 16:40:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$19.88 USD** | **$38.16 USD** | 🔴 **-4.59%** ($-1.84) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $102.89 | $9.92 | 📉 -0.79% | 1h 39m |
| `ETH-USD` | 0.004144 | $2412.98 | $2401.96 | $9.95 | 📉 -0.46% | 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto y de renta variable continúa bajo presión generalizada con una tendencia bajista de corto plazo, aunque se observan niveles extremos de sobreventa en activos digitales clave como SOL-USD y ETH-USD (RSI diario cerca o por debajo de 30). Las bolsas tradicionales están abiertas, pero dado el sesgo táctico hacia criptomonedas 24/7 y la necesidad de mantener liquidez controlada, evaluaremos mantener nuestras posiciones actuales mientras consolidan su soporte o rotar según el comportamiento del momentum de 1 hora."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD se encuentra en una fase de consolidación tras la entrada en sobreventa. A pesar de una ligera caída del 0.79%, el RSI de 1 hora en 26.5 sugiere que la presión vendedora podría estar agotándose, por lo que mantendremos la posición buscando el rebote técnico hacia la zona de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un RSI diario de 29.8 y un RSI de 1 hora en 32.0, lo que confirma sobreventa extrema. Mantenemos la posición abierta recientemente para capturar el esperado impulso de reversión a la media, respetando estrictamente los límites de stop-loss.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré temporalmente las posiciones de SOL-USD y ETH-USD para permitirles desarrollar el rebote técnico desde zonas de sobreventa extrema en marcos de tiempo de 1 hora y diario. Monitorizaré de cerca el stop-loss estricto del -2.0% y buscaré tomas de ganancia (take-profit) en el rango de +2.0% a +3.5%. Mantendré una reserva de efectivo adecuada de $18.29 USD para reaccionar rápidamente ante cualquier cambio abrupto en el momentum."
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
