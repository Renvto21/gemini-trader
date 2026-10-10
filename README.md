# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 23:40:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.23 USD** | **$40.34 USD** | 🟢 **+0.85%** ($+0.34) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.88 | $20.16 | 📈 +0.79% |
| `ETH-USD` | 0.006448 | $2481.58 | $2492.61 | $16.07 | 📈 +0.44% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema con SOL-USD (RSI en 22.2) y ETH-USD (RSI en 26.8), lo cual representa una excelente oportunidad de rebote técnico (Mean Reversion) a pesar de la tendencia bajista de corto plazo. Nuestras posiciones actuales muestran ganancias moderadas pero el RSI extremadamente bajo en ambos activos sugiere que están listos para un rebote alcista mayor, por lo que mantenemos la exposición actual y utilizaremos el efectivo disponible si es necesario, o mantenemos HOLD para dejar correr las ganancias según nuestra estrategia de alta volatilidad."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en clara sobreventa con un RSI de 22.2, acumulando una caída semanal del 8.16% pero mostrando un intento de estabilización en 24h. Nuestra posición está ligeramente en positivo (+0.79%). Dado que buscamos capturar rebotes rápidos y el activo está extremadamente deprimido técnicamente, mantenemos la posición para aprovechar el imminent rebote hacia la media.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD presenta condiciones técnicas similares a Solana, con un RSI de 26.8 indicando sobreventa profunda y un rendimiento de 7 días a la baja del 7.24%. La posición actual registra un beneficio modesto del 0.44%. Mantenemos la posición para permitir que el impulso compense la caída semanal y alcance nuestra meta de take-profit.

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
