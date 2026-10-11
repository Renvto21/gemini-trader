# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 04:40:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.02 USD** | **$40.25 USD** | **$40.27 USD** | 🟢 **+0.68%** ($+0.27) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.220708 | $109.23 | $109.38 | $24.14 | 📈 +0.14% |
| `ETH-USD` | 0.006448 | $2481.58 | $2498.52 | $16.11 | 📈 +0.68% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra señales mixtas, con un sesgo alcista moderado en los índices tradicionales (SPY, QQQ) y valores tecnológicos como MSFT, mientras que las criptomonedas principales se encuentran profundamente en zona de sobreventa técnica (RSI de SOL-USD en 21.2 y ETH-USD en 28.1). Esto presenta una oportunidad clásica de reversión a la media (mean reversion) para capturar rebotes agresivos en cripto tras fuertes caídas semanales, a pesar de la tendencia bajista temporal a corto plazo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD se encuentra en extrema sobreventa con un RSI de 21.2 tras una caída semanal del -9.42%. Mantenemos la posición para capturar el inminente rebote técnico hacia la media, alineado con nuestra estrategia agresiva de buscar retornos rápidos del 2% al 6%.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH-USD muestra un RSI profundamente deprimido en 28.1 y una caída acumulada semanal de -7.84%. Al igual que Solana, presenta una excelente oportunidad de rebote técnico y esperamos que recupere valor en las próximas sesiones sin necesidad de liquidar con ganancias mínimas.

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
