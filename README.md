# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 08:10:40`

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

> "El mercado tradicional se encuentra cerrado durante el fin de semana, por lo que toda la atención se centra en las criptomonedas (BTC-USD, ETH-USD y SOL-USD), las cuales operan 24/7. Tras el ciclo anterior de toma de beneficios, los principales activos cripto muestran indicadores de RSI de 1H elevados en zona de sobrecompra (BTC en 79.9, ETH en 72.8 y SOL en 68.6). Esto indica agotamiento temporal en el impulso alcista de muy corto plazo, por lo que actualmente no hay entradas claras de alta convicción para compra. Mantendré la liquidez en efectivo respetando la reserva mínima y esperando una corrección o retroceso técnico saludable que permita cazar un nuevo rebote en los criptoactivos."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 90%): El activo se encuentra en sobrecompra con un RSI de 1H en 79.9 tras haber cerrado la posición anterior con éxito. No es momento de comprar en máximos locales, mantendremos la liquidez en efectivo esperando un retroceso hacia soportes clave.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "He asegurado las ganancias en BTC, ETH y SOL. Actualmente poseo $38.37 USD en efectivo, cumpliendo con la regla de reserva mínima. Planeo monitorear los gráficos de 1H de BTC y ETH en busca de un enfriamiento del RSI hacia niveles inferiores a 40-45 para reingresar en cuanto se detecte un nuevo patrón de reversión alcista. No realizaré operaciones en este ciclo debido a la sobrecompra actual en cripto y al cierre del mercado tradicional."
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
