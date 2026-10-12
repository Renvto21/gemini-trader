# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 07:50:36`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$37.40 USD** | **$41.40 USD** | 🟢 **+3.50%** ($+1.40) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.307862 | $111.77 | $111.72 | $34.39 | 📉 -0.05% |
| `ETH-USD` | 0.001175 | $2553.82 | $2555.40 | $3.00 | 📈 +0.06% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con sesgo alcista moderado en índices tradicionales como SPY y QQQ, mientras que las criptomonedas se encuentran en una fase de consolidación bajista a corto plazo pero con indicadores de sobreventa atractivos (SOL con RSI en 32.1 y ETH con RSI en 36.0). Mantenemos nuestra exposición actual en SOL buscando un rebote técnico inminente desde la zona de soporte y observamos la posición en ETH. Dado que la reserva de efectivo está en el límite mínimo de $4.00 USD y no hay posiciones con ganancias superiores al 2.5% para tomar beneficios de inmediato, optamos por mantener nuestras posiciones actuales intactas y permitir que la estrategia de reversión a la media en cripto actúe."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 82%): SOL-USD se encuentra en condición de sobreventa técnica con un RSI de 32.1 y una caída acumulada del -7.51% en 7 días, cumpliendo exactamente con nuestra tesis de cazar rebotes. El PnL actual es prácticamente plano (-0.05%), por lo que mantenemos la posición para capturar el movimiento alcista esperado hacia la resistencia inmediata.
- **[HOLD] ETH-USD** (Confianza: 78%): ETH-USD muestra un RSI de 36.0 en zona de compresión bajista y un rendimiento reciente negativo del -5.27% en la semana. La posición actual es pequeña ($3.00 USD) y se encuentra estable con un leve beneficio del +0.06%, por lo que la mantenemos a la espera de una ruptura de momentum que justifique una ampliación o salida.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 07:40` | 🟢 BUY | `ETH-USD` | $3.00 | $2553.82 | ETH-USD presenta un RSI de 35.7 indicando condiciones cercanas a la sobreventa, lo que act... |
| `2026-10-12 07:30` | 🔴 SELL | `ETH-USD` | $7.00 | $2553.60 | ETH-USD se encuentra estancado con un PnL cercano a 0% sin momentum inmediato. Vendemos la... |
| `2026-10-12 07:00` | 🟢 BUY | `SOL-USD` | $4.00 | $111.65 | SOL-USD está en zona de sobreventa profunda con un RSI de 31.8 y una caída semanal de -7.5... |
| `2026-10-12 06:10` | 🟢 BUY | `ETH-USD` | $2.00 | $2552.03 | ETH-USD presenta un RSI de 35.5 en clara zona de sobreventa tras caídas semanales del -5.3... |
| `2026-10-12 05:50` | 🟢 BUY | `ETH-USD` | $5.00 | $2553.65 | ETH-USD presenta un RSI de 35.7 en clara zona de sobreventa técnica tras una caída semanal... |

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
