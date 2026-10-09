# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 20:20:52`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.08 USD** | **$40.19 USD** | 🟢 **+0.46%** ($+0.19) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.22 | $20.04 | 📈 +0.18% |
| `ETH-USD` | 0.006448 | $2481.58 | $2487.61 | $16.04 | 📈 +0.24% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado tecnológico y los índices principales (QQQ, SPY) muestran fortaleza sostenida, mientras que el sector cripto se encuentra en niveles extremos de sobreventa técnica. SOL-USD (RSI 20.4) y ETH-USD (RSI 25.9) presentan condiciones ideales de reversión a la media (mean reversion) tras fuertes retrocesos de 7 días (-8.71% y -7.43% respectivamente). Con BTC rebotando +1.11% y el efectivo en $4.11 USD cumpliendo con la reserva mínima exigida ($4.00 USD), la estrategia óptima es mantener con firmeza las posiciones abiertas a la espera del catalizador de rebote rápido de +2% a +5% para ejecutar la toma de beneficios."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 90%): SOL se encuentra en una zona de sobreventa extrema con RSI 14 en 20.4. La posición ya está en leve terreno positivo (+0.18%) y tiene un ratio riesgo-beneficio altamente favorable. No se ha alcanzado el umbral de take-profit (+2.5%) ni de stop-loss (-2.5%), por lo que se mantiene la posición para capturar el rebote proyectado hacia los $112-$115.
- **[HOLD] ETH-USD** (Confianza: 86%): ETH muestra señales de estabilización diaria (+0.64%) con un RSI profundamente deprimido en 25.9. Al no disponer de liquidez sobrante por encima del piso mínimo de $4.00 USD y encontrarse la posición en ligera ganancia (+0.24%), se mantiene para maximizar el retorno del impulso técnico esperado sin asumir rotaciones innecesarias.

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
