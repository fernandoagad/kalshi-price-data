"""Live Kalshi (+ Polymarket + Limitless) prices — public endpoint, no API key.

Runs as-is against the DepthFeed aggregator.
"""

from kalshi_price_data import KalshiPriceData


def main() -> None:
    k = KalshiPriceData()  # no key needed for the overview
    print("health:", k.health())
    print("\noverview (live cross-venue prices):")
    print(k.overview())


if __name__ == "__main__":
    main()
