# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 12:50:34`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$3.10 USD** | **$37.76 USD** | **$40.86 USD** | 🟢 **+2.15%** ($+0.86) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.340197 | $109.29 | $110.98 | $37.76 | 📈 +1.55% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema (RSI de SOL-USD en 25.2 y ETH-USD en 32.1), lo que representa una oportunidad ideal de rebote técnico (mean reversion) bajo nuestra estrategia agresiva. Dado que tenemos todo el capital invertido y cero efectivo actual, es necesario realizar una toma parcial de ganancias en SOL-USD (que muestra un avance constante) para liberar liquidez y así reasignar a nuevas oportunidades o consolidar posiciones de alta convicción."*

**Operaciones del ciclo:**
- **[SELL] ETH-USD** (Confianza: 85%): Vendemos la posición completa de ETH-USD para liberar capital en efectivo y aprovechar las caídas más profundas y el mayor potencial de rebote que presenta SOL-USD en este momento, rotando nuestro capital hacia el activo con mayor beta.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 12:50` | 🔴 SELL | `ETH-USD` | $3.10 | $2526.95 | Vendemos la posición completa de ETH-USD para liberar capital en efectivo y aprovechar las... |
| `2026-10-11 12:10` | 🟢 BUY | `ETH-USD` | $3.08 | $2504.75 | ETH-USD se encuentra en un estado de sobreventa extrema con un RSI de 28.6 y una caída sem... |
| `2026-10-11 11:00` | 🟢 BUY | `SOL-USD` | $12.00 | $109.33 | Aprovechamos la altísima sobreventa en SOL-USD (RSI de 21.2 y -9.46% en 7 días) para incre... |
| `2026-10-11 11:00` | 🔴 SELL | `ETH-USD` | $10.00 | $2499.66 | ETH-USD está estancado con un PnL cercano a 0% (-0.03%). Vendemos la posición completa par... |
| `2026-10-11 10:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2500.42 | ETH-USD presenta un RSI de 28.2 en profunda sobreventa y una caída semanal del 7.77%, cump... |

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
