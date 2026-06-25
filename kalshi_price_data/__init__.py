"""
kalshi_price_data — Kalshi prediction-market PRICE DATA through the DepthFeed
aggregator: live yes/no prices, full order-book depth, and continuous history
pre-stitched for you — Kalshi, Polymarket and Limitless in one API.

"Price data" = the prediction-market contract price (yes/no quoted 0..1 =
implied probability), NOT the $KALSHI pre-IPO stock.

Get a key + docs: https://depthfeed.com/price-data
"""

from .client import KalshiPriceData

__all__ = ["KalshiPriceData"]
__version__ = "1.0.0"
