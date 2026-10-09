# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 19:00:54`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$35.96 USD** | **$40.07 USD** | 🟢 **+0.18%** ($+0.07) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $108.79 | $19.96 | 📉 -0.21% |
| `ETH-USD` | 0.006448 | $2481.58 | $2482.07 | $16.00 | 📈 +0.02% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra divergencias importantes: mientras el sector tecnológico tradicional (MSFT, QQQ) mantiene un sesgo alcista, el mercado cripto (SOL, ETH) ha sufrido fuertes correcciones semanales que han llevado sus indicadores técnicos a niveles de sobreventa extrema (RSI < 25). Esta capitulación de corto plazo representa una oportunidad ideal de rebote técnico (Mean Reversion) bajo nuestra estrategia agresiva."*

**Operaciones del ciclo:**
- **[SELL] NVDA** (Confianza: 85%): Rotación activa de capital. NVDA se encuentra estancada con un rendimiento de -0.16% y un RSI neutral de 52.8 sin momentum claro. Liquidamos la posición para liberar $4.99 USD de efectivo y financiar una jugada de mayor convicción y potencial de rebote en cripto.
- **[BUY] ETH-USD** (Confianza: 90%): ETH-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.0. Utilizando el capital liberado de NVDA, incrementamos nuestra posición para capturar un rebote técnico rápido hacia la media, manteniendo la reserva de liquidez por encima del mínimo de $4.00 USD.

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
