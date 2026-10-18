# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 09:50:36`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$38.37 USD** | **$0.00 USD** | **$38.37 USD** | 🔴 **-4.07%** ($-1.63) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *(Ninguna posición abierta - 100% en efectivo)* | - | - | - | - | - | - |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "Los mercados tradicionales (Wall Street) se encuentran cerrados con precios congelados y algunos índices como QQQ y NVDA mostrando condiciones de sobreventa extrema en el RSI de 1H, los cuales deberemos vigilar en cuanto abran. Las criptomonedas (BTC-USD, ETH-USD y SOL-USD) permanecen abiertas 24/7, pero sus indicadores de corto plazo (RSI de 1H entre 61 y 69) se mantienen elevados tras las tomas de beneficios del ciclo anterior. Dado que nuestra regla principal exige buscar rebotes desde zonas de sobreventa profunda y el efectivo actual está disponible en $38.37 USD, mantendremos la paciencia táctica esperando un retroceso más claro en cripto antes de desplegar capital de forma agresiva."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): El RSI de 1H se encuentra en 69.3, cerca de la zona de sobrecompra. No es momento óptimo para entrar en compras de rebote (mean reversion). Esperaré a que el precio corrija ligeramente hacia un RSI de 1H cercano a 40 para desplegar $10.00 USD con alta convicción.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Tengo $38.37 USD en liquidez. Las criptomonedas aún no muestran el retroceso correctivo deseado (RSI de 1H en zona neutro-alta). Esperaré a que el RSI de 1H en BTC-USD o SOL-USD baje hacia la zona de 40 para realizar compras de alta convicción por un monto de $10.00 USD cada una. Mantendré la disciplina y el efectivo intacto hasta ver esa confirmación técnica."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **70** | 🎯 **41.4%** (29W / 27L / 14BE) | 🔴 **$-1.49 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 08:00` | 🔴 SELL (+0.13$) | `ETH-USD` | $10.13 | $2415.11 | ETH-USD registra un RSI de 1H en 72.1 (sobrecompra) y una ganancia de +1.26%. Se procede a... |
| `2026-10-18 08:00` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $103.84 | SOL-USD presenta un RSI de 1H en 67.6 acercándose a zona de sobrecompra con una ganancia d... |
| `2026-10-18 08:00` | 🔴 SELL (+0.10$) | `BTC-USD` | $10.08 | $81974.15 | BTC-USD ha alcanzado un RSI de 1H en 78.8 (sobrecompra profunda) tras el rebote esperado, ... |
| `2026-10-17 19:10` | 🟢 BUY | `ETH-USD` | $10.00 | $2385.05 | ETH-USD muestra un RSI de 1H en 29.0 (sobreventa profunda) combinado con un cambio de 1h p... |
| `2026-10-17 19:10` | 🟢 BUY | `SOL-USD` | $10.00 | $102.65 | SOL-USD presenta un RSI de 1H en 31.5 saliendo de zona de sobreventa estricta y un cambio ... |

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
