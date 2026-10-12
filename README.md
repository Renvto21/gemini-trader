# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 23:00:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.93 USD** | **$32.31 USD** | **$41.24 USD** | 🟢 **+3.10%** ($+1.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.289416 | $111.58 | $111.64 | $32.31 | 📈 +0.05% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con sesgo alcista en indices y tecnologia (QQQ, SPY y MSFT firmes sobre sus medias moviles), mientras que las criptomonedas (SOL y ETH) presentan condiciones tecnicas de sobreventa extrema (RSI de 27.3 y 34.2 respectivamente) tras caidas semanales. Mantengo una posicion pesada en SOL-USD que se encuentra estancada con rendimiento cercano a cero, y una pequena fraccion en ETH-USD. Dado que ETH-USD tiene un valor muy bajo ($3.92) y no muestra el momentum agresivo que busco para rotacion rapida, y teniendo en cuenta que la posicion en SOL-USD esta practicamente plana, decido mantener SOL-USD para capturar el rebote por sobreventa extrema dada su cercania a soporte, pero realizo una accion estrategica para optimizar capital."*

**Operaciones del ciclo:**
- **[SELL] ETH-USD** (Confianza: 85%): La posicion en ETH-USD esta estancada y representa un monto muy pequeno ($3.92) sin suficiente fuerza de recuperacion inmediata. Vendo la totalidad para liberar efectivo y sumarlo a la reserva tactica, preparandome para rotar agresivamente hacia activos con mejor momento tecnico si surge la oportunidad.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 23:00` | 🔴 SELL | `ETH-USD` | $3.92 | $2541.25 | La posicion en ETH-USD esta estancada y representa un monto muy pequeno ($3.92) sin sufici... |
| `2026-10-11 22:00` | 🔴 SELL | `ETH-USD` | $5.00 | $2542.93 | Vendemos parcialmente la posición en ETH-USD para liberar efectivo y cumplir con la regla ... |
| `2026-10-11 21:50` | 🟢 BUY | `ETH-USD` | $8.92 | $2542.73 | ETH-USD está en condiciones de clara sobreventa técnica (RSI de 34.5) tras una caída seman... |
| `2026-10-11 21:50` | 🔴 SELL | `SOL-USD` | $8.93 | $111.63 | Liberamos una fracción de la posición en SOL-USD que se encuentra estancada con rendimient... |
| `2026-10-11 21:20` | 🟢 BUY | `SOL-USD` | $4.24 | $111.11 | Aprovechamos el capital liberado para incrementar la exposición en SOL-USD. Se encuentra e... |

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
