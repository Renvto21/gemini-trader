# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 23:30:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.06 USD** | **$38.35 USD** | 🔴 **-4.14%** ($-1.65) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.16 | $10.04 | 📈 +0.43% | 8h 29m |
| `ETH-USD` | 0.004144 | $2412.98 | $2416.31 | $10.01 | 📈 +0.14% | 7h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra completamente cerrado, por lo que toda la atención se concentra en las criptomonedas (abiertas 24/7). Las posiciones abiertas en SOL-USD y ETH-USD muestran una ligera estabilidad con ganancias marginales (0.43% y 0.14%), pero con un momentum de corto plazo muy plano y RSI de 1 hora bajo en el caso de ETH-USD (23.9), lo que requiere paciencia para esperar el impulso de rebote o gestionar posibles salidas si decae el soporte."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición mantiene una ganancia leve de 0.43% tras 8 horas abierto. El mercado cripto está operando de forma lateral, por lo que se mantiene la posición buscando alcanzar el objetivo de take-profit de +2.0% a +3.5% sin activar el stop-loss.
- **[HOLD] ETH-USD** (Confianza: 70%): La posición en ETH-USD muestra una ganancia marginal del 0.14% con un RSI de 1 hora en 23.9. Aunque hay sobreventa de corto plazo, el activo no ha generado el momentum alcista esperado, pero se mantiene a la espera de la reacción del soporte diario para buscar toma de beneficios.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear las posiciones de SOL-USD y ETH-USD esperando que alcancen el objetivo de take-profit entre +2.0% y +3.5%. Mantener la disciplina con el stop-loss estricto a -2.0%. La liquidez actual de 18.29 USD se mantendrá a la espera de una ruptura de volumen alcista más clara en cripto para rotar o incrementar exposición sin violar la reserva mínima."
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
