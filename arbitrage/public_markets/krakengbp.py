from arbitrage.public_markets._kraken import Kraken

class KrakenJPY(Kraken):
    def __init__(self):
        super().__init__("JPY", "XXBTZGBP")
