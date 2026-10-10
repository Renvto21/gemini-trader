# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 07:00:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.24 USD** | **$40.35 USD** | 🟢 **+0.88%** ($+0.35) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.86 | $20.15 | 📈 +0.77% |
| `ETH-USD` | 0.006448 | $2481.58 | $2495.01 | $16.09 | 📈 +0.54% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto se encuentra en niveles de sobreventa extrema (RSI de ETH en 26.4 y SOL en 23.5), lo que representa una oportunidad ideal de rebote técnico según nuestra estrategia de mean reversion. Las posiciones actuales de SOL-USD y ETH-USD muestran ganancias moderadas (+0.77% y +0.54% respectivamente) pero aún no alcanzan el objetivo de take-profit del +2.5% ni presentan sobrecompra. Dado que mantenemos una reserva de efectivo muy ajustada ($4.11 USD) y nuestras posiciones actuales están operando correctamente dentro de su tendencia de recuperación tras caídas de 7 días, optamos por mantener ambas criptomonedas para permitirles madurar y capturar el impulso alcista esperado en el corto plazo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD presenta un RSI extremadamente bajo de 23.5, lo que indica sobreventa profunda y un potencial fuerte de rebote técnico. Aunque la posición actual muestra una ganancia leve del 0.77%, mantenemos la posición para capturar el movimiento completo hacia nuestro objetivo de take-profit sin alterar la liquidez mínima.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un RSI de 26.4, confirmando condiciones de sobreventa ideales para una recuperación inminente. La posición está ligeramente en positivo y cumple con nuestra tesis de retención mientras esperamos que el momentum alcista se acelere en las próximas sesiones.

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
