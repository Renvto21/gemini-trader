# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 08:10:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$11.97 USD** | **$39.49 USD** | 🔴 **-1.27%** ($-0.51) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83301.99 | $6.01 | 📈 +0.21% | 11h 9m |
| `SOL-USD` | 0.055840 | $107.45 | $106.61 | $5.95 | 📉 -0.78% | 8h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la atención se centra en las criptomonedas. BTC-USD y SOL-USD muestran una consolidación lateral con ligeras variaciones negativas en el corto plazo (1h), manteniendo un comportamiento relativamente estable respecto al ciclo anterior. No se observan señales inmediatas de sobreventa extrema o rupturas alcistas claras que justifiquen una nueva entrada agresiva, por lo que la prioridad actual es mantener la liquidez y proteger las posiciones abiertas."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 70%): BTC-USD se mantiene estable con un PnL positivo de +0.21% tras más de 11 horas de holding. No hay señales de sobrecompra ni motivos para vender, por lo que mantenemos la posición esperando el objetivo de take-profit.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD registra una ligera pérdida de -0.78% en un rango controlado, muy lejos del stop-loss estricto de -2.0%. El RSI diario sigue en zona de soporte potencial, por lo que mantenemos la posición para permitir que se desarrolle el rebote técnico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales en BTC-USD y SOL-USD bajo estricta vigilancia, respetando el stop-loss de -2.0% y buscando asegurar beneficios si alcanzan la zona de +2.0% a +3.5%. Los $27.53 USD de efectivo se mantendrán en reserva táctica esperando oportunidades de alta convicción en cripto o la apertura de los mercados tradicionales."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **49** | 🎯 **44.9%** (22W / 13L / 14BE) | 🔴 **$-0.39 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |

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
