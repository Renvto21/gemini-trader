# 🤖 Gemini Autonomous Trader (Paper Trading)

Bot autónomo de inversión experimental impulsado por **Gemini Flash**.

El bot simula una cuenta con un capital inicial de **$20.00 USD**, monitorea el mercado en tiempo real (acciones, ETFs y criptomonedas) con indicadores técnicos y noticias recientes, y le consulta a Gemini qué acciones tomar (BUY, SELL, HOLD) bajo estrictas reglas de gestión de riesgo.

---

## 🚀 Inicio Rápido

### 1. Obtén tu API Key Gratuita de Gemini
1. Entra a [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Inicia sesión con tu cuenta de Google.
3. Haz clic en **"Create API key"** y copia la clave.
4. Pega la clave dentro del archivo `.env`:
   ```env
   GEMINI_API_KEY=AIzaSy...
   ```

### 2. Comandos disponibles

* **Ver el estado actual del portafolio:**
  ```powershell
  python main.py --status
  ```

* **Ejecutar un ciclo de análisis y trading (una sola vez):**
  ```powershell
  python main.py --run-once
  ```

* **Ejecutar el bot en bucle automático (cada 1 hora por defecto):**
  ```powershell
  python main.py --loop --interval 3600
  ```

---

## 📁 Estructura del Proyecto

* [main.py](file:///C:/Users/arria/.gemini/antigravity/scratch/gemini-trader/main.py): Orquesta la ejecución del ciclo y la consola interactiva.
* [agent.py](file:///C:/Users/arria/.gemini/antigravity/scratch/gemini-trader/agent.py): Conexión con Gemini y prompt de gestión de riesgo y análisis.
* [portfolio.py](file:///C:/Users/arria/.gemini/antigravity/scratch/gemini-trader/portfolio.py): Simulador de saldo, registro de órdenes y cálculo de rentabilidad.
* [market_data.py](file:///C:/Users/arria/.gemini/antigravity/scratch/gemini-trader/market_data.py): Descarga datos de precios, RSI, medias móviles y noticias.
* [portfolio.json](file:///C:/Users/arria/.gemini/antigravity/scratch/gemini-trader/portfolio.json): Base de datos local con el estado del dinero y las posiciones.
