from arbitrage.public_markets._binance import Binance

class BinanceUSDT(Binance):
    def __init__(self):
        super().__init__("USD", "BTCUSDT")