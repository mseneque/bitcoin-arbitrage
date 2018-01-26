import sys
sys.path.append('../')
sys.path.append('C:\\users\\Jurovich13112014\\MattDropbox\\Dropbox\\scripts\\bitcoin-arbitrage\\arbitrage\\public_markets')
sys.path.append('C:\\users\\Jurovich13112014\\MattDropbox\\Dropbox\\scripts\\bitcoin-arbitrage\\arbitrage')
sys.path.append('C:\\users\\Jurovich13112014\\MattDropbox\\Dropbox\\scripts\\bitcoin-arbitrage')
print(sys.path)

import unittest

import arbitrage

depths1 = {
    'PaymiumEUR':
    {'asks': [{'amount': 4, 'price': 32.8},
              {'amount': 8, 'price': 32.9},
              {'amount': 2, 'price': 33.0},
              {'amount': 3, 'price': 33.6}],
     'bids': [{'amount': 2, 'price': 31.8},
              {'amount': 4, 'price': 31.6},
              {'amount': 6, 'price': 31.4},
              {'amount': 2, 'price': 30}]},
    'MtGoxEUR':
    {'asks': [{'amount': 1, 'price': 34.2},
              {'amount': 2, 'price': 34.3},
              {'amount': 3, 'price': 34.5},
              {'amount': 3, 'price': 35.0}],
     'bids': [{'amount': 2, 'price': 33.2},
              {'amount': 3, 'price': 33.1},
              {'amount': 5, 'price': 32.6},
              {'amount': 10, 'price': 32.3}]}}

depths2 = {
    'PaymiumEUR':
    {'asks': [{'amount': 4, 'price': 32.8},
              {'amount': 8, 'price': 32.9},
              {'amount': 2, 'price': 33.0},
              {'amount': 3, 'price': 33.6}]},
    'MtGoxEUR':
    {'bids': [{'amount': 2, 'price': 33.2},
              {'amount': 3, 'price': 33.1},
              {'amount': 5, 'price': 32.6},
              {'amount': 10, 'price': 32.3}]}}

depths3 = {
    'PaymiumEUR':
    {'asks': [{'amount': 1, 'price': 34.2},
              {'amount': 2, 'price': 34.3},
              {'amount': 3, 'price': 34.5},
              {'amount': 3, 'price': 35.0}]},
    'MtGoxEUR':
    {'bids': [{'amount': 2, 'price': 33.2},
              {'amount': 3, 'price': 33.1},
              {'amount': 5, 'price': 32.6},
              {'amount': 10, 'price': 32.3}]}}

