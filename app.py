import alpaca_trade_api as tradeapi

class Martingale(object):
    def _init_(self):
        self.key = 'PKQJ3TDTOBFHMGDF8IYP'
        self.secret = 'rzrWJ6n7i8HEGB30dARTy57RQoA8SSszkUO87nIY'
        self.alpaca_endpoint = 'https://paper-api.alpaca.markets'
        self.api = tradeapi.REST(self.key,self.secret,self.alpaca_endpoint)
        self.symbol = 'SPY'
        self.current_order = None
        self.last_price = 0

        try:
            self.position = int(self.api.get_position(self.symbol).qty)

        except:
            self.position = 0

    def submit_order(self, target):
           if self.current_order is not None:
            self.api.cancel_order(self.current_order.id)

            delta = target - self.position
            if delta == 0:
             return
           print('Processing the order for {target} shares')

           if delta > 0:
            buy_quantity = delta
            if self.position < 0:
                buy_quantity = min(abs(self.position),buy_quantity)
            print('Buying {buy_quantity} shares')
            self.current_order = self.api.submit_order(self.symbol,buy_quantity, 'buy','limit','day', self.last_price)

            if delta < 0:
             sell_quantity = abs(delta)
            if self.position > 0:
                sell_quantity = min(abs(self.position),sell_quantity)
            print('Selling {sell_quantity} shares')
            self.current_order = self.api.submit_order(self.symbol, sell_quantity, 'sell', 'limit', 'day', self.last_price)

           if __name__ == '_main_':
            t = Martingale()
            t.submit_order(5)



















