# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 08:50:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.23 USD** | **$40.34 USD** | 🟢 **+0.85%** ($+0.34) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.78 | $20.14 | 📈 +0.69% |
| `ETH-USD` | 0.006448 | $2481.58 | $2495.61 | $16.09 | 📈 +0.57% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto se encuentra en una fase de sobreventa extrema a corto plazo (RSI de ETH-USD en 26.5 y SOL-USD en 23.3), lo que representa una oportunidad clásica de mean reversion para cazar rebotes técnicos agresivos. Las posiciones actuales de SOL y ETH muestran ligeras ganancias pero aún no alcanzan el objetivo de +2.5% para take-profit, y el efectivo disponible es muy bajo ($4.11), cumpliendo con la reserva mínima de liquidez. Por lo tanto, mantenemos las posiciones actuales aprovechando la sobreventa y esperamos una rotación futura al alcanzar los objetivos de ganancia."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD tiene un RSI de 23.3 indicando sobreventa profunda. Mantenemos la posición para capturar el rebote técnico hacia la media, ya que la ganancia actual del 0.69% aún no alcanza nuestro umbral de take-profit del 2.5%.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD presenta un RSI de 26.5 en clara sobreventa técnica. Conservamos la posición actual esperando un rebote inminente que permita materializar ganancias rápidas.

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