depths4 = {
    'GatecoinEUR':
    {'asks': [{'price': 9698.0, 'amount': 0.01},
              {'price': 9699.0, 'amount': 0.01},
              {'price': 9724.0, 'amount': 0.00421},
              {'price': 9724.8, 'amount': 0.01},
              {'price': 9749.9, 'amount': 0.5533},
              {'price': 9750.0, 'amount': 0.2},
              {'price': 9800.0, 'amount': 0.01042},
              {'price': 9870.0, 'amount': 0.67763},
              {'price': 9950.4, 'amount': 0.25},
              {'price': 9999.0, 'amount': 0.03695028},
              {'price': 10150.0, 'amount': 85.76744271},
              {'price': 10199.0, 'amount': 1.24672219},
              {'price': 10200.0, 'amount': 0.16754},
              {'price': 11050.0, 'amount': 0.12164},
              {'price': 12290.0, 'amount': 0.56865},
              {'price': 12989.0, 'amount': 0.46246},
              {'price': 13261.0, 'amount': 1.0},
              {'price': 14000.0, 'amount': 0.01423},
              {'price': 14300.0, 'amount': 0.03508784}, 
              {'price': 15000.0, 'amount': 0.02007024}, 
              {'price': 15175.0, 'amount': 0.15}, 
              {'price': 15500.0, 'amount': 0.1}, 
              {'price': 16150.0, 'amount': 0.03233}, 
              {'price': 16500.0, 'amount': 0.5}, 
              {'price': 16888.0, 'amount': 0.4}, 
              {'price': 16999.0, 'amount': 0.03557}, 
              {'price': 17500.0, 'amount': 0.00364}, 
              {'price': 17800.0, 'amount': 0.00958}, 
              {'price': 17951.0, 'amount': 0.14714}, 
              {'price': 18888.0, 'amount': 0.4}, 
              {'price': 610101.0, 'amount': 0.1}], 
     'bids': [{'price': 8865.8, 'amount': 2.0}, 
              {'price': 8849.1, 'amount': 1.7375098}, 
              {'price': 8849.0, 'amount': 0.24889381}, 
              {'price': 8757.1, 'amount': 0.24076748}, 
              {'price': 8750.0, 'amount': 0.18801736}, 
              {'price': 8500.0, 'amount': 0.05861836}, 
              {'price': 8400.0, 'amount': 0.04745296}, 
              {'price': 8350.0, 'amount': 0.11934277}, 
              {'price': 8300.0, 'amount': 0.003}, 
              {'price': 8300.0, 'amount': 1.0}, 
              {'price': 8070.0, 'amount': 0.0025}, 
              {'price': 8000.0, 'amount': 0.2}, 
              {'price': 8000.0, 'amount': 0.0124564}, 
              {'price': 8000.0, 'amount': 0.33694693}, 
              {'price': 7805.0, 'amount': 0.00479658}, 
              {'price': 7500.0, 'amount': 0.3}, 
              {'price': 1000.0, 'amount': 0.00049825}, 
              {'price': 0.1, 'amount': 2.8898854}]},
    'GDAXEUR':
    {'asks': [{'price': 9039.61, 'amount': 0.91550217}, 
              {'price': 9039.7, 'amount': 5.43085}, 
              {'price': 9040.0, 'amount': 0.0634303}, 
              {'price': 9040.08, 'amount': 0.00235532}, 
              {'price': 9045.0, 'amount': 0.125}, 
              {'price': 9045.1, 'amount': 0.01}, 
              {'price': 9045.11, 'amount': 0.001}, 
              {'price': 9046.67, 'amount': 0.001}, 
              {'price': 9047.31, 'amount': 0.01}, 
              {'price': 9050.0, 'amount': 0.001}, 
              {'price': 9050.63, 'amount': 0.005359}, 
              {'price': 9059.96, 'amount': 0.53604705}, 
              {'price': 9066.91, 'amount': 0.53604705}, 
              {'price': 9070.6, 'amount': 0.15}, 
              {'price': 9070.77, 'amount': 0.17762778}, 
              {'price': 9076.0, 'amount': 0.09047146}, 
              {'price': 9076.14, 'amount': 0.01}, 
              {'price': 9076.31, 'amount': 0.05}, 
              {'price': 9077.79, 'amount': 0.53604705}, 
              {'price': 9079.32, 'amount': 0.07675642}, 
              {'price': 9081.09, 'amount': 0.13815276}, 
              {'price': 9084.3, 'amount': 0.53604705}, 
              {'price': 9084.31, 'amount': 0.0148}, 
              {'price': 9086.67, 'amount': 0.742524}, 
              {'price': 9086.68, 'amount': 0.12957926}, 
              {'price': 9088.0, 'amount': 0.001}, 
              {'price': 9088.6, 'amount': 2.0}, 
              {'price': 9090.0, 'amount': 0.0034}, 
              {'price': 9093.24, 'amount': 0.09047146}, 
              {'price': 9093.33, 'amount': 0.44296788}, 
              {'price': 9094.48, 'amount': 0.005}, 
              {'price': 9099.99, 'amount': 0.07675642}, 
              {'price': 9100.0, 'amount': 0.98121851}, 
              {'price': 9101.99, 'amount': 0.12815276}, 
              {'price': 9102.0, 'amount': 0.03049538}, 
              {'price': 9104.85, 'amount': 0.001}, 
              {'price': 9108.46, 'amount': 0.01}, 
              {'price': 9110.0, 'amount': 0.004}, 
              {'price': 9110.33, 'amount': 0.01001111}, 
              {'price': 9110.4, 'amount': 0.32713}, 
              {'price': 9110.62, 'amount': 0.74}, 
              {'price': 9113.31, 'amount': 0.09047146}, 
              {'price': 9116.33, 'amount': 0.01416093}, 
              {'price': 9117.54, 'amount': 0.1}, 
              {'price': 9117.55, 'amount': 0.07675642}, 
              {'price': 9117.57, 'amount': 0.5}, 
              {'price': 9118.63, 'amount': 7.46524}, 
              {'price': 9119.99, 'amount': 0.53604705}, 
              {'price': 9120.0, 'amount': 0.2607}, 
              {'price': 9120.59, 'amount': 0.001}], 
     'bids': [{'price': 9039.6, 'amount': 1.35758538}, 
              {'price': 9039.0, 'amount': 0.005}, 
              {'price': 9038.0, 'amount': 0.0055}, 
              {'price': 9037.05, 'amount': 0.03206454}, 
              {'price': 9037.04, 'amount': 0.12777035}, 
              {'price': 9036.9, 'amount': 0.00394266}, 
              {'price': 9035.02, 'amount': 0.16582425}, 
              {'price': 9035.01, 'amount': 0.055}, 
              {'price': 9035.0, 'amount': 0.03}, 
              {'price': 9033.0, 'amount': 0.11154561}, 
              {'price': 9032.56, 'amount': 0.46709006}, 
              {'price': 9032.05, 'amount': 0.003}, 
              {'price': 9032.0, 'amount': 0.504315}, 
              {'price': 9031.63, 'amount': 0.89439266}, 
              {'price': 9031.62, 'amount': 0.30445867}, 
              {'price': 9031.53, 'amount': 0.001}, 
              {'price': 9031.29, 'amount': 0.17840417}, 
              {'price': 9030.21, 'amount': 0.005}, 
              {'price': 9030.2, 'amount': 0.04281305}, 
              {'price': 9030.02, 'amount': 0.00376605}, 
              {'price': 9030.01, 'amount': 0.2}, 
              {'price': 9030.0, 'amount': 0.46883803}, 
              {'price': 9029.38, 'amount': 0.048}, 
              {'price': 9028.35, 'amount': 0.27321896}, 
              {'price': 9028.34, 'amount': 0.15}, 
              {'price': 9027.38, 'amount': 0.12777035}, 
              {'price': 9027.37, 'amount': 0.2}, 
              {'price': 9027.27, 'amount': 0.44620945}, 
              {'price': 9027.12, 'amount': 0.5}, 
              {'price': 9025.93, 'amount': 0.16582425}, 
              {'price': 9025.92, 'amount': 0.0310632}, 
              {'price': 9025.91, 'amount': 0.105}, 
              {'price': 9025.01, 'amount': 0.22047755},
              {'price': 9025.0, 'amount': 0.95403673}, 
              {'price': 9024.82, 'amount': 0.04729304}, 
              {'price': 9024.39, 'amount': 0.0546232}, 
              {'price': 9023.0, 'amount': 0.021}, 
              {'price': 9022.68, 'amount': 0.02}, 
              {'price': 9022.0, 'amount': 1.0583092}, 
              {'price': 9021.69, 'amount': 0.01025068}, 
              {'price': 9021.4, 'amount': 0.0208}, 
              {'price': 9021.23, 'amount': 0.05}, 
              {'price': 9021.0, 'amount': 0.01}, 
              {'price': 9020.92, 'amount': 0.89439266}, 
              {'price': 9020.91, 'amount': 0.21255448}, 
              {'price': 9020.05, 'amount': 0.26747071}, 
              {'price': 9020.0, 'amount': 7.51300568}, 
              {'price': 9019.75, 'amount': 0.01}, 
              {'price': 9019.0, 'amount': 0.008071}, 
              {'price': 9017.63, 'amount': 0.29358192}]}}

