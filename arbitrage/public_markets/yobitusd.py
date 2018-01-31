from arbitrage.public_markets._yobit import Yobit

class YobitUSD(Yobit):
    def __init__(self):
        super().__init__("USD", "btc_usd")