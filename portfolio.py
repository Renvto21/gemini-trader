import json
import os
from datetime import datetime
from typing import Dict, Any, List

PORTFOLIO_FILE = "portfolio.json"

class PortfolioManager:
    def __init__(self, file_path: str = PORTFOLIO_FILE, initial_cash: float = 20.0):
        self.file_path = file_path
        self.initial_cash = initial_cash
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"[Aviso] No se pudo leer {self.file_path}, creando uno nuevo: {e}")
        
        default_data = {
            "initial_capital": self.initial_cash,
            "cash": self.initial_cash,
            "positions": {}, # ticker -> {"shares": float, "avg_price": float}
            "history": []
        }
        self._save_data(default_data)
        return default_data

    def _save_data(self, data: Dict[str, Any]):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def save(self):
        self._save_data(self.data)

    @property
    def cash(self) -> float:
        return float(self.data.get("cash", 0.0))

    @property
    def positions(self) -> Dict[str, Dict[str, float]]:
        return self.data.get("positions", {})

    def get_summary(self, current_prices: Dict[str, float]) -> Dict[str, Any]:
        cash = self.cash
        positions_value = 0.0
        positions_detail = []

        for ticker, pos in self.positions.items():
            shares = pos.get("shares", 0.0)
            avg_price = pos.get("avg_price", 0.0)
            raw_price = current_prices.get(ticker)
            
            # Si el precio no está disponible o es NaN, usar precio de compra o anterior
            if raw_price is None or (isinstance(raw_price, float) and (raw_price != raw_price or raw_price <= 0)):
                current_price = avg_price
            else:
                current_price = raw_price

            curr_val = shares * current_price
            cost_val = shares * avg_price
            pnl = curr_val - cost_val
            pnl_pct = (pnl / cost_val * 100) if cost_val > 0 else 0.0

            positions_value += curr_val
            positions_detail.append({
                "ticker": ticker,
                "shares": round(shares, 6),
                "avg_price": round(avg_price, 2),
                "current_price": round(current_price, 2),
                "current_value": round(curr_val, 2),
                "pnl_usd": round(pnl, 2),
                "pnl_pct": round(pnl_pct, 2)
            })

        total_equity = cash + positions_value
        initial_cap = self.data.get("initial_capital", self.initial_cash)
        total_pnl = total_equity - initial_cap
        total_pnl_pct = (total_pnl / initial_cap * 100) if initial_cap > 0 else 0.0

        return {
            "initial_capital": round(initial_cap, 2),
            "cash": round(cash, 2),
            "positions_value": round(positions_value, 2),
            "total_equity": round(total_equity, 2),
            "total_pnl_usd": round(total_pnl, 2),
            "total_pnl_pct": round(total_pnl_pct, 2),
            "positions": positions_detail
        }

    def execute_buy(self, ticker: str, amount_usd: float, current_price: float, reason: str = "") -> bool:
        if amount_usd <= 0 or current_price <= 0:
            return False
        if amount_usd > self.cash:
            print(f"[Error] Saldo insuficiente. Requerido: ${amount_usd:.2f}, Disponible: ${self.cash:.2f}")
            return False

        shares_to_buy = amount_usd / current_price
        self.data["cash"] -= amount_usd

        pos = self.data["positions"].get(ticker, {"shares": 0.0, "avg_price": 0.0})
        total_shares = pos["shares"] + shares_to_buy
        total_cost = (pos["shares"] * pos["avg_price"]) + amount_usd
        new_avg_price = total_cost / total_shares if total_shares > 0 else current_price

        self.data["positions"][ticker] = {
            "shares": total_shares,
            "avg_price": new_avg_price
        }

        self.data["history"].append({
            "timestamp": datetime.now().isoformat(),
            "action": "BUY",
            "ticker": ticker,
            "amount_usd": round(amount_usd, 2),
            "shares": round(shares_to_buy, 6),
            "price": round(current_price, 2),
            "reason": reason
        })

        self.save()
        return True

    def execute_sell(self, ticker: str, shares_to_sell: float, current_price: float, reason: str = "") -> bool:
        if ticker not in self.data["positions"]:
            print(f"[Error] No posees acciones de {ticker}.")
            return False

        current_shares = self.data["positions"][ticker]["shares"]
        if shares_to_sell <= 0 or shares_to_sell > current_shares:
            # Vender todo si excede levemente por redondeo
            shares_to_sell = current_shares

        proceeds = shares_to_sell * current_price
        self.data["cash"] += proceeds
        remaining_shares = current_shares - shares_to_sell

        if remaining_shares < 1e-6:
            del self.data["positions"][ticker]
        else:
            self.data["positions"][ticker]["shares"] = remaining_shares

        self.data["history"].append({
            "timestamp": datetime.now().isoformat(),
            "action": "SELL",
            "ticker": ticker,
            "amount_usd": round(proceeds, 2),
            "shares": round(shares_to_sell, 6),
            "price": round(current_price, 2),
            "reason": reason
        })

        self.save()
        return True
