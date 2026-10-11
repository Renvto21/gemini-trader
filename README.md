# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 04:00:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.02 USD** | **$40.37 USD** | **$40.39 USD** | 🟢 **+0.98%** ($+0.39) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.220708 | $109.23 | $109.75 | $24.22 | 📈 +0.48% |
| `ETH-USD` | 0.006448 | $2481.58 | $2504.21 | $16.15 | 📈 +0.91% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema con SOL-USD (RSI en 23.1) y ETH-USD (RSI en 28.0) tras caídas semanales significativas, lo que activa nuestra estrategia de captura de rebotes por reversión a la media. En el sector tecnológico, MSFT ha entrado en sobrecompra (RSI 72.3) pero mantenemos nuestro foco principal en la rotación y consolidación de nuestras posiciones actuales en cripto que están comenzando a estabilizarse. Dado que el efectivo disponible es casi nulo, mantenemos la estructura actual sin ventas forzosas ya que las posiciones están en positivo pero aún no alcanzan el objetivo estricto de take-profit del +2.5%."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra en sobreventa extrema (RSI 14 de 23.1), lo que presenta una excelente oportunidad de rebote técnico. Mantenemos la posición actual para capturar el movimiento alcista esperado hacia el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 78%): ETH-USD muestra un RSI de 28.0 en zona de sobreventa, alineado con nuestra estrategia agresiva de cazar rebotes en cripto de alta beta. Esperamos un repunte para asegurar ganancias o rotar capital eficientemente.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 03:20` | 🟢 BUY | `SOL-USD` | $12.00 | $109.35 | SOL-USD se encuentra en una situación de sobreventa técnica masiva con un RSI de 14 en 21.... |
| `2026-10-11 03:20` | 🔴 SELL | `MSFT` | $12.00 | $535.07 | MSFT ha entrado en zona de sobrecompra técnica con un RSI de 72.3. Aplicando la regla táct... |
| `2026-10-11 03:10` | 🟢 BUY | `MSFT` | $12.00 | $535.07 | Aprovechando la fuerte subida de MSFT (2.38% en 24h y RSI de 72.3 en zona de aceleración d... |
| `2026-10-11 03:10` | 🔴 SELL | `SOL-USD` | $12.02 | $109.29 | Liberando parcialmente capital de SOL-USD para aprovechar una rotación táctica hacia activ... |
| `2026-10-11 02:20` | 🟢 BUY | `SOL-USD` | $4.11 | $109.54 | SOL-USD se encuentra en extrema sobreventa técnica con un RSI de 22.4 y una caída semanal ... |

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
