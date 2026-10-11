# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 21:50:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.29 USD** | **$40.40 USD** | 🟢 **+1.01%** ($+0.40) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.85 | $20.15 | 📈 +0.76% |
| `ETH-USD` | 0.006448 | $2481.58 | $2503.44 | $16.14 | 📈 +0.88% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un rebote técnico generalizado con activos tecnológicos y criptomonedas intentando estabilizarse tras caídas recientes. Las criptomonedas SOL-USD y ETH-USD se mantienen en niveles de profunda sobreventa (RSI 23.5 y 27.8 respectivamente), lo que presenta una oportunidad de acumulación para un rebote alcista, aunque con ganancias aún moderadas en cartera (+0.76% y +0.88%). Por otro lado, MSFT ha entrado en zona de sobrecompra clara (RSI 72.3) con un fuerte incremento diario del 2.38%. Mantendremos las posiciones actuales en cripto a la espera de que el impulso alcista se acelere, operando bajo una postura de retención estricta mientras evaluamos posibles rotaciones si el mercado rompe soportes."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra en extrema sobreventa técnica con un RSI de 23.5. A pesar de estar en tendencia bajista a corto plazo, el potencial de rebote por mean reversion es alto y la posición actual muestra una ligera ganancia positiva (+0.76%). Mantenemos la posición para capturar el movimiento alcista.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD presenta un RSI de 27.8, reflejando condiciones similares de sobreventa a las de SOL. La posición actual genera una rentabilidad del +0.88%. Conservamos los activos para permitir que el momentum alcista desarrolle su potencial hacia la zona de toma de beneficios.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-10 12:10` | 🔴 SELL | `MSFT` | $4.11 | $535.07 | MSFT ha alcanzado un RSI de 72.3 (sobrecompra) cumpliendo con la regla táctica de toma de ... |
| `2026-10-10 12:00` | 🟢 BUY | `MSFT` | $4.11 | $535.07 | Aprovechamos el capital liberado de GLD para entrar en MSFT, que muestra un fuerte momentu... |
| `2026-10-10 12:00` | 🔴 SELL | `GLD` | $4.11 | $384.58 | Liberamos la totalidad de la posición en GLD ya que se encuentra estancada con 0% de PnL y... |
| `2026-10-10 11:50` | 🟢 BUY | `GLD` | $4.11 | $384.58 | Aprovechamos el efectivo disponible para cazar un rebote por sobreventa en GLD, cuyo RSI s... |
| `2026-10-09 19:00` | 🟢 BUY | `ETH-USD` | $5.00 | $2482.07 | ETH-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.0. Utilizando el c... |

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
