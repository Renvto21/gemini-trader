# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 00:50:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.54 USD** | **$17.09 USD** | **$39.63 USD** | 🔴 **-0.93%** ($-0.37) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2515.14 | $5.01 | 📈 +0.27% | 7h 40m |
| `BTC-USD` | 0.000072 | $83128.62 | $83732.15 | $6.04 | 📈 +0.73% | 3h 49m |
| `SOL-USD` | 0.055840 | $107.45 | $108.03 | $6.03 | 📈 +0.54% | 1h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto muestra un sesgo positivo de corto plazo con rebotes moderados en BTC-USD, ETH-USD y SOL-USD tras tocar niveles de sobreventa diaria, aunque la tendencia general sigue bajo la SMA20. Los mercados tradicionales de Wall Street permanecen cerrados (fin de semana o fuera de horario), por lo que toda la operativa activa se concentra exclusivamente en las criptomonedas 24/7."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD se encuentra operando con ganancia positiva (+0.73%) y un RSI de 1H en 62.1 mostrando impulso alcista continuo. Mantenemos la posición a la espera de la zona objetivo de take-profit (+2.0% a +3.5%).
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD presenta un rendimiento positivo estable (+0.27%) y un RSI de 1H en 59.1. Continuamos operando el rebote técnico diario buscando aproximarnos al take-profit.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD muestra un progreso positivo de +0.54% con un RSI de 1H en 65.1 tras la sólida entrada previa. Mantenemos el plan táctico de retención hasta la zona de toma de ganancias.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, ETH-USD y SOL-USD mientras continúen escalando hacia la zona objetivo de take-profit del +2.0% al +3.5% o alcancen un RSI de 1 hora superior a 70. Vigilar de cerca el comportamiento del precio para asegurar ganancias rápidamente y rotar capital según las reglas de momentum. El stop-loss estricto se mantiene en -2.0% y se preserva una reserva de liquidez adecuada."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **48** | 🎯 **45.8%** (22W / 12L / 14BE) | 🔴 **$-0.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |

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
