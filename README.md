# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 01:00:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$2.09 USD** | **$37.60 USD** | **$39.70 USD** | 🔴 **-0.76%** ($-0.30) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.350407 | $106.82 | $107.31 | $37.60 | 📈 +0.46% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema, destacando SOL-USD con un RSI de 25.3 y ETH-USD con un RSI de 31.0, lo cual presenta una oportunidad ideal para cazar un rebote por reversión a la media. Nuestras posiciones actuales están estancadas con ganancias mínimas y necesitamos optimizar liquidez para capitalizar estas caídas en activos de alta volatilidad. El efectivo disponible es escaso, por lo que rotaremos una posición para maximizar la agresividad de la táctica."*

**Operaciones del ciclo:**
- **[SELL] ETH-USD** (Confianza: 85%): Vendemos la totalidad de ETH-USD para liberar capital líquido de inmediato y redirigirlo hacia la oportunidad de mayor potencial de rebote en el ecosistema cripto, manteniendo nuestra disciplina de rotación activa de capital.
- **[BUY] SOL-USD** (Confianza: 90%): Aprovechamos la sobreventa extrema de SOL-USD (RSI 25.3 y caída semanal de -11.16%) para incrementar posición con alta convicción. Buscamos capturar el rebote técnico rápido del 3% al 5% apoyados en el fuerte impulso de reversión a la media.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 01:00` | 🟢 BUY | `SOL-USD` | $12.00 | $107.31 | Aprovechamos la sobreventa extrema de SOL-USD (RSI 25.3 y caída semanal de -11.16%) para i... |
| `2026-10-13 01:00` | 🔴 SELL | `ETH-USD` | $10.10 | $2504.55 | Vendemos la totalidad de ETH-USD para liberar capital líquido de inmediato y redirigirlo h... |
| `2026-10-13 00:40` | 🟢 BUY | `SOL-USD` | $3.43 | $107.26 | SOL-USD se encuentra en profunda sobreventa técnica con un RSI de 25.2 y una caída del 11.... |
| `2026-10-13 00:10` | 🟢 BUY | `SOL-USD` | $10.00 | $106.61 | SOL-USD se encuentra en una clara condición de sobreventa con un RSI de 24.5 y una caída d... |
| `2026-10-12 23:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2480.01 | Ethereum se encuentra en clara sobreventa con un RSI de 29.5 y una caída semanal del 8.06%... |

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
