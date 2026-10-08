import yfinance as yf
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

def calculate_rsi(prices, window: int = 14) -> float:
    """Calcula un RSI simple de 14 periodos."""
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
    
    for ticker_symbol in watchlist:
        try:
            ticker = yf.Ticker(ticker_symbol)
            # Historial de 1 mes en velas diarias
            hist = ticker.history(period="1mo", interval="1d")
            if hist.empty or len(hist) < 2:
                continue

            close_prices = hist['Close'].tolist()
            current_price = close_prices[-1]
            prev_price = close_prices[-2]
            change_24h = ((current_price - prev_price) / prev_price) * 100

            # Cambio 7 días
            price_7d = close_prices[-7] if len(close_prices) >= 7 else close_prices[0]
            change_7d = ((current_price - price_7d) / price_7d) * 100

            # Media móvil de 20 días
            sma_20 = sum(close_prices[-20:]) / min(len(close_prices), 20)
            trend = "ALCISTA (sobre SMA20)" if current_price > sma_20 else "BAJISTA (bajo SMA20)"

            # RSI 14
            rsi_14 = calculate_rsi(close_prices, window=14)

            # Noticias recientes (títulos)
            news_headlines = []
            try:
                for item in (ticker.news or [])[:3]:
                    title = item.get("content", {}).get("title") or item.get("title")
                    if title:
                        news_headlines.append(title)
            except Exception:
                pass

            snapshot[ticker_symbol] = {
                "current_price": round(current_price, 2),
                "change_24h_pct": round(change_24h, 2),
                "change_7d_pct": round(change_7d, 2),
                "rsi_14": round(rsi_14, 1),
                "trend": trend,
                "recent_news": news_headlines
            }
        except Exception as e:
            print(f"[Error consultando {ticker_symbol}]: {e}")

    return snapshot

if __name__ == "__main__":
    print("Probando descarga de datos de mercado...")
    data = get_market_snapshot(["BTC-USD", "SPY"])
    import pprint
    pprint.pprint(data)
