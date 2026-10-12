# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 11:00:53`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$36.94 USD** | **$40.95 USD** | 🟢 **+2.37%** ($+0.95) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.307862 | $111.77 | $110.31 | $33.96 | 📉 -1.31% |
| `ETH-USD` | 0.001175 | $2553.82 | $2539.03 | $2.98 | 📉 -0.58% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con ligera presión bajista en criptomonedas y tecnología de alto beta, aunque con excelentes oportunidades de reversión a la media. SOL-USD presenta un RSI extremadamente sobrevendido de 29.0 y una caída semanal del 8.67%, lo que activa nuestra estrategia agresiva de caza de rebotes técnicos. ETH-USD también se encuentra en niveles de sobreventa con RSI de 33.7. Mantenemos nuestra disciplina operativa buscando maximizar el rendimiento con una rotación eficiente y control de riesgo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 90%): SOL-USD muestra un RSI de 29.0 en clara zona de sobreventa técnica. A pesar de una pequeña pérdida actual de -1.31%, estamos ante una jugada clásica de rebote por mean reversion. El efectivo disponible es de apenas $4.00 USD cumpliendo la regla de reserva mínima, por lo que mantenemos la posición para capturar el inminente rebote alcista hacia el objetivo del +4%.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH-USD presenta un RSI de 33.7, muy cerca de la zona de sobreventa profunda y con una caída semanal acumulada del -5.88%. La posición actual es pequeña pero se mantiene intacta esperando el impulso alcista del sector cripto para tomar ganancias rápidas.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 07:40` | 🟢 BUY | `ETH-USD` | $3.00 | $2553.82 | ETH-USD presenta un RSI de 35.7 indicando condiciones cercanas a la sobreventa, lo que act... |
| `2026-10-12 07:30` | 🔴 SELL | `ETH-USD` | $7.00 | $2553.60 | ETH-USD se encuentra estancado con un PnL cercano a 0% sin momentum inmediato. Vendemos la... |
| `2026-10-12 07:00` | 🟢 BUY | `SOL-USD` | $4.00 | $111.65 | SOL-USD está en zona de sobreventa profunda con un RSI de 31.8 y una caída semanal de -7.5... |
| `2026-10-12 06:10` | 🟢 BUY | `ETH-USD` | $2.00 | $2552.03 | ETH-USD presenta un RSI de 35.5 en clara zona de sobreventa tras caídas semanales del -5.3... |
| `2026-10-12 05:50` | 🟢 BUY | `ETH-USD` | $5.00 | $2553.65 | ETH-USD presenta un RSI de 35.7 en clara zona de sobreventa técnica tras una caída semanal... |

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
