# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 06:10:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$38.48 USD** | **$0.00 USD** | **$38.48 USD** | 🔴 **-3.81%** ($-1.52) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *(Ninguna posición abierta - 100% en efectivo)* | - | - | - | - | - | - |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional (Wall Street) se encuentra completamente CERRADO, por lo que toda la atención y liquidez deben centrarse exclusivamente en el mercado de criptomonedas (ABIERTO 24/7). En cuanto a las criptomonedas analizadas (BTC-USD, ETH-USD y SOL-USD), ETH y SOL mantienen un RSI en temporalidad de 1 hora elevado en zona de sobrecompra (>80), mientras que Bitcoin se encuentra en un punto neutral (RSI 1H en 58). Siguiendo las reglas de nuestra estrategia de mean reversion y momentum, no es el momento óptimo para entrar en compras masivas ya que los rebotes recientes ya se han enfriado y los activos no muestran condiciones de sobreventa intradiaria extrema (<35). Mantengo la paciencia táctica y la disciplina de esperar caídas intradiarias más pronunciadas."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 50%): El activo se encuentra abierto pero su RSI de 1 hora se mantiene en 80.6 (sobrecompra), lo cual infringe la regla de entrada por rebote desde sobreventa extrema. Esperaré a una corrección intradiaria.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantengo mi efectivo disponible de $38.48 USD. Las criptomonedas siguen digiriendo los rebotes previos con RSI 1H elevados. Plan táctico para el próximo ciclo: monitorear de cerca a ETH-USD y SOL-USD en busca de una corrección intradiaria que hunda el RSI 1H por debajo de 35 y active una entrada agresiva de alto potencial de rebote. Mantener estricta disciplina en la reserva de efectivo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **65** | 🎯 **40.0%** (26W / 25L / 14BE) | 🔴 **$-1.41 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 04:30` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $104.94 | SOL-USD ha alcanzado un RSI de 1 hora de 70.4, entrando en zona de sobrecompra, y acumula ... |
| `2026-10-17 04:00` | 🔴 SELL (+0.07$) | `ETH-USD` | $10.07 | $2429.64 | ETH-USD ha alcanzado un RSI de 1 hora de 73.3, entrando en zona de sobrecompra. Siguiendo ... |
| `2026-10-16 16:30` | 🟢 BUY | `ETH-USD` | $10.00 | $2412.98 | ETH-USD muestra un RSI diario en niveles de sobreventa extrema (30.3) y un cambio positivo... |
| `2026-10-16 16:30` | 🔴 SELL (-0.11$) | `MSFT` | $6.39 | $526.18 | MSFT lleva más de 1 día y 5 horas abierto mostrando debilidad persistente y un rendimiento... |
| `2026-10-16 15:01` | 🟢 BUY | `SOL-USD` | $10.00 | $103.71 | SOL-USD presenta un RSI de 1 hora en 34.3 saliendo de la zona de sobreventa extrema, acomp... |

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
