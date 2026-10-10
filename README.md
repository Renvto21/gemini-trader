# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 03:20:33`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.23 USD** | **$40.34 USD** | 🟢 **+0.85%** ($+0.34) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.82 | $20.15 | 📈 +0.73% |
| `ETH-USD` | 0.006448 | $2481.58 | $2494.48 | $16.08 | 📈 +0.52% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa con SOL-USD (RSI 22.0) y ETH-USD (RSI 27.1), manteniendo una caída semanal pero iniciando un ligero rebote en 24h. Por otro lado, MSFT ha entrado en sobrecompra (RSI 72.3) con un fuerte impulso alcista, y activos de alto beta como QQQ y NVDA se mantienen estables. Nuestra liquidez está cerca del objetivo mínimo ($4.11 USD) y nuestras posiciones actuales en cripto están acumulando ligeras ganancias pero sin alcanzar el take-profit del 2.5%, por lo que optamos por mantenerlas y aprovechar el profundo descuento técnico para el rebote."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en una situación clara de sobreventa extrema (RSI de 22.0). Aunque la tendencia es bajista a corto plazo, el nivel del RSI sugiere un rebote técnico inminente hacia la media, por lo que mantenemos la posición para capturar el movimiento alcista.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD registra un RSI de 27.1 en zona de sobreventa con un leve repunte del 0.91% en 24h. Mantenemos la posición actual para aprovechar la recuperación técnica esperada en el ecosistema cripto.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-09 19:00` | 🟢 BUY | `ETH-USD` | $5.00 | $2482.07 | ETH-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.0. Utilizando el c... |
| `2026-10-09 19:00` | 🔴 SELL | `NVDA` | $4.99 | $229.28 | Rotación activa de capital. NVDA se encuentra estancada con un rendimiento de -0.16% y un ... |
| `2026-10-09 18:50` | 🟢 BUY | `SOL-USD` | $5.00 | $108.91 | Oportunidad de alta convicción por sobreventa extrema. SOL-USD tiene un RSI de 20.2 tras u... |
| `2026-10-09 18:50` | 🔴 SELL | `QQQ` | $5.00 | $751.27 | Rotación de capital activo. QQQ se encuentra estancado con rendimiento plano (-0.06%) y si... |
| `2026-10-09 18:40` | 🟢 BUY | `SOL-USD` | $5.00 | $109.02 | SOL-USD está extremadamente sobrevendido con un RSI de 20.3. Ejecutamos una compra agresiv... |

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
