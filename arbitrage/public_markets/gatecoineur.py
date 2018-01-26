from arbitrage.public_markets._gatecoin import Gatecoin

class GatecoinEUR(Gatecoin):
    def __init__(self):
        super().__init__("EUR", "BTCEUR")
