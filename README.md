# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 18:40:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$38.05 USD** | **$0.00 USD** | **$38.05 USD** | 🔴 **-4.88%** ($-1.95) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *(Ninguna posición abierta - 100% en efectivo)* | - | - | - | - | - | - |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas continúa bajo una fuerte presión bajista, con SOL-USD y ETH-USD rompiendo soportes de corto plazo y registrando pérdidas cercanas al -2.1% y -2.2% respectivamente, situándose por debajo de sus medias móviles de 20 días y con un RSI de 1 hora profundamente deprimido (por debajo de 24). Los mercados tradicionales de Wall Street se encuentran cerrados. El momentum alcista esperado no se materializó y el soporte ha cedido, activando nuestras reglas de gestión de riesgo."

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 95%): La posición ha alcanzado una pérdida de -2.08%, rompiendo el límite de stop-loss estricto del -2.0%. El momentum de corto plazo sigue deteriorándose con un RSI de 1 hora en 23.8 y un cambio de -2.18% en la última hora, por lo que es imperativo cortar la pérdida y proteger el capital.
- **[SELL] ETH-USD** (Confianza: 95%): La posición acumula una pérdida de -2.21%, excediendo el umbral de stop-loss del -2.0%. El RSI de 1 hora se mantiene en niveles muy débiles (23.3) y el impulso bajista persiste, obligando a la liquidación inmediata para preservar liquidez.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Las posiciones abiertas en SOL-USD y ETH-USD han superado nuestro límite de tolerancia de pérdida del -2.0% (actualmente rondando el -2.08% y -2.21%). Siguiendo estrictamente el plan táctico, procedemos a liquidar ambas posiciones para cortar las pérdidas a tiempo, preservar el capital remanente en efectivo y evitar un mayor deterioro ante la persistencia de la tendencia bajista. En el próximo ciclo buscaremos puntos de entrada con confirmación real de volumen y giro de RSI."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **67** | 🎯 **38.8%** (26W / 27L / 14BE) | 🔴 **$-1.84 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 18:40` | 🔴 SELL (-0.22$) | `ETH-USD` | $9.78 | $2370.09 | La posición acumula una pérdida de -2.21%, excediendo el umbral de stop-loss del -2.0%. El... |
| `2026-10-17 18:40` | 🔴 SELL (-0.21$) | `SOL-USD` | $9.79 | $101.78 | La posición ha alcanzado una pérdida de -2.08%, rompiendo el límite de stop-loss estricto ... |
| `2026-10-17 11:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2423.75 | ETH-USD presenta un RSI diario en niveles de sobreventa profunda (28.9) y un cambio positi... |
| `2026-10-17 10:20` | 🟢 BUY | `SOL-USD` | $10.00 | $103.94 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (22.5) y un cambio positiv... |
| `2026-10-17 04:30` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $104.94 | SOL-USD ha alcanzado un RSI de 1 hora de 70.4, entrando en zona de sobrecompra, y acumula ... |

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
