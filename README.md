# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 14:10:54`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.61 USD** | **$39.61 USD** | 🔴 **-0.98%** ($-0.39) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.369466 | $107.20 | $107.20 | $39.61 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra una dinámica mixta con oportunidades claras de sobreventa en criptomonedas clave. SOL-USD mantiene una fuerte condición de sobreventa con un RSI de 27.6 tras una caída semanal del 7.76%, lo que activa nuestra estrategia de rebote por reversión a la media. ETH-USD también presenta un RSI atractivo de 35.4 con un incremento diario del 2.45%. Mantenemos nuestra posición actual en SOL-USD ya que se encuentra en zona crítica de rebote y no ha roto los niveles de stop-loss, prefiriendo conservar la exposición para capturar el movimiento alcista esperado sin realizar ventas innecesarias en este momento."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): La posición en SOL-USD se mantiene intacta con un RSI de 27.6 que indica extrema sobreventa. Estamos listos para cazar el rebote técnico de +2% a +6% previsto por nuestra estrategia de alta volatilidad, por lo que no es momento de vender con una PnL neutral sino de esperar la recuperación.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 14:01` | 🟢 BUY | `SOL-USD` | $7.97 | $107.29 | SOL-USD presenta una condición de sobreventa extrema con un RSI de 27.9 y un desplome sema... |
| `2026-10-13 14:01` | 🔴 SELL | `ETH-USD` | $7.97 | $2508.01 | Liberamos la totalidad de la posición en ETH-USD para consolidar efectivo y rotar hacia un... |
| `2026-10-13 08:30` | 🟢 BUY | `ETH-USD` | $7.96 | $2505.44 | ETH-USD muestra un RSI de 35.6 en zona de sobreventa y un cambio positivo de 2.45% en 24 h... |
| `2026-10-13 08:30` | 🔴 SELL | `NVDA` | $7.96 | $226.32 | Liberamos capital de NVDA que se encuentra lateral y bajo su SMA20 sin momentum claro, par... |
| `2026-10-13 08:10` | 🟢 BUY | `NVDA` | $7.96 | $226.32 | Aprovechamos la corrección reciente de NVDA (caída de 7 días del -3.26% con un RSI de 46.4... |

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
