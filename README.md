# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 03:10:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.24 USD** | **$40.35 USD** | 🟢 **+0.88%** ($+0.35) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.88 | $20.16 | 📈 +0.79% |
| `ETH-USD` | 0.006448 | $2481.58 | $2494.70 | $16.08 | 📈 +0.53% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa con SOL-USD (RSI 22.2) y ETH-USD (RSI 27.2) ofreciendo excelentes oportunidades de rebote por reversión a la media (Mean Reversion). Ambas posiciones actuales se mantienen estables con ganancias modestas sin alcanzar el objetivo de take-profit del +2.5%. El efectivo actual es de $4.11 USD, cumpliendo con la reserva mínima establecida de $4.00 USD, por lo que no hay capital disponible adicional para nuevas compras sin realizar una rotación táctica previa. Por lo tanto, se decide mantener (HOLD) las posiciones actuales mientras desarrollan su potencial de recuperación."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD presenta un RSI muy deprimido de 22.2, lo que indica sobreventa extrema y un potencial de rebote alcista considerable. Aunque el PnL es de +0.79%, aún no alcanza el umbral de take-profit del +2.5%, por lo que se mantiene para capturar el movimiento alcista esperado.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD registra un RSI de 27.2 en zona de clara sobreventa técnica. Mantiene una ganancia flotante de +0.53% y se prefiere conservar la posición para capitalizar la recuperación inminente de la criptomoneda junto a SOL-USD.

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
