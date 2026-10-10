# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 10:00:52`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.19 USD** | **$40.30 USD** | 🟢 **+0.75%** ($+0.30) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.62 | $20.11 | 📈 +0.55% |
| `ETH-USD` | 0.006448 | $2481.58 | $2494.14 | $16.08 | 📈 +0.51% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa técnica con SOL-USD (RSI 22.7) y ETH-USD (RSI 26.3) profundamente deprimidos tras caídas semanales cercanas al -9% y -8%. Por otro lado, MSFT presenta un RSI de sobrecompra en 72.3 tras fuertes ganancias. Con un efectivo actual de $4.11 y nuestras posiciones actuales con ganancias mínimas sin alcanzar aún el objetivo del +2.5% de take-profit, decidimos mantener la disciplina y retener las posiciones en cripto para cazar el rebote inminente de mean-reversion, operando bajo una postura de mantener liquidez estricta."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en un estado de sobreventa extrema (RSI de 22.7). A pesar de la tendencia bajista de corto plazo, las condiciones son ideales para un rebote técnico inminente hacia la media. Mantenemos la posición para capturar el movimiento alcista.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD presenta un RSI de 26.3, también en zona de profunda sobreventa. Las caídas semanales abren espacio para un fuerte impulso de recuperación técnica. Retenemos para proteger el capital y buscar el objetivo de ganancia del +2.5%.

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
