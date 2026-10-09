# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 20:30:52`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.05 USD** | **$40.16 USD** | 🟢 **+0.41%** ($+0.16) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.14 | $20.02 | 📈 +0.11% |
| `ETH-USD` | 0.006448 | $2481.58 | $2486.56 | $16.03 | 📈 +0.20% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado general muestra fortaleza en índices bursátiles (SPY, QQQ en tendencia alcista), mientras que el sector cripto atraviesa una condición extrema de sobreventa técnica tras fuertes retrocesos semanales. SOL-USD (RSI 20.4) y ETH-USD (RSI 25.8) presentan condiciones ideales de reversión a la media (Mean Reversion), con BTC-USD comenzando a estabilizarse (+1.07% en 24h). Con la liquidez en $4.11 USD justo en el límite de la reserva obligatoria ($4.00 USD), la estrategia cuantitativa óptima es mantener posiciones para capturar el rebote proyectado del +2% al +6% antes de ejecutar tomas de ganancias."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL se encuentra en niveles de extrema sobreventa con un RSI de 20.4 tras caer -8.78% en 7 días. La posición está en verde (+0.11%) y el ratio riesgo/beneficio favorece mantener con convicción alta para capitalizar el rebote técnico hacia la zona de take-profit (+2.5% a +5%).
- **[HOLD] ETH-USD** (Confianza: 85%): ETH muestra señales tempranas de giro alcista diario (+0.59%) con un RSI de 25.8 en zona de capitulación. Mantener es la táctica correcta para permitir que el momentum alcista se desarrolle sin forzar rotación prematura antes de alcanzar el objetivo de ganancia rápida.

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
