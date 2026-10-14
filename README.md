# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 09:20:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$27.53 USD** | **$12.03 USD** | **$39.56 USD** | 🔴 **-1.11%** ($-0.44) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $83614.87 | $6.04 | 📈 +0.58% | 12h 19m |
| `SOL-USD` | 0.055840 | $107.45 | $107.37 | $6.00 | 📉 -0.07% | 10h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con un sesgo moderadamente alcista en el corto plazo, mientras que los activos tradicionales de Wall Street se encuentran cerrados. BTC-USD muestra estabilidad con un PnL positivo del 0.58% tras 12 horas, y SOL-USD se mantiene plano con un RSI diario en sobreventa extrema (29.2). No se observan aún señales claras de sobrecompra (>70 en RSI de 1H) que fuercen una toma de beneficios inmediata, ni tampoco pérdidas que activen los stop-loss, por lo que el enfoque es mantener la disciplina táctica actual."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD se encuentra en terreno positivo (PnL +0.58%) con un holding time de 12 horas. El RSI de 1H está neutral en 53.3, por lo que mantenemos la posición esperando mayor expansión hacia los objetivos de take-profit.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra un PnL plano (-0.07%) y un RSI diario en sobreventa extrema (29.2). Aunque el impulso ha sido lento, el contexto técnico respalda mantener la posición a la espera de un rebote más fuerte.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener BTC-USD y SOL-USD en cartera por ahora. Monitorear de cerca el RSI de 1H y el avance de precios para ejecutar tomas de beneficios parciales o totales si BTC o SOL se acercan a zonas de sobrecompra (RSI 1H > 70 o PnL entre +2% y +3.5%). Si el holding time supera las 20 horas sin momentum alcista significativo, procederemos a rotar el capital hacia oportunidades más dinámicas."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **49** | 🎯 **44.9%** (22W / 13L / 14BE) | 🔴 **$-0.39 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |

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
