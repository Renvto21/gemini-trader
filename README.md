# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 11:21:08`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$39.12 USD** | **$0.00 USD** | **$39.12 USD** | 🔴 **-2.19%** ($-0.88) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *(Ninguna posición abierta - 100% en efectivo)* | - | - | - | - | - | - |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El portafolio se encuentra actualmente en efectivo tras haber tomado ganancias con éxito en las posiciones de criptomonedas (BTC-USD, ETH-USD, SOL-USD). Analizando el mercado actual, la mayoría de los activos tradicionales operan con un sentimiento mixto o bajista de corto plazo. En el sector cripto (24/7), BTC-USD, ETH-USD y SOL-USD ya se encuentran con un RSI de 1 hora en zona de sobrecompra (>70), tras el fuerte impulso alcista reciente, por lo que no es prudente perseguir compras en este momento exacto. Mantendremos la liquidez en espera de una corrección menor o pullback que ofrezca un mejor punto de entrada para cazar nuevos rebotes técnicos."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD presenta un RSI de 1 hora en 71.9 (sobrecompra) tras el reciente movimiento alcista. No es el momento óptimo para comprar; esperamos un retroceso táctico para reingresar buscando el siguiente rebote.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "El efectivo actual es de $39.12 USD. Las criptomonedas principales (BTC, ETH, SOL) están en sobrecompra de 1h; esperaremos una corrección de corto plazo hacia soportes o una disminución del RSI por debajo de 50 para volver a abrir posiciones de alta convicción. Mantendremos el plan táctico de rotación rápida y control estricto de riesgo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **81** | 🎯 **44.4%** (36W / 30L / 15BE) | 🔴 **$-0.74 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-20 11:10` | 🔴 SELL (+0.12$) | `BTC-USD` | $8.69 | $82949.93 | BTC-USD muestra un RSI de 1 hora en 72.2 (sobrecompra) y un rendimiento positivo de +1.45%... |
| `2026-10-20 11:10` | 🔴 SELL (+0.28$) | `SOL-USD` | $10.28 | $107.08 | SOL-USD registra un excelente rendimiento de +2.83% con un RSI de 1 hora en sobrecompra (7... |
| `2026-10-20 11:10` | 🔴 SELL (+0.23$) | `ETH-USD` | $10.23 | $2449.11 | ETH-USD ha alcanzado un PnL de +2.32% y su RSI de 1 hora ha tocado el nivel de sobrecompra... |
| `2026-10-20 10:50` | 🔴 SELL (-0.08$) | `QQQ` | $9.92 | $713.02 | QQQ lleva más de 24 horas abierto sin momentum alcista, con un rendimiento de -0.82% y baj... |
| `2026-10-19 23:00` | 🟢 BUY | `BTC-USD` | $4.00 | $81646.39 | BTC-USD presenta un RSI de 1 hora en 27.7, nivel de sobreventa profunda ideal para un rebo... |

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
