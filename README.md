# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 08:20:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.16 USD** | **$39.16 USD** | 🔴 **-2.10%** ($-0.84) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $105.69 | $31.20 | 📉 -1.38% |
| `NVDA` | 0.035171 | $226.32 | $226.32 | $7.96 | 📈 -0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra condiciones mixtas con un sesgo bajista temporal en varios activos principales, pero destacan oportunidades de sobreventa extrema en criptomonedas como SOL-USD con un RSI en 23.2, lo que representa una clara oportunidad de rebote técnico (Mean Reversion) para capturar movimientos alcistas rápidos. Mantenemos nuestras posiciones actuales esperando el impulso y gestionando estrictamente el riesgo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 90%): SOL-USD se encuentra en una situación de sobreventa extrema con un RSI de 23.2 tras una caída semanal del 9.06%. Mantenemos la posición actual para cazar el inminente rebote técnico hacia la resistencia inmediata, cumpliendo con nuestra estrategia agresiva de buscar retornos rápidos.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 08:10` | 🟢 BUY | `NVDA` | $7.96 | $226.32 | Aprovechamos la corrección reciente de NVDA (caída de 7 días del -3.26% con un RSI de 46.4... |
| `2026-10-13 08:10` | 🔴 SELL | `ETH-USD` | $7.96 | $2494.07 | Ejecutamos rotación activa de capital vendiendo la posición completa de ETH-USD para liber... |
| `2026-10-13 02:30` | 🟢 BUY | `SOL-USD` | $4.00 | $108.19 | SOL-USD presenta un RSI extremadamente bajo de 26.3, lo que indica sobreventa técnica seve... |
| `2026-10-13 01:30` | 🟢 BUY | `SOL-USD` | $6.23 | $107.75 | SOL-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.8 tras una caída s... |
| `2026-10-13 01:10` | 🟢 BUY | `ETH-USD` | $8.00 | $2506.03 | ETH-USD se encuentra en clara sobreventa técnica con un RSI de 31.1 tras una caída semanal... |

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
