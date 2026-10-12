# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 04:50:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.02 USD** | **$37.65 USD** | **$41.67 USD** | 🟢 **+4.18%** ($+1.67) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.280926 | $111.80 | $112.66 | $31.65 | 📈 +0.77% |
| `ETH-USD` | 0.002342 | $2562.29 | $2562.29 | $6.00 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra oportunidades claras de rebote técnico en criptomonedas debido a condiciones de sobreventa. ETH-USD ha entrado en zona de sobreventa con un RSI de 36.9 y una caída acumulada del 5.01% en los últimos 7 días, lo que representa una excelente oportunidad de mean reversion. Por su parte, SOL-USD se mantiene en cartera mostrando estabilidad con un RSI de 35.1, esperando su propio rebote alcista."*

**Operaciones del ciclo:**
- **[BUY] ETH-USD** (Confianza: 85%): ETH-USD presenta condiciones ideales de sobreventa con un RSI de 36.9 y un descuento del 5.01% en 7 días, cumpliendo con la estrategia de cazar rebotes en cripto para maximizar el potencial de crecimiento a corto plazo.

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
