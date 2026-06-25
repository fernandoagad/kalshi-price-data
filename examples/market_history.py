"""Historical Kalshi yes/no order book for one ticker.

Needs a DepthFeed key with Kalshi coverage (Pro plan):
https://kalshipricedata.com/price-data
    export DEPTHFEED_API_KEY=...
"""

import os

from kalshi_price_data import KalshiPriceData


def main() -> None:
    key = os.environ.get("DEPTHFEED_API_KEY")
    if not key:
        raise SystemExit("Set DEPTHFEED_API_KEY (https://kalshipricedata.com/price-data)")

    k = KalshiPriceData(api_key=key)

    markets = k.markets(coin="btc", type="15m", limit=1)
    ticker = markets[0]["ticker"]
    print("ticker:", ticker, "-", markets[0].get("title"))

    book = k.orderbook_latest(ticker)
    best_yes = (book.get("yes_prices") or book.get("bids") or [None])[0]
    print("latest book, best yes:", best_yes)

    snaps = k.snapshots(ticker, limit=5)
    print(f"{len(snaps)} historical snapshots")


if __name__ == "__main__":
    main()
