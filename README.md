# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 11:42:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.78 USD** | **$39.78 USD** | 🔴 **-0.55%** ($-0.22) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $107.66 | $31.78 | 📈 +0.45% |
| `ETH-USD` | 0.003177 | $2505.44 | $2518.09 | $8.00 | 📈 +0.50% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra señales claras de rebote técnico desde niveles de sobreventa. Solana (SOL-USD) registra un RSI de 28.9 con un impulso de +1.99% en 24h, mientras que Ethereum (ETH-USD) presenta un RSI de 36.9 y un alza de +3.02%. Ambas posiciones en cartera tienen ganancias modestas (+0.45% y +0.50%) pero aún no alcanzan la meta de take-profit del +2.5%. Dado que estamos completamente in invested y la prioridad es la rotación y captura de momentum rápido, mantendremos las posiciones actuales ya que muestran el rebote esperado tras caídas semanales."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD está rebotando desde una zona de sobreventa extrema (RSI 28.9). Mantiene un impulso positivo reciente del +1.99% en 24h, por lo que esperamos que continúe su camino hacia la zona objetivo de take-profit.

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
