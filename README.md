# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 03:50:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.02 USD** | **$40.38 USD** | **$40.40 USD** | 🟢 **+1.00%** ($+0.40) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.220708 | $109.23 | $109.77 | $24.23 | 📈 +0.49% |
| `ETH-USD` | 0.006448 | $2481.58 | $2504.93 | $16.15 | 📈 +0.94% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra resiliencia en los índices principales y acciones tecnológicas como MSFT, la cual ha entrado en zona de sobrecompra (RSI 72.3). Por otro lado, las criptomonedas SOL-USD y ETH-USD se encuentran en niveles de sobreventa extrema con RSI de 23.2 y 28.1 respectivamente, lo cual presenta una oportunidad ideal para mantener posiciones y buscar el rebote técnico según nuestra estrategia agresiva."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 90%): SOL-USD tiene un RSI extremadamente bajo de 23.2, lo que indica sobreventa profunda. Mantenemos la posición para capturar el rebote alcista inminente hacia nuestro objetivo de ganancia rápida.

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
