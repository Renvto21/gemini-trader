import json
import os
from datetime import datetime
from typing import Dict, Any, List, Optional

def get_chile_now():
    try:
        from zoneinfo import ZoneInfo
        return datetime.now(ZoneInfo("America/Santiago"))
    except Exception:
        from datetime import timezone, timedelta
        return datetime.now(timezone(timedelta(hours=-3)))

def parse_iso_datetime(dt_str: str) -> datetime:
    try:
        dt = datetime.fromisoformat(dt_str)
        if dt.tzinfo is None:
            from datetime import timezone, timedelta
            dt = dt.replace(tzinfo=timezone(timedelta(hours=-3)))
        return dt
    except Exception:
        return get_chile_now()

def format_duration(opened_at_str: Optional[str]) -> str:
    if not opened_at_str:
        return "Reciente"
    try:
        opened_dt = parse_iso_datetime(opened_at_str)
        now = get_chile_now()
        total_seconds = max(0, int((now - opened_dt).total_seconds()))
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        if hours >= 24:
            days = hours // 24
            return f"{days}d {hours % 24}h"
        elif hours > 0:
            return f"{hours}h {minutes}m"
        else:
            return f"{minutes}m"
    except Exception:
        return "Reciente"

PORTFOLIO_FILE = "portfolio.json"

