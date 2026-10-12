# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 04:20:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$41.71 USD** | **$41.71 USD** | 🟢 **+4.28%** ($+1.71) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.280926 | $111.80 | $112.77 | $31.68 | 📈 +0.87% |
| `ETH-USD` | 0.003904 | $2561.78 | $2569.61 | $10.03 | 📈 +0.31% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un tono mixto con recuperación en los índices principales y acciones tecnológicas como MSFT liderando con un RSI de sobrecompra en 72.3. En el segmento cripto, SOL y ETH se encuentran en zonas de sobreventa técnica (RSI de 35.5 y 37.8 respectivamente) tras caídas semanales, lo cual representa una oportunidad de rebote por reversión a la media según la estrategia táctica agresiva. Dado que el portafolio actual está invertido al 100% y sin efectivo disponible, y buscando mantener flexibilidad para capturar movimientos rápidos, se decide mantener las posiciones actuales en cripto que ya muestran un ligero repunte de 24 horas y están listas para buscar el objetivo de +2.5% o superior."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición en SOL-USD muestra un RSI en zona de sobreventa (35.5) y un ligero repunte del 1.37% en 24 horas. Mantenemos la posición para capturar el rebote técnico hacia el objetivo de ganancia rápida.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 03:40` | 🟢 BUY | `SOL-USD` | $4.00 | $112.34 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 29.5 y una caída semanal de... |
| `2026-10-12 03:20` | 🟢 BUY | `SOL-USD` | $2.92 | $112.10 | Aprovechamos la reserva de efectivo por encima del mínimo requerido ($4.00) para increment... |
| `2026-10-12 03:01` | 🟢 BUY | `ETH-USD` | $10.00 | $2561.78 | ETH-USD se encuentra en clara sobreventa técnica (RSI de 37) y muestra un repunte del 2.31... |
| `2026-10-12 03:01` | 🔴 SELL | `SOL-USD` | $16.91 | $112.74 | Vendemos parcialmente SOL-USD para capitalizar una pequeña ganancia y liberar efectivo, pe... |
| `2026-10-12 02:30` | 🟢 BUY | `SOL-USD` | $4.95 | $112.41 | SOL-USD mantiene un RSI en zona crítica de sobreventa (29.7) y un cambio positivo de 2.16%... |

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
