# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 11:40:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$37.42 USD** | **$2.96 USD** | **$40.38 USD** | 🟢 **+0.95%** ($+0.38) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001175 | $2553.82 | $2517.68 | $2.96 | 📉 -1.42% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto presenta condiciones de sobreventa extrema, destacando SOL-USD con un RSI de 26.9 y una caída acumulada del 9.99% en 7 días, lo que activa nuestra regla de caza de rebrotes por Mean Reversion. La posición actual en SOL-USD ha tocado el límite del stop-loss estricto (-2.58%), por lo que es imperativo liquidarla para cortar pérdidas y reasignar el capital de manera más eficiente hacia nuevas oportunidades o mantener la disciplina de riesgo. ETH-USD muestra también un RSI bajo (31.8), pero decidimos mantener una postura neutral mientras rotamos liquidez."*

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 90%): Activación del stop-loss estricto debido a que la posición ha caído un -2.58%, rompiendo el nivel crítico de tolerancia al riesgo. Vendemos la totalidad para evitar caídas mayores y liberar efectivo para futuras operaciones tácticas.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 11:40` | 🔴 SELL | `SOL-USD` | $37.42 | $108.72 | Activación del stop-loss estricto debido a que la posición ha caído un -2.58%, rompiendo e... |
| `2026-10-12 11:10` | 🟢 BUY | `SOL-USD` | $4.00 | $110.16 | SOL-USD presenta un RSI extremadamente bajo de 28.8 y una caída acumulada del 8.8% en 7 dí... |
| `2026-10-12 07:40` | 🟢 BUY | `ETH-USD` | $3.00 | $2553.82 | ETH-USD presenta un RSI de 35.7 indicando condiciones cercanas a la sobreventa, lo que act... |
| `2026-10-12 07:30` | 🔴 SELL | `ETH-USD` | $7.00 | $2553.60 | ETH-USD se encuentra estancado con un PnL cercano a 0% sin momentum inmediato. Vendemos la... |
| `2026-10-12 07:00` | 🟢 BUY | `SOL-USD` | $4.00 | $111.65 | SOL-USD está en zona de sobreventa profunda con un RSI de 31.8 y una caída semanal de -7.5... |

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
