# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 01:40:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.20 USD** | **$40.32 USD** | 🟢 **+0.79%** ($+0.32) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.75 | $20.13 | 📈 +0.67% |
| `ETH-USD` | 0.006448 | $2481.58 | $2492.57 | $16.07 | 📈 +0.44% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto se encuentra en niveles extremos de sobreventa técnica (SOL-USD con RSI de 21.8 y ETH-USD con RSI de 26.8 tras caídas semanales superiores al 7%), lo cual activa nuestra estrategia de mean reversion para cazar rebotes agresivos. Por otro lado, en el sector tecnológico, MSFT muestra un RSI de 72.3 en zona de sobrecompra, pero nuestras posiciones actuales están en cripto y el efectivo disponible es de apenas 4.11 USD. Mantendremos las posiciones de SOL y ETH intactas ya que muestran un comportamiento inicial positivo y están configuradas para el rebote esperado, operando en HOLD por este ciclo al estar el capital desplegado y cumpliendo con la reserva mínima de liquidez."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 90%): SOL-USD presenta un RSI extremadamente bajo de 21.8 en zona de profunda sobreventa. Aunque acumula una caída semanal del 8.27%, el precio actual muestra signos de estabilización y el portafolio busca capitalizar el rebote técnico inminente sin necesidad de vender prematuramente.
- **[HOLD] ETH-USD** (Confianza: 88%): ETH-USD registra un RSI de 26.8, indicando también una fuerte sobreventa. Mantenemos la posición para capturar el movimiento de recuperación hacia la media, respetando los niveles de stop-loss y aprovechando la alta volatilidad a nuestro favor.

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
