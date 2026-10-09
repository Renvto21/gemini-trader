# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 18:50:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.12 USD** | **$35.97 USD** | **$40.09 USD** | 🟢 **+0.23%** ($+0.09) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `NVDA` | 0.021772 | $229.65 | $229.28 | $4.99 | 📉 -0.16% |
| `SOL-USD` | 0.183448 | $109.02 | $108.91 | $19.98 | 📉 -0.10% |
| `ETH-USD` | 0.004433 | $2481.36 | $2482.00 | $11.00 | 📈 +0.03% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto presenta una capitulación severa a corto plazo con SOL-USD en un RSI extremadamente bajo de 20.2 y ETH-USD en 24.9, lo que representa una oportunidad excepcional de reversión a la media (mean reversion). Mientras tanto, la tecnología tradicional (QQQ) muestra un comportamiento lateral y estancado. Rotamos capital de QQQ hacia SOL-USD para maximizar el potencial de rebote rápido."*

**Operaciones del ciclo:**
- **[SELL] QQQ** (Confianza: 85%): Rotación de capital activo. QQQ se encuentra estancado con rendimiento plano (-0.06%) y sin momentum claro. Liberamos estos $5.00 USD para asignarlos a un activo con un RSI extremadamente deprimido que ofrece un ratio riesgo/beneficio mucho más explosivo en el corto plazo.
- **[BUY] SOL-USD** (Confianza: 90%): Oportunidad de alta convicción por sobreventa extrema. SOL-USD tiene un RSI de 20.2 tras una caída del -8.97% en los últimos 7 días. Con el efectivo liberado de QQQ, incrementamos nuestra exposición buscando capturar un rebote técnico rápido de entre +3% y +6%.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-09 18:50` | 🟢 BUY | `SOL-USD` | $5.00 | $108.91 | Oportunidad de alta convicción por sobreventa extrema. SOL-USD tiene un RSI de 20.2 tras u... |
| `2026-10-09 18:50` | 🔴 SELL | `QQQ` | $5.00 | $751.27 | Rotación de capital activo. QQQ se encuentra estancado con rendimiento plano (-0.06%) y si... |
| `2026-10-09 18:40` | 🟢 BUY | `SOL-USD` | $5.00 | $109.02 | SOL-USD está extremadamente sobrevendido con un RSI de 20.3. Ejecutamos una compra agresiv... |
| `2026-10-09 18:40` | 🔴 SELL | `SPY` | $5.03 | $778.57 | Liberamos capital de SPY, un activo de bajo beta y lento movimiento, para financiar una op... |
| `2026-10-09 18:31` | 🟢 BUY | `ETH-USD` | $6.00 | $2481.06 | Oportunidad de alta convicción por sobreventa extrema (RSI de 24.8). Con los $6.00 USD lib... |

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
