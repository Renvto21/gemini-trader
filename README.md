# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 16:50:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$19.92 USD** | **$38.21 USD** | 🔴 **-4.47%** ($-1.79) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $103.22 | $9.95 | 📉 -0.47% | 1h 49m |
| `ETH-USD` | 0.004144 | $2412.98 | $2405.50 | $9.97 | 📉 -0.31% | 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se encuentra bajo presión bajista con la mayoría de los activos cotizando por debajo de su SMA20. Sin embargo, los criptoactivos en nuestra cartera (SOL-USD y ETH-USD) muestran ligeros intentos de recuperación en el corto plazo tras tocar zonas de sobreventa extrema, aunque se mantienen dentro de una tendencia macro delicada. Mantendremos la disciplina con nuestras posiciones abiertas y la gestión estricta de riesgo."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición lleva poco tiempo abierta (1h 49m) y mantiene un rendimiento cercano al punto de entrada (-0.47%). El RSI de 1 hora está en 29.9 y el cambio reciente es positivo, por lo que esperamos que desarrolle el rebote técnico esperado sin activar el stop-loss.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD muestra un RSI diario en sobreventa extrema (29.9) y un holding time muy corto (19m) con una pérdida mínima de -0.31%. Daremos espacio para que el precio reaccione al alza desde los soportes actuales.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré las posiciones de SOL-USD y ETH-USD por el momento, vigilando de cerca el stop-loss estricto del -2.0% y esperando un impulso hacia la zona de take-profit entre +2.0% y +3.5%. Conservaré la liquidez actual para reaccionar ante cualquier cambio en el momentum de los mercados 24/7."
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
