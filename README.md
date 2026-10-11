# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 03:10:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.02 USD** | **$40.25 USD** | **$40.28 USD** | 🟢 **+0.69%** ($+0.28) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.110969 | $109.11 | $109.29 | $12.13 | 📈 +0.16% |
| `ETH-USD` | 0.006448 | $2481.58 | $2501.17 | $16.13 | 📈 +0.79% |
| `MSFT` | 0.022427 | $535.07 | $535.07 | $12.00 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo alcista moderado en índices principales como SPY y QQQ, mientras que las criptomonedas (SOL-USD y ETH-USD) se encuentran en condiciones de sobreventa extrema con niveles de RSI de 21.5 y 27.5 respectivamente, tras caídas semanales significativas. El portafolio actual está completamente invertido y estancado con ganancias mínimas en cripto, lo que abre una ventana perfecta para rotar capital hacia valores tecnológicos con momentum alcista confirmado como MSFT, cuyo RSI se encuentra en zona de sobrecompra técnica (72.3) y muestra un fuerte rendimiento diario del 2.38%."*

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 85%): Liberando parcialmente capital de SOL-USD para aprovechar una rotación táctica hacia activos con momentum alcista superior, asegurando el poco beneficio y manteniendo exposición reducida en el activo.
- **[BUY] MSFT** (Confianza: 90%): Aprovechando la fuerte subida de MSFT (2.38% en 24h y RSI de 72.3 en zona de aceleración de momentum) para capturar ganancias rápidas bajo la estrategia de crecimiento y alta convicción.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 03:10` | 🟢 BUY | `MSFT` | $12.00 | $535.07 | Aprovechando la fuerte subida de MSFT (2.38% en 24h y RSI de 72.3 en zona de aceleración d... |
| `2026-10-11 03:10` | 🔴 SELL | `SOL-USD` | $12.02 | $109.29 | Liberando parcialmente capital de SOL-USD para aprovechar una rotación táctica hacia activ... |
| `2026-10-11 02:20` | 🟢 BUY | `SOL-USD` | $4.11 | $109.54 | SOL-USD se encuentra en extrema sobreventa técnica con un RSI de 22.4 y una caída semanal ... |
| `2026-10-10 12:10` | 🔴 SELL | `MSFT` | $4.11 | $535.07 | MSFT ha alcanzado un RSI de 72.3 (sobrecompra) cumpliendo con la regla táctica de toma de ... |
| `2026-10-10 12:00` | 🟢 BUY | `MSFT` | $4.11 | $535.07 | Aprovechamos el capital liberado de GLD para entrar en MSFT, que muestra un fuerte momentu... |

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