class PortfolioManager:
    def __init__(self, file_path: str = PORTFOLIO_FILE, initial_cash: float = 40.0):
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
            "history": [],
            "memory": {
                "notes": "Sin notas previas. Inicio de bitácora.",
                "updated_at": get_chile_now().isoformat()
            }
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

            opened_at = pos.get("opened_at")
            if not opened_at:
                for h in reversed(self.data.get("history", [])):
                    if h.get("ticker") == ticker and h.get("action") == "BUY":
                        opened_at = h.get("timestamp")
                        pos["opened_at"] = opened_at
                        break
            hold_time = format_duration(opened_at)

            positions_value += curr_val
            positions_detail.append({
                "ticker": ticker,
                "shares": round(shares, 6),
                "avg_price": round(avg_price, 2),
                "current_price": round(current_price, 2),
                "current_value": round(curr_val, 2),
                "pnl_usd": round(pnl, 2),
                "pnl_pct": round(pnl_pct, 2),
                "opened_at": opened_at,
                "holding_time": hold_time
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

    def get_memory(self) -> str:
        mem = self.data.get("memory")
        if isinstance(mem, dict):
            return mem.get("notes", "Sin notas previas. Inicio de bitácora.")
        elif isinstance(mem, str):
            return mem
        return "Sin notas previas. Inicio de bitácora."

    def update_memory(self, notes: str):
        if not notes:
            return
        self.data["memory"] = {
            "notes": notes.strip(),
            "updated_at": get_chile_now().isoformat()
        }
        self.save()

    def get_recent_history(self, n: int = 3) -> List[Dict[str, Any]]:
        history = self.data.get("history", [])
        return history[-n:] if history else []

    def execute_buy(self, ticker: str, amount_usd: float, current_price: float, reason: str = "") -> bool:
        if amount_usd <= 0 or current_price <= 0:
            return False
        if amount_usd > self.cash:
            print(f"[Error] Saldo insuficiente. Requerido: ${amount_usd:.2f}, Disponible: ${self.cash:.2f}")
            return False

        shares_to_buy = amount_usd / current_price
        self.data["cash"] -= amount_usd

        pos = self.data["positions"].get(ticker, {"shares": 0.0, "avg_price": 0.0})
        is_new = pos.get("shares", 0.0) <= 0
        total_shares = pos["shares"] + shares_to_buy
        total_cost = (pos["shares"] * pos["avg_price"]) + amount_usd
        new_avg_price = total_cost / total_shares if total_shares > 0 else current_price
        opened_at = pos.get("opened_at") or get_chile_now().isoformat() if not is_new else get_chile_now().isoformat()

        self.data["positions"][ticker] = {
            "shares": total_shares,
            "avg_price": new_avg_price,
            "opened_at": opened_at
        }

        self.data["history"].append({
            "timestamp": get_chile_now().isoformat(),
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

        pos = self.data["positions"][ticker]
        current_shares = pos["shares"]
        avg_price = pos.get("avg_price", current_price)
        if shares_to_sell <= 0 or shares_to_sell > current_shares:
            shares_to_sell = current_shares

        proceeds = shares_to_sell * current_price
        cost_basis = shares_to_sell * avg_price
        pnl_trade = proceeds - cost_basis
        pnl_trade_pct = (pnl_trade / cost_basis * 100) if cost_basis > 0 else 0.0

        self.data["cash"] += proceeds
        remaining_shares = current_shares - shares_to_sell

        if remaining_shares < 1e-6:
            del self.data["positions"][ticker]
        else:
            self.data["positions"][ticker]["shares"] = remaining_shares

        self.data["history"].append({
            "timestamp": get_chile_now().isoformat(),
            "action": "SELL",
            "ticker": ticker,
            "amount_usd": round(proceeds, 2),
            "shares": round(shares_to_sell, 6),
            "price": round(current_price, 2),
            "pnl_usd": round(pnl_trade, 2),
            "pnl_pct": round(pnl_trade_pct, 2),
            "reason": reason
        })

        self.save()
        return True

    def check_and_execute_circuit_breakers(
        self,
        current_prices: Dict[str, float],
        stop_loss_pct: float = -3.0,
        take_profit_pct: float = 4.0
    ) -> List[Dict[str, Any]]:
        """Verifica automáticamente si alguna posición superó los límites estrictos de Stop-Loss o Take-Profit y la liquida."""
        triggered = []
        for ticker in list(self.positions.keys()):
            pos = self.positions.get(ticker)
            if not pos:
                continue
            shares = pos.get("shares", 0.0)
            avg_price = pos.get("avg_price", 0.0)
            current_price = current_prices.get(ticker)
            if not current_price or avg_price <= 0 or shares <= 0:
                continue

            pnl_pct = ((current_price - avg_price) / avg_price) * 100

            if pnl_pct <= stop_loss_pct:
                reason = f"🚨 STOP-LOSS AUTOMÁTICO (CIRCUIT BREAKER): Pérdida de {pnl_pct:+.2f}% superó el límite de seguridad de {stop_loss_pct:.1f}%. Venta ejecutada por código para proteger capital."
                self.execute_sell(ticker, shares, current_price, reason)
                triggered.append({
                    "ticker": ticker,
                    "action": "SELL",
                    "type": "STOP_LOSS",
                    "pnl_pct": pnl_pct,
                    "reason": reason
                })
            elif pnl_pct >= take_profit_pct:
                reason = f"🎯 TAKE-PROFIT AUTOMÁTICO (CIRCUIT BREAKER): Ganancia de {pnl_pct:+.2f}% superó el objetivo de +{take_profit_pct:.1f}%. Venta ejecutada por código para asegurar ganancias en efectivo."
                self.execute_sell(ticker, shares, current_price, reason)
                triggered.append({
                    "ticker": ticker,
                    "action": "SELL",
                    "type": "TAKE_PROFIT",
                    "pnl_pct": pnl_pct,
                    "reason": reason
                })

        return triggered

    def get_performance_stats(self) -> Dict[str, Any]:
        """Calcula estadísticas cuantitativas de todas las operaciones cerradas en el historial."""
        history = self.data.get("history", [])
        trades = []
        buys = {}
        for h in history:
            act = h.get("action")
            ticker = h.get("ticker")
            if act == "BUY":
                if ticker not in buys:
                    buys[ticker] = []
                buys[ticker].append({
                    "shares": float(h.get("shares", 0.0)),
                    "price": float(h.get("price", 0.0))
                })
            elif act == "SELL":
                shares_to_sell = float(h.get("shares", 0.0))
                sell_price = float(h.get("price", 0.0))
                cost = 0.0
                rem = shares_to_sell
                while rem > 0 and ticker in buys and buys[ticker]:
                    b = buys[ticker][0]
                    take = min(rem, b["shares"])
                    cost += take * b["price"]
                    b["shares"] -= take
                    rem -= take
                    if b["shares"] <= 1e-6:
                        buys[ticker].pop(0)

                if "pnl_usd" in h and h["pnl_usd"] is not None:
                    pnl_usd = float(h["pnl_usd"])
                    pnl_pct = float(h.get("pnl_pct", 0.0))
                else:
                    pnl_usd = (shares_to_sell * sell_price) - cost if cost > 0 else 0.0
                    pnl_pct = (pnl_usd / cost * 100) if cost > 0 else 0.0

                trades.append({
                    "ticker": ticker,
                    "amount_usd": round(shares_to_sell * sell_price, 2),
                    "pnl_usd": round(pnl_usd, 2),
                    "pnl_pct": round(pnl_pct, 2),
                    "timestamp": h.get("timestamp", "")
                })

        total_closed = len(trades)
        wins = [t for t in trades if t["pnl_usd"] > 0]
        losses = [t for t in trades if t["pnl_usd"] < 0]
        breakevens = [t for t in trades if t["pnl_usd"] == 0]
        total_pnl = sum(t["pnl_usd"] for t in trades)
        win_rate = (len(wins) / total_closed * 100) if total_closed > 0 else 0.0

        best_trade = max(trades, key=lambda x: x["pnl_usd"]) if trades else None
        worst_trade = min(trades, key=lambda x: x["pnl_usd"]) if trades else None

        return {
            "total_closed_trades": total_closed,
            "wins": len(wins),
            "losses": len(losses),
            "breakevens": len(breakevens),
            "win_rate_pct": round(win_rate, 1),
            "realized_pnl_usd": round(total_pnl, 2),
            "best_trade": best_trade,
            "worst_trade": worst_trade
        }
