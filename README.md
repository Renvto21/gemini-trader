# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 09:01:01`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.24 USD** | **$39.24 USD** | 🔴 **-1.89%** ($-0.76) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $106.07 | $31.31 | 📉 -1.03% |
| `ETH-USD` | 0.003177 | $2505.44 | $2496.33 | $7.93 | 📉 -0.36% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa técnica con SOL-USD (RSI en 24.4) y ETH-USD (RSI en 34.6), lo cual representa una oportunidad clara de rebote por reversión a la media según nuestra estrategia táctica agresiva. Dado que mantenemos el 100% del capital invertido y cero efectivo actual, mantendremos las posiciones actuales para permitirles completar el rebote técnico hacia la zona objetivo del +2% al +6%, aprovechando la recuperación reciente de 24 horas en ambos activos."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD se encuentra en un estado de sobreventa extrema con un RSI de 24.4, lo que aumenta drásticamente la probabilidad de un rebote técnico alcista a corto plazo. A pesar de una pequeña pérdida flotante de -1.03%, la estrategia exige mantener o cazar este tipo de oportunidades con alto potencial de recuperación rápida.

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
