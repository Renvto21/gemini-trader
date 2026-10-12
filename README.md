# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 04:30:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$10.02 USD** | **$31.66 USD** | **$41.68 USD** | 🟢 **+4.21%** ($+1.68) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.280926 | $111.80 | $112.70 | $31.66 | 📈 +0.80% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un tono mixto con sesgo alcista en índices tradicionales y tecnológicas principales, mientras que las criptomonedas como SOL y ETH se encuentran recuperándose desde niveles de sobreventa técnica con RSI cercano a 35-37. Nuestra posición actual en SOL-USD y ETH-USD está estancada con ganancias mínimas (< 1%) y sin el momentum explosivo deseado, por lo que rotaremos parte de este capital para asegurar liquidez y buscar oportunidades con mayor fuerza en el sector tecnológico o prepararnos para nuevos rebotes tácticos."*

**Operaciones del ciclo:**
- **[SELL] ETH-USD** (Confianza: 85%): Rotación activa de capital. ETH muestra una ganancia marginal del 0.23% sin momentum fuerte a corto plazo. Vendemos la posición completa para liberar los 10.02 USD en efectivo y cumplir con la estrategia de rotación hacia oportunidades con mayor beta o mantener la flexibilidad requerida.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 04:30` | 🔴 SELL | `ETH-USD` | $10.02 | $2567.68 | Rotación activa de capital. ETH muestra una ganancia marginal del 0.23% sin momentum fuert... |
| `2026-10-12 03:40` | 🟢 BUY | `SOL-USD` | $4.00 | $112.34 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 29.5 y una caída semanal de... |
| `2026-10-12 03:20` | 🟢 BUY | `SOL-USD` | $2.92 | $112.10 | Aprovechamos la reserva de efectivo por encima del mínimo requerido ($4.00) para increment... |
| `2026-10-12 03:01` | 🟢 BUY | `ETH-USD` | $10.00 | $2561.78 | ETH-USD se encuentra en clara sobreventa técnica (RSI de 37) y muestra un repunte del 2.31... |
| `2026-10-12 03:01` | 🔴 SELL | `SOL-USD` | $16.91 | $112.74 | Vendemos parcialmente SOL-USD para capitalizar una pequeña ganancia y liberar efectivo, pe... |

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
