# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 04:10:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$12.01 USD** | **$39.54 USD** | 🔴 **-1.16%** ($-0.46) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83420.94 | $6.02 | 📈 +0.35% | 7h 9m |
| `SOL-USD` | 0.055840 | $107.45 | $107.26 | $5.99 | 📉 -0.18% | 4h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se encuentra abierto con un comportamiento mixto y estable. BTC-USD registra una ganancia del 2.03% en 24h con un RSI de 1h en 60.5, mientras que SOL-USD muestra un cambio positivo moderado pero mantiene un RSI diario en niveles bajos de sobreventa extrema (27.8). Los mercados tradicionales (Wall Street) permanecen cerrados, por lo que toda la atención operativa se concentra en las criptomonedas disponibles 24/7."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): La posición en BTC-USD muestra un PnL positivo del 0.35% tras 7 horas abierta. El RSI de 1h se sitúa en 60.5, acercándose de forma saludable al impulso alcista sin llegar a sobrecompra extrema. Mantenemos la posición a la espera de buscar el objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD se mantiene estable con un PnL de -0.18%. A pesar de llevar cerca de 5 horas abierta, el RSI diario continúa en sobreventa extrema (27.8) respaldando la tesis de rebote técnico de mediano plazo. Dejamos que la posición desarrolle su potencial.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de BTC-USD y SOL-USD ya que muestran un comportamiento estable y rentabilidades cercanas al equilibrio, con BTC con un pequeño PnL positivo. Vigilaremos de cerca si BTC-USD se acerca al rango de sobrecompra en 1h (>70) para tomar ganancias parciales, o si SOL-USD rompe los soportes a la baja para activar el stop-loss. Mantendremos liquidez en reserva para futuras oportunidades de alta convicción."
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
