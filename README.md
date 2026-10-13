# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 17:40:24`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.68 USD** | **$34.97 USD** | **$39.65 USD** | 🔴 **-0.87%** ($-0.35) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.279466 | $107.20 | $107.23 | $29.97 | 📈 +0.03% | 3h 38m |
| `ETH-USD` | 0.001993 | $2508.37 | $2509.33 | $5.00 | 📈 +0.04% | 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto muestra signos mixtos pero con oportunidades claras de sobreventa en SOL-USD (RSI de 27.7) y un rebote incipiente en ETH-USD. La liquidez disponible es baja debido a que estamos posicionados en activos altamente especulativos. Mantenemos una postura agresiva buscando capturar los rebotes técnicos de corto plazo según la estrategia de mean reversion."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra en una profunda zona de sobreventa con un RSI de 27.7, lo que ofrece un escenario ideal para un rebote técnico inminente. El holding time actual es de casi 4 horas, por lo que le daremos margen para que el momentum alcista se materialice.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones actuales en SOL-USD y ETH-USD supervisando de cerca el take-profit en caso de alcanzar un +2.5% o cruzar RSI de sobrecompra. Stop-loss estricto en -2.5%. Si SOL-USD no muestra aceleración en las próximas horas, rotar el capital hacia activos con mayor momentum."
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |
| `2026-10-13 16:30` | 🟢 BUY | `ETH-USD` | $9.68 | $2507.92 | ETH-USD muestra un RSI de 35.8 en zona de fuerte sobreventa y un impulso alcista diario de... |
| `2026-10-13 16:30` | 🔴 SELL | `SOL-USD` | $9.69 | $107.65 | Realizamos una toma parcial de beneficios y rotación de capital liberando aproximadamente ... |
| `2026-10-13 14:01` | 🟢 BUY | `SOL-USD` | $7.97 | $107.29 | SOL-USD presenta una condición de sobreventa extrema con un RSI de 27.9 y un desplome sema... |

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
