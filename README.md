# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 08:30:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.50 USD** | **$39.50 USD** | 🔴 **-1.24%** ($-0.50) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $106.85 | $31.54 | 📉 -0.30% |
| `ETH-USD` | 0.003177 | $2505.44 | $2505.44 | $7.96 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra oportunidades claras de rebote en el sector cripto debido a condiciones de sobreventa extrema, destacando ETH-USD con un RSI de 35.6 y un rendimiento alcista diario del 2.5%, lo que indica un fuerte potencial de mean reversion a corto plazo. Mantenemos SOL-USD ya que se encuentra en un RSI de 26.6 consolidando para un rebote inminente. NVDA se mantiene sin cambios significativos con una pérdida neutral cercana a cero, mientras que MSFT muestra un RSI de sobrecompra (>77) perfecto para evaluar tomas de ganancias si estuviera en cartera. Rotamos parte de la posición estancada en NVDA para capitalizar la fuerte recuperación técnica que está comenzando en ETH-USD."*

**Operaciones del ciclo:**
- **[SELL] NVDA** (Confianza: 82%): Liberamos capital de NVDA que se encuentra lateral y bajo su SMA20 sin momentum claro, para financiar la entrada en un activo de cripto con mayor velocidad de rebote.
- **[BUY] ETH-USD** (Confianza: 88%): ETH-USD muestra un RSI de 35.6 en zona de sobreventa y un cambio positivo de 2.45% en 24 horas, lo que activa nuestra estrategia de cazar rebotes por mean reversion con alta convicción para buscar un rendimiento rápido del +3% al +5%.

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
