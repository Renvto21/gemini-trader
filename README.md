# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 20:41:16`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.05 USD** | **$40.16 USD** | 🟢 **+0.40%** ($+0.16) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.12 | $20.02 | 📈 +0.09% |
| `ETH-USD` | 0.006448 | $2481.58 | $2486.16 | $16.03 | 📈 +0.18% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado accionario tecnológico muestra solidez y estabilidad con SPY y QQQ en tendencia alcista sobre la SMA20, mientras que el sector cripto se encuentra en una fase de extrema sobreventa técnica (SOL-USD en RSI 20.3 y ETH-USD en RSI 25.7). Esta divergencia abre una ventana óptima para capturar rebotes agresivos por reversión a la media. Con una liquidez actual de $4.11 USD, nos encontramos en el límite de la reserva mínima requerida ($4.00 USD), por lo que la postura táctica más eficiente es mantener las posiciones abiertas para capturar el recorrido alcista proyectado del +2% al +5%."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 90%): SOL se encuentra en sobreventa extrema con un RSI 14 de 20.3 tras una caída semanal del -8.8%. Nuestra entrada está prácticamente a precio de mercado (+0.09% PnL). Mantener es la jugada con mayor asimetría positiva a la espera del catalizador de rebote hacia la SMA20 para ejecutar take-profit.
- **[HOLD] ETH-USD** (Confianza: 88%): ETH muestra señales iniciales de estabilización con +0.58% en 24h y un RSI deprimido en 25.7. Al estar en zona de reversión a la media y no haber alcanzado ni el objetivo de toma de ganancias (+2.5%) ni el nivel de stop-loss, mantenemos la posición con alta convicción para maximizar el retorno del rebote.

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
