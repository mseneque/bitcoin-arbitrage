from arbitrage.public_markets._acx import Acx

class AcxAUD(Acx):
    def __init__(self):
        super().__init__("AUD", "btcaud")