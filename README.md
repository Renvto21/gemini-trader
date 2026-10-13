# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 21:30:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$38.61 USD** | **$0.00 USD** | **$38.61 USD** | 🔴 **-3.47%** ($-1.39) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| *(Ninguna posición abierta - 100% en efectivo)* | - | - | - | - | - |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto atraviesa una fuerte fase de corrección a corto plazo con los activos principales bajando, situando a ETH-USD y SOL-USD en niveles extremos de sobreventa técnica (RSI de 26.4 y 22.0 respectivamente). Sin embargo, nuestras posiciones actuales en cripto se acercan o superan los límites del stop-loss estricto (-2.5% a -3.0%). Por otro lado, MSFT ha entrado en zona de sobrecompra clara (RSI 72.3), pero dado que no lo tenemos en cartera, mantenemos la disciplina táctica de cortar pérdidas en las posiciones cripto debilitadas para proteger el capital remanente o reasignarlo según las reglas."*

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 90%): La posición ha acumulado una pérdida del -2.64%, acercándose peligrosamente al stop-loss estricto (-3.0%), y el activo muestra una caída sostenida con un RSI de 22.0. Es imperativo cortar la pérdida de inmediato para evitar un daño mayor al portafolio y preservar capital.
- **[SELL] ETH-USD** (Confianza: 90%): La posición registra una pérdida del -2.44% bajo una tendencia bajista marcada y un RSI de sobreventa extrema en 26.4. Aplicamos el stop-loss estricto para mitigar riesgos y liberar efectivo hacia oportunidades con mejor momentum técnico.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 21:30` | 🔴 SELL | `ETH-USD` | $11.71 | $2419.82 | La posición registra una pérdida del -2.44% bajo una tendencia bajista marcada y un RSI de... |
| `2026-10-12 21:30` | 🔴 SELL | `SOL-USD` | $22.91 | $103.78 | La posición ha acumulado una pérdida del -2.64%, acercándose peligrosamente al stop-loss e... |
| `2026-10-12 20:10` | 🟢 BUY | `SOL-USD` | $5.53 | $106.20 | SOL-USD presenta una condición de sobreventa extrema con un RSI de 24.1 y una caída de 7 d... |
| `2026-10-12 20:00` | 🟢 BUY | `SOL-USD` | $8.00 | $106.40 | SOL-USD se encuentra en clara sobreventa con un RSI de 24.3 y una caída de -11.91% en 7 dí... |
| `2026-10-12 19:40` | 🟢 BUY | `ETH-USD` | $12.00 | $2480.41 | ETH-USD se encuentra en una clara condición de sobreventa con un RSI de 14 de 29.5 y una c... |

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
