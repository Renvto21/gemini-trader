import yfinance as yf
from datetime import datetime
from typing import Dict, Any, List

DEFAULT_WATCHLIST = [
    "SPY",      # S&P 500 ETF
    "QQQ",      # Nasdaq 100 ETF
    "NVDA",     # Nvidia
    "AAPL",     # Apple
    "MSFT",     # Microsoft
    "GLD",      # Oro
    "BTC-USD",  # Bitcoin
    "ETH-USD",  # Ethereum
    "SOL-USD"   # Solana
]

def is_us_market_open() -> bool:
    """Verifica si la bolsa de Nueva York (NYSE/NASDAQ) está abierta actualmente."""
    try:
        from zoneinfo import ZoneInfo
        now_ny = datetime.now(ZoneInfo("America/New_York"))
    except Exception:
        from datetime import timezone, timedelta
        now_ny = datetime.now(timezone(timedelta(hours=-4)))
    
    # 5: Sábado, 6: Domingo
    if now_ny.weekday() >= 5:
        return False
    # Horario regular: 09:30 a 16:00 hora de Nueva York
    market_open = now_ny.replace(hour=9, minute=30, second=0, microsecond=0)
    market_close = now_ny.replace(hour=16, minute=0, second=0, microsecond=0)
    return market_open <= now_ny <= market_close

def calculate_rsi(prices: List[float], window: int = 14) -> float:
    """Calcula un RSI de N periodos."""
    if len(prices) < window + 1:
        return 50.0
    deltas = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
    gains = [d if d > 0 else 0.0 for d in deltas[-window:]]
    losses = [-d if d < 0 else 0.0 for d in deltas[-window:]]

    avg_gain = sum(gains) / window
    avg_loss = sum(losses) / window

    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return 100.0 - (100.0 / (1.0 + rs))

def get_market_snapshot(watchlist: List[str] = None) -> Dict[str, Any]:
    if watchlist is None:
        watchlist = DEFAULT_WATCHLIST

    snapshot = {}
    us_open = is_us_market_open()
    
    for ticker_symbol in watchlist:
        try:
            ticker = yf.Ticker(ticker_symbol)
            is_crypto = "-USD" in ticker_symbol
            market_status = "ABIERTO (24/7)" if is_crypto else ("ABIERTO" if us_open else "CERRADO (Precios congelados)")

            # 1. Velas diarias para tendencia macro (1 mes)
            hist = ticker.history(period="1mo", interval="1d")
            if hist.empty:
                continue

            hist = hist.dropna(subset=['Close'])
            close_prices = [float(p) for p in hist['Close'].tolist() if p == p and p > 0]
            
            if len(close_prices) < 2:
                try:
                    last_p = getattr(ticker.fast_info, 'last_price', None)
                    if last_p and last_p == last_p and last_p > 0:
                        close_prices.append(float(last_p))
                except Exception:
                    pass

            if len(close_prices) < 2:
                continue

            current_price = close_prices[-1]
            prev_price = close_prices[-2]
            change_24h = ((current_price - prev_price) / prev_price) * 100

            # Cambio 7 días
            price_7d = close_prices[-7] if len(close_prices) >= 7 else close_prices[0]
            change_7d = ((current_price - price_7d) / price_7d) * 100

            # Media móvil de 20 días y RSI Diario
            sma_20 = sum(close_prices[-20:]) / min(len(close_prices), 20)
            trend = "ALCISTA (sobre SMA20)" if current_price > sma_20 else "BAJISTA (bajo SMA20)"
            rsi_daily = calculate_rsi(close_prices, window=14)

            # 2. Velas de 1 hora para detección de rebotes intradiarios (últimos 5 días)
            rsi_1h = rsi_daily # Fallback si no hay velas horarias
            change_1h = 0.0
            try:
                hist_1h = ticker.history(period="5d", interval="1h")
                if not hist_1h.empty:
                    hist_1h = hist_1h.dropna(subset=['Close'])
                    close_1h = [float(p) for p in hist_1h['Close'].tolist() if p == p and p > 0]
                    if len(close_1h) >= 2:
                        change_1h = ((close_1h[-1] - close_1h[-2]) / close_1h[-2]) * 100
                    if len(close_1h) >= 15:
                        rsi_1h = calculate_rsi(close_1h, window=14)
                    elif len(close_1h) > 2:
                        rsi_1h = calculate_rsi(close_1h, window=min(14, len(close_1h) - 1))
            except Exception as e_intraday:
                pass

            # 3. Noticias recientes
            news_headlines = []
            try:
                for item in (ticker.news or [])[:3]:
                    title = item.get("content", {}).get("title") or item.get("title")
                    if title:
                        news_headlines.append(title)
            except Exception:
                pass

            snapshot[ticker_symbol] = {
                "market_status": market_status,
                "current_price": round(current_price, 2),
                "change_1h_pct": round(change_1h, 2),
                "change_24h_pct": round(change_24h, 2),
                "change_7d_pct": round(change_7d, 2),
                "rsi_1h": round(rsi_1h, 1),
                "rsi_daily": round(rsi_daily, 1),
                "trend": trend,
                "recent_news": news_headlines
            }
        except Exception as e:
            print(f"[Error consultando {ticker_symbol}]: {e}")

    return snapshot

if __name__ == "__main__":
    print("Probando descarga de datos de mercado con velas intradiarias...")
    data = get_market_snapshot(["BTC-USD", "NVDA"])
    import pprint
    pprint.pprint(data)
