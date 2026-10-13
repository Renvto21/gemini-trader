# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 10:33:23`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.49 USD** | **$39.49 USD** | 🔴 **-1.27%** ($-0.51) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $106.79 | $31.52 | 📉 -0.36% |
| `ETH-USD` | 0.003177 | $2505.44 | $2507.37 | $7.97 | 📈 +0.08% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra divergencia con consolidación en índices tradicionales y tech (NVDA -0.80%, QQQ -0.83%), mientras que el sector cripto exhibe señales incipientes de rebote técnico desde niveles de sobreventa severa. SOL-USD presenta un RSI 14 extremo de 26.5 con un giro positivo en 24h (+1.17%), y ETH-USD consolida en RSI 35.8 con avance de +2.58%. Ambos activos ofrecen una configuración clásica de reversión a la media con alto potencial de alcanzar el objetivo del +2% al +6%."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD se encuentra en sobreventa extrema (RSI 26.5) y muestra inicio de rebote (+1.17% en 24h). Con un PnL controlado de -0.36%, no activa stop-loss (-2.5%). Mantener es óptimo para capturar la expansión alcista hacia el target de toma de beneficios del +2.5% a +6%.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD se sitúa en zona de reversión alcista (RSI 35.8) con fuerte impulso de +2.58% en las últimas 24h. La posición está en terreno positivo (+0.08%) y con momentum favorable hacia el umbral de take-profit.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 08:30` | 🟢 BUY | `ETH-USD` | $7.96 | $2505.44 | ETH-USD muestra un RSI de 35.6 en zona de sobreventa y un cambio positivo de 2.45% en 24 h... |
| `2026-10-13 08:30` | 🔴 SELL | `NVDA` | $7.96 | $226.32 | Liberamos capital de NVDA que se encuentra lateral y bajo su SMA20 sin momentum claro, par... |
| `2026-10-13 08:10` | 🟢 BUY | `NVDA` | $7.96 | $226.32 | Aprovechamos la corrección reciente de NVDA (caída de 7 días del -3.26% con un RSI de 46.4... |
| `2026-10-13 08:10` | 🔴 SELL | `ETH-USD` | $7.96 | $2494.07 | Ejecutamos rotación activa de capital vendiendo la posición completa de ETH-USD para liber... |
| `2026-10-13 02:30` | 🟢 BUY | `SOL-USD` | $4.00 | $108.19 | SOL-USD presenta un RSI extremadamente bajo de 26.3, lo que indica sobreventa técnica seve... |

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
