# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 07:41:03`

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

> "El mercado tradicional se encuentra cerrado por fin de semana, por lo que toda la liquidez y atención táctica se centra en los activos cripto (24/7). ETH-USD y SOL-USD muestran RSI de 1 hora en zonas de sobrecompra o muy elevadas (80.3 y 70.2 respectivamente), mientras que BTC-USD mantiene un perfil neutral con RSI de 1 hora en 45.7 y RSI diario en 38.9. No hay oportunidades óptimas de rebote desde sobreventa extrema en este instante para los activos abiertos, por lo que se mantiene la postura de paciencia táctica y estricta conservación de liquidez."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): El activo se encuentra en una zona de consolidación con RSI diario en 38.9 y RSI de 1 hora en 45.7. No presenta una sobreventa extrema ni un momentum alcista confirmado para ejecutar una compra inmediata, por lo que se prefiere esperar a una mejor señal técnica.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantengo mi efectivo disponible de $38.48 USD respetando la reserva mínima de efectivo de $4.00 USD. ETH-USD (RSI 1h: 80.3) y SOL-USD (RSI 1h: 70.2) siguen elevados, por lo que esperaré un retroceso claro del RSI de 1 hora hacia niveles inferiores a 35 para buscar entradas de rebote agresivas. Monitorearé de cerca a BTC-USD por si se presenta una oportunidad de acumulación en soporte."
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
