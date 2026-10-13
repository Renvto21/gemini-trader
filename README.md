# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 13:51:30`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.73 USD** | **$39.73 USD** | 🔴 **-0.68%** ($-0.27) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $107.53 | $31.74 | 📈 +0.33% |
| `ETH-USD` | 0.003177 | $2505.44 | $2513.71 | $7.99 | 📈 +0.33% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra señales mixtas con presión bajista previa en cripto pero con intentos claros de rebote técnico. SOL-USD presenta un RSI muy comprimido en 28.5 (sobreventa extrema) con un rebote en 24h del 1.87%, y ETH-USD también muestra un RSI de 36.5 y un incremento diario de 2.84%, indicando que las condiciones para la reversión a la media están activas. Mantenemos posiciones actuales mientras evaluamos la exposición total para mantener la reserva de efectivo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en zona de sobreventa extrema con un RSI de 28.5 y comenzando un rebote técnico del 1.87% en 24h. Mantenemos la posición para capturar el movimiento alcista esperado hacia la media.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 08:30` | 🟢 BUY | `ETH-USD` | $7.96 | $2505.44 | ETH-USD muestra un RSI de 35.6 en zona de sobreventa y un cambio positivo de 2.45% en 24 h... |
| `2026-10-13 08:30` | 🔴 SELL | `NVDA` | $7.96 | $226.32 | Liberamos capital de NVDA que se encuentra lateral y bajo su SMA20 sin momentum claro, par... |
| `2026-10-13 08:10` | 🟢 BUY | `NVDA` | $7.96 | $226.32 | Aprovechamos la corrección reciente de NVDA (caída de 7 días del -3.26% con un RSI de 46.4... |
| `2026-10-13 08:10` | 🔴 SELL | `ETH-USD` | $7.96 | $2494.07 | Ejecutamos rotación activa de capital vendiendo la posición completa de ETH-USD para liber... |
| `2026-10-13 02:30` | 🟢 BUY | `SOL-USD` | $4.00 | $108.19 | SOL-USD presenta un RSI extremadamente bajo de 26.3, lo que indica sobreventa técnica seve... |

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
