# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 08:10:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.24 USD** | **$39.25 USD** | 🔴 **-1.89%** ($-0.75) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $105.98 | $31.28 | 📉 -1.11% |
| `NVDA` | 0.035171 | $226.32 | $226.32 | $7.96 | 📈 -0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra una divergencia interesante con las criptomonedas experimentando caídas semanales pero con signos claros de sobreventa extrema (como SOL-USD con un RSI de 24.1), lo cual representa una excelente oportunidad táctica de rebote por mean reversion. Las posiciones actuales en cartera se mantienen dentro de los márgenes de tolerancia sin haber tocado el stop-loss estricto de -3.0%, pero no presentan un momentum alcista inmediato. El efectivo actual es de 0.0 USD, por lo que es necesario realizar una rotación táctica de capital para liberar liquidez y capitalizar el fuerte potencial de rebote en activos de alta beta como NVDA, que ha corregido recientemente."*

**Operaciones del ciclo:**
- **[SELL] ETH-USD** (Confianza: 85%): Ejecutamos rotación activa de capital vendiendo la posición completa de ETH-USD para liberar los 7.96 USD en efectivo y financiar una nueva entrada con mayor potencial de rebote técnico en el sector tecnológico de alto beta.
- **[BUY] NVDA** (Confianza: 85%): Aprovechamos la corrección reciente de NVDA (caída de 7 días del -3.26% con un RSI de 46.4) para cazar un rebote táctico de corto plazo dentro del sector tech, utilizando el capital rotado desde ETH-USD.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 08:10` | 🟢 BUY | `NVDA` | $7.96 | $226.32 | Aprovechamos la corrección reciente de NVDA (caída de 7 días del -3.26% con un RSI de 46.4... |
| `2026-10-13 08:10` | 🔴 SELL | `ETH-USD` | $7.96 | $2494.07 | Ejecutamos rotación activa de capital vendiendo la posición completa de ETH-USD para liber... |
| `2026-10-13 02:30` | 🟢 BUY | `SOL-USD` | $4.00 | $108.19 | SOL-USD presenta un RSI extremadamente bajo de 26.3, lo que indica sobreventa técnica seve... |
| `2026-10-13 01:30` | 🟢 BUY | `SOL-USD` | $6.23 | $107.75 | SOL-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.8 tras una caída s... |
| `2026-10-13 01:10` | 🟢 BUY | `ETH-USD` | $8.00 | $2506.03 | ETH-USD se encuentra en clara sobreventa técnica con un RSI de 31.1 tras una caída semanal... |

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
