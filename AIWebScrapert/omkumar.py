from typing import Dict, List
from datamodel import OrderDepth, TradingState, Order
import collections
from collections import defaultdict
import numpy as np
import copy

empty_dict = {
    'STARFRUIT': 0,
    'AMETHYSTS': 0,
    'ORCHIDS': 0,
    'ROSES': 0,
    'CHOCOLATE': 0,
    'STRAWBERRIES': 0,
    'GIFT_BASKET': 0
}

def def_value():
    return copy.deepcopy(empty_dict)

INF = int(1e9)

class Trader:
    position = copy.deepcopy(empty_dict)
    POSITION_LIMIT = {
        'STARFRUIT': 20,
        'AMETHYSTS': 20,
        'ORCHIDS': 100,
        'ROSES': 60,
        'CHOCOLATE': 250,
        'STRAWBERRIES': 350,
        'GIFT_BASKET': 60
    }
    volume_traded = copy.deepcopy(empty_dict)
    price_history = defaultdict(list)
    
    def __init__(self):
        self.window_size = 5
        self.std_multiplier = 1.5
        self.min_spread = 2

    def get_mid_price(self, order_depth):
        sell_orders = sorted(order_depth.sell_orders.items())
        buy_orders = sorted(order_depth.buy_orders.items(), reverse=True)
        if not sell_orders or not buy_orders:
            return None
        return (sell_orders[0][0] + buy_orders[0][0]) / 2

    def calculate_fair_value(self, product):
        if len(self.price_history[product]) < self.window_size:
            return None
        prices = self.price_history[product][-self.window_size:]
        return np.mean(prices)

    def compute_orders_basic(self, product, order_depth):
        orders = []
        cpos = self.position[product]
        limit = self.POSITION_LIMIT[product]
        
        osell = collections.OrderedDict(sorted(order_depth.sell_orders.items()))
        obuy = collections.OrderedDict(sorted(order_depth.buy_orders.items(), reverse=True))
        
        best_bid = obuy[next(iter(obuy))] if obuy else -INF
        best_ask = osell[next(iter(osell))] if osell else INF
        
        mid_price = self.get_mid_price(order_depth)
        if mid_price is None:
            return orders
            
        fair_value = self.calculate_fair_value(product) or mid_price
        
        # Market making strategy
        bid_price = int(min(fair_value - self.min_spread, best_bid + 1))
        ask_price = int(max(fair_value + self.min_spread, best_ask - 1))
        
        # Take profitable opportunities
        for price, vol in osell.items():
            if price < fair_value and cpos < limit:
                qty = min(-vol, limit - cpos)
                orders.append(Order(product, price, qty))
                cpos += qty
                
        for price, vol in obuy.items():
            if price > fair_value and cpos > -limit:
                qty = max(-vol, -limit - cpos)
                orders.append(Order(product, price, qty))
                cpos += qty
        
        # Add market making orders
        if cpos < limit:
            qty = min(10, limit - cpos)
            orders.append(Order(product, bid_price, qty))
            
        if cpos > -limit:
            qty = max(-10, -limit - cpos)
            orders.append(Order(product, ask_price, qty))
            
        return orders

    def compute_basket_orders(self, order_depth):
        orders = {
            'CHOCOLATE': [],
            'STRAWBERRIES': [],
            'ROSES': [],
            'GIFT_BASKET': []
        }
        
        products = ['CHOCOLATE', 'STRAWBERRIES', 'ROSES', 'GIFT_BASKET']
        mid_prices = {}
        
        for p in products:
            mid_prices[p] = self.get_mid_price(order_depth[p])
            if mid_prices[p] is None:
                return orders
                
        # Basket arbitrage: 1 Gift = 4 Chocolate + 6 Strawberries + 1 Rose + premium
        premium = 380
        basket_value = (4 * mid_prices['CHOCOLATE'] + 
                       6 * mid_prices['STRAWBERRIES'] + 
                       mid_prices['ROSES'] + premium)
        spread = mid_prices['GIFT_BASKET'] - basket_value
        
        if spread > 50:  # Sell basket, buy components
            vol = min(self.position['GIFT_BASKET'] + self.POSITION_LIMIT['GIFT_BASKET'],
                     self.POSITION_LIMIT['CHOCOLATE']//4,
                     self.POSITION_LIMIT['STRAWBERRIES']//6,
                     self.POSITION_LIMIT['ROSES'])
            if vol > 0:
                orders['GIFT_BASKET'].append(Order('GIFT_BASKET', 
                    sorted(order_depth['GIFT_BASKET'].buy_orders.keys())[-1], -vol))
                orders['CHOCOLATE'].append(Order('CHOCOLATE',
                    sorted(order_depth['CHOCOLATE'].sell_orders.keys())[0], 4*vol))
                orders['STRAWBERRIES'].append(Order('STRAWBERRIES',
                    sorted(order_depth['STRAWBERRIES'].sell_orders.keys())[0], 6*vol))
                orders['ROSES'].append(Order('ROSES',
                    sorted(order_depth['ROSES'].sell_orders.keys())[0], vol))
                    
        elif spread < -50:  # Buy basket, sell components
            vol = min(self.POSITION_LIMIT['GIFT_BASKET'] - self.position['GIFT_BASKET'],
                     -self.position['CHOCOLATE']//4,
                     -self.position['STRAWBERRIES']//6,
                     -self.position['ROSES'])
            if vol > 0:
                orders['GIFT_BASKET'].append(Order('GIFT_BASKET',
                    sorted(order_depth['GIFT_BASKET'].sell_orders.keys())[0], vol))
                orders['CHOCOLATE'].append(Order('CHOCOLATE',
                    sorted(order_depth['CHOCOLATE'].buy_orders.keys())[-1], -4*vol))
                orders['STRAWBERRIES'].append(Order('STRAWBERRIES',
                    sorted(order_depth['STRAWBERRIES'].buy_orders.keys())[-1], -6*vol))
                orders['ROSES'].append(Order('ROSES',
                    sorted(order_depth['ROSES'].buy_orders.keys())[-1], -vol))
                    
        return orders

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        result = {p: [] for p in empty_dict.keys()}
        
        # Update positions
        for key, val in state.position.items():
            self.position[key] = val
            
        # Update price history
        for product in state.order_depths:
            mid_price = self.get_mid_price(state.order_depths[product])
            if mid_price:
                self.price_history[product].append(mid_price)
                
        # Generate orders for individual products
        for product in ['STARFRUIT', 'AMETHYSTS', 'ORCHIDS']:
            orders = self.compute_orders_basic(product, state.order_depths[product])
            result[product] = orders
            
        # Generate basket orders
        basket_orders = self.compute_basket_orders(state.order_depths)
        for product in basket_orders:
            result[product] = basket_orders[product]
            
        # Update volume traded
        for product in state.own_trades:
            for trade in state.own_trades[product]:
                self.volume_traded[product] += abs(trade.quantity)
                
        return result