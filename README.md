# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 08:40:45`

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

> "El mercado tradicional se encuentra cerrado por fin de semana, por lo que el enfoque táctico se concentra al 100% en criptomonedas (activos abiertos 24/7). ETH-USD muestra un RSI diario muy deprimido en 29.8, pero su RSI de 1 hora está en 71.9 (sobrecompra), tras haber rebotado exitosamente en ciclos anteriores. Por otro lado, BTC-USD y SOL-USD están mostrando consolidación con RSI de 1 hora neutrales (43.7 y 61.2 respectivamente), sin el gatillo inmediato de sobreventa extrema (< 35) combinado con cambio positivo de 1 hora que exige la estrategia para un nuevo rebote agresivo. Contamos con $38.48 USD disponibles y mantendremos la disciplina esperando el momento exacto."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 50%): El RSI de 1 hora de BTC-USD está en 43.7 y su cambio de 1 hora es ligeramente negativo (-0.1%), lo que indica ausencia de un gatillo claro de rebote inminente. Esperaremos una compresión a sobreventa de corto plazo para ejecutar una compra táctica.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener la reserva de efectivo de $38.48 USD intacta. Monitorear de cerca BTC-USD y SOL-USD en busca de una compresión en el RSI de 1 hora por debajo de 35 acompañada de un cambio positivo de 1 hora para desplegar una entrada de $6.00 a $8.00 USD. Vigilar ETH-USD para posibles retrocesos que permitan reingresar tras la reciente toma de ganancias."
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
