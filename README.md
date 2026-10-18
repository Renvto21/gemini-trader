# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 16:50:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$37.98 USD** | **$0.00 USD** | **$37.98 USD** | 🔴 **-5.04%** ($-2.02) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *(Ninguna posición abierta - 100% en efectivo)* | - | - | - | - | - | - |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra completamente cerrado durante el fin de semana, por lo que toda la atención y liquidez deben centrarse estrictamente en los activos de criptomonedas (abiertos 24/7). Observamos un contexto general bajista en los criptoactivos principales, con SOL-USD y ETH-USD registrando RSI diarios extremadamente deprimidos (15.5 y 20.8 respectivamente) pero con un momentum de 1 h todavía ligeramente negativo y sin confirmación clara de giro alcista. Mantendremos la paciencia disciplinada con nuestra reserva de efectivo mientras esperamos que se rompa la tendencia bajista de corto plazo y aparezca un verdadero patrón de reversión (RSI 1H saliendo de sobreventa con cambio positivo)."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 50%): A pesar de tener un RSI diario de 20.8 y un RSI de 1h en 19.9, el cambio de 1 hora sigue siendo negativo (-1.02%) y no muestra la confirmación de giro alcista requerida por nuestra estrategia de rebotes. Mantenemos el efectivo en reserva esperando una señal más clara.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Hemos ejecutado con éxito la salida táctica de las posiciones estancadas en SOL-USD y ETH-USD para proteger el capital tras el drawdown reciente. Actualmente disponemos de $37.98 USD en efectivo. Para los siguientes ciclos, el plan consiste en no apresurarnos a reingresar: vigilaremos de cerca a ETH-USD y BTC-USD en busca de una divergencia alcista en el RSI de 1 hora o un cambio porcentual positivo superior al +0.5% en 1h que confirme el inicio del rebote técnico. Stop-loss automático por código a -3% y take-profit agresivo entre +2% y +3.5%."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **72** | 🎯 **40.3%** (29W / 29L / 14BE) | 🔴 **$-1.88 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 16:40` | 🔴 SELL (-0.19$) | `ETH-USD` | $9.81 | $2332.39 | ETH-USD registra una pérdida del -1.92% con un RSI de 1 hora en 18.5 que refleja debilidad... |
| `2026-10-18 16:40` | 🔴 SELL (-0.20$) | `SOL-USD` | $9.80 | $100.90 | La posición en SOL-USD lleva casi 6 horas abierta con una pérdida del -1.95% y un RSI de 1... |
| `2026-10-18 12:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2377.97 | ETH-USD presenta un RSI diario extremadamente bajo en 22.0 y un RSI de 1 hora saliendo de ... |
| `2026-10-18 11:01` | 🟢 BUY | `SOL-USD` | $10.00 | $102.91 | SOL-USD muestra un RSI diario extremadamente bajo (16.4) en zona de sobreventa profunda y ... |
| `2026-10-18 08:00` | 🔴 SELL (+0.13$) | `ETH-USD` | $10.13 | $2415.11 | ETH-USD registra un RSI de 1H en 72.1 (sobrecompra) y una ganancia de +1.26%. Se procede a... |

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
