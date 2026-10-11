# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 20:10:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.02 USD** | **$41.02 USD** | **$41.04 USD** | 🟢 **+2.61%** ($+1.04) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.296859 | $111.70 | $111.10 | $32.98 | 📉 -0.53% |
| `ETH-USD` | 0.003174 | $2520.20 | $2533.43 | $8.04 | 📈 +0.52% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones claras de sobreventa técnica con SOL-USD registrando un RSI extremadamente bajo de 25.6 y ETH-USD en 33.1, lo que activa nuestra estrategia de cazar rebotes por mean reversion. Por otro lado, MSFT ha entrado en zona de sobrecompra con un RSI de 72.3. Nuestra liquidez en efectivo es casi nula (0.02 USD), por lo que debemos mantener nuestras posiciones con fuerte potencial de rebote como SOL-USD y asegurar la pequeña ganancia actual de ETH-USD si es necesario, pero dado que ETH está rebotando desde niveles de sobreventa, decidimos mantener ambas posiciones actuales para capturar la recuperación completa hacia el objetivo del +2% al +6%."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 90%): SOL-USD presenta un RSI muy deprimido de 25.6, lo que indica sobreventa profunda y una oportunidad ideal para un rebote técnico inminente según nuestra estrategia agresiva de mean reversion.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH-USD se mantiene estable con un RSI de 33.1 mostrando señales tempranas de recuperación tras caídas semanales, ideal para acompañar el impulso alcista del sector cripto.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 20:00` | 🟢 BUY | `SOL-USD` | $4.00 | $110.96 | SOL-USD se encuentra en una clara condicion de sobreventa tecnica profunda con un RSI de 2... |
| `2026-10-11 18:20` | 🟢 BUY | `ETH-USD` | $8.00 | $2520.20 | ETH-USD presenta un RSI de 31.1 y una caída acumulada del 7.04% en los últimos 7 días, sit... |
| `2026-10-11 17:50` | 🔴 SELL | `ETH-USD` | $12.02 | $2536.22 | ETH-USD se encuentra estancado con una ganancia mínima de +0.19% y bajo una tendencia baji... |
| `2026-10-11 17:40` | 🟢 BUY | `SOL-USD` | $4.00 | $111.14 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 25.7 y una... |
| `2026-10-11 14:10` | 🟢 BUY | `SOL-USD` | $5.16 | $111.90 | SOL-USD presenta un RSI de 28.2 indicando sobreventa clara tras una caída semanal del 7.33... |

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
