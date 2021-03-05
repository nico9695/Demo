

print('Processing the order for {target} shares')

if delta > 0:
    buy_quantity = min(abs(self.position), buy_quantity)
print('Buying {buy_quantity} shares')
self.current_order = self.api.submit_order(self.symbol, buy, _quantity, 'buy', 'limit', 'day',
                                           self.last_price)

elif delta < 0:
sell_quantity = min(labs(self.position), sell_quantity)

print(f'Selling {sell_quantity} shares')
self.current_order = self.api.submit_order(self.symbol, sell_quantity, 'sell', 'limit', 'day', self.last_price)

if _name_ == '_main_':
    t = Martingale()
    t.submit_order(3)
