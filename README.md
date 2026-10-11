# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 03:20:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.02 USD** | **$40.27 USD** | **$40.29 USD** | 🟢 **+0.72%** ($+0.29) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.220708 | $109.23 | $109.35 | $24.13 | 📈 +0.11% |
| `ETH-USD` | 0.006448 | $2481.58 | $2501.99 | $16.13 | 📈 +0.82% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo alcista moderado en los índices tradicionales (SPY, QQQ), mientras que las criptomonedas han sufrido caídas recientes pero presentan condiciones extremas de sobreventa técnica. MSFT ha alcanzado una zona de sobrecompra (RSI en 72.3) con una ganancia del 0.0%, cumpliendo la regla de rotación de capital para asegurar ganancias y liberar liquidez. Por otro lado, SOL-USD presenta un RSI extremadamente bajo de 21.7, lo que representa una oportunidad ideal de rebote por reversión a la media (Mean Reversion)."*

**Operaciones del ciclo:**
- **[SELL] MSFT** (Confianza: 90%): MSFT ha entrado en zona de sobrecompra técnica con un RSI de 72.3. Aplicando la regla táctica de toma rápida de ganancias y rotación de capital, vendemos la posición completa para liberar efectivo y financiar una oportunidad de alto potencial en cripto con sobreventa extrema.
- **[BUY] SOL-USD** (Confianza: 88%): SOL-USD se encuentra en una situación de sobreventa técnica masiva con un RSI de 14 en 21.7 tras una caída semanal del -10.02%. Esto activa nuestra estrategia agresiva de caza de rebordes por reversión a la media, asignando un tamaño de alta convicción para capturar el rebote alcista inminente.

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
