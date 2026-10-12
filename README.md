# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 05:10:36`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.02 USD** | **$37.51 USD** | **$41.54 USD** | 🟢 **+3.84%** ($+1.54) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.280926 | $111.80 | $112.22 | $31.53 | 📈 +0.37% |
| `ETH-USD` | 0.002342 | $2562.29 | $2557.22 | $5.99 | 📉 -0.20% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa técnica con SOL-USD (RSI 33.7) y ETH-USD (RSI 36.2) tocando niveles atractivos para un rebote de reversión a la media (Mean Reversion). Ambas posiciones actuales están estancadas con mínimos movimientos. Por otro lado, en el sector tecnológico, MSFT ha entrado en fuerte sobrecompra (RSI 72.3), lo que indica un excelente momento para buscar oportunidades o mantener liquidez activa, aunque nuestra estrategia actual se enfoca en exprimir los rebotes de cripto con alta convicción."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en una zona clara de sobreventa con un RSI de 33.7 tras una caída semanal del 7.09%. Aunque el PnL actual es plano (+0.37%), mantenemos la posición para capturar el rebote técnico agresivo esperado en cripto según nuestra táctica.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 04:50` | 🟢 BUY | `ETH-USD` | $6.00 | $2562.29 | ETH-USD presenta condiciones ideales de sobreventa con un RSI de 36.9 y un descuento del 5... |
| `2026-10-12 04:30` | 🔴 SELL | `ETH-USD` | $10.02 | $2567.68 | Rotación activa de capital. ETH muestra una ganancia marginal del 0.23% sin momentum fuert... |
| `2026-10-12 03:40` | 🟢 BUY | `SOL-USD` | $4.00 | $112.34 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 29.5 y una caída semanal de... |
| `2026-10-12 03:20` | 🟢 BUY | `SOL-USD` | $2.92 | $112.10 | Aprovechamos la reserva de efectivo por encima del mínimo requerido ($4.00) para increment... |
| `2026-10-12 03:01` | 🟢 BUY | `ETH-USD` | $10.00 | $2561.78 | ETH-USD se encuentra en clara sobreventa técnica (RSI de 37) y muestra un repunte del 2.31... |

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
