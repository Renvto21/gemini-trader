# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 21:30:52`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.08 USD** | **$40.19 USD** | 🟢 **+0.48%** ($+0.19) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.23 | $20.04 | 📈 +0.19% |
| `ETH-USD` | 0.006448 | $2481.58 | $2488.37 | $16.04 | 📈 +0.27% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto presenta una fuerte condición de sobreventa en el corto plazo, con SOL-USD y ETH-USD registrando niveles de RSI extremadamente bajos (20.5 y 26.1 respectivamente). Mientras tanto, el sector tecnológico (NVDA, QQQ) muestra mayor resiliencia pero con menor potencial de rebote inmediato en comparación con las criptomonedas. Mantener la exposición actual en SOL y ETH es la decisión táctica más óptima para capturar el inminente rebote técnico (Mean Reversion) sin comprometer la reserva de liquidez mínima de $4.00 USD."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 90%): SOL se encuentra en una zona de sobreventa extrema con un RSI de 20.5. Vender en este punto iría en contra de nuestra estrategia de rebotes técnicos. Mantenemos la posición con alta convicción esperando un movimiento rápido al alza del +2% al +6%.
- **[HOLD] ETH-USD** (Confianza: 88%): ETH presenta un RSI de 26.1, confirmando una fuerte capitulación de corto plazo. Dado que el precio promedio de compra está prácticamente a la par del precio actual, mantenemos la posición para maximizar el retorno cuando comience el rebote de la liquidez global.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-09 19:00` | 🟢 BUY | `ETH-USD` | $5.00 | $2482.07 | ETH-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.0. Utilizando el c... |
| `2026-10-09 19:00` | 🔴 SELL | `NVDA` | $4.99 | $229.28 | Rotación activa de capital. NVDA se encuentra estancada con un rendimiento de -0.16% y un ... |
| `2026-10-09 18:50` | 🟢 BUY | `SOL-USD` | $5.00 | $108.91 | Oportunidad de alta convicción por sobreventa extrema. SOL-USD tiene un RSI de 20.2 tras u... |
| `2026-10-09 18:50` | 🔴 SELL | `QQQ` | $5.00 | $751.27 | Rotación de capital activo. QQQ se encuentra estancado con rendimiento plano (-0.06%) y si... |
| `2026-10-09 18:40` | 🟢 BUY | `SOL-USD` | $5.00 | $109.02 | SOL-USD está extremadamente sobrevendido con un RSI de 20.3. Ejecutamos una compra agresiv... |

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
