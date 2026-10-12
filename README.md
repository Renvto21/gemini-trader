# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 20:50:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$35.10 USD** | **$39.09 USD** | 🔴 **-2.26%** ($-0.91) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.220744 | $106.59 | $105.44 | $23.28 | 📉 -1.08% |
| `ETH-USD` | 0.004838 | $2480.41 | $2443.68 | $11.82 | 📉 -1.48% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto se encuentra bajo una fuerte presión bajista a corto plazo, con SOL-USD y ETH-USD experimentando caídas significativas que han llevado sus indicadores RSI a niveles extremos de sobreventa (23.4 y 27.5 respectivamente). Mantendremos nuestras posiciones actuales ya que estas condiciones extremas de sobreventa técnica ofrecen una oportunidad inminente de rebote por reversión a la media (mean reversion). Dado que nuestro efectivo disponible es de solo $4.00 USD (nuestro límite mínimo de reserva), no realizaremos nuevas compras en este ciclo y nos enfocaremos en permitir que nuestras criptomonedas capturen el rebote técnico tan pronto como el impulso bajista se agote."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD presenta un RSI extremadamente bajo de 23.4 y una caída de -5.22% en 24 horas. Aunque estamos en -1.08%, la estrategia de rebote técnico sugiere mantener la posición para capturar la inminente reversión alcista desde niveles de sobreventa profunda.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD registra un RSI de 27.5 en zona de profunda sobreventa. Mantenemos la posición actual con una pérdida de -1.48% esperando el rebote técnico hacia la media sin activar el stop-loss estricto.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 20:10` | 🟢 BUY | `SOL-USD` | $5.53 | $106.20 | SOL-USD presenta una condición de sobreventa extrema con un RSI de 24.1 y una caída de 7 d... |
| `2026-10-12 20:00` | 🟢 BUY | `SOL-USD` | $8.00 | $106.40 | SOL-USD se encuentra en clara sobreventa con un RSI de 24.3 y una caída de -11.91% en 7 dí... |
| `2026-10-12 19:40` | 🟢 BUY | `ETH-USD` | $12.00 | $2480.41 | ETH-USD se encuentra en una clara condición de sobreventa con un RSI de 14 de 29.5 y una c... |
| `2026-10-12 19:30` | 🟢 BUY | `SOL-USD` | $10.00 | $106.97 | SOL-USD se encuentra en clara condición de sobreventa profunda con un RSI de 24.9 y una ca... |
| `2026-10-12 19:20` | 🔴 SELL | `SOL-USD` | $39.52 | $106.94 | La posición actual en SOL-USD acumula un PnL de -2.11% acercándose peligrosamente al stop-... |

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
