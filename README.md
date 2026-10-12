# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 21:20:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$41.05 USD** | **$41.05 USD** | 🟢 **+2.62%** ($+1.05) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.369416 | $111.58 | $111.11 | $41.05 | 📉 -0.42% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un tono moderadamente alcista en los índices principales y tecnología, destacando el fuerte impulso de MSFT que ha entrado en zona de sobrecompra técnica (RSI en 72.3). Por el lado de criptomonedas, SOL-USD presenta una condición extrema de sobreventa con un RSI de 25.6 tras una caída semanal del -7.98%, lo cual representa una oportunidad clara de rebote por reversión a la media. Con un portafolio completamente invertido y sin efectivo disponible, es necesario realizar una rotación táctica vendiendo parcialmente una posición estancada o con menor potencial inmediato para liberar liquidez y cazar el rebote en Solana."*

**Operaciones del ciclo:**
- **[SELL] ETH-USD** (Confianza: 85%): Vendemos la totalidad de la posición en ETH-USD (valorada en aproximadamente 4.24 USD) para liberar capital y efectivo. Aunque ETH muestra un RSI bajo, SOL-USD ofrece una oportunidad de rebote técnico mucho más agresiva y con mayor potencial de recuperación inmediata dada su profunda sobreventa (RSI 25.6).
- **[BUY] SOL-USD** (Confianza: 90%): Aprovechamos el capital liberado para incrementar la exposición en SOL-USD. Se encuentra en una situación óptima de sobreventa extrema (RSI de 25.6) tras una corrección semanal del -7.98%. Aplicamos nuestra estrategia de cazar rebotes por mean reversion para capturar un movimiento rápido al alza.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 21:20` | 🟢 BUY | `SOL-USD` | $4.24 | $111.11 | Aprovechamos el capital liberado para incrementar la exposición en SOL-USD. Se encuentra e... |
| `2026-10-11 21:20` | 🔴 SELL | `ETH-USD` | $4.24 | $2534.63 | Vendemos la totalidad de la posición en ETH-USD (valorada en aproximadamente 4.24 USD) par... |
| `2026-10-11 21:10` | 🟢 BUY | `SOL-USD` | $3.82 | $111.13 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 25.7 y una caída semanal de... |
| `2026-10-11 21:10` | 🔴 SELL | `MSFT` | $3.82 | $535.07 | MSFT ha alcanzado un RSI de 72.3 en zona de sobrecompra y acumula un avance sólido. Ejecut... |
| `2026-10-11 21:00` | 🟢 BUY | `MSFT` | $3.82 | $535.07 | MSFT muestra un fuerte momentum alcista con un incremento de 2.38% en 24 horas y un RSI en... |

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