class TestArbitrage(unittest.TestCase):
    def setUp(self):
        self.arbitrer = arbitrage.Arbitrer()

    def test_getprofit1(self):
        self.arbitrer.depths = depths2
        profit, vol, wb, ws = self.arbitrer.get_profit_for(
            0, 0, 'PaymiumEUR', 'MtGoxEUR')
        assert(80 == int(profit * 100))
        assert(vol == 2)

    def test_getprofit2(self):
        self.arbitrer.depths = depths2
        profit, vol, wb, ws = self.arbitrer.get_profit_for(
            2, 1, 'PaymiumEUR', 'MtGoxEUR')
        assert(159 == int(profit * 100))
        assert(vol == 5)

    def test_getprofit3(self):
        self.arbitrer.depths = depths3
        profit, vol, wb, ws = self.arbitrer.get_profit_for(
            2, 1, 'PaymiumEUR', 'MtGoxEUR')
        assert(profit == 0)
        assert(vol == 0)

    def test_getprofit4(self):
        self.arbitrer.depths = depths4
        profit, vol, wb, ws = self.arbitrer.get_profit_for(
            2, 1, 'GatecoinEUR', 'GDAXEUR')
        assert(profit == 0)
        assert(vol == 0)

if __name__ == '__main__':
    unittest.main()
