# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 00:10:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.08 USD** | **$38.37 USD** | 🔴 **-4.08%** ($-1.63) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.36 | $10.06 | 📈 +0.63% | 9h 9m |
| `ETH-USD` | 0.004144 | $2412.98 | $2417.30 | $10.02 | 📈 +0.18% | 7h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado y los mercados de criptomonedas operan de forma lateral con sesgo ligeramente bajista. Las posiciones abiertas en SOL-USD y ETH-USD muestran ganancias mínimas pero estables (+0.63% y +0.18% respectivamente), manteniéndose dentro del rango operativo sin activar los stops de pérdida ni alcanzar aún el objetivo de take-profit. La liquidez actual es de 18.29 USD, cumpliendo holgadamente con la reserva mínima."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición muestra un rendimiento positivo de +0.63% y se encuentra operando dentro de los parámetros esperados de rebote técnico, por lo que se mantiene activa buscando el take-profit.
- **[HOLD] ETH-USD** (Confianza: 80%): La posición se mantiene estable con una pequeña ganancia del +0.18%, respetando el plan táctico a la espera de un mayor impulso intradiario.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones de SOL-USD y ETH-USD esperando el impulso alcista necesario para alcanzar el objetivo de take-profit entre +2.0% y +3.5%. El stop-loss se mantiene rigurosamente en -2.0% para limitar riesgos. Seguiremos vigilando el RSI de 1 hora en busca de una aceleración alcista antes de desplegar más capital."
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
