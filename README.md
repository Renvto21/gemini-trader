# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 16:50:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.45 USD** | **$40.56 USD** | 🟢 **+1.39%** ($+0.56) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.34 | $20.24 | 📈 +1.21% |
| `ETH-USD` | 0.006448 | $2481.58 | $2513.39 | $16.21 | 📈 +1.28% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un tono mixto con recuperación en los índices tradicionales (SPY y QQQ) y en tecnológicas como MSFT, que ha entrado en sobrecompra con un RSI de 72.3. En el sector cripto, SOL-USD y ETH-USD se encuentran en profunda sobreventa técnica con RSI de 25.2 y 29.5 respectivamente, tras caídas semanales significativas. Mantenemos nuestras posiciones en SOL y ETH buscando capturar el rebote por mean reversion, y dado que nuestro efectivo disponible es de apenas $4.11 USD (alineado con la regla de reserva mínima) y ninguna de nuestras posiciones ha alcanzado aún el take-profit del +2.5% ni el stop-loss, la decisión táctica óptima es mantener el portafolio actual y dejar que madure el impulso alcista en cripto."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD está en clara sobreventa (RSI 25.2) y mostrando un repunte del 1.1% en 24h. Nuestra posición tiene una ganancia actual de +1.21%, acercándose a nuestra zona de take-profit del +2.5%. Mantenemos para capturar el rebote técnico completo.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD presenta condiciones similares con un RSI de 29.5 en zona de sobreventa y una ganancia actual de +1.28%. Esperamos la continuación del rebote hacia la resistencia a corto plazo para asegurar ganancias.

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
