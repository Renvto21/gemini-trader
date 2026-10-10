# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 09:30:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.20 USD** | **$40.31 USD** | 🟢 **+0.77%** ($+0.31) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.63 | $20.11 | 📈 +0.56% |
| `ETH-USD` | 0.006448 | $2481.58 | $2494.59 | $16.08 | 📈 +0.52% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con debilidad y condiciones de sobreventa extrema en criptomonedas clave como SOL-USD (RSI 22.7) y ETH-USD (RSI 26.3), lo cual representa una excelente oportunidad de rebote técnico por mean reversion. Por otro lado, activos tecnológicos y el mercado general se mantienen con tendencia alcista, destacando MSFT en zona de sobrecompra (RSI 72.3). Mantendremos nuestras posiciones actuales en cripto mientras muestran señales de estabilización para capturar el rebote esperado."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en una condición de sobreventa extrema (RSI de 22.7) tras una caída semanal del -9.79%. Aunque está bajo la SMA20, la estrategia agresiva de mean reversion busca capturar el rebote alcista inminente. Mantenemos la posición para aprovechar la recuperación.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD presenta un RSI de 26.3, mostrando fuerte sobreventa técnica similar a Solana. Las ganancias actuales son moderadas (+0.52%) y esperamos un movimiento de recuperación mayor antes de tomar beneficios o rotar el capital.

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
