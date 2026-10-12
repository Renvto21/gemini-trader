# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 07:20:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$41.30 USD** | **$41.31 USD** | 🟢 **+3.27%** ($+1.31) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.307862 | $111.77 | $111.42 | $34.30 | 📉 -0.32% |
| `ETH-USD` | 0.002742 | $2553.19 | $2553.88 | $7.00 | 📈 +0.03% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo mixto con los índices principales y la tecnología con buen soporte alcista, mientras que las criptomonedas continúan sufriendo caídas semanales pero presentan condiciones técnicas claras de sobreventa (ETH con RSI 35.8 y SOL con RSI 31.0). Mantengo la postura de gestión táctica rotando capital para aprovechar los rebotes en cripto y maximizar la eficiencia del portafolio."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 82%): SOL-USD se encuentra en clara sobreventa con un RSI de 31.0 tras una caída semanal del -7.76%. Aunque está bajo la SMA20, esperamos un rebote técnico inminente de corto plazo para capturar ganancias del 2% al 4%.
- **[HOLD] ETH-USD** (Confianza: 78%): ETH-USD muestra un RSI de 35.8 en zona de atractiva sobreventa técnica. Mantenemos la posición actual para aprovechar la reversión a la media junto con el impulso general del ecosistema cripto.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 07:00` | 🟢 BUY | `SOL-USD` | $4.00 | $111.65 | SOL-USD está en zona de sobreventa profunda con un RSI de 31.8 y una caída semanal de -7.5... |
| `2026-10-12 06:10` | 🟢 BUY | `ETH-USD` | $2.00 | $2552.03 | ETH-USD presenta un RSI de 35.5 en clara zona de sobreventa tras caídas semanales del -5.3... |
| `2026-10-12 05:50` | 🟢 BUY | `ETH-USD` | $5.00 | $2553.65 | ETH-USD presenta un RSI de 35.7 en clara zona de sobreventa técnica tras una caída semanal... |
| `2026-10-12 05:50` | 🔴 SELL | `SOL-USD` | $5.00 | $111.85 | Liberamos una pequeña porción de SOL-USD para rescatar liquidez y financiar una entrada tá... |
| `2026-10-12 05:30` | 🔴 SELL | `ETH-USD` | $5.98 | $2553.85 | Rotación activa de capital. ETH se encuentra estancado y bajo su SMA20 con un PnL de -0.33... |

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
