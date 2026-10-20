# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 11:01:12`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$9.92 USD** | **$28.76 USD** | **$38.68 USD** | 🔴 **-3.30%** ($-1.32) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.004178 | $2393.62 | $2408.71 | $10.06 | 📈 +0.63% | 22h 9m |
| `SOL-USD` | 0.096034 | $104.13 | $105.21 | $10.10 | 📈 +1.04% | 18h 20m |
| `BTC-USD` | 0.000105 | $81767.70 | $82050.37 | $8.59 | 📈 +0.35% | 17h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto muestra un comportamiento estable con ligeros avances de corto plazo, manteniendo a nuestras posiciones en zona positiva tras los rebotes técnicos esperados. Las criptomonedas principales operan 24/7 ofreciendo la única alternativa líquida y activa. Los índices y acciones de Wall Street se encuentran abiertos pero sin momentum alcista significativo, manteniendo una tendencia general bajista bajo la SMA20. Mantendremos la exposición actual en cripto mientras se acercan gradualmente a nuestros objetivos de take-profit."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD presenta una ganancia actual de +1.04% y un RSI de 1 hora en 57.4, avanzando de forma consistente hacia el objetivo de take-profit sin señales de agotamiento inmediato.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Las posiciones en ETH-USD, SOL-USD y BTC-USD muestran ganancias moderadas pero estables (entre +0.35% y +1.04%). Mantendremos estas posiciones monitoreando de cerca el RSI de 1 hora para asegurar beneficios parciales o totales si alcanzan el rango de take-profit del +2.0% al +3.5%, o si el RSI de 1 hora supera el nivel de sobrecompra de 70. La liquidez en efectivo remanente se mantendrá temporalmente a la espera de una mayor confirmación de volatilidad."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **78** | 🎯 **42.3%** (33W / 30L / 15BE) | 🔴 **$-1.37 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-20 10:50` | 🔴 SELL (-0.08$) | `QQQ` | $9.92 | $713.02 | QQQ lleva más de 24 horas abierto sin momentum alcista, con un rendimiento de -0.82% y baj... |
| `2026-10-19 23:00` | 🟢 BUY | `BTC-USD` | $4.00 | $81646.39 | BTC-USD presenta un RSI de 1 hora en 27.7, nivel de sobreventa profunda ideal para un rebo... |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |

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
