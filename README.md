# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 03:30:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.02 USD** | **$40.28 USD** | **$40.30 USD** | 🟢 **+0.76%** ($+0.30) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.220708 | $109.23 | $109.43 | $24.15 | 📈 +0.18% |
| `ETH-USD` | 0.006448 | $2481.58 | $2501.70 | $16.13 | 📈 +0.81% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo alcista moderado en índices tradicionales como SPY y QQQ, mientras que el sector cripto (SOL-USD y ETH-USD) se encuentra en niveles extremos de sobreventa técnica con RSI en 22.0 y 27.5 respectivamente, tras caídas semanales significativas. Mantenemos nuestras posiciones en cripto buscando aprovechar el rebote técnico por mean reversion, y dado que estamos completamente invertidos con efectivo casi nulo, no ejecutaremos nuevas compras en este ciclo para no sobreapalancar la cartera."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD presenta un RSI extremadamente bajo de 22.0, lo que indica una clara sobreventa y un potencial inminente de rebote alcista. Mantenemos la posición para capturar el movimiento táctico esperado.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD registra un RSI de 27.5 en zona de sobreventa con una ganancia actual del 0.81%. Mantenemos la posición para buscar una toma de ganancias cercana al objetivo de +2.5%.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 03:20` | 🟢 BUY | `SOL-USD` | $12.00 | $109.35 | SOL-USD se encuentra en una situación de sobreventa técnica masiva con un RSI de 14 en 21.... |
| `2026-10-11 03:20` | 🔴 SELL | `MSFT` | $12.00 | $535.07 | MSFT ha entrado en zona de sobrecompra técnica con un RSI de 72.3. Aplicando la regla táct... |
| `2026-10-11 03:10` | 🟢 BUY | `MSFT` | $12.00 | $535.07 | Aprovechando la fuerte subida de MSFT (2.38% en 24h y RSI de 72.3 en zona de aceleración d... |
| `2026-10-11 03:10` | 🔴 SELL | `SOL-USD` | $12.02 | $109.29 | Liberando parcialmente capital de SOL-USD para aprovechar una rotación táctica hacia activ... |
| `2026-10-11 02:20` | 🟢 BUY | `SOL-USD` | $4.11 | $109.54 | SOL-USD se encuentra en extrema sobreventa técnica con un RSI de 22.4 y una caída semanal ... |

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
