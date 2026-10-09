# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 20:00:59`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.05 USD** | **$40.16 USD** | 🟢 **+0.40%** ($+0.16) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.11 | $20.02 | 📈 +0.08% |
| `ETH-USD` | 0.006448 | $2481.58 | $2486.69 | $16.03 | 📈 +0.21% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto presenta una fuerte condición de sobreventa en el corto plazo, con SOL-USD registrando un RSI extremadamente bajo de 20.3 y ETH-USD en 25.8. Esta capitulación técnica representa una oportunidad clásica de reversión a la media (Mean Reversion). Mientras tanto, el sector tecnológico (QQQ, NVDA) se mantiene estable y alcista, lo que sugiere que el apetito por el riesgo global sigue intacto y favorecerá un rebote rápido en los activos digitales de alta beta."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 90%): SOL-USD se encuentra en niveles de sobreventa extrema con un RSI de 20.3. Mantener la posición actual de $20.02 es crucial para capturar el inminente rebote técnico del 2% al 6%. No vendemos porque estaríamos liquidando en el soporte dinámico, y no compramos más para respetar el límite de reserva de efectivo de $4.00 USD.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH-USD muestra un RSI de 25.8, lo que indica un agotamiento de la fuerza vendedora. Con una asignación de $16.03, mantenemos la posición esperando una reversión alcista rápida hacia la media móvil. El efectivo restante ($4.11) se conserva como reserva mínima de seguridad.

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
