# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 16:30:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.37 USD** | **$19.77 USD** | **$38.14 USD** | 🔴 **-4.65%** ($-1.86) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.097172 | $102.91 | $101.52 | $9.86 | 📉 -1.35% | 5h 29m |
| `ETH-USD` | 0.004205 | $2377.97 | $2354.98 | $9.90 | 📉 -0.97% | 4h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se encuentra abierto 24/7 pero mantiene una estructura lateral a bajista con baja volatilidad de corto plazo. SOL-USD y ETH-USD muestran RSI de 1 hora deprimidos (28.6 y 22.7 respectivamente), lo que indica agotamiento del impulso bajista de corto plazo pero sin una confirmación alcista todavía. Los mercados tradicionales están cerrados, por lo que toda la atención se centra en la gestión de las criptomonedas abiertas."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 60%): La posición en SOL-USD registra una pérdida leve de -1.35% tras más de 5 horas. Aunque el RSI de 1 hora está en 28.6 (sobreventa leve), el precio se mantiene consolidando y no ha tocado el stop-loss estricto del -2.0%. Esperamos un reote técnico.
- **[HOLD] ETH-USD** (Confianza: 60%): ETH-USD muestra un comportamiento similar con una pérdida de -0.97% y un RSI de 1 hora en 22.7. Mantenemos la posición buscando la reacción alcista desde el soporte diario, controlando el riesgo de cerca.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Las posiciones en SOL-USD y ETH-USD llevan más de 4-5 horas abiertas con pérdidas menores pero estancadas. Mantendremos las posiciones vigentes un ciclo más vigilando estrictamente el límite de pérdida del -2.0%. Si el RSI de 1 hora rompe al alza superando 35 con volumen, mantendremos; de lo contrario, en el próximo ciclo procederemos a rotar capital hacia liquidez o activos más dinámicos."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **70** | 🎯 **41.4%** (29W / 27L / 14BE) | 🔴 **$-1.49 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 12:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2377.97 | ETH-USD presenta un RSI diario extremadamente bajo en 22.0 y un RSI de 1 hora saliendo de ... |
| `2026-10-18 11:01` | 🟢 BUY | `SOL-USD` | $10.00 | $102.91 | SOL-USD muestra un RSI diario extremadamente bajo (16.4) en zona de sobreventa profunda y ... |
| `2026-10-18 08:00` | 🔴 SELL (+0.13$) | `ETH-USD` | $10.13 | $2415.11 | ETH-USD registra un RSI de 1H en 72.1 (sobrecompra) y una ganancia de +1.26%. Se procede a... |
| `2026-10-18 08:00` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $103.84 | SOL-USD presenta un RSI de 1H en 67.6 acercándose a zona de sobrecompra con una ganancia d... |
| `2026-10-18 08:00` | 🔴 SELL (+0.10$) | `BTC-USD` | $10.08 | $81974.15 | BTC-USD ha alcanzado un RSI de 1H en 78.8 (sobrecompra profunda) tras el rebote esperado, ... |

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
