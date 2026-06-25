"""Keyless demo — real cross-venue order-book depth, no signup.

Runs as-is against the public DepthFeed demo endpoint (BTC 15-minute, top levels
per side). A taste of the full archive; grab a key for every level, asset,
window and the full history: https://kalshipricedata.com/price-data
"""

from kalshi_price_data import KalshiPriceData


def main() -> None:
    k = KalshiPriceData()  # no key
    d = k.demo()
    books = (d.get("data") or {}).get("books") or {}
    print("venues with a live book:", [v for v, b in books.items() if isinstance(b, dict)])
    for venue, b in books.items():
        if isinstance(b, dict):
            near = b.get("yes") or b.get("bids") or []
            far = b.get("no") or b.get("asks") or []
            print(f"  {venue:11} top {near[:1]}  /  {far[:1]}")


if __name__ == "__main__":
    main()
