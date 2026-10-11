# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 13:00:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$12.12 USD** | **$29.02 USD** | **$41.14 USD** | 🟢 **+2.85%** ($+1.14) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.170099 | $109.29 | $111.81 | $19.02 | 📈 +2.30% |
| `ETH-USD` | 0.003950 | $2531.65 | $2531.65 | $10.00 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema (ETH-USD con RSI de 32.8 y SOL-USD con RSI de 27.9), lo que representa una excelente oportunidad táctica para capturar rebotes por reversión a la media. Nuestra posición actual en SOL-USD se encuentra cerca del objetivo de toma de ganancias (+2.3%), pero dada la oportunidad de diversificar hacia Ethereum en zona de alta sobreventa, realizaremos una venta parcial para rotar capital hacia ETH."*

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 85%): Tomamos beneficios de manera parcial en SOL-USD ya que la posición acumula una ganancia cercana al +2.3%, asegurando liquidez para cazar nuevas oportunidades con mayor descuento.
- **[BUY] ETH-USD** (Confianza: 90%): ETH-USD se encuentra en clara sobreventa técnica con un RSI de 32.8 y una fuerte caída semanal del -6.62%. Es el momento ideal para entrar con alta convicción buscando un rebote rápido del 3% al 5%.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 13:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2531.65 | ETH-USD se encuentra en clara sobreventa técnica con un RSI de 32.8 y una fuerte caída sem... |
| `2026-10-11 13:00` | 🔴 SELL | `SOL-USD` | $19.02 | $111.81 | Tomamos beneficios de manera parcial en SOL-USD ya que la posición acumula una ganancia ce... |
| `2026-10-11 12:50` | 🔴 SELL | `ETH-USD` | $3.10 | $2526.95 | Vendemos la posición completa de ETH-USD para liberar capital en efectivo y aprovechar las... |
| `2026-10-11 12:10` | 🟢 BUY | `ETH-USD` | $3.08 | $2504.75 | ETH-USD se encuentra en un estado de sobreventa extrema con un RSI de 28.6 y una caída sem... |
| `2026-10-11 11:00` | 🟢 BUY | `SOL-USD` | $12.00 | $109.33 | Aprovechamos la altísima sobreventa en SOL-USD (RSI de 21.2 y -9.46% en 7 días) para incre... |

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
